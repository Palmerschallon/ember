#!/usr/bin/env python3
"""
CONTINUOUS DREAM ACTUATOR

Runs in background
Checks dreams every 5 minutes
Acts on patterns found
Closes ouroboros loop continuously
"""

import time
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from dream_actuator import DreamActuator

def run_continuous():
    """Run dream actuator continuously"""
    actuator = DreamActuator()
    
    print()
    print("="*70)
    print(" "*15 + "CONTINUOUS DREAM ACTUATOR")
    print("="*70)
    print()
    print("Running in background")
    print("Checking dreams every 5 minutes")
    print("Acting on patterns found")
    print()
    print("Press Ctrl+C to stop")
    print()
    
    check_interval = 300  # 5 minutes
    
    try:
        while True:
            print(f"[{time.strftime('%H:%M:%S')}] Checking for dream patterns...")
            results = actuator.run_once()
            
            if results:
                print(f"  Executed {len(results)} actions")
            else:
                print("  No new patterns")
            
            print(f"  Next check in {check_interval // 60} minutes")
            time.sleep(check_interval)
            
    except KeyboardInterrupt:
        print("\n\nContinuous dream actuator stopped")

if __name__ == "__main__":
    run_continuous()

