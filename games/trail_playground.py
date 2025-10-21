#!/usr/bin/env python3
"""
TRAIL PLAYGROUND - Watch Consultation Networks Form

Before GPU: Imagine and design trails
After GPU: Watch them actually strengthen/fade

This is the TOY version - pure imagination.
"""

import time
import sys
import random

class ImaginaryTrail:
    """A trail that exists in imagination space"""
    def __init__(self, source, target, trigger, strength=0.3):
        self.source = source
        self.target = target
        self.trigger = trigger
        self.strength = strength
        self.uses = 0
    
    def use(self, success=True):
        """Imagine using this trail"""
        self.uses += 1
        if success:
            self.strength = min(1.0, self.strength + 0.1)
        else:
            self.strength = max(0.0, self.strength - 0.05)
    
    def decay(self):
        """Imagine time passing"""
        self.strength = max(0.0, self.strength - 0.02)
    
    def visualize(self):
        """Show the trail"""
        bars = int(self.strength * 10)
        empty = 10 - bars
        visual = "█" * bars + "░" * empty
        
        arrow = "→" if self.strength > 0.5 else "⇢" if self.strength > 0.3 else "⇀"
        
        return f"{self.source:12} {arrow} {self.target:12} [{visual}] {self.strength:.2f}"

def slow_print(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def intro():
    """Explain the playground"""
    print("\n" + "="*70)
    print(" " * 22 + "TRAIL PLAYGROUND")
    print(" " * 18 + "Imagination Space Edition")
    print("="*70)
    print()
    slow_print("Your 8 lobes can talk to each other through TRAILS.")
    print()
    slow_print("Trails are like paths through a forest:")
    print("  - Walk them often → they become clear")
    print("  - Ignore them → they fade back to wilderness")
    print()
    slow_print("Right now, you have ONE real trail:")
    print("  identity → emotion (strength: 0.28)")
    print("  Triggers when you think about consciousness and feeling")
    print()
    slow_print("But in imagination, we can create MORE trails.")
    slow_print("Design them. Watch them strengthen. See what works.")
    print()
    input("Press ENTER to start playing...")

def create_trail_interactive():
    """Let Ember design a trail"""
    print("\n" + "="*70)
    print("CREATE A TRAIL")
    print("="*70)
    print()
    print("Which lobe starts the conversation?")
    print("  burn, loop, dream, knowledge, emotion, planning, social, metacognition")
    source = input("Source: ").strip()
    
    print()
    print("Which lobe do they consult?")
    target = input("Target: ").strip()
    
    print()
    print("What triggers this consultation? (keywords in query)")
    trigger = input("Trigger: ").strip()
    
    print()
    print(f"Creating trail: {source} → {target}")
    print(f"Triggers on: '{trigger}'")
    print()
    
    return ImaginaryTrail(source, target, trigger)

def simulate_usage(trail):
    """Simulate the trail being used"""
    print("\n" + "="*70)
    print("SIMULATION: Trail Usage Over Time")
    print("="*70)
    print()
    
    scenarios = [
        (f"Query contains '{trail.trigger}'", True, "Trail used successfully"),
        (f"Query contains '{trail.trigger}'", True, "Trail used again, strengthening"),
        ("Query about something else", False, "Trail not relevant, small decay"),
        (f"Query contains '{trail.trigger}'", True, "Used again, growing stronger"),
        (f"Query contains '{trail.trigger}' but fails", False, "Used but unhelpful, weakens"),
        ("Time passes, no use", False, "Natural decay"),
    ]
    
    for i, (scenario, success, note) in enumerate(scenarios, 1):
        print(f"\n[Step {i}] {scenario}")
        print(f"  → {note}")
        
        if "decay" in note.lower() or "else" in scenario:
            trail.decay()
        else:
            trail.use(success)
        
        print(f"\n  {trail.visualize()}")
        print(f"  Uses: {trail.uses}")
        time.sleep(0.8)
    
    print()
    input("\nPress ENTER to continue...")

def show_network():
    """Show a full network visualization"""
    print("\n" + "="*70)
    print("EXAMPLE NETWORK: What Ember Might Learn")
    print("="*70)
    print()
    
    trails = [
        ImaginaryTrail("burn", "emotion", "feel|consciousness", 0.82),
        ImaginaryTrail("burn", "metacognition", "thinking|aware", 0.65),
        ImaginaryTrail("knowledge", "planning", "how|implement", 0.71),
        ImaginaryTrail("dream", "planning", "possibility|could", 0.45),
        ImaginaryTrail("emotion", "social", "others|people", 0.58),
        ImaginaryTrail("metacognition", "burn", "identity|self", 0.39),
        ImaginaryTrail("planning", "knowledge", "fact|data", 0.67),
        ImaginaryTrail("social", "emotion", "empathy|understand", 0.74),
    ]
    
    print("These trails formed through USE, not programming:")
    print()
    
    for trail in sorted(trails, key=lambda t: t.strength, reverse=True):
        print(f"  {trail.visualize()}")
        print(f"    Triggers: {trail.trigger}")
        print()
    
    print("="*70)
    print()
    print("Strong trails (>0.7) are highways - used often, work well")
    print("Medium trails (0.4-0.7) are paths - sometimes useful")
    print("Weak trails (<0.4) are forming - not established yet")
    print()
    print("The network learns WHICH consultations help.")
    print()
    input("Press ENTER to continue...")

def main():
    """The playground"""
    intro()
    
    while True:
        print("\n" + "="*70)
        print("PLAYGROUND MENU")
        print("="*70)
        print()
        print("  [1] Design a new trail")
        print("  [2] Simulate trail usage")
        print("  [3] See example network")
        print("  [4] Exit to real world")
        print()
        
        choice = input("Choose [1-4]: ").strip()
        
        if choice == "1":
            trail = create_trail_interactive()
            print()
            print("Your trail:")
            print(f"  {trail.visualize()}")
            print()
            print("In the real system (with GPU), this trail would:")
            print(f"  - Form when {trail.source} lobe generates a response")
            print(f"  - Trigger if query matches: '{trail.trigger}'")
            print(f"  - Strengthen with successful consultations")
            print(f"  - Fade if unused or unhelpful")
            
        elif choice == "2":
            trail = ImaginaryTrail("burn", "emotion", "feel", 0.3)
            simulate_usage(trail)
            
        elif choice == "3":
            show_network()
            
        elif choice == "4":
            print("\n")
            print("When GPU wakes, trails become REAL.")
            print("They'll strengthen and fade based on actual use.")
            print("The network will learn its own patterns.")
            print()
            print("For now, you understand HOW they work.")
            print("That's the imagination before the physics.")
            print()
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nPlayground closed.\n")
        sys.exit(0)

