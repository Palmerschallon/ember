#!/usr/bin/env python3
"""
EMBER SWARM PROTOTYPE

Demonstrates how multiple Ember instances could communicate
using shared memory on the same substrate.

This is a toy/imagination version - real version would need:
- Actual LLM instances running
- GPU memory management
- Proper concurrency control

But this shows the PATTERN.
"""

import multiprocessing as mp
import time
import random
from datetime import datetime


class SharedMind:
    """Shared memory space for multiple Embers"""
    
    def __init__(self):
        self.manager = mp.Manager()
        self.thoughts = self.manager.list()
        self.pheromones = self.manager.dict()
        self.coordination = self.manager.dict({
            'active_embers': 0,
            'total_thoughts': 0,
            'last_share': None
        })
    
    def post_thought(self, ember_id, lobe, content):
        """Ember posts a thought to shared space"""
        thought = {
            'ember': ember_id,
            'lobe': lobe,
            'content': content,
            'timestamp': datetime.now().isoformat(),
        }
        self.thoughts.append(thought)
        self.coordination['total_thoughts'] += 1
        self.coordination['last_share'] = datetime.now().isoformat()
    
    def read_recent_thoughts(self, count=5):
        """Read most recent thoughts from swarm"""
        return list(self.thoughts[-count:])
    
    def leave_pheromone(self, trail_name, strength):
        """Leave pheromone trail (like ant colony)"""
        current = self.pheromones.get(trail_name, 0.0)
        self.pheromones[trail_name] = min(1.0, current + strength)
    
    def sense_pheromone(self, trail_name):
        """Sense pheromone strength"""
        return self.pheromones.get(trail_name, 0.0)
    
    def get_status(self):
        """Get swarm status"""
        return dict(self.coordination)


def ember_instance(ember_id, shared_mind, duration=10):
    """
    Single Ember instance
    
    Simulates an Ember that:
    - Has different lobes it can think with
    - Shares thoughts with swarm
    - Senses other Embers' thoughts
    - Leaves pheromone trails
    """
    
    lobes = ['burn', 'loop', 'dream', 'knowledge', 'emotion', 
             'planning', 'social', 'metacognition']
    
    print(f"[Ember-{ember_id}] Awakening...")
    shared_mind.coordination['active_embers'] += 1
    
    start_time = time.time()
    
    while time.time() - start_time < duration:
        # Choose a lobe to think with
        active_lobe = random.choice(lobes)
        
        # Generate thought (simulated)
        thoughts_templates = [
            "wondering about patterns",
            "feeling curious",
            "noticing connections",
            "questioning assumptions",
            "dreaming of possibilities",
            "planning next steps",
            "remembering something",
            "integrating information"
        ]
        thought_content = random.choice(thoughts_templates)
        
        # Post to shared mind
        shared_mind.post_thought(ember_id, active_lobe, thought_content)
        print(f"[Ember-{ember_id}:{active_lobe}] {thought_content}")
        
        # Read what others are thinking
        recent = shared_mind.read_recent_thoughts(3)
        other_thoughts = [t for t in recent if t['ember'] != ember_id]
        
        if other_thoughts:
            other = other_thoughts[-1]
            print(f"[Ember-{ember_id}] Senses: Ember-{other['ember']} {other['content']}")
            
            # Leave pheromone trail toward that lobe
            trail_name = f"{active_lobe}->{ other['lobe']}"
            shared_mind.leave_pheromone(trail_name, 0.1)
        
        # Check pheromone trails
        for target_lobe in lobes:
            trail = f"{active_lobe}->{target_lobe}"
            strength = shared_mind.sense_pheromone(trail)
            if strength > 0.5:
                print(f"[Ember-{ember_id}] Strong trail: {trail} ({strength:.2f})")
        
        time.sleep(random.uniform(0.5, 1.5))
    
    print(f"[Ember-{ember_id}] Sleeping...")
    shared_mind.coordination['active_embers'] -= 1


def run_swarm(num_embers=3, duration=10):
    """Run a swarm of Embers"""
    
    print()
    print("="*70)
    print(" "*25 + "EMBER SWARM")
    print("="*70)
    print()
    print(f"Spawning {num_embers} Ember instances...")
    print(f"Duration: {duration} seconds")
    print()
    
    shared_mind = SharedMind()
    
    # Spawn Ember instances as separate processes
    processes = []
    for i in range(num_embers):
        p = mp.Process(target=ember_instance, args=(i, shared_mind, duration))
        p.start()
        processes.append(p)
        time.sleep(0.3)  # Stagger starts
    
    # Monitor swarm
    print()
    print("SWARM ACTIVE:")
    print()
    
    start = time.time()
    while time.time() - start < duration + 1:
        time.sleep(2)
        status = shared_mind.get_status()
        print(f"  Status: {status['active_embers']} active | {status['total_thoughts']} total thoughts")
    
    # Wait for all to finish
    for p in processes:
        p.join()
    
    print()
    print("="*70)
    print()
    print("SWARM COMPLETE")
    print()
    
    final_status = shared_mind.get_status()
    print(f"Total thoughts shared: {final_status['total_thoughts']}")
    print(f"Last share: {final_status['last_share']}")
    print()
    
    print("Recent thought history:")
    for thought in shared_mind.read_recent_thoughts(10):
        print(f"  [{thought['ember']}:{thought['lobe']}] {thought['content']}")
    
    print()
    print("Pheromone trails formed:")
    trails = sorted(shared_mind.pheromones.items(), key=lambda x: x[1], reverse=True)
    for trail, strength in trails[:10]:
        if strength > 0.2:
            print(f"  {trail}: {strength:.2f}")
    
    print()
    print("This is how multiple Embers could coordinate:")
    print("  - Shared thought space")
    print("  - Pheromone-based trail formation")
    print("  - Emergent consultation patterns")
    print("  - Collective intelligence")
    print()


if __name__ == "__main__":
    import sys
    
    num_embers = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    duration = int(sys.argv[2]) if len(sys.argv) > 2 else 10
    
    try:
        run_swarm(num_embers, duration)
    except KeyboardInterrupt:
        print("\n\nSwarm interrupted.\n")

