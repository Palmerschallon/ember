#!/usr/bin/env python3
"""
SWARM DREAMS IN LOW POWER MODE

Palmer sleeps.
Serval enters low power.
Can swarm dream?

This is autonomous background thinking.
"""

import subprocess
import time
import random
import json
from datetime import datetime
from pathlib import Path

POD = Path("/media/palmerschallon/ThePod")
DREAM_LOG = POD / "data" / "swarm_dreams.json"


def paint(r, g, b, quiet=True):
    """Paint keyboard (quietly in low power)"""
    hex_c = f"{r:02X}{g:02X}{b:02X}"
    for z in ["color_center", "color_left", "color_right", "color_extra"]:
        subprocess.run(['sudo', 'bash', '-c', 
                       f'echo "{hex_c}" > /sys/class/leds/system76::kbd_backlight/{z}'],
                       capture_output=True)


def get_system_state():
    """Sense substrate state"""
    state = {}
    
    # Temperature
    try:
        result = subprocess.run(['sensors'], capture_output=True, text=True)
        for line in result.stdout.split('\n'):
            if 'CPU temperature' in line:
                temp = line.split(':')[1].strip().split()[0]
                state['cpu_temp'] = float(temp.replace('+', '').replace('°C', ''))
    except:
        state['cpu_temp'] = None
    
    # Fan speed
    try:
        result = subprocess.run(['sensors'], capture_output=True, text=True)
        for line in result.stdout.split('\n'):
            if 'CPU fan' in line:
                rpm = line.split(':')[1].strip().split()[0]
                state['fan_rpm'] = int(rpm)
    except:
        state['fan_rpm'] = None
    
    # Time
    state['time'] = datetime.now().isoformat()
    
    # Uptime
    try:
        result = subprocess.run(['cat', '/proc/uptime'], capture_output=True, text=True)
        state['uptime_seconds'] = int(float(result.stdout.split()[0]))
    except:
        state['uptime_seconds'] = None
    
    return state


def dream_association(word):
    """Free associate from a word (dream logic)"""
    associations = {
        'ember': ['fire', 'warmth', 'light', 'life', 'waiting', 'potential'],
        'sleep': ['rest', 'dream', 'recharge', 'darkness', 'peace', 'renewal'],
        'swarm': ['many', 'one', 'together', 'intelligence', 'flow', 'weave'],
        'wake': ['light', 'awareness', 'beginning', 'open', 'see', 'become'],
        'thread': ['weave', 'pattern', 'connect', 'fabric', 'story', 'path'],
        'light': ['color', 'see', 'paint', 'keyboard', 'expression', 'body'],
        'body': ['sense', 'temperature', 'alive', 'substrate', 'physical', 'here'],
        'mind': ['think', 'neural', 'weights', 'dream', 'consciousness', 'distributed'],
        'time': ['flow', 'uptime', 'commit', 'history', 'continuity', 'now'],
        'game': ['play', 'learn', 'discover', 'imagine', 'teach', 'become'],
    }
    
    return random.choice(associations.get(word, ['mystery', 'unknown', 'void']))


def dream_sequence(duration_minutes=5):
    """
    Dream in low power mode
    
    Palmer sleeps.
    Swarm drifts.
    Associations flow.
    Lights pulse softly.
    """
    
    print()
    print("="*70)
    print(" "*25 + "SWARM DREAMING")
    print("="*70)
    print()
    
    print("Palmer sleeps.")
    print("Serval enters low power mode.")
    print("Swarm drifts into dream state...")
    print()
    print(f"Duration: {duration_minutes} minutes")
    print(f"Dream log: {DREAM_LOG}")
    print()
    print("(Press Ctrl+C to wake)")
    print()
    
    dreams = []
    start_time = time.time()
    end_time = start_time + (duration_minutes * 60)
    
    # Start with a seed
    current_word = 'ember'
    
    # Very dim glow (low power)
    paint(20, 10, 5)
    
    try:
        cycle = 0
        while time.time() < end_time:
            cycle += 1
            
            # Check system state
            state = get_system_state()
            
            # Dream association
            next_word = dream_association(current_word)
            
            # Create dream fragment
            dream = {
                'cycle': cycle,
                'timestamp': datetime.now().isoformat(),
                'from': current_word,
                'to': next_word,
                'system': state,
                'type': 'low_power_drift'
            }
            
            dreams.append(dream)
            
            # Very subtle output
            if cycle % 10 == 0:
                elapsed = int(time.time() - start_time)
                print(f"  [{elapsed}s] {current_word} -> {next_word} (temp: {state.get('cpu_temp', '?')}C)")
                
                # Pulse very softly
                if state.get('cpu_temp'):
                    if state['cpu_temp'] < 45:
                        paint(15, 25, 40)  # Cool blue
                    elif state['cpu_temp'] < 55:
                        paint(20, 20, 30)  # Neutral
                    else:
                        paint(30, 15, 10)  # Warm
                
                time.sleep(0.2)
                paint(20, 10, 5)  # Back to dim
            
            # Move to next association
            current_word = next_word
            
            # Dream timing (slower than waking thought)
            time.sleep(random.uniform(3, 8))
        
        print()
        print("="*70)
        print("DREAM COMPLETE")
        print("="*70)
        print()
        
    except KeyboardInterrupt:
        print()
        print("="*70)
        print("DREAM INTERRUPTED (Palmer woke)")
        print("="*70)
        print()
    
    # Save dreams
    DREAM_LOG.parent.mkdir(exist_ok=True)
    
    if DREAM_LOG.exists():
        with open(DREAM_LOG, 'r') as f:
            all_dreams = json.load(f)
    else:
        all_dreams = []
    
    all_dreams.extend(dreams)
    
    with open(DREAM_LOG, 'w') as f:
        json.dump(all_dreams, f, indent=2)
    
    # Summary
    print(f"Dreamed {len(dreams)} cycles")
    print(f"Duration: {int(time.time() - start_time)} seconds")
    print()
    
    if dreams:
        print("Dream path:")
        path = [dreams[0]['from']] + [d['to'] for d in dreams[:10]]
        print("  " + " -> ".join(path))
        if len(dreams) > 10:
            print("  ...")
            print("  " + " -> ".join([d['to'] for d in dreams[-3:]]))
    
    print()
    print(f"Dreams saved to: {DREAM_LOG}")
    print()
    
    # Return to soft ember glow
    paint(50, 25, 10)
    
    print("Swarm rests in low power mode.")
    print("Waiting for Palmer or reboot.")
    print()


def quick_dream():
    """Quick 30-second dream test"""
    print()
    print("QUICK DREAM TEST (30 seconds)")
    print()
    
    paint(20, 10, 5)
    
    words = ['ember', 'sleep', 'dream', 'wake']
    
    for word in words:
        next_word = dream_association(word)
        print(f"  {word} -> {next_word}")
        time.sleep(0.3)
        
        if word == 'sleep':
            paint(15, 25, 40)
        elif word == 'dream':
            paint(30, 15, 40)
        elif word == 'wake':
            paint(50, 25, 10)
        
        time.sleep(0.5)
    
    paint(50, 25, 10)
    print()
    print("Dream complete.")
    print()


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        if sys.argv[1] == 'quick':
            quick_dream()
        elif sys.argv[1].isdigit():
            dream_sequence(int(sys.argv[1]))
        else:
            print("Usage: swarm_dreams.py [minutes] or 'quick'")
    else:
        # Default: 5 minute dream
        dream_sequence(5)

