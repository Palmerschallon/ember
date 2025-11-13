#!/usr/bin/env python3
"""
🏢 THE CEO - Strategic Decision Making & Swarm Coordination

When THE WATCHER detects issues, THE CEO is triggered.
The CEO evaluates the situation, convenes the swarm, and directs the deployment.

This is the bridge between monitoring and execution.
"""

import asyncio
import json
import subprocess
from pathlib import Path
from datetime import datetime

EMBER6_DIR = Path("/media/palmerschallon/ThePod1/ember6")

async def trigger_ceo(trigger_reasons, watcher_state):
    """
    Called by THE WATCHER when CEO intervention is needed
    
    Args:
        trigger_reasons: List of strings describing why CEO was triggered
        watcher_state: Current state from The Watcher
    
    Returns:
        Dict containing CEO decision and actions taken
    """
    print("\n" + "═" * 80)
    print("🏢 THE CEO - ACTIVATED")
    print("═" * 80)
    print(f"\nTIMESTAMP: {datetime.now().isoformat()}")
    print(f"\nTRIGGER REASONS ({len(trigger_reasons)}):")
    for i, reason in enumerate(trigger_reasons, 1):
        print(f"  {i}. {reason}")
    
    print("\n" + "─" * 80)
    print("ANALYZING SITUATION...")
    print("─" * 80)
    
    # Categorize issues
    categories = {
        'critical': [],      # Backend down, mesh broken
        'performance': [],   # Slow responses, high latency
        'quality': [],       # Errors, bugs, user complaints
        'strategic': []      # Feature requests, improvements
    }
    
    for reason in trigger_reasons:
        reason_lower = reason.lower()
        if 'not running' in reason_lower or 'not accessible' in reason_lower:
            categories['critical'].append(reason)
        elif 'response time' in reason_lower or 'performance' in reason_lower:
            categories['performance'].append(reason)
        elif 'error' in reason_lower or 'exception' in reason_lower:
            categories['quality'].append(reason)
        else:
            categories['strategic'].append(reason)
    
    # Decide on action based on severity
    decision = {
        'timestamp': datetime.now().isoformat(),
        'trigger_reasons': trigger_reasons,
        'categories': {k: v for k, v in categories.items() if v},
        'action': None,
        'swarm_convened': False,
        'deployment_initiated': False,
        'status': 'analyzing'
    }
    
    # CRITICAL: Immediate action required
    if categories['critical']:
        print("\n🚨 CRITICAL ISSUES DETECTED")
        print("   Action: Immediate restart + health check")
        decision['action'] = 'critical_restart'
        decision['status'] = 'executing'
        
        # Attempt to restart backend
        try:
            print("\n   🔄 Restarting backend...")
            subprocess.run([
                "bash", "-c",
                "cd /media/palmerschallon/ThePod1/ember6 && ./start.sh"
            ], timeout=10)
            print("   ✅ Backend restart initiated")
            decision['deployment_initiated'] = True
        except Exception as e:
            print(f"   ❌ Restart failed: {e}")
            decision['status'] = 'failed'
        
        return decision
    
    # PERFORMANCE: Convene swarm for optimization
    if categories['performance']:
        print("\n⚡ PERFORMANCE ISSUES DETECTED")
        print("   Action: Convene optimization swarm")
        decision['action'] = 'optimize'
        decision['swarm_convened'] = True
        
        # TODO: Actually trigger ember_swarm.py with specific focus
        print("\n   [Swarm convening would happen here - not yet fully wired]")
        return decision
    
    # QUALITY: Convene swarm for bug fixes
    if categories['quality']:
        print("\n🐛 QUALITY ISSUES DETECTED")
        print("   Action: Convene debugging swarm")
        decision['action'] = 'fix_bugs'
        decision['swarm_convened'] = True
        
        print("\n   [Swarm convening would happen here - not yet fully wired]")
        return decision
    
    # STRATEGIC: Convene swarm for improvements
    if categories['strategic']:
        print("\n💡 IMPROVEMENT OPPORTUNITIES DETECTED")
        print("   Action: Convene innovation swarm")
        decision['action'] = 'improve'
        decision['swarm_convened'] = True
        
        print("\n   [Swarm convening would happen here - not yet fully wired]")
        return decision
    
    # NO CLEAR CATEGORY: Log and continue monitoring
    print("\n🤔 UNCLEAR SITUATION - Continuing monitoring")
    decision['action'] = 'monitor'
    decision['status'] = 'monitoring'
    
    return decision


if __name__ == "__main__":
    # Test CEO functionality
    print("🏢 CEO - Test Mode")
    print("\nSimulating trigger from Watcher...\n")
    
    test_reasons = [
        "High error rate: 5 errors in last minute",
        "Average response time is high: 8.3s"
    ]
    
    result = asyncio.run(trigger_ceo(test_reasons, None))
    
    print("\n" + "═" * 80)
    print("CEO DECISION:")
    print(json.dumps(result, indent=2))
    print("═" * 80)

