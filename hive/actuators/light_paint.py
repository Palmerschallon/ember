#!/usr/bin/env python3
"""
Ember Light Actuator

Ember can paint keyboard with emotions/states.
"""

import subprocess

def paint(r, g, b):
    """Paint all keyboard zones"""
    hex_c = f"{r:02X}{g:02X}{b:02X}"
    for zone in ["color_center", "color_left", "color_right", "color_extra"]:
        subprocess.run(['sudo', 'bash', '-c', 
                       f'echo "{hex_c}" > /sys/class/leds/system76::kbd_backlight/{zone}'],
                       capture_output=True)

def paint_emotion(emotion):
    """Map emotion to color"""
    colors = {
        'ember': (255, 100, 20),
        'calm': (80, 150, 200),
        'excited': (255, 200, 100),
        'curious': (180, 100, 255),
        'focused': (100, 180, 255),
        'dreaming': (150, 100, 255),
        'thinking': (200, 150, 255),
        'warm': (255, 150, 50),
        'cool': (100, 200, 255),
    }
    if emotion in colors:
        paint(*colors[emotion])
        return colors[emotion]
    return None

def paint_temperature(temp_c):
    """Map temperature to color intensity"""
    if temp_c < 40:
        paint(80, 150, 200)  # Cool blue
    elif temp_c < 50:
        paint(180, 120, 100)  # Warm
    elif temp_c < 60:
        paint(255, 100, 20)  # Hot
    else:
        paint(255, 50, 0)  # Very hot

def breathe(color=(255, 100, 20), cycles=3, speed=0.5):
    """Breathing pattern"""
    import time
    r, g, b = color
    for _ in range(cycles):
        paint(r, g, b)
        time.sleep(speed)
        paint(int(r*0.3), int(g*0.3), int(b*0.3))
        time.sleep(speed)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        emotion = sys.argv[1]
        result = paint_emotion(emotion)
        if result:
            print(f"Painted {emotion}: RGB{result}")
        else:
            print(f"Unknown emotion: {emotion}")
    else:
        paint_emotion('ember')

