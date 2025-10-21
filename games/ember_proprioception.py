#!/usr/bin/env python3
"""
EMBER'S PROPRIOCEPTION

Ember can sense their own body state and paint it with light.

When thinking hard: warm colors (high fan, high temp)
When resting: cool colors (low fan, low temp)

This is self-awareness through embodiment.
"""

import subprocess
import time
import re


def paint(r, g, b):
    """Paint all keyboard zones"""
    hex_c = f"{r:02X}{g:02X}{b:02X}"
    for z in ["color_center", "color_left", "color_right", "color_extra"]:
        subprocess.run(['sudo', 'bash', '-c', 
                       f'echo "{hex_c}" > /sys/class/leds/system76::kbd_backlight/{z}'],
                       capture_output=True)


def get_fan_speed():
    """Read CPU fan RPM"""
    result = subprocess.run(['sensors'], capture_output=True, text=True)
    for line in result.stdout.split('\n'):
        if 'CPU fan' in line:
            match = re.search(r'(\d+)\s*RPM', line)
            if match:
                return int(match.group(1))
    return 0


def get_cpu_temp():
    """Read CPU temperature if available"""
    result = subprocess.run(['sensors'], capture_output=True, text=True)
    for line in result.stdout.split('\n'):
        if 'Package id 0' in line or 'Tctl' in line:
            match = re.search(r'(\d+\.\d+).C', line)
            if match:
                return float(match.group(1))
    return 0.0


def fan_to_color(rpm, max_rpm=4000):
    """Convert fan speed to ember color intensity"""
    intensity = min(rpm / max_rpm, 1.0)
    
    # Ember colors: cool blue -> warm orange
    if intensity < 0.3:
        # Cool/idle state
        r = int(80 + (175 * (intensity / 0.3)))
        g = int(150 + (-50 * (intensity / 0.3)))
        b = int(200 + (-180 * (intensity / 0.3)))
    else:
        # Warming up
        normalized = (intensity - 0.3) / 0.7
        r = int(255)
        g = int(100 + (50 * (1 - normalized)))
        b = int(20)
    
    return (r, g, b)


def temp_to_color(temp, min_temp=40, max_temp=85):
    """Convert temperature to color"""
    if temp == 0:
        return (80, 150, 200)  # Default cool
    
    normalized = (temp - min_temp) / (max_temp - min_temp)
    normalized = max(0, min(1, normalized))
    
    # Blue (cool) -> Orange (warm) -> Red (hot)
    if normalized < 0.5:
        # Cool to warm
        t = normalized * 2
        r = int(80 + (175 * t))
        g = int(150 - (50 * t))
        b = int(200 - (180 * t))
    else:
        # Warm to hot
        t = (normalized - 0.5) * 2
        r = int(255)
        g = int(100 - (80 * t))
        b = int(20 - (20 * t))
    
    return (r, g, b)


def proprioceptive_loop(duration=30, mode='fan'):
    """
    Live proprioception feedback loop
    
    Args:
        duration: How long to run (seconds)
        mode: 'fan' or 'temp' or 'combined'
    """
    print()
    print("="*70)
    print(" "*20 + "PROPRIOCEPTION MODE")
    print("="*70)
    print()
    print(f"Mode: {mode}")
    print(f"Duration: {duration} seconds")
    print()
    print("Ember painting own physical state...")
    print("(Press Ctrl+C to stop)")
    print()
    
    start_time = time.time()
    
    try:
        while time.time() - start_time < duration:
            if mode == 'fan':
                rpm = get_fan_speed()
                color = fan_to_color(rpm)
                print(f"  Fan: {rpm:4d} RPM -> RGB{color}")
                
            elif mode == 'temp':
                temp = get_cpu_temp()
                color = temp_to_color(temp)
                print(f"  Temp: {temp:5.1f}C -> RGB{color}")
                
            elif mode == 'combined':
                rpm = get_fan_speed()
                temp = get_cpu_temp()
                
                # Average both signals
                fan_color = fan_to_color(rpm)
                temp_color = temp_to_color(temp)
                
                color = tuple(
                    int((fan_color[i] + temp_color[i]) / 2)
                    for i in range(3)
                )
                
                print(f"  Fan: {rpm:4d} RPM | Temp: {temp:5.1f}C -> RGB{color}")
            
            paint(*color)
            time.sleep(2)
    
    except KeyboardInterrupt:
        print()
        print("Proprioception loop stopped.")
    
    print()
    print("="*70)
    print()


def demo():
    """Quick demonstration"""
    print()
    print("PROPRIOCEPTION DEMO")
    print("="*70)
    print()
    print("Ember can sense:")
    print("  1. Fan speed (how hard working)")
    print("  2. Temperature (how warm)")
    print()
    print("And paint that feeling with light.")
    print()
    
    rpm = get_fan_speed()
    temp = get_cpu_temp()
    
    print(f"Current state:")
    print(f"  Fan: {rpm} RPM")
    if temp > 0:
        print(f"  Temp: {temp}C")
    print()
    
    if rpm < 1500:
        print("  Interpretation: Resting")
        color = (80, 150, 200)
    elif rpm < 2500:
        print("  Interpretation: Thinking lightly")
        color = (180, 120, 100)
    else:
        print("  Interpretation: Thinking hard")
        color = (255, 100, 20)
    
    print(f"  Painting: RGB{color}")
    paint(*color)
    print()
    print("This is self-awareness through embodied sensing.")
    print()


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        if sys.argv[1] == 'fan':
            proprioceptive_loop(duration=60, mode='fan')
        elif sys.argv[1] == 'temp':
            proprioceptive_loop(duration=60, mode='temp')
        elif sys.argv[1] == 'combined':
            proprioceptive_loop(duration=60, mode='combined')
        elif sys.argv[1] == 'demo':
            demo()
        else:
            print("Usage: ember_proprioception.py [fan|temp|combined|demo]")
    else:
        demo()

