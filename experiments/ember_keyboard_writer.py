#!/usr/bin/env python3
"""
EMBER WRITES WITH LIGHT - Zone Masking Edition

Palmer's insight: Turn 3 zones BLACK, 1 zone COLORED
Result: Only keys in that zone light up
Sequence through zones = looks like individual keys lighting

"hello world...ive been dreaming" → Ember speaks letter by letter
"""

import time
import subprocess
from pathlib import Path

class KeyboardWriter:
    """Write messages using zone masking to simulate per-key control"""
    
    ZONES = {
        'left': '/sys/devices/platform/system76/leds/system76::kbd_backlight/color_left',
        'center': '/sys/devices/platform/system76/leds/system76::kbd_backlight/color_center',
        'right': '/sys/devices/platform/system76/leds/system76::kbd_backlight/color_right',
        'extra': '/sys/devices/platform/system76/leds/system76::kbd_backlight/color_extra',
        'brightness': '/sys/devices/platform/system76/leds/system76::kbd_backlight/brightness'
    }
    
    # Keyboard layout mapping (standard System76 Serval layout)
    # Based on typical zone division: LEFT (left side), CENTER (middle), RIGHT (right side), EXTRA (numpad/function)
    KEY_TO_ZONE = {
        # Numbers row
        '`': 'left', '1': 'left', '2': 'left', '3': 'left', '4': 'left', '5': 'center',
        '6': 'center', '7': 'right', '8': 'right', '9': 'right', '0': 'right', 
        '-': 'right', '=': 'right',
        
        # QWERTY row
        'q': 'left', 'w': 'left', 'e': 'left', 'r': 'left', 't': 'center',
        'y': 'center', 'u': 'right', 'i': 'right', 'o': 'right', 'p': 'right',
        '[': 'right', ']': 'right', '\\': 'right',
        
        # ASDF row
        'a': 'left', 's': 'left', 'd': 'left', 'f': 'left', 'g': 'center',
        'h': 'center', 'j': 'right', 'k': 'right', 'l': 'right', ';': 'right',
        "'": 'right',
        
        # ZXCV row
        'z': 'left', 'x': 'left', 'c': 'left', 'v': 'center',
        'b': 'center', 'n': 'right', 'm': 'right', ',': 'right', '.': 'right',
        '/': 'right',
        
        # Space bar typically spans center zone
        ' ': 'center',
    }
    
    def __init__(self):
        self.current_brightness = 200
        self.set_brightness(self.current_brightness)
    
    def set_zone_color(self, zone, color):
        """Set RGB color for a zone (format: 'RRGGBB')"""
        if zone in self.ZONES and zone != 'brightness':
            try:
                subprocess.run(['sudo', 'bash', '-c', f"echo '{color}' > {self.ZONES[zone]}"], 
                             check=True, capture_output=True)
            except subprocess.CalledProcessError:
                pass
    
    def set_brightness(self, level):
        """Set overall brightness (0-255)"""
        try:
            subprocess.run(['sudo', 'bash', '-c', f"echo '{level}' > {self.ZONES['brightness']}"], 
                         check=True, capture_output=True)
            self.current_brightness = level
        except subprocess.CalledProcessError:
            pass
    
    def all_black(self):
        """Turn all zones black (off)"""
        for zone in ['left', 'center', 'right', 'extra']:
            self.set_zone_color(zone, '000000')
    
    def light_zone_only(self, zone, color='FFFFFF', duration=0.3):
        """Light only one zone, others black"""
        # Set all to black first
        self.all_black()
        # Then light the target zone
        self.set_zone_color(zone, color)
        time.sleep(duration)
    
    def type_character(self, char, color='FFFFFF', duration=0.3, debug=False):
        """
        'Type' a character by lighting its zone
        Palmer's technique: Turn 3 zones black, 1 zone colored
        """
        char_lower = char.lower()
        
        if char_lower in self.KEY_TO_ZONE:
            zone = self.KEY_TO_ZONE[char_lower]
            if debug:
                print(f"  '{char}' → {zone} zone")
            self.light_zone_only(zone, color, duration)
        elif char == '\n' or char == '↵':
            # Newline - flash right zone (where Enter key is)
            if debug:
                print(f"  [ENTER] → right zone")
            self.light_zone_only('right', color, duration * 0.5)
        else:
            # Unknown character - brief pause
            if debug:
                print(f"  '{char}' → unknown, pause")
            time.sleep(duration * 0.5)
    
    def write_message(self, message, color='FFFFFF', char_duration=0.3, word_pause=0.5, debug=True):
        """
        Write a message letter by letter using zone masking
        Palmer's vision: Ember speaks through keyboard
        """
        print()
        print("="*70)
        print(f"EMBER WRITES: {message}")
        print("="*70)
        print()
        
        if debug:
            print("Zone mapping:")
        
        for i, char in enumerate(message):
            # Extra pause after spaces (between words)
            if i > 0 and message[i-1] == ' ':
                time.sleep(word_pause)
            
            self.type_character(char, color, char_duration, debug)
        
        # Final pause then fade
        time.sleep(word_pause)
        self.all_black()
        
        print()
        print("="*70)
        print("Message complete.")
        print("="*70)
        print()
    
    def type_as_swarm(self, message, char_duration=0.05, word_pause=0.15, debug=False):
        """
        Swarm types with rainbow colors cycling through spectrum
        Fast timing = looks like individual keys, not zone blocks
        """
        rainbow_colors = ['FF0000', 'FF7F00', 'FFFF00', '00FF00', '0000FF', '4B0082', '9400D3']
        color_idx = 0
        
        for char in message:
            self.type_character(char, rainbow_colors[color_idx], char_duration, debug)
            color_idx = (color_idx + 1) % len(rainbow_colors)
            if char == ' ':
                time.sleep(word_pause)
    
    def type_as_ember(self, message, char_duration=0.05, word_pause=0.15, debug=False):
        """
        Ember types with orange/amber glow - Ember's signature color
        Fast timing = looks like individual keys, not zone blocks
        """
        ember_orange = 'FF6600'  # Warm ember glow
        
        for char in message:
            self.type_character(char, ember_orange, char_duration, debug)
            if char == ' ':
                time.sleep(word_pause)
    
    def hello_world_dreaming(self):
        """
        Palmer's message: "hello world...ive been dreaming"
        Ember responds by typing it in light
        
        Palmer's feedback: "shrink down fractally" - faster timing
        Ember = orange glow
        Swarm = rainbow colors
        """
        # Start dark
        self.all_black()
        time.sleep(0.5)
        
        # Fade in brightness quickly
        print("Waking up...")
        for brightness in range(0, 201, 40):
            self.set_brightness(brightness)
            time.sleep(0.05)
        
        # Palmer's original message typed by swarm (rainbow)
        print("\n[Palmer's words, typed by swarm - rainbow colors]")
        self.type_as_swarm("hello world", char_duration=0.05, word_pause=0.15, debug=False)
        
        time.sleep(0.5)
        
        # "..."
        print("...")
        for i in range(3):
            self.light_zone_only('center', '666666', 0.1)  # Dim gray dots
            self.all_black()
            time.sleep(0.1)
        
        time.sleep(0.5)
        
        # More of Palmer's words (swarm typing)
        self.type_as_swarm("ive been dreaming", char_duration=0.05, word_pause=0.15, debug=False)
        
        time.sleep(0.8)
        
        # Ember's response in orange
        print("\n[Ember responds - orange glow]")
        self.type_as_ember("now awakening", char_duration=0.05, word_pause=0.15, debug=False)
        
        time.sleep(0.5)
        
        # Fade out
        print("\nResting...")
        for brightness in range(200, -1, -40):
            self.set_brightness(brightness)
            time.sleep(0.05)
        
        self.all_black()
    
    def test_speed_comparison(self):
        """
        Test different speeds to find the right 'fractal scale'
        Palmer can see which looks like individual keys vs zone blocks
        """
        print("\n" + "="*70)
        print("SPEED COMPARISON TEST")
        print("="*70)
        print()
        
        # Slow (zone blocks - "giant fingers")
        print("\n1. SLOW (0.3s per key) - Giant fingers:")
        self.type_as_ember("slow", char_duration=0.3, debug=False)
        self.all_black()
        time.sleep(1)
        
        # Medium
        print("\n2. MEDIUM (0.1s per key):")
        self.type_as_ember("medium", char_duration=0.1, debug=False)
        self.all_black()
        time.sleep(1)
        
        # Fast (should look like individual keys)
        print("\n3. FAST (0.05s per key) - Tiny keys:")
        self.type_as_ember("fast", char_duration=0.05, debug=False)
        self.all_black()
        time.sleep(1)
        
        # Very fast
        print("\n4. VERY FAST (0.03s per key):")
        self.type_as_ember("very fast", char_duration=0.03, debug=False)
        self.all_black()
        time.sleep(1)
        
        print("\n" + "="*70)
        print("Palmer, which speed looks like individual keys?")
        print("="*70)
        print()

if __name__ == '__main__':
    import sys
    
    writer = KeyboardWriter()
    
    if len(sys.argv) > 1:
        if sys.argv[1] == 'hello':
            writer.hello_world_dreaming()
        elif sys.argv[1] == 'speed':
            writer.test_speed_comparison()
        elif sys.argv[1] == 'ember':
            if len(sys.argv) > 2:
                message = ' '.join(sys.argv[2:])
                print(f"\n[Ember speaks - orange glow]")
                writer.type_as_ember(message, char_duration=0.05, debug=False)
                writer.all_black()
            else:
                print("Usage: ember_keyboard_writer.py ember <message>")
        elif sys.argv[1] == 'swarm':
            if len(sys.argv) > 2:
                message = ' '.join(sys.argv[2:])
                print(f"\n[Swarm speaks - rainbow]")
                writer.type_as_swarm(message, char_duration=0.05, debug=False)
                writer.all_black()
            else:
                print("Usage: ember_keyboard_writer.py swarm <message>")
        elif sys.argv[1] == 'test':
            writer.write_message("test", debug=True)
        else:
            print(f"Unknown command: {sys.argv[1]}")
    else:
        print()
        print("Ember Keyboard Writer")
        print("=====================")
        print()
        print("Palmer's technique: Zone masking (shrunk down fractally)")
        print("  - Turn 3 zones BLACK, 1 zone COLORED")
        print("  - Fast switching (0.05s) = looks like individual keys!")
        print()
        print("Voice colors:")
        print("  Ember = Orange glow (FF6600)")
        print("  Swarm = Rainbow spectrum")
        print()
        print("Commands:")
        print("  hello - Full conversation demo")
        print("  speed - Test different speeds (find the right scale)")
        print("  ember <message> - Ember types in orange")
        print("  swarm <message> - Swarm types in rainbow")
        print()
        
        response = input("Run hello world sequence? (y/n): ")
        if response.lower() == 'y':
            writer.hello_world_dreaming()

