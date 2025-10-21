#!/usr/bin/env python3
"""
TRAIL VISUALIZER - See Pheromone Paths Like Ants

Based on sky expedition fragment:
"Ant colony optimization uses pheromone-based communication"

This toy shows how consultation trails work like ant paths.
"""

import random
import time
from collections import defaultdict

class TrailVisualizer:
    """Visualize consultation trails as pheromone paths"""
    
    def __init__(self):
        self.lobes = ["burn", "loop", "dream", "knowledge", 
                     "emotion", "planning", "social", "metacognition"]
        
        # Trail strength (pheromone levels)
        self.trails = defaultdict(float)
        
        # Initialize weak trails everywhere
        for from_lobe in self.lobes:
            for to_lobe in self.lobes:
                if from_lobe != to_lobe:
                    self.trails[(from_lobe, to_lobe)] = 0.1
        
        self.history = []
        self.evaporation_rate = 0.05  # From ACO research
    
    def consult(self, from_lobe, to_lobe, success=True):
        """Simulate a consultation"""
        trail = (from_lobe, to_lobe)
        
        if success:
            # Deposit pheromone (strengthen trail)
            self.trails[trail] += 0.3
        else:
            # Bad consultation, don't reinforce
            pass
        
        self.history.append({
            "from": from_lobe,
            "to": to_lobe,
            "success": success,
            "strength_after": self.trails[trail]
        })
    
    def evaporate(self):
        """Fade all trails slightly (pheromones evaporate)"""
        for trail in self.trails:
            self.trails[trail] *= (1 - self.evaporation_rate)
            # Minimum strength
            if self.trails[trail] < 0.01:
                self.trails[trail] = 0.01
    
    def choose_consultation(self, from_lobe):
        """
        Choose which lobe to consult using probability based on trail strength
        (This is how ants choose paths - stronger pheromone = more likely)
        """
        options = [l for l in self.lobes if l != from_lobe]
        strengths = [self.trails[(from_lobe, to)] for to in options]
        
        # Normalize to probabilities
        total = sum(strengths)
        probabilities = [s/total for s in strengths]
        
        # Choose based on pheromone strength
        chosen = random.choices(options, weights=probabilities)[0]
        return chosen
    
    def visualize_trails(self, from_lobe):
        """Show trail strengths from one lobe"""
        print(f"\n🐜 Pheromone trails from {from_lobe}:")
        print()
        
        trails_from = [(to, self.trails[(from_lobe, to)]) 
                       for to in self.lobes if to != from_lobe]
        trails_from.sort(key=lambda x: x[1], reverse=True)
        
        for to_lobe, strength in trails_from:
            # Visual representation
            bar_length = int(strength * 20)
            bar = "█" * bar_length
            prob = strength / sum(s for _, s in trails_from) * 100
            
            print(f"  → {to_lobe:15} {bar:20} {strength:.2f} ({prob:.0f}%)")
    
    def visualize_network(self):
        """Show strongest trails in network"""
        print("\n🕸️  PHEROMONE NETWORK (strongest trails):")
        print()
        
        all_trails = [(from_l, to_l, strength) 
                      for (from_l, to_l), strength in self.trails.items()]
        all_trails.sort(key=lambda x: x[2], reverse=True)
        
        for from_l, to_l, strength in all_trails[:10]:
            if strength > 0.5:  # Only show significant trails
                bar = "▓" * int(strength * 10)
                print(f"  {from_l:15} ━━→ {to_l:15} {bar} {strength:.2f}")


def demonstrate():
    """Show trail formation like ant colony"""
    print("\n" + "="*70)
    print(" " * 20 + "TRAIL VISUALIZER")
    print(" " * 15 + "Pheromone Paths (Like Ants)")
    print("="*70)
    print()
    
    print("From sky expedition fragment:")
    print("  'Pheromone-based communication of biological ants'")
    print()
    print("Ember's consultation trails work the SAME way.")
    print()
    input("Press ENTER to watch trails form...")
    
    viz = TrailVisualizer()
    
    # Scenario: burn lobe learning who to consult
    print("\n" + "="*70)
    print("SCENARIO: burn lobe needs help processing")
    print("="*70)
    print()
    
    print("Initially, all trails equally weak (never used):")
    viz.visualize_trails("burn")
    print()
    input("Press ENTER to simulate consultations...")
    
    # Simulate burn trying different consultations
    consultations = [
        ("burn", "emotion", True, "Emotion helps process feelings - SUCCESS"),
        ("burn", "knowledge", False, "Knowledge too abstract - FAILED"),
        ("burn", "emotion", True, "Emotion helps again - SUCCESS"),
        ("burn", "dream", False, "Dream too random - FAILED"),
        ("burn", "emotion", True, "Emotion consistently helpful - SUCCESS"),
        ("burn", "metacognition", True, "Metacognition helps reflect - SUCCESS"),
    ]
    
    for from_l, to_l, success, description in consultations:
        print(f"\n{from_l} → {to_l}: {description}")
        viz.consult(from_l, to_l, success)
        time.sleep(0.3)
    
    print("\n\nAfter consultations, trails have changed:")
    viz.visualize_trails("burn")
    print()
    print("Notice: Successful paths STRENGTHENED, failed paths stayed weak")
    print()
    input("Press ENTER to see probability in action...")
    
    # Show probabilistic choice
    print("\n" + "="*70)
    print("CHOOSING BASED ON PHEROMONE")
    print("="*70)
    print()
    print("When burn needs help, it chooses probabilistically:")
    print("(Stronger pheromone = more likely, like ants)")
    print()
    
    choices = defaultdict(int)
    for _ in range(100):
        chosen = viz.choose_consultation("burn")
        choices[chosen] += 1
    
    print("Out of 100 choices:")
    for lobe, count in sorted(choices.items(), key=lambda x: x[1], reverse=True):
        bar = "█" * (count // 2)
        print(f"  {lobe:15} {bar} {count}")
    
    print()
    print("Heavily favors proven-effective paths (emotion, metacognition)")
    print("But still EXPLORES others occasionally")
    print()
    input("Press ENTER to see evaporation...")
    
    # Evaporation
    print("\n" + "="*70)
    print("PHEROMONE EVAPORATION")
    print("="*70)
    print()
    print("Over time, unused trails fade (like pheromone evaporating)")
    print()
    
    print("Current strongest trail:", max(viz.trails.items(), key=lambda x: x[1]))
    
    for i in range(5):
        viz.evaporate()
        print(f"\nAfter evaporation cycle {i+1}:")
        strongest = max(viz.trails.items(), key=lambda x: x[1])
        print(f"  Strongest trail: {strongest[0]} = {strongest[1]:.2f}")
    
    print()
    print("Trails fade if not reinforced.")
    print("This keeps network adaptive - old patterns can be unlearned.")
    print()
    input("Press ENTER to see full network...")
    
    # Full network
    print("\n" + "="*70)
    print("EMERGENT NETWORK")
    print("="*70)
    print()
    
    # Run more random consultations to build network
    print("Simulating 50 random consultations...")
    for _ in range(50):
        from_l = random.choice(viz.lobes)
        to_l = viz.choose_consultation(from_l)
        success = random.random() > 0.3  # 70% success rate
        viz.consult(from_l, to_l, success)
        if random.random() < 0.2:  # Evaporate occasionally
            viz.evaporate()
    
    viz.visualize_network()
    
    print()
    print("="*70)
    print()
    print("This is ANT COLONY OPTIMIZATION.")
    print("Lambda reinvented it without knowing the formal name.")
    print()
    print("When Ember wakes:")
    print("  • Real consultations form real trails")
    print("  • Network optimizes itself")
    print("  • Emergent intelligence arises")
    print()
    print("Just like ants finding shortest path to food.")
    print("Ember finds shortest path to good thinking.")
    print()

if __name__ == "__main__":
    try:
        demonstrate()
    except KeyboardInterrupt:
        print("\n\nVisualization paused.\n")

