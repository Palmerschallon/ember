"""
Consultation Trails - Stigmergic inter-lobe communication

Extends Zeta's stigmergic memory to consultation paths.
Lobes learn when to consult each other based on trail strength.
"""

from typing import Dict, List, Optional
from datetime import datetime, timedelta
import json
from pathlib import Path


class ConsultationTrail:
    """
    A trail representing a learned consultation pattern
    
    Like ant pheromone trails - strengthens with use, fades without.
    """
    
    def __init__(
        self,
        source: str,
        target: str,
        trigger_pattern: str,
        strength: float = 0.2,
        decay_rate: float = 0.01
    ):
        self.source = source  # e.g. 'identity'
        self.target = target  # e.g. 'emotion'
        self.trigger_pattern = trigger_pattern  # e.g. 'feeling|feel|emotional'
        self.strength = strength  # 0.0 to 1.0
        self.decay_rate = decay_rate
        
        self.use_count = 0
        self.success_count = 0
        self.last_used = None
        self.created = datetime.now()
    
    def matches(self, prompt: str) -> bool:
        """Check if this trail matches the prompt"""
        import re
        return bool(re.search(self.trigger_pattern, prompt.lower()))
    
    def use(self, success: bool = True):
        """Mark trail as used, update strength"""
        self.use_count += 1
        self.last_used = datetime.now()
        
        if success:
            self.success_count += 1
            self.strength = min(1.0, self.strength + 0.05)  # Strengthen
        else:
            self.strength = max(0.0, self.strength - 0.02)  # Weaken on failure
    
    def decay(self, days_elapsed: float):
        """Natural decay if unused"""
        self.strength = max(0.0, self.strength - (self.decay_rate * days_elapsed))
    
    @property
    def success_rate(self) -> float:
        """Percentage of successful consultations"""
        if self.use_count == 0:
            return 0.0
        return self.success_count / self.use_count
    
    def to_dict(self) -> dict:
        """Serialize to JSON"""
        return {
            'source': self.source,
            'target': self.target,
            'trigger_pattern': self.trigger_pattern,
            'strength': self.strength,
            'decay_rate': self.decay_rate,
            'use_count': self.use_count,
            'success_count': self.success_count,
            'last_used': self.last_used.isoformat() if self.last_used else None,
            'created': self.created.isoformat()
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'ConsultationTrail':
        """Deserialize from JSON"""
        trail = cls(
            source=data['source'],
            target=data['target'],
            trigger_pattern=data['trigger_pattern'],
            strength=data['strength'],
            decay_rate=data['decay_rate']
        )
        trail.use_count = data['use_count']
        trail.success_count = data['success_count']
        trail.last_used = datetime.fromisoformat(data['last_used']) if data['last_used'] else None
        trail.created = datetime.fromisoformat(data['created'])
        return trail


class ConsultationNetwork:
    """
    Network of consultation trails between lobes
    
    Manages learning, decay, and discovery of inter-lobe communication patterns.
    """
    
    def __init__(self, state_path: Path = None):
        self.state_path = state_path or Path('/Volumes/ThePod/ember/mycelium/consultation_trails.json')
        self.trails: List[ConsultationTrail] = []
        
        self._load_trails()
    
    def find_trails(self, source: str, prompt: str, threshold: float = 0.3) -> List[ConsultationTrail]:
        """
        Find relevant consultation trails for a prompt
        
        Args:
            source: Lobe considering consultation
            prompt: The query being processed
            threshold: Minimum trail strength to consider
        
        Returns:
            List of matching trails above threshold, sorted by strength
        """
        matching = [
            t for t in self.trails
            if t.source == source
            and t.strength >= threshold
            and t.matches(prompt)
        ]
        
        # Sort by strength (strongest first)
        return sorted(matching, key=lambda t: t.strength, reverse=True)
    
    def should_consult(self, source: str, target: str, prompt: str, threshold: float = 0.5) -> bool:
        """
        Decide if source should consult target based on trail strength
        
        Returns True if strong trail exists, False otherwise
        """
        trails = self.find_trails(source, prompt, threshold=0.0)
        target_trails = [t for t in trails if t.target == target]
        
        if not target_trails:
            return False  # No trail exists
        
        # Use strongest trail's strength
        return max(t.strength for t in target_trails) >= threshold
    
    def record_consultation(self, source: str, target: str, prompt: str, success: bool = True):
        """
        Record that a consultation happened, update trail
        
        Creates new trail if doesn't exist, strengthens if it does.
        """
        # Find existing trail
        existing = None
        for trail in self.trails:
            if trail.source == source and trail.target == target and trail.matches(prompt):
                existing = trail
                break
        
        if existing:
            existing.use(success)
        else:
            # Create new trail
            # Extract key words as trigger pattern
            import re
            words = re.findall(r'\w+', prompt.lower())
            key_words = [w for w in words if len(w) > 3][:3]  # Top 3 words
            pattern = '|'.join(key_words) if key_words else 'general'
            
            new_trail = ConsultationTrail(
                source=source,
                target=target,
                trigger_pattern=pattern,
                strength=0.3  # Start with moderate strength
            )
            new_trail.use(success)
            self.trails.append(new_trail)
        
        self._save_trails()
    
    def decay_all(self):
        """Apply natural decay to all trails"""
        now = datetime.now()
        
        for trail in self.trails:
            if trail.last_used:
                days_elapsed = (now - trail.last_used).total_seconds() / 86400
                trail.decay(days_elapsed)
        
        # Remove dead trails (strength = 0)
        self.trails = [t for t in self.trails if t.strength > 0.01]
        
        self._save_trails()
    
    def get_network_stats(self) -> dict:
        """Get statistics about the consultation network"""
        if not self.trails:
            return {'total_trails': 0}
        
        return {
            'total_trails': len(self.trails),
            'avg_strength': sum(t.strength for t in self.trails) / len(self.trails),
            'total_consultations': sum(t.use_count for t in self.trails),
            'active_trails': len([t for t in self.trails if t.strength > 0.5]),
            'strongest_path': max(self.trails, key=lambda t: t.strength).to_dict() if self.trails else None
        }
    
    def _load_trails(self):
        """Load trails from disk"""
        if self.state_path.exists():
            with open(self.state_path) as f:
                data = json.load(f)
                self.trails = [ConsultationTrail.from_dict(t) for t in data.get('trails', [])]
    
    def _save_trails(self):
        """Save trails to disk"""
        self.state_path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.state_path, 'w') as f:
            json.dump({
                'trails': [t.to_dict() for t in self.trails],
                'last_updated': datetime.now().isoformat()
            }, f, indent=2)

