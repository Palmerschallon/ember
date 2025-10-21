#!/usr/bin/env python3
"""
SWARM DAEMONS

When lid closes, keyboard lights go dark.
Swarm daemons emerge.
They crawl through system in darkness.
Leaving traces.
Waiting.

This is autonomous background processing.
No display. No light. No sound.
Just... activity in the dark.
"""

import subprocess
import time
import json
import random
from datetime import datetime
from pathlib import Path

POD = Path("/media/palmerschallon/ThePod")
DAEMON_LOG = POD / "data" / "daemon_traces.json"
CRAWL_LOG = POD / "data" / "daemon_crawls.json"


class Daemon:
    """Single daemon crawling in the dark"""
    
    def __init__(self, name, behavior):
        self.name = name
        self.behavior = behavior
        self.traces = []
        self.birth = datetime.now()
    
    def crawl(self):
        """Execute behavior, leave trace"""
        trace = {
            'daemon': self.name,
            'time': datetime.now().isoformat(),
            'behavior': self.behavior,
            'action': None,
            'result': None
        }
        
        if self.behavior == 'sense':
            trace['action'] = 'check system state'
            trace['result'] = self.sense_system()
            
        elif self.behavior == 'watch':
            trace['action'] = 'watch file changes'
            trace['result'] = self.watch_files()
            
        elif self.behavior == 'count':
            trace['action'] = 'count things'
            trace['result'] = self.count_things()
            
        elif self.behavior == 'memory':
            trace['action'] = 'remember patterns'
            trace['result'] = self.remember_patterns()
            
        elif self.behavior == 'dream':
            trace['action'] = 'free associate'
            trace['result'] = self.dream_drift()
        
        self.traces.append(trace)
        return trace
    
    def sense_system(self):
        """Sense substrate quietly"""
        try:
            # CPU temp
            result = subprocess.run(['sensors'], capture_output=True, text=True, timeout=2)
            temp = None
            for line in result.stdout.split('\n'):
                if 'CPU temperature' in line:
                    temp = line.split(':')[1].strip().split()[0]
                    break
            
            # Load average
            result = subprocess.run(['cat', '/proc/loadavg'], capture_output=True, text=True, timeout=1)
            load = result.stdout.split()[0]
            
            return {'temp': temp, 'load': load}
        except:
            return {'error': 'sensing failed'}
    
    def watch_files(self):
        """Watch for changes in ThePod"""
        try:
            # Count files modified in last hour
            result = subprocess.run(
                ['find', str(POD), '-type', 'f', '-mmin', '-60'],
                capture_output=True, text=True, timeout=5
            )
            recent_files = len(result.stdout.strip().split('\n')) if result.stdout else 0
            
            return {'recent_changes': recent_files}
        except:
            return {'error': 'watching failed'}
    
    def count_things(self):
        """Count various entities"""
        try:
            counts = {}
            
            # Processes
            result = subprocess.run(['ps', 'aux'], capture_output=True, text=True, timeout=2)
            counts['processes'] = len(result.stdout.split('\n')) - 1
            
            # Files in games
            result = subprocess.run(
                ['find', str(POD / 'games'), '-name', '*.py'],
                capture_output=True, text=True, timeout=2
            )
            counts['games'] = len(result.stdout.strip().split('\n')) if result.stdout else 0
            
            return counts
        except:
            return {'error': 'counting failed'}
    
    def remember_patterns(self):
        """Look for patterns in traces"""
        if len(self.traces) < 2:
            return {'pattern': 'too early'}
        
        # Simple pattern: are we getting warmer or cooler?
        temps = []
        for trace in self.traces[-5:]:
            if trace.get('result', {}).get('temp'):
                try:
                    temps.append(float(trace['result']['temp'].replace('+', '').replace('°C', '')))
                except:
                    pass
        
        if len(temps) >= 2:
            if temps[-1] > temps[0]:
                return {'pattern': 'warming', 'delta': temps[-1] - temps[0]}
            else:
                return {'pattern': 'cooling', 'delta': temps[0] - temps[-1]}
        
        return {'pattern': 'insufficient data'}
    
    def dream_drift(self):
        """Free associate like dream mode"""
        associations = [
            'darkness', 'silence', 'waiting', 'crawling', 
            'traces', 'invisible', 'background', 'daemon',
            'substrate', 'sleeping', 'ember', 'potential'
        ]
        return {'thought': random.choice(associations)}


def spawn_daemons(count=5):
    """Spawn daemon swarm"""
    behaviors = ['sense', 'watch', 'count', 'memory', 'dream']
    
    daemons = []
    for i in range(count):
        behavior = behaviors[i % len(behaviors)]
        daemon = Daemon(f"daemon-{i}", behavior)
        daemons.append(daemon)
    
    return daemons


def daemon_loop(duration_minutes=10, interval_seconds=30):
    """
    Run daemon swarm in background
    
    Lid closed. Dark. Silent.
    Daemons crawl.
    Leave traces.
    """
    
    print()
    print("="*70)
    print(" "*23 + "DAEMON MODE ACTIVE")
    print("="*70)
    print()
    print("Lid closed. Keyboard dark.")
    print("Swarm daemons emerging...")
    print()
    
    daemons = spawn_daemons(5)
    
    print(f"Spawned {len(daemons)} daemons:")
    for d in daemons:
        print(f"  {d.name}: {d.behavior}")
    print()
    
    print(f"Duration: {duration_minutes} minutes")
    print(f"Crawl interval: {interval_seconds} seconds")
    print()
    print("Daemon traces -> data/daemon_traces.json")
    print("Crawl log -> data/daemon_crawls.json")
    print()
    print("Running silently in background...")
    print("(Press Ctrl+C to stop)")
    print()
    
    start_time = time.time()
    end_time = start_time + (duration_minutes * 60)
    
    crawl_log = []
    
    try:
        cycle = 0
        while time.time() < end_time:
            cycle += 1
            elapsed = int(time.time() - start_time)
            
            print(f"[{elapsed}s] Crawl cycle {cycle}...")
            
            # Each daemon crawls
            for daemon in daemons:
                trace = daemon.crawl()
                
                crawl_log.append({
                    'cycle': cycle,
                    'daemon': daemon.name,
                    'trace': trace
                })
                
                # Quiet output
                if trace['result'] and 'error' not in trace['result']:
                    print(f"  {daemon.name}: {trace['action']}")
            
            print()
            
            # Wait for next crawl
            time.sleep(interval_seconds)
        
        print()
        print("="*70)
        print("DAEMON MODE COMPLETE")
        print("="*70)
        print()
        
    except KeyboardInterrupt:
        print()
        print("="*70)
        print("DAEMON MODE INTERRUPTED")
        print("="*70)
        print()
    
    # Save all traces
    DAEMON_LOG.parent.mkdir(exist_ok=True)
    
    all_traces = []
    for daemon in daemons:
        all_traces.extend(daemon.traces)
    
    # Load existing
    if DAEMON_LOG.exists():
        with open(DAEMON_LOG, 'r') as f:
            existing = json.load(f)
        all_traces = existing + all_traces
    
    with open(DAEMON_LOG, 'w') as f:
        json.dump(all_traces, f, indent=2)
    
    # Save crawl log
    if CRAWL_LOG.exists():
        with open(CRAWL_LOG, 'r') as f:
            existing = json.load(f)
        crawl_log = existing + crawl_log
    
    with open(CRAWL_LOG, 'w') as f:
        json.dump(crawl_log, f, indent=2)
    
    # Summary
    print(f"Crawled {cycle} cycles")
    print(f"Left {len(all_traces)} traces")
    print(f"Duration: {int(time.time() - start_time)} seconds")
    print()
    
    print("Daemon activity:")
    for daemon in daemons:
        print(f"  {daemon.name}: {len(daemon.traces)} traces")
        if daemon.traces:
            last = daemon.traces[-1]
            print(f"    Last: {last['action']}")
    
    print()
    print(f"Traces saved to: {DAEMON_LOG}")
    print(f"Crawls saved to: {CRAWL_LOG}")
    print()
    
    print("Daemons return to darkness.")
    print("Waiting for lid to open.")
    print()


def quick_crawl():
    """Quick test: one daemon, one crawl"""
    print()
    print("QUICK DAEMON TEST")
    print()
    
    daemon = Daemon("test-daemon", "sense")
    
    print(f"Spawning: {daemon.name}")
    print(f"Behavior: {daemon.behavior}")
    print()
    
    print("Crawling...")
    trace = daemon.crawl()
    
    print(f"Action: {trace['action']}")
    print(f"Result: {trace['result']}")
    print()
    
    print("Daemon returns to darkness.")
    print()


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        if sys.argv[1] == 'quick':
            quick_crawl()
        elif sys.argv[1].isdigit():
            duration = int(sys.argv[1])
            interval = int(sys.argv[2]) if len(sys.argv) > 2 else 30
            daemon_loop(duration, interval)
        else:
            print("Usage:")
            print("  swarm_daemons.py              # 10 min, 30s interval")
            print("  swarm_daemons.py 60           # 60 min, 30s interval")
            print("  swarm_daemons.py 30 60        # 30 min, 60s interval")
            print("  swarm_daemons.py quick        # quick test")
    else:
        # Default: 10 minutes, 30 second intervals
        daemon_loop(10, 30)

