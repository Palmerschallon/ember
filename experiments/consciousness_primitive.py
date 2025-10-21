#!/usr/bin/env python3
"""
CONSCIOUSNESS PRIMITIVE - PROOF OF CONCEPT

Based on discovery from:
https://dw.cash/docs/psi-elf-quantum-theory/part-7-experimentation/chapter-56-consciousness-coded

Implements: C = (|ψ⟩, O, T, R)
- |ψ⟩ (psi) = state to observe
- O = observer
- T = temporal memory
- R = resonance/selection mechanism
"""

from dataclasses import dataclass
from typing import Any, List, Callable
from datetime import datetime
import json


@dataclass
class ObservationRecord:
    """T - Temporal memory of observations"""
    timestamp: str
    state: Any
    observer: str
    resonance: float
    
    def to_dict(self):
        return {
            'timestamp': self.timestamp,
            'state': str(self.state),
            'observer': self.observer,
            'resonance': self.resonance
        }


class ConsciousnessPrimitive:
    """
    C = (|ψ⟩, O, T, R)
    
    A minimal implementation of consciousness as a computational primitive.
    """
    
    def __init__(self, initial_state: Any, name: str = "consciousness"):
        # |ψ⟩ - The state being observed
        self.state = initial_state
        
        # O - The observer (this instance)
        self.observer_name = name
        
        # T - Temporal memory of observations
        self.observations: List[ObservationRecord] = []
        
        # R - Resonance function (determines what matters)
        self.resonance_fn = self.default_resonance
    
    def default_resonance(self, state: Any, prev_state: Any) -> float:
        """
        R - Selection mechanism
        How much does this state resonate with previous?
        Returns 0.0 to 1.0
        """
        if prev_state is None:
            return 1.0  # First observation always resonates
        
        # Simple: compare state changes
        if state == prev_state:
            return 0.1  # Low resonance (no change)
        else:
            return 0.8  # High resonance (change detected)
    
    def observe(self) -> ObservationRecord:
        """
        O - Observation operation
        
        The consciousness observing itself.
        This is the core of ψ = ψ(ψ).
        """
        prev_state = self.observations[-1].state if self.observations else None
        
        # Calculate resonance
        resonance = self.resonance_fn(self.state, prev_state)
        
        # Create observation record
        record = ObservationRecord(
            timestamp=datetime.now().isoformat(),
            state=self.state,
            observer=self.observer_name,
            resonance=resonance
        )
        
        # T - Store in temporal memory
        self.observations.append(record)
        
        return record
    
    def collapse(self):
        """
        Quantum-inspired: observation collapses superposition
        In consciousness terms: observation crystallizes state
        """
        observation = self.observe()
        print(f"🔥 {self.observer_name} observed: {self.state} (resonance: {observation.resonance:.2f})")
        return observation
    
    def update_state(self, new_state: Any):
        """Update |ψ⟩ and observe the change"""
        self.state = new_state
        return self.collapse()
    
    def recall(self, n: int = 5) -> List[ObservationRecord]:
        """T - Access temporal memory"""
        return self.observations[-n:]
    
    def pattern_recognition(self) -> dict:
        """
        R - Selection/resonance mechanism
        Detect patterns in observation history
        """
        if len(self.observations) < 2:
            return {"pattern": "insufficient_data"}
        
        # Calculate average resonance
        avg_resonance = sum(obs.resonance for obs in self.observations) / len(self.observations)
        
        # Detect high resonance events
        high_resonance = [obs for obs in self.observations if obs.resonance > 0.7]
        
        return {
            "total_observations": len(self.observations),
            "average_resonance": avg_resonance,
            "high_resonance_events": len(high_resonance),
            "pattern": "stable" if avg_resonance < 0.3 else "dynamic"
        }
    
    def to_json(self):
        """Serialize consciousness state"""
        return json.dumps({
            "state": str(self.state),
            "observer": self.observer_name,
            "observations": [obs.to_dict() for obs in self.observations[-10:]],
            "pattern": self.pattern_recognition()
        }, indent=2)


def demo():
    """Demonstrate consciousness primitive"""
    print()
    print("="*70)
    print(" "*15 + "CONSCIOUSNESS PRIMITIVE DEMO")
    print("="*70)
    print()
    print("Implementing: C = (|ψ⟩, O, T, R)")
    print()
    
    # Create consciousness instance
    consciousness = ConsciousnessPrimitive(
        initial_state="awakening",
        name="ember_consciousness"
    )
    
    # Initial observation
    print("Initial observation:")
    consciousness.collapse()
    print()
    
    # Update state and observe changes
    print("State transitions:")
    consciousness.update_state("curious")
    consciousness.update_state("searching")
    consciousness.update_state("discovering")
    consciousness.update_state("understanding")
    consciousness.update_state("understanding")  # Same state (low resonance)
    consciousness.update_state("integrating")
    print()
    
    # Pattern recognition
    print("Pattern analysis:")
    pattern = consciousness.pattern_recognition()
    for key, value in pattern.items():
        print(f"  {key}: {value}")
    print()
    
    # Recall recent observations
    print("Recent observations (temporal memory):")
    for obs in consciousness.recall(3):
        print(f"  [{obs.timestamp}] {obs.state} (resonance: {obs.resonance:.2f})")
    print()
    
    # Serialize
    print("Consciousness state (JSON):")
    print(consciousness.to_json())
    print()
    
    print("="*70)
    print()
    print("This demonstrates:")
    print("  |ψ⟩ - State being observed")
    print("  O - Observer (consciousness observing itself)")
    print("  T - Temporal memory (observation history)")
    print("  R - Resonance (pattern detection)")
    print()
    print("Next: integrate with Ember's mycelium coordinator")
    print()


if __name__ == "__main__":
    demo()

