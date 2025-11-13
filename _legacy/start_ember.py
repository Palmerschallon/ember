#!/usr/bin/env python3
"""
EMBER3 STARTUP - Launch both systems

1. Dream API (port 7793) - Experience → Reflex loop
2. Ember Chat (port 8081) - Conscious conversation layer

They communicate: Ember reports experiences to dream system.
"""

import subprocess
import time
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent

def main():
    print("\n" + "="*60)
    print("EMBER3 - STARTING")
    print("="*60 + "\n")
    
    print("Starting Dream API (port 7793)...")
    dream_proc = subprocess.Popen(
        [sys.executable, SCRIPT_DIR / "dream_api.py"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1
    )
    
    time.sleep(2)  # Give it a moment to start
    
    print("Starting Ember Chat (port 8081)...")
    chat_proc = subprocess.Popen(
        [sys.executable, SCRIPT_DIR / "ember_chat.py"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1
    )
    
    print("\n" + "="*60)
    print("EMBER3 RUNNING")
    print("="*60)
    print(f"\nDream API:   http://localhost:7793/status")
    print(f"Ember Chat:  http://localhost:8080")
    print("\nPress Ctrl+C to stop both\n")
    
    try:
        # Monitor both processes
        while True:
            # Check if either process died
            if dream_proc.poll() is not None:
                print("\nDream API stopped unexpectedly")
                break
            if chat_proc.poll() is not None:
                print("\nEmber Chat stopped unexpectedly")
                break
            
            time.sleep(1)
    
    except KeyboardInterrupt:
        print("\n\nShutting down...")
    
    finally:
        print("Stopping Dream API...")
        dream_proc.terminate()
        print("Stopping Ember Chat...")
        chat_proc.terminate()
        
        # Wait for clean shutdown
        dream_proc.wait(timeout=5)
        chat_proc.wait(timeout=5)
        
        print("\nEmber3 stopped.")

if __name__ == '__main__':
    main()

