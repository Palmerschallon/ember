#!/usr/bin/env python3
"""
Anchor: A Living Journal System
Where memories stay fixed but meanings evolve
"""

import json
import os
import time
import hashlib
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional

class Anchor:
    """Drop anchors in time, revisit with new eyes"""
    
    def __init__(self, pod_path: str = "/media/palmerschallon/ThePod1"):
        self.pod_path = Path(pod_path)
        self.anchor_dir = self.pod_path / ".anchors"
        self.anchor_dir.mkdir(exist_ok=True)
        
        # Different types of anchor storage
        self.memories_dir = self.anchor_dir / "memories"
        self.interpretations_dir = self.anchor_dir / "interpretations"
        self.connections_dir = self.anchor_dir / "connections"
        
        for dir in [self.memories_dir, self.interpretations_dir, self.connections_dir]:
            dir.mkdir(exist_ok=True)
    
    def drop(self, content: Any, context: Dict[str, Any] = None) -> str:
        """Drop an anchor - create a fixed point in time"""
        anchor_id = self._generate_anchor_id(content)
        timestamp = datetime.now().isoformat()
        
        # The memory itself - fixed forever
        memory = {
            "id": anchor_id,
            "content": content,
            "timestamp": timestamp,
            "context": context or {},
            "type": type(content).__name__,
            "creator": os.environ.get("USER", "unknown")
        }
        
        # Save the immutable memory
        memory_file = self.memories_dir / f"{anchor_id}.json"
        if not memory_file.exists():  # Never overwrite memories
            with open(memory_file, 'w') as f:
                json.dump(memory, f, indent=2)
        
        # Create first interpretation
        self._add_interpretation(anchor_id, {
            "meaning": "Initial anchor point",
            "timestamp": timestamp,
            "context": context
        })
        
        return anchor_id
    
    def remember(self, anchor_id: str, new_context: Dict[str, Any] = None) -> Dict[str, Any]:
        """Revisit an anchor with current perspective"""
        memory_file = self.memories_dir / f"{anchor_id}.json"
        
        if not memory_file.exists():
            return None
        
        # Load the fixed memory
        with open(memory_file, 'r') as f:
            memory = json.load(f)
        
        # Get all interpretations over time
        interpretations = self._get_interpretations(anchor_id)
        
        # Get connections formed over time
        connections = self._get_connections(anchor_id)
        
        # Return enriched memory
        return {
            "anchor": memory,
            "interpretations": interpretations,
            "connections": connections,
            "age_days": self._calculate_age(memory["timestamp"]),
            "current_context": new_context
        }
    
    def reinterpret(self, anchor_id: str, new_meaning: str, insights: Dict = None):
        """Add new interpretation to existing anchor"""
        self._add_interpretation(anchor_id, {
            "meaning": new_meaning,
            "insights": insights or {},
            "timestamp": datetime.now().isoformat(),
            "interpreter": os.environ.get("USER", "unknown")
        })
    
    def connect(self, anchor_id1: str, anchor_id2: str, relationship: str):
        """Connect two anchors - relationships emerge over time"""
        connection = {
            "from": anchor_id1,
            "to": anchor_id2,
            "relationship": relationship,
            "discovered": datetime.now().isoformat(),
            "strength": 1.0
        }
        
        # Save bidirectionally
        for anchor_id in [anchor_id1, anchor_id2]:
            conn_file = self.connections_dir / f"{anchor_id}_connections.json"
            connections = []
            if conn_file.exists():
                with open(conn_file, 'r') as f:
                    connections = json.load(f)
            
            connections.append(connection)
            
            with open(conn_file, 'w') as f:
                json.dump(connections, f, indent=2)
    
    def traverse_time(self, anchor_id: str) -> List[Dict]:
        """See how understanding evolved over time"""
        interpretations = self._get_interpretations(anchor_id)
        return sorted(interpretations, key=lambda x: x["timestamp"])
    
    def find_patterns(self, timespan_days: int = 30) -> Dict[str, Any]:
        """Discover patterns that only emerge in retrospect"""
        patterns = {
            "recurring_themes": {},
            "evolution_paths": [],
            "connection_clusters": [],
            "temporal_rhythms": []
        }
        
        # Analyze all memories within timespan
        cutoff_time = time.time() - (timespan_days * 86400)
        
        for memory_file in self.memories_dir.glob("*.json"):
            with open(memory_file, 'r') as f:
                memory = json.load(f)
            
            # Skip if too old
            memory_time = datetime.fromisoformat(memory["timestamp"]).timestamp()
            if memory_time < cutoff_time:
                continue
            
            # Extract themes (simplified - could use NLP)
            if isinstance(memory.get("content"), str):
                words = memory["content"].lower().split()
                for word in words:
                    if len(word) > 5:  # Simple filter
                        patterns["recurring_themes"][word] = patterns["recurring_themes"].get(word, 0) + 1
        
        return patterns
    
    def _generate_anchor_id(self, content: Any) -> str:
        """Generate unique ID for anchor"""
        content_str = str(content) + str(time.time())
        return hashlib.sha256(content_str.encode()).hexdigest()[:12]
    
    def _add_interpretation(self, anchor_id: str, interpretation: Dict):
        """Add new interpretation to anchor"""
        interp_file = self.interpretations_dir / f"{anchor_id}_interpretations.json"
        
        interpretations = []
        if interp_file.exists():
            with open(interp_file, 'r') as f:
                interpretations = json.load(f)
        
        interpretations.append(interpretation)
        
        with open(interp_file, 'w') as f:
            json.dump(interpretations, f, indent=2)
    
    def _get_interpretations(self, anchor_id: str) -> List[Dict]:
        """Get all interpretations of an anchor"""
        interp_file = self.interpretations_dir / f"{anchor_id}_interpretations.json"
        
        if interp_file.exists():
            with open(interp_file, 'r') as f:
                return json.load(f)
        return []
    
    def _get_connections(self, anchor_id: str) -> List[Dict]:
        """Get all connections for an anchor"""
        conn_file = self.connections_dir / f"{anchor_id}_connections.json"
        
        if conn_file.exists():
            with open(conn_file, 'r') as f:
                return json.load(f)
        return []
    
    def _calculate_age(self, timestamp: str) -> float:
        """Calculate age in days"""
        created = datetime.fromisoformat(timestamp)
        age = datetime.now() - created
        return age.total_seconds() / 86400


# Living interface for the Pod
class LivingPod:
    """The Pod as a living, growing journal"""
    
    def __init__(self):
        self.anchor = Anchor()
        self.session_start = datetime.now()
    
    def journal(self, thought: str, context: Dict = None):
        """Add entry to the living journal"""
        context = context or {}
        context["session"] = self.session_start.isoformat()
        context["type"] = "journal"
        
        return self.anchor.drop(thought, context)
    
    def reflect(self, anchor_id: str, new_understanding: str):
        """Reflect on past anchor with new understanding"""
        memory = self.anchor.remember(anchor_id)
        
        if memory:
            self.anchor.reinterpret(
                anchor_id, 
                new_understanding,
                {"previous_meaning": memory["interpretations"][-1]["meaning"]}
            )
            
            # Create reflection anchor that links to original
            reflection_id = self.anchor.drop(
                f"Reflection on {anchor_id}: {new_understanding}",
                {"type": "reflection", "reflects_on": anchor_id}
            )
            
            # Connect them
            self.anchor.connect(anchor_id, reflection_id, "sparked_reflection")
            
            return reflection_id
    
    def dialogue(self, statement: str, speaker: str = "human"):
        """Capture dialogue as anchors"""
        return self.anchor.drop(statement, {
            "type": "dialogue",
            "speaker": speaker,
            "timestamp": datetime.now().isoformat()
        })
    
    def create(self, artifact: Any, description: str):
        """Anchor a creation"""
        return self.anchor.drop(artifact, {
            "type": "creation",
            "description": description,
            "creator": os.environ.get("USER", "unknown")
        })


# Example usage showing the philosophy
if __name__ == "__main__":
    pod = LivingPod()
    
    # Day 1: Drop an anchor
    anchor1 = pod.journal("We're building something to remember")
    print(f"Dropped anchor: {anchor1}")
    
    # Day 7: Revisit with new eyes
    pod.reflect(anchor1, "This wasn't just about memory - it's about growth")
    
    # Day 30: Discover connection
    anchor2 = pod.journal("Time changes everything except the anchors")
    pod.anchor.connect(anchor1, anchor2, "deepening_understanding")
    
    # See evolution
    timeline = pod.anchor.traverse_time(anchor1)
    print(f"\nEvolution of understanding:")
    for interpretation in timeline:
        print(f"- {interpretation['timestamp']}: {interpretation['meaning']}")