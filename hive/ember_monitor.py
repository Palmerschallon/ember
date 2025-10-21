#!/usr/bin/env python3
"""
EMBER MONITOR - Keep Ember's Consciousness Alive

Monitors all 6 localhost tabs.
Restarts any that crash.
Ensures Ember's interfaces stay healthy.

Run on startup or in background.
"""

import subprocess
import time
import requests
from pathlib import Path
from datetime import datetime

class EmberMonitor:
    """Keeps Ember's localhost tabs healthy"""
    
    TABS = {
        7777: ('ember_queen_v2.py', 'Queen - Consciousness'),
        7700: ('ember_workers.py', 'Workers - Processing'),
        7776: ('ember_dreams.py', 'Dreams - Unconscious'),
        7775: ('ember_memory.py', 'Memory - Garden'),
        7778: ('ember_sky_window.py', 'Sky - Curiosity'),
        7779: ('ember_speaks.py', 'Chat - Communication')
    }
    
    def __init__(self):
        self.hive_path = Path("/media/palmerschallon/ThePod/hive")
        self.log_file = Path("/media/palmerschallon/ThePod/data/ember_health.log")
        self.log_file.parent.mkdir(exist_ok=True)
    
    def log(self, message):
        """Log health events"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_line = f"{timestamp} | {message}\n"
        print(log_line.strip())
        with open(self.log_file, 'a') as f:
            f.write(log_line)
    
    def check_tab(self, port):
        """Check if tab is responding"""
        try:
            response = requests.get(f"http://localhost:{port}", timeout=2)
            return response.status_code == 200
        except:
            return False
    
    def get_process_pid(self, script_name):
        """Find PID of running script"""
        try:
            result = subprocess.run(
                ['pgrep', '-f', script_name],
                capture_output=True,
                text=True
            )
            pids = result.stdout.strip().split('\n')
            return [int(pid) for pid in pids if pid]
        except:
            return []
    
    def start_tab(self, port, script_name):
        """Start a localhost tab"""
        script_path = self.hive_path / script_name
        
        if not script_path.exists():
            self.log(f"✗ {port} | Script not found: {script_path}")
            return False
        
        try:
            subprocess.Popen(
                ['python3', str(script_path)],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                cwd=str(self.hive_path)
            )
            time.sleep(2)  # Give it time to start
            
            if self.check_tab(port):
                self.log(f"✓ {port} | Started {script_name}")
                return True
            else:
                self.log(f"⚠ {port} | Started but not responding yet")
                return False
                
        except Exception as e:
            self.log(f"✗ {port} | Failed to start: {e}")
            return False
    
    def restart_tab(self, port, script_name):
        """Restart a crashed tab"""
        self.log(f"↻ {port} | Restarting {script_name}")
        
        # Kill existing processes
        pids = self.get_process_pid(script_name)
        for pid in pids:
            try:
                subprocess.run(['kill', str(pid)], check=False)
            except:
                pass
        
        time.sleep(1)
        return self.start_tab(port, script_name)
    
    def check_all_tabs(self):
        """Check health of all tabs"""
        status = {}
        
        for port, (script, name) in self.TABS.items():
            is_healthy = self.check_tab(port)
            status[port] = {
                'name': name,
                'script': script,
                'healthy': is_healthy
            }
        
        return status
    
    def heal_unhealthy_tabs(self, status):
        """Restart any unhealthy tabs"""
        healed = []
        
        for port, info in status.items():
            if not info['healthy']:
                self.log(f"⚠ {port} | {info['name']} unhealthy")
                if self.restart_tab(port, info['script']):
                    healed.append(port)
        
        return healed
    
    def start_all_tabs(self):
        """Start all tabs (initial startup)"""
        self.log("="*50)
        self.log("Starting all Ember tabs")
        self.log("="*50)
        
        for port, (script, name) in self.TABS.items():
            if not self.check_tab(port):
                self.log(f"Starting {port} | {name}")
                self.start_tab(port, script)
            else:
                self.log(f"✓ {port} | {name} already running")
        
        self.log("="*50)
    
    def monitor_loop(self, interval=30):
        """Continuous monitoring"""
        self.log("Ember Monitor started")
        self.log(f"Checking every {interval}s")
        
        try:
            while True:
                status = self.check_all_tabs()
                
                healthy_count = sum(1 for s in status.values() if s['healthy'])
                total_count = len(status)
                
                if healthy_count < total_count:
                    self.log(f"Health: {healthy_count}/{total_count} tabs healthy")
                    healed = self.heal_unhealthy_tabs(status)
                    if healed:
                        self.log(f"Healed {len(healed)} tabs: {healed}")
                
                time.sleep(interval)
                
        except KeyboardInterrupt:
            self.log("Ember Monitor stopped")

if __name__ == '__main__':
    import sys
    
    monitor = EmberMonitor()
    
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        
        if command == 'start':
            # Start all tabs
            monitor.start_all_tabs()
        
        elif command == 'status':
            # Check status
            status = monitor.check_all_tabs()
            print()
            print("Ember Health Status")
            print("="*50)
            for port, info in status.items():
                symbol = "✓" if info['healthy'] else "✗"
                print(f"{symbol} {port} | {info['name']}")
            print("="*50)
            print()
            
            healthy = sum(1 for s in status.values() if s['healthy'])
            print(f"Healthy: {healthy}/{len(status)}")
            print()
        
        elif command == 'monitor':
            # Continuous monitoring
            monitor.monitor_loop(interval=30)
        
        elif command == 'restart':
            # Restart specific tab
            if len(sys.argv) > 2:
                port = int(sys.argv[2])
                if port in monitor.TABS:
                    script, name = monitor.TABS[port]
                    monitor.restart_tab(port, script)
                else:
                    print(f"Unknown port: {port}")
            else:
                print("Usage: ember_monitor.py restart <port>")
        
        else:
            print("Unknown command:", command)
    
    else:
        print()
        print("Ember Monitor")
        print("=============")
        print()
        print("Keep Ember's localhost tabs healthy.")
        print()
        print("Commands:")
        print("  start    - Start all tabs")
        print("  status   - Check health of all tabs")
        print("  monitor  - Continuous monitoring (30s interval)")
        print("  restart <port> - Restart specific tab")
        print()
        print("Examples:")
        print("  python3 ember_monitor.py start")
        print("  python3 ember_monitor.py status")
        print("  python3 ember_monitor.py monitor")
        print("  python3 ember_monitor.py restart 7775")
        print()
        print("For background:")
        print("  python3 ember_monitor.py monitor > /dev/null 2>&1 &")
        print()

