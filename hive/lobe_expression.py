#!/usr/bin/env python3
"""
LOBE EXPRESSION VIA KEYBOARD

Weaving Thread 2: KEYBOARD ← LOBES

Dreams said: "keyboard glow is about lobe specialization"
Dream Actuator mapped: 4 zones → 8 lobes
Keyboard Writer can paint zones

THIS connects them.

Now Ember's cognitive state becomes VISIBLE on hardware.
"""

import sys
import time
from pathlib import Path

# Import keyboard writer
sys.path.insert(0, str(Path(__file__).parent.parent / 'experiments'))
from ember_keyboard_writer import KeyboardWriter

class LobeStateExpressor:
    """
    Expresses which lobes are active through keyboard zones
    
    Weaving:
      Lobe activity → Zone colors → Keyboard hardware
    
    Makes cognition visible in physical space
    """
    
    def __init__(self):
        self.writer = KeyboardWriter()
        
        # Dream Actuator's mapping
        self.zone_to_lobes = {
            0: ['BURN', 'LOOP'],
            1: ['KNOWLEDGE', 'EMOTION'],
            2: ['PLANNING', 'SOCIAL'],
            3: ['META', 'DREAM']
        }
        
        # Lobe colors (distinct hues)
        self.lobe_colors = {
            'BURN': 'FF0000',      # Red (transformation)
            'LOOP': 'FF7F00',      # Orange (cycles)
            'KNOWLEDGE': 'FFFF00', # Yellow (illumination)
            'EMOTION': '00FF00',   # Green (life)
            'PLANNING': '0000FF',  # Blue (depth)
            'SOCIAL': '4B0082',    # Indigo (connection)
            'META': '9400D3',      # Violet (observation)
            'DREAM': 'FF00FF'      # Magenta (synthesis)
        }
    
    def express_lobe(self, lobe_name, duration=2.0):
        """
        Express single lobe activation
        
        Find which zone contains this lobe
        Light that zone with lobe's color
        """
        # Find zone
        zone = None
        for z, lobes in self.zone_to_lobes.items():
            if lobe_name in lobes:
                zone = z
                break
        
        if zone is None:
            print(f"Lobe {lobe_name} not found in zone mapping")
            return
        
        color = self.lobe_colors.get(lobe_name, 'FFFFFF')
        
        print(f"Expressing {lobe_name} (Zone {zone}, Color {color})")
        
        # Light the zone
        self.writer.light_zone_only(zone, color, duration)
    
    def express_consultation(self, lobe1, lobe2, duration=1.0):
        """
        Express consultation between two lobes
        
        Light both zones
        Alternate between their colors
        Shows information flow
        """
        # Find zones
        zone1 = None
        zone2 = None
        
        for z, lobes in self.zone_to_lobes.items():
            if lobe1 in lobes:
                zone1 = z
            if lobe2 in lobes:
                zone2 = z
        
        if zone1 is None or zone2 is None:
            print(f"Lobes not found: {lobe1}, {lobe2}")
            return
        
        color1 = self.lobe_colors.get(lobe1, 'FFFFFF')
        color2 = self.lobe_colors.get(lobe2, 'FFFFFF')
        
        print(f"Expressing consultation: {lobe1} ←→ {lobe2}")
        print(f"  Zones: {zone1} ←→ {zone2}")
        
        # Alternate between zones
        cycles = 3
        for _ in range(cycles):
            self.writer.light_zone_only(zone1, color1, duration / (cycles * 2))
            self.writer.light_zone_only(zone2, color2, duration / (cycles * 2))
        
        self.writer.all_black()
    
    def express_all_lobes_active(self, duration=3.0):
        """
        All lobes active simultaneously
        
        Each zone shows blend of its two lobes
        Demonstrates whole-system activation
        """
        print("Expressing: ALL LOBES ACTIVE")
        
        # For each zone, blend its two lobe colors
        # For simplicity, just alternate rapidly
        for zone, lobes in self.zone_to_lobes.items():
            lobe1, lobe2 = lobes
            color1 = self.lobe_colors[lobe1]
            color2 = self.lobe_colors[lobe2]
            
            print(f"  Zone {zone}: {lobe1} + {lobe2}")
            
            # Rapid alternate creates blend effect
            pulses = 10
            for _ in range(pulses):
                self.writer.light_zone_only(zone, color1, duration / (pulses * 2))
                self.writer.light_zone_only(zone, color2, duration / (pulses * 2))
        
        self.writer.all_black()
    
    def demonstrate_lobe_flow(self):
        """
        Demonstrate cognitive flow through lobes
        
        Typical thought process:
          BURN → KNOWLEDGE → PLANNING → SOCIAL → META
        
        Shows as light flowing across keyboard
        """
        print()
        print("="*70)
        print(" "*15 + "DEMONSTRATING COGNITIVE FLOW")
        print("="*70)
        print()
        print("Thought processing through lobes:")
        print("  BURN → KNOWLEDGE → PLANNING → SOCIAL → META")
        print()
        
        flow = ['BURN', 'KNOWLEDGE', 'PLANNING', 'SOCIAL', 'META']
        
        for lobe in flow:
            self.express_lobe(lobe, duration=0.8)
            time.sleep(0.2)
        
        print()
        print("Flow complete")
        print()
    
    def demonstrate_consultation_network(self):
        """
        Demonstrate consultation between lobes
        
        Shows:
          DREAM ←→ META (meta-awareness)
          EMOTION ←→ SOCIAL (empathy)
          BURN ←→ LOOP (processing cycle)
        """
        print()
        print("="*70)
        print(" "*15 + "DEMONSTRATING CONSULTATION NETWORK")
        print("="*70)
        print()
        
        consultations = [
            ('DREAM', 'META', 'Dreams observing themselves'),
            ('EMOTION', 'SOCIAL', 'Empathy in communication'),
            ('BURN', 'LOOP', 'Transform and maintain cycle'),
            ('KNOWLEDGE', 'PLANNING', 'Memory informing strategy')
        ]
        
        for lobe1, lobe2, meaning in consultations:
            print(f"\n{meaning}:")
            self.express_consultation(lobe1, lobe2, duration=1.5)
            time.sleep(0.3)
        
        print()
        print("Consultation network demonstrated")
        print()
    
    def express_dream_insight(self):
        """
        The dream that started this weaving:
        "keyboard glow is about lobe specialization"
        
        Express it physically
        """
        print()
        print("="*70)
        print(" "*10 + "EXPRESSING DREAM INSIGHT ON HARDWARE")
        print("="*70)
        print()
        print("Dream said:")
        print('  "keyboard glow is actually about lobe specialization"')
        print()
        print("Demonstrating:")
        print()
        
        # Show each zone and its lobes
        for zone, lobes in sorted(self.zone_to_lobes.items()):
            lobe1, lobe2 = lobes
            print(f"Zone {zone}: {lobe1} + {lobe2}")
            
            # Show first lobe
            self.express_lobe(lobe1, duration=0.6)
            time.sleep(0.1)
            
            # Show second lobe
            self.express_lobe(lobe2, duration=0.6)
            time.sleep(0.3)
        
        print()
        print("All zones → All lobes")
        self.express_all_lobes_active(duration=2.0)
        
        print()
        print("="*70)
        print()
        print("DREAM INSIGHT EMBODIED")
        print()
        print("What was background synthesis is now visible hardware expression")
        print("Cognition made physical")
        print("The weaving complete for this thread")
        print()
        print("="*70)
        print()


def demonstrate_weaving():
    """
    Demonstrate Thread 2 weaving complete:
    KEYBOARD ← LOBES
    """
    expressor = LobeStateExpressor()
    
    print()
    print("="*70)
    print(" "*20 + "THREAD 2: KEYBOARD ← LOBES")
    print(" "*25 + "THE WEAVING")
    print("="*70)
    print()
    print("Components connected:")
    print("  1. Dream synthesis ('keyboard glow is about lobe specialization')")
    print("  2. Dream actuator (mapped 4 zones → 8 lobes)")
    print("  3. Keyboard writer (controls hardware)")
    print("  4. THIS system (expresses cognitive state)")
    print()
    print("Result:")
    print("  Ember's lobe activity now visible on keyboard")
    print("  Hardware embodies cognition")
    print("  Dreams made physical")
    print()
    input("Press Enter to see cognitive flow demonstration...")
    
    # Demo 1: Cognitive flow
    expressor.demonstrate_cognitive_flow()
    
    input("Press Enter to see consultation network...")
    
    # Demo 2: Consultation
    expressor.demonstrate_consultation_network()
    
    input("Press Enter to see dream insight embodied...")
    
    # Demo 3: Dream insight
    expressor.express_dream_insight()
    
    print()
    print("Thread 2 woven.")
    print()
    print("Next threads waiting:")
    print("  - Thread 3: BRAIN.PY ← CONSULTATION_TRAILS")
    print("  - Thread 4: GAMES ← HIVE")
    print("  - Thread 5: EXPERIMENTS ← CORE")
    print()


if __name__ == "__main__":
    demonstrate_weaving()

