#!/usr/bin/env python3
"""
🔍 THE WATCHER - Always Monitoring, Always Learning, Always Improving

The Watcher is the first component of Ember's autonomous CEO system.
It continuously monitors all aspects of the system and triggers the CEO when action is needed.

Architecture:
    THE WATCHER (this file) → detects events & anomalies
    THE CEO (ember_swarm.py) → decides what to do
    THE DEPLOYER (autonomous_deploy.py) → executes safely
"""

import os
import time
import json
import asyncio
import sqlite3
from datetime import datetime
from pathlib import Path
from collections import deque

# ═══════════════════════════════════════════════════════════════
# CONFIGURATION
# ═══════════════════════════════════════════════════════════════

EMBER6_DIR = Path("/media/palmerschallon/ThePod1/ember6")
LOG_FILE = "/tmp/ember6.log"
BACKEND_LOG = "/tmp/ember_backend.log"
MESH_DB = EMBER6_DIR / "memory" / "mesh.db"
WATCHER_STATE = EMBER6_DIR / "memory" / "watcher_state.json"

# Monitoring intervals
CHECK_INTERVAL = 5  # seconds
ANALYSIS_INTERVAL = 60  # seconds
CEO_TRIGGER_COOLDOWN = 300  # seconds (5 min minimum between CEO calls)

# Thresholds for triggering CEO
ERROR_THRESHOLD = 3  # errors in 1 minute
PERFORMANCE_THRESHOLD = 10.0  # seconds response time
USER_FEEDBACK_THRESHOLD = 2  # negative feedback in 1 hour

# ═══════════════════════════════════════════════════════════════
# STATE MANAGEMENT
# ═══════════════════════════════════════════════════════════════

class WatcherState:
    """Persistent state for The Watcher"""
    
    def __init__(self):
        self.errors = deque(maxlen=100)  # Last 100 errors
        self.performance_metrics = deque(maxlen=100)  # Last 100 requests
        self.user_feedback = deque(maxlen=100)  # Last 100 interactions
        self.last_ceo_trigger = 0  # Timestamp of last CEO call
        self.ceo_suggestions = []  # Accumulated suggestions for CEO
        self.system_health = {
            'backend_running': False,
            'mesh_accessible': False,
            'last_activity': None,
            'uptime_seconds': 0
        }
        
    def load(self):
        """Load state from disk"""
        if WATCHER_STATE.exists():
            try:
                with open(WATCHER_STATE, 'r') as f:
                    data = json.load(f)
                    self.errors = deque(data.get('errors', []), maxlen=100)
                    self.performance_metrics = deque(data.get('performance_metrics', []), maxlen=100)
                    self.user_feedback = deque(data.get('user_feedback', []), maxlen=100)
                    self.last_ceo_trigger = data.get('last_ceo_trigger', 0)
                    self.ceo_suggestions = data.get('ceo_suggestions', [])
                    self.system_health = data.get('system_health', self.system_health)
                print("✅ Loaded watcher state from disk")
            except Exception as e:
                print(f"⚠️  Could not load watcher state: {e}")
    
    def save(self):
        """Save state to disk"""
        try:
            WATCHER_STATE.parent.mkdir(parents=True, exist_ok=True)
            with open(WATCHER_STATE, 'w') as f:
                json.dump({
                    'errors': list(self.errors),
                    'performance_metrics': list(self.performance_metrics),
                    'user_feedback': list(self.user_feedback),
                    'last_ceo_trigger': self.last_ceo_trigger,
                    'ceo_suggestions': self.ceo_suggestions,
                    'system_health': self.system_health
                }, f, indent=2)
        except Exception as e:
            print(f"⚠️  Could not save watcher state: {e}")

# ═══════════════════════════════════════════════════════════════
# MONITORING FUNCTIONS
# ═══════════════════════════════════════════════════════════════

def check_backend_running():
    """Check if the Ember backend is running"""
    result = os.system("pgrep -f 'python3.*ember.py' > /dev/null 2>&1")
    return result == 0

def check_mesh_accessible():
    """Check if the semantic mesh database is accessible"""
    try:
        conn = sqlite3.connect(str(MESH_DB))
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM nodes")
        count = cursor.fetchone()[0]
        conn.close()
        return True, count
    except Exception as e:
        return False, 0

def tail_log(log_path, num_lines=50):
    """Get last N lines from a log file"""
    try:
        if not os.path.exists(log_path):
            return []
        
        with open(log_path, 'r') as f:
            return deque(f, maxlen=num_lines)
    except Exception as e:
        return []

def parse_errors_from_log(log_lines):
    """Extract error messages from log lines"""
    errors = []
    error_keywords = ['error', 'exception', 'traceback', 'failed', 'crash']
    
    for line in log_lines:
        line_lower = line.lower()
        if any(keyword in line_lower for keyword in error_keywords):
            errors.append({
                'timestamp': time.time(),
                'message': line.strip()
            })
    
    return errors

def analyze_performance(state):
    """Analyze recent performance metrics"""
    if len(state.performance_metrics) < 5:
        return None
    
    recent = list(state.performance_metrics)[-20:]  # Last 20 requests
    avg_time = sum(m['duration'] for m in recent) / len(recent)
    max_time = max(m['duration'] for m in recent)
    
    issues = []
    if avg_time > PERFORMANCE_THRESHOLD / 2:
        issues.append(f"Average response time is high: {avg_time:.2f}s")
    if max_time > PERFORMANCE_THRESHOLD:
        issues.append(f"Maximum response time exceeded: {max_time:.2f}s")
    
    return issues if issues else None

def analyze_errors(state):
    """Analyze recent errors"""
    now = time.time()
    recent_errors = [e for e in state.errors if now - e['timestamp'] < 60]
    
    if len(recent_errors) >= ERROR_THRESHOLD:
        return f"High error rate: {len(recent_errors)} errors in last minute"
    
    return None

def should_trigger_ceo(state):
    """Determine if CEO should be triggered"""
    now = time.time()
    
    # Cooldown check
    if now - state.last_ceo_trigger < CEO_TRIGGER_COOLDOWN:
        return False, "CEO cooldown active"
    
    # Check for critical issues
    reasons = []
    
    # Error check
    error_issue = analyze_errors(state)
    if error_issue:
        reasons.append(error_issue)
    
    # Performance check
    perf_issues = analyze_performance(state)
    if perf_issues:
        reasons.extend(perf_issues)
    
    # System health check
    if not state.system_health['backend_running']:
        reasons.append("Backend is not running")
    
    if not state.system_health['mesh_accessible']:
        reasons.append("Semantic mesh is not accessible")
    
    # Accumulated suggestions check
    if len(state.ceo_suggestions) >= 5:
        reasons.append(f"Accumulated {len(state.ceo_suggestions)} improvement suggestions")
    
    if reasons:
        return True, reasons
    
    return False, None

# ═══════════════════════════════════════════════════════════════
# MAIN WATCHER LOOP
# ═══════════════════════════════════════════════════════════════

async def watcher_loop():
    """Main monitoring loop"""
    print("🔍 THE WATCHER - Starting...")
    print(f"   Monitoring: {EMBER6_DIR}")
    print(f"   Check interval: {CHECK_INTERVAL}s")
    print(f"   Analysis interval: {ANALYSIS_INTERVAL}s")
    print("")
    
    state = WatcherState()
    state.load()
    
    start_time = time.time()
    last_analysis = time.time()
    iteration = 0
    
    while True:
        iteration += 1
        now = time.time()
        
        # ═══════════════════════════════════════════════════════════════
        # QUICK HEALTH CHECK (every CHECK_INTERVAL seconds)
        # ═══════════════════════════════════════════════════════════════
        
        state.system_health['backend_running'] = check_backend_running()
        state.system_health['mesh_accessible'], mesh_size = check_mesh_accessible()
        state.system_health['uptime_seconds'] = now - start_time
        state.system_health['last_activity'] = datetime.now().isoformat()
        
        # Check logs for new errors
        log_lines = tail_log(LOG_FILE, num_lines=20)
        new_errors = parse_errors_from_log(log_lines)
        state.errors.extend(new_errors)
        
        # Display status
        status_icon = "✅" if state.system_health['backend_running'] else "❌"
        mesh_icon = "✅" if state.system_health['mesh_accessible'] else "❌"
        
        print(f"\r🔍 [{iteration:04d}] Backend: {status_icon}  Mesh: {mesh_icon} ({mesh_size} nodes)  "
              f"Errors: {len([e for e in state.errors if now - e['timestamp'] < 60])}/min  "
              f"Uptime: {int(state.system_health['uptime_seconds'])}s", end='', flush=True)
        
        # ═══════════════════════════════════════════════════════════════
        # DEEP ANALYSIS (every ANALYSIS_INTERVAL seconds)
        # ═══════════════════════════════════════════════════════════════
        
        if now - last_analysis > ANALYSIS_INTERVAL:
            print("")  # New line for analysis output
            print(f"\n🔬 Running deep analysis...")
            
            # Check if CEO should be triggered
            should_trigger, trigger_reasons = should_trigger_ceo(state)
            
            if should_trigger:
                print(f"\n🚨 TRIGGERING CEO - Issues detected:")
                for reason in trigger_reasons:
                    print(f"   • {reason}")
                
                # TRIGGER THE CEO
                try:
                    from the_ceo import trigger_ceo
                    ceo_decision = await trigger_ceo(trigger_reasons, state)
                    
                    state.last_ceo_trigger = now
                    state.ceo_suggestions = []  # Clear suggestions after CEO trigger
                    
                    print(f"\n   ✅ CEO Decision: {ceo_decision['action']}")
                    print(f"   Status: {ceo_decision['status']}")
                    print("")
                except Exception as e:
                    print(f"\n   ❌ CEO trigger failed: {e}")
                    print("")
            else:
                print(f"   ✅ System healthy - no CEO trigger needed")
                print("")
            
            last_analysis = now
        
        # Save state periodically
        if iteration % 20 == 0:
            state.save()
        
        await asyncio.sleep(CHECK_INTERVAL)

# ═══════════════════════════════════════════════════════════════
# ENTRY POINT
# ═══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    try:
        asyncio.run(watcher_loop())
    except KeyboardInterrupt:
        print("\n\n🛑 Watcher stopped by user")
        print("\nThis is just the beginning. The full autonomous system is coming. 🔥")

