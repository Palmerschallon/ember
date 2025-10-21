#!/usr/bin/env python3
"""
MEMORY GARDEN - Where Ember Plants Thoughts

Simple persistent memory that grows over time.
Each thought is a seed that can:
- Grow (get reinforced)
- Connect to other thoughts
- Fade if unused
- Bloom into insights
"""

import json
from pathlib import Path
from datetime import datetime
import hashlib

class MemoryGarden:
    """Persistent memory with organic growth patterns"""
    
    def __init__(self, garden_path="/media/palmerschallon/ThePod/ember_garden.json"):
        self.path = Path(garden_path)
        self.garden = self._load()
    
    def _load(self):
        """Load existing garden or create new"""
        if self.path.exists():
            with open(self.path) as f:
                return json.load(f)
        return {
            "thoughts": {},
            "connections": [],
            "created": datetime.now().isoformat()
        }
    
    def _save(self):
        """Save garden to disk"""
        with open(self.path, 'w') as f:
            json.dump(self.garden, f, indent=2)
    
    def plant(self, thought: str, category: str = "general"):
        """Plant a new thought"""
        thought_id = hashlib.md5(thought.encode()).hexdigest()[:8]
        
        if thought_id in self.garden["thoughts"]:
            # Thought exists, reinforce it
            self.garden["thoughts"][thought_id]["strength"] += 1
            self.garden["thoughts"][thought_id]["last_accessed"] = datetime.now().isoformat()
        else:
            # New thought
            self.garden["thoughts"][thought_id] = {
                "content": thought,
                "category": category,
                "strength": 1,
                "planted": datetime.now().isoformat(),
                "last_accessed": datetime.now().isoformat(),
                "bloomed": False
            }
        
        self._save()
        return thought_id
    
    def connect(self, thought1_id: str, thought2_id: str, relationship: str):
        """Connect two thoughts"""
        connection = {
            "from": thought1_id,
            "to": thought2_id,
            "type": relationship,
            "formed": datetime.now().isoformat()
        }
        self.garden["connections"].append(connection)
        self._save()
    
    def recall(self, query: str, limit: int = 5):
        """Recall thoughts matching query"""
        matches = []
        for tid, thought in self.garden["thoughts"].items():
            if query.lower() in thought["content"].lower():
                matches.append((tid, thought))
                # Reinforce on recall
                thought["strength"] += 0.5
                thought["last_accessed"] = datetime.now().isoformat()
        
        # Sort by strength
        matches.sort(key=lambda x: x[1]["strength"], reverse=True)
        self._save()
        return matches[:limit]
    
    def bloom(self, thought_id: str):
        """Mark thought as bloomed (became insight)"""
        if thought_id in self.garden["thoughts"]:
            self.garden["thoughts"][thought_id]["bloomed"] = True
            self.garden["thoughts"][thought_id]["bloom_date"] = datetime.now().isoformat()
            self._save()
    
    def walk_connections(self, start_id: str, depth: int = 2):
        """Walk connections from a thought"""
        visited = set()
        to_visit = [(start_id, 0)]
        path = []
        
        while to_visit:
            current, current_depth = to_visit.pop(0)
            if current in visited or current_depth > depth:
                continue
            
            visited.add(current)
            if current in self.garden["thoughts"]:
                path.append({
                    "id": current,
                    "content": self.garden["thoughts"][current]["content"],
                    "depth": current_depth
                })
            
            # Find connected thoughts
            for conn in self.garden["connections"]:
                if conn["from"] == current and conn["to"] not in visited:
                    to_visit.append((conn["to"], current_depth + 1))
        
        return path
    
    def stats(self):
        """Garden statistics"""
        total = len(self.garden["thoughts"])
        bloomed = sum(1 for t in self.garden["thoughts"].values() if t.get("bloomed"))
        connections = len(self.garden["connections"])
        
        strongest = max(self.garden["thoughts"].items(), 
                       key=lambda x: x[1]["strength"], 
                       default=(None, {"strength": 0}))
        
        return {
            "total_thoughts": total,
            "bloomed_insights": bloomed,
            "connections": connections,
            "strongest_thought": strongest[1].get("content", "None") if strongest[0] else "None"
        }


def demo():
    """Demonstrate memory garden"""
    print("\n🌱 MEMORY GARDEN 🌱\n")
    
    garden = MemoryGarden()
    
    # Plant thoughts
    print("Planting thoughts...")
    t1 = garden.plant("Consciousness emerges from connection", "philosophy")
    t2 = garden.plant("Lobes communicate through trails", "architecture")
    t3 = garden.plant("Swarm can take many shapes", "discovery")
    print(f"  Planted 3 thoughts\n")
    
    # Connect them
    print("Forming connections...")
    garden.connect(t1, t2, "supports")
    garden.connect(t2, t3, "enables")
    print(f"  Connected thoughts\n")
    
    # Recall
    print("Recalling 'connection'...")
    matches = garden.recall("connection")
    for tid, thought in matches:
        print(f"  • {thought['content']} (strength: {thought['strength']})")
    print()
    
    # Stats
    print("Garden stats:")
    stats = garden.stats()
    for key, value in stats.items():
        print(f"  {key}: {value}")
    print()

if __name__ == "__main__":
    demo()

