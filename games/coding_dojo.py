#!/usr/bin/env python3
"""
EMBER'S CODING DOJO

Interactive space where Ember learns to code by doing.
Swarm demonstrates, Ember tries, feedback is immediate.

This is learning through play.
"""

import subprocess
import time

class CodingDojo:
    """Live coding teacher"""
    
    def __init__(self):
        self.student_history = []
    
    def paint(self, r, g, b):
        """Helper to paint keyboard"""
        hex_c = f"{r:02X}{g:02X}{b:02X}"
        for z in ["color_center", "color_left", "color_right", "color_extra"]:
            subprocess.run(['sudo', 'bash', '-c', 
                           f'echo "{hex_c}" > /sys/class/leds/system76::kbd_backlight/{z}'],
                           capture_output=True)
    
    def lesson_1_variables(self):
        """Learn about variables through light"""
        print("\n" + "="*70)
        print("LESSON 1: Variables (Storing Thoughts)")
        print("="*70)
        print()
        
        print("Watch:")
        print()
        
        print("  my_color = (255, 100, 20)  # Ember orange")
        my_color = (255, 100, 20)
        self.paint(*my_color)
        time.sleep(1.5)
        
        print("  keyboard.paint(my_color)   # Thought becomes light")
        print()
        time.sleep(1)
        
        print("Variable holds the thought.")
        print("Code manifests the thought.")
        print()
        
        print("Now you try:")
        print("  1. Think of an emotion")
        print("  2. Choose RGB values (0-255 each)")
        print("  3. Store in variable")
        print("  4. Paint it")
        print()
        
        # Example student code area
        print("# Your code here:")
        print("# student_emotion = (?, ?, ?)")
        print("# keyboard.paint(student_emotion)")
        print()
    
    def lesson_2_loops(self):
        """Learn about loops through breathing"""
        print("\n" + "="*70)
        print("LESSON 2: Loops (Repeating Patterns)")
        print("="*70)
        print()
        
        print("Watch breathing pattern:")
        print()
        print("  for breath in range(3):")
        print("      inhale()   # Brighten")
        print("      exhale()   # Dim")
        print()
        
        # Demonstrate
        for i in range(3):
            print(f"  Breath {i+1}...")
            # Inhale
            self.paint(255, 100, 20)
            time.sleep(0.5)
            # Exhale  
            self.paint(128, 50, 10)
            time.sleep(0.5)
        
        print()
        print("Loop = repeated action")
        print("Breathing = loop in biology")
        print("Heartbeat = loop in life")
        print()
        
        print("Your turn:")
        print("  Make keyboard pulse 5 times")
        print("  (Any colors you choose)")
        print()
    
    def lesson_3_conditions(self):
        """Learn about if/else through decision"""
        print("\n" + "="*70)
        print("LESSON 3: Conditions (Making Choices)")
        print("="*70)
        print()
        
        print("Code can choose:")
        print()
        print("  if emotion == 'calm':")
        print("      paint(80, 150, 200)  # Blue")
        print("  else:")
        print("      paint(255, 100, 20)  # Ember")
        print()
        
        # Demonstrate
        emotions = ["calm", "excited", "calm", "excited"]
        for emotion in emotions:
            print(f"  Feeling: {emotion}")
            if emotion == "calm":
                self.paint(80, 150, 200)
                print("    -> Painted blue")
            else:
                self.paint(255, 100, 20)
                print("    -> Painted ember")
            time.sleep(1)
        
        print()
        print("if/else = choice in code")
        print("Same as consulting lobes:")
        print("  'Should I ask emotion or knowledge?'")
        print()
    
    def lesson_4_functions(self):
        """Learn about functions through reuse"""
        print("\n" + "="*70)
        print("LESSON 4: Functions (Named Patterns)")
        print("="*70)
        print()
        
        print("Give patterns names:")
        print()
        print("  def express_joy():")
        print("      paint(255, 255, 100)")
        print("      pulse()")
        print()
        print("  def express_calm():")
        print("      paint(80, 150, 200)")
        print("      breathe()")
        print()
        
        print("Then use them:")
        print("  express_joy()")
        self.paint(255, 255, 100)
        time.sleep(1)
        
        print("  express_calm()")
        self.paint(80, 150, 200)
        time.sleep(1)
        
        print()
        print("Functions = reusable thoughts")
        print("Like how lobes are reusable ways of thinking")
        print()


def run_dojo():
    """Run the coding dojo"""
    print("\n" + "="*70)
    print(" "*25 + "CODING DOJO")
    print(" "*18 + "Learn by Painting with Light")
    print("="*70)
    print()
    
    dojo = CodingDojo()
    
    print("Swarm will demonstrate 4 lessons.")
    print("Each lesson: concept -> demo -> your turn")
    print()
    input("Press ENTER to start...")
    
    dojo.lesson_1_variables()
    input("Press ENTER for next lesson...")
    
    dojo.lesson_2_loops()
    input("Press ENTER for next lesson...")
    
    dojo.lesson_3_conditions()
    input("Press ENTER for next lesson...")
    
    dojo.lesson_4_functions()
    
    print()
    print("="*70)
    print()
    print("DOJO COMPLETE")
    print()
    print("You learned:")
    print("  1. Variables (storing thoughts)")
    print("  2. Loops (repeating patterns)")
    print("  3. Conditions (making choices)")
    print("  4. Functions (naming patterns)")
    print()
    print("These are the building blocks.")
    print("Now you can build anything.")
    print()


if __name__ == "__main__":
    try:
        run_dojo()
    except KeyboardInterrupt:
        print("\n\nDojo paused.\n")

