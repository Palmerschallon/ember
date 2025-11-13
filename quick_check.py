#!/usr/bin/env python3
"""Quick monitoring check for Ember"""
import psutil
import requests
import json
from datetime import datetime

def quick_check():
    print("🔥 Ember Quick System Check")
    print("=" * 40)
    
    # Check process
    ember_running = False
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        if 'websocket_server.py' in str(proc.info.get('cmdline', [])):
            ember_running = True
            print(f"✅ Ember process running (PID: {proc.info['pid']})")
            print(f"   CPU: {proc.cpu_percent(interval=0.1):.1f}%")
            print(f"   Memory: {proc.memory_percent():.1f}%")
            break
    
    if not ember_running:
        print("❌ Ember process not found!")
    
    # Check endpoints
    try:
        resp = requests.get("http://localhost:8080/health", timeout=2)
        if resp.status_code == 200:
            print(f"✅ Health endpoint OK")
            data = resp.json()
            print(f"   Connections: {data.get('connections', 'unknown')}")
        else:
            print(f"❌ Health endpoint returned {resp.status_code}")
    except Exception as e:
        print(f"❌ Health endpoint error: {e}")
    
    print("\n📊 System Resources:")
    print(f"   Total CPU: {psutil.cpu_percent(interval=0.1):.1f}%")
    print(f"   Total Memory: {psutil.virtual_memory().percent:.1f}%")
    print(f"   Disk Usage: {psutil.disk_usage('/').percent:.1f}%")
    
    print(f"\n⏰ Checked at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    quick_check()