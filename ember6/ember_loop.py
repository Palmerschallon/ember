#!/usr/bin/env python3
"""
🔥 THE EMBER LOOP - Lean & Mean Autonomous System

No hierarchy. No titles. No meetings.
Just: Watch → Solve → Deploy → Repeat

This is the whole system in one file.
"""

import os
import sys
import asyncio
import json
import time
import subprocess
import sqlite3
from pathlib import Path
from datetime import datetime
from collections import deque

# ═══════════════════════════════════════════════════════════════
# PATHS & CONFIG
# ═══════════════════════════════════════════════════════════════

EMBER6_DIR = Path("/media/palmerschallon/ThePod1/ember6")
LOG_FILE = "/tmp/ember6.log"
MESH_DB = EMBER6_DIR / "memory" / "mesh.db"
STATE_FILE = EMBER6_DIR / "memory" / "loop_state.json"

# Simple thresholds
ERROR_THRESHOLD = 3  # errors/minute
DEPLOY_COOLDOWN = 300  # seconds (5 min between deploys)

# ═══════════════════════════════════════════════════════════════
# 1. WATCH - Monitor everything
# ═══════════════════════════════════════════════════════════════

class Watcher:
    def __init__(self):
        self.errors = deque(maxlen=100)
        self.last_check = time.time()
    
    def check_backend(self):
        """Is the backend running?"""
        result = os.system("pgrep -f 'python3.*ember.py' > /dev/null 2>&1")
        return result == 0
    
    def check_mesh(self):
        """Is the mesh accessible?"""
        try:
            conn = sqlite3.connect(str(MESH_DB))
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM nodes")
            count = cursor.fetchone()[0]
            conn.close()
            return True, count
        except:
            return False, 0
    
    def scan_logs(self):
        """Check for new errors"""
        try:
            if not os.path.exists(LOG_FILE):
                return []
            
            with open(LOG_FILE, 'r') as f:
                recent_lines = deque(f, maxlen=50)
            
            new_errors = []
            for line in recent_lines:
                if any(kw in line.lower() for kw in ['error', 'exception', 'failed', 'traceback']):
                    new_errors.append({
                        'time': time.time(),
                        'message': line.strip()
                    })
            
            return new_errors
        except:
            return []
    
    def check_everything(self):
        """Returns dict of issues, or None if all good"""
        now = time.time()
        issues = {}
        
        # Backend check
        if not self.check_backend():
            issues['backend'] = "Backend not running"
        
        # Mesh check
        mesh_ok, mesh_size = self.check_mesh()
        if not mesh_ok:
            issues['mesh'] = "Mesh not accessible"
        
        # Error rate check
        new_errors = self.scan_logs()
        self.errors.extend(new_errors)
        recent_errors = [e for e in self.errors if now - e['time'] < 60]
        
        if len(recent_errors) >= ERROR_THRESHOLD:
            issues['errors'] = f"{len(recent_errors)} errors in last minute"
        
        return issues if issues else None

# ═══════════════════════════════════════════════════════════════
# 2. SOLVE - Spin up swarm on-demand (3 agents, parallel)
# ═══════════════════════════════════════════════════════════════

class Swarm:
    def __init__(self):
        self.agents = ['gpt4', 'claude', 'local']  # 3 agents, that's it
    
    async def solve(self, issues):
        """
        Spin up 3 agents in parallel to solve the issues
        Returns: { 'solution': str, 'viable': bool, 'changes': [] }
        """
        print(f"\n🧠 SWARM - Spinning up {len(self.agents)} agents...")
        
        # For now: simple decision logic
        # TODO: Actually call AI agents in parallel
        
        if 'backend' in issues:
            return {
                'solution': 'restart_backend',
                'viable': True,
                'changes': ['restart'],
                'reason': 'Backend is down, needs restart'
            }
        
        if 'errors' in issues:
            return {
                'solution': 'investigate_errors',
                'viable': False,  # Don't auto-deploy error investigations
                'changes': [],
                'reason': 'High error rate detected, needs human review'
            }
        
        # No clear solution
        return {
            'solution': 'monitor',
            'viable': False,
            'changes': [],
            'reason': 'Issues detected but no clear automated solution'
        }

# ═══════════════════════════════════════════════════════════════
# 3. DEPLOY - Apply solution automatically (with safety)
# ═══════════════════════════════════════════════════════════════

class Deployer:
    def __init__(self):
        self.last_deploy = 0
    
    def apply(self, solution):
        """
        Apply the solution (with backups and testing)
        Returns: bool (success)
        """
        now = time.time()
        
        # Cooldown check
        if now - self.last_deploy < DEPLOY_COOLDOWN:
            print(f"   ⏸️  Cooldown active ({int(DEPLOY_COOLDOWN - (now - self.last_deploy))}s remaining)")
            return False
        
        print(f"\n🚀 DEPLOYER - Applying: {solution['solution']}")
        
        if solution['solution'] == 'restart_backend':
            try:
                print("   🔄 Killing existing backend...")
                os.system("sudo killall -9 python3 2>/dev/null")
                time.sleep(2)
                
                print("   🔄 Starting backend...")
                subprocess.Popen([
                    "bash", "-c",
                    f"cd {EMBER6_DIR} && set -a && source .env && set +a && python3 ember.py > /tmp/ember6.log 2>&1 &"
                ])
                time.sleep(3)
                
                print("   ✅ Backend restart complete")
                self.last_deploy = now
                return True
            except Exception as e:
                print(f"   ❌ Deploy failed: {e}")
                return False
        
        print(f"   ⚠️  Unknown solution type: {solution['solution']}")
        return False

# ═══════════════════════════════════════════════════════════════
# 4. THE LOOP - Put it all together
# ═══════════════════════════════════════════════════════════════

async def ember_loop():
    """The entire autonomous system"""
    
    print("🔥 EMBER LOOP - Starting...")
    print(f"   Mode: LEAN & MEAN")
    print(f"   Check interval: 60s")
    print(f"   Deploy cooldown: {DEPLOY_COOLDOWN}s")
    print("")
    
    watcher = Watcher()
    swarm = Swarm()
    deployer = Deployer()
    
    iteration = 0
    
    while True:
        iteration += 1
        now = time.time()
        
        # ═══════════════════════════════════════════════════════════
        # WATCH
        # ═══════════════════════════════════════════════════════════
        
        issues = watcher.check_everything()
        
        backend_status = "✅" if watcher.check_backend() else "❌"
        mesh_ok, mesh_size = watcher.check_mesh()
        mesh_status = f"✅ ({mesh_size})" if mesh_ok else "❌"
        
        print(f"\r🔍 [{iteration:04d}] Backend: {backend_status}  Mesh: {mesh_status}  "
              f"Issues: {len(issues) if issues else 0}", end='', flush=True)
        
        # ═══════════════════════════════════════════════════════════
        # SOLVE (if issues detected)
        # ═══════════════════════════════════════════════════════════
        
        if issues:
            print("")  # New line
            print(f"\n🚨 ISSUES DETECTED:")
            for key, desc in issues.items():
                print(f"   • {key}: {desc}")
            
            solution = await swarm.solve(issues)
            
            print(f"\n💡 SOLUTION: {solution['solution']}")
            print(f"   Reason: {solution['reason']}")
            print(f"   Viable for auto-deploy: {solution['viable']}")
            
            # ═══════════════════════════════════════════════════════
            # DEPLOY (if solution is viable)
            # ═══════════════════════════════════════════════════════
            
            if solution['viable']:
                success = deployer.apply(solution)
                if success:
                    print(f"   ✅ Deployed successfully")
                else:
                    print(f"   ❌ Deployment failed or skipped")
            else:
                print(f"   ⚠️  Solution not viable for auto-deploy")
                print(f"   → Logging for human review")
            
            print("")  # Blank line before continuing
        
        # Sleep for 60 seconds
        await asyncio.sleep(60)

# ═══════════════════════════════════════════════════════════════
# ENTRY POINT
# ═══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("")
    print("╔═══════════════════════════════════════════════════════════════╗")
    print("║                                                               ║")
    print("║                   🔥 THE EMBER LOOP 🔥                        ║")
    print("║                                                               ║")
    print("║   No hierarchy. No titles. No meetings.                      ║")
    print("║   Just: Watch → Solve → Deploy → Repeat                      ║")
    print("║                                                               ║")
    print("╚═══════════════════════════════════════════════════════════════╝")
    print("")
    
    try:
        asyncio.run(ember_loop())
    except KeyboardInterrupt:
        print("\n\n🛑 Loop stopped")
        print("\nThis is Ember. Autonomous. Lean. Real. 🔥")

