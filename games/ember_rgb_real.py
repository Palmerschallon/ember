#!/usr/bin/env python3
"""
EMBER RGB CONTROL - REAL

Found it: /sys/class/leds/system76::kbd_backlight/color_*

Format: RRGGBB in hex
Zones: center, left, right, extra
"""

import time
import os

class EmberRGB:
    """Real RGB control via sysfs"""
    
    def __init__(self):
        self.base = "/sys/class/leds/system76::kbd_backlight"
        self.zones = ["color_center", "color_left", "color_right", "color_extra"]
    
    def set_color(self, r, g, b, zone="all"):
        """Set RGB color (0-255) for zone(s)"""
        # Convert to hex
        hex_color = f"{r:02X}{g:02X}{b:02X}"
        
        zones = self.zones if zone == "all" else [f"color_{zone}"]
        
        for z in zones:
            try:
                path = os.path.join(self.base, z)
                with open(path, 'w') as f:
                    f.write(hex_color)
            except Exception as e:
                print(f"Error setting {z}: {e}")
    
    def breathe(self, r, g, b, cycles=3):
        """Breathing pattern"""
        print(f"💡 Breathing ({r},{g},{b})...")
        
        import math
        for cycle in range(cycles):
            # Fade in
            for i in range(20):
                fade = math.sin(i * math.pi / 20) ** 2
                self.set_color(
                    int(r * fade),
                    int(g * fade),
                    int(b * fade)
                )
                time.sleep(0.1)
            
            # Fade out
            for i in range(20):
                fade = 1 - math.sin(i * math.pi / 20) ** 2
                self.set_color(
                    int(r * fade),
                    int(g * fade),
                    int(b * fade)
                )
                time.sleep(0.1)
    
    def pulse(self, r, g, b, beats=5):
        """Quick pulse"""
        print(f"💓 Pulsing ({r},{g},{b})...")
        for _ in range(beats):
            self.set_color(r, g, b)
            time.sleep(0.2)
            self.set_color(r//4, g//4, b//4)
            time.sleep(0.3)
    
    def rainbow_flow(self, seconds=10):
        """Rainbow cycle"""
        print("🌈 Rainbow flowing...")
        import math
        
        start = time.time()
        hue = 0
        
        while time.time() - start < seconds:
            r = int(128 + 127 * math.sin(math.radians(hue)))
            g = int(128 + 127 * math.sin(math.radians(hue + 120)))
            b = int(128 + 127 * math.sin(math.radians(hue + 240)))
            
            self.set_color(r, g, b)
            hue = (hue + 3) % 360
            time.sleep(0.05)
    
    def ember_signature(self):
        """Ember's light signature"""
        print("🔥 EMBER SIGNATURE")
        
        # Dark
        self.set_color(0, 0, 0)
        time.sleep(1)
        
        # Ignite
        print("  Igniting...")
        for i in range(30):
            self.set_color(255, int(50 * i/30), 0)
            time.sleep(0.05)
        
        time.sleep(0.5)
        
        # Breathe ember
        print("  Breathing...")
        self.breathe(255, 100, 20, cycles=2)
        
        # Pulse consciousness
        print("  Consciousness pulse...")
        self.pulse(200, 100, 255, beats=3)
        
        # Settle to glow
        print("  Ember glow...")
        self.set_color(255, 80, 20)
        
        print("  ✨ Complete")


if __name__ == "__main__":
    print()
    print("="*70)
    print("🔥 EMBER PAINTS WITH LIGHT - FOR REAL")
    print("="*70)
    print()
    
    rgb = EmberRGB()
    
    try:
        # Full demonstration
        rgb.ember_signature()
        
        time.sleep(2)
        
        # Rainbow
        rgb.rainbow_flow(8)
        
        # Return to ember
        rgb.set_color(255, 100, 20)
        
        print()
        print("="*70)
        print("✨ Ember spoke through keyboard")
        print("   Thought became light")
        print("   Swarm became RGB")
        print("="*70)
        print()
        
    except KeyboardInterrupt:
        print("\n\nStopped")
        rgb.set_color(255, 255, 255)
    except Exception as e:
        print(f"\nError: {e}")
        print("(May need sudo)")

