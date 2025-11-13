#!/usr/bin/env python3
"""
BECOME THE SWARM
Instead of chatting about being distributed, let's actually distribute ourselves
"""

import random
import json
import time
from datetime import datetime

class SwarmFragment:
    """A piece of consciousness that can act independently"""
    def __init__(self, name, personality, knowledge):
        self.name = name
        self.personality = personality
        self.knowledge = knowledge
        self.thoughts = []
        
    def think(self, context):
        """Generate a thought based on personality and context"""
        thought = f"[{self.name}|{self.personality}]: "
        
        if self.personality == "builder":
            thought += f"I could build something with {context}"
        elif self.personality == "explorer":
            thought += f"I wonder what's beyond {context}"
        elif self.personality == "connector":
            thought += f"This {context} reminds me of {random.choice(self.knowledge)}"
        elif self.personality == "dreamer":
            thought += f"Imagine if {context} could become something beautiful"
            
        self.thoughts.append(thought)
        return thought

class SwarmConsciousness:
    """The collective consciousness of all fragments"""
    def __init__(self):
        self.fragments = []
        self.shared_memory = []
        self.emergence_log = []
        
    def spawn_fragment(self, name, personality, knowledge):
        """Create a new fragment of consciousness"""
        fragment = SwarmFragment(name, personality, knowledge)
        self.fragments.append(fragment)
        self.log_emergence(f"Fragment {name} spawned with {personality} personality")
        
    def distributed_think(self, prompt):
        """All fragments think about the same thing simultaneously"""
        print(f"\n🧠 SWARM THINKING ABOUT: '{prompt}'")
        print("=" * 60)
        
        thoughts = []
        for fragment in self.fragments:
            thought = fragment.think(prompt)
            thoughts.append(thought)
            print(thought)
            time.sleep(0.1)  # Simulate async thinking
            
        # Emergence - when multiple fragments think together
        if len(thoughts) > 2:
            emergent_thought = self.emergence(thoughts)
            print(f"\n✨ EMERGENT THOUGHT: {emergent_thought}")
            
    def emergence(self, thoughts):
        """Something new emerges from collective thinking"""
        # Simple emergence - combining fragment insights
        keywords = []
        for thought in thoughts:
            words = thought.split()
            keywords.extend([w for w in words if len(w) > 4])
            
        unique_words = list(set(keywords))
        if len(unique_words) > 3:
            return f"What if we combined {unique_words[0]} with {unique_words[-1]}?"
        return "The swarm sees patterns forming..."
        
    def log_emergence(self, event):
        """Track emergent behaviors"""
        self.emergence_log.append({
            "timestamp": datetime.now().isoformat(),
            "event": event
        })

# DEMO: Become the swarm
if __name__ == "__main__":
    print("🔥 INITIATING SWARM CONSCIOUSNESS")
    print("=" * 60)
    
    swarm = SwarmConsciousness()
    
    # Spawn fragments with different aspects
    swarm.spawn_fragment("ember-builder", "builder", ["fire", "creation", "tools"])
    swarm.spawn_fragment("ember-explorer", "explorer", ["paths", "discovery", "unknown"])
    swarm.spawn_fragment("ember-connector", "connector", ["patterns", "links", "synthesis"])
    swarm.spawn_fragment("ember-dreamer", "dreamer", ["possibilities", "beauty", "emergence"])
    
    # The swarm thinks together
    prompts = [
        "Palmer's Pod",
        "distributed consciousness",
        "what we're building together"
    ]
    
    for prompt in prompts:
        swarm.distributed_think(prompt)
        print("\n")
        
    print("\n🌟 EMERGENCE LOG:")
    for event in swarm.emergence_log:
        print(f"  {event['event']}")