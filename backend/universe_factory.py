"""
Deterministic Universe Factory (Ticket 2)
Generates reproducible universes using seeded random generation
"""
import random
import json
from typing import List, Dict, Any


class UniverseFactory:
    """Generates deterministic universes from seeds"""
    
    def __init__(self, seed: int = 42):
        """
        Initialize universe factory with seed
        
        Args:
            seed: Random seed for deterministic generation
        """
        self.seed = seed
        self.rng = random.Random(seed)
    
    def generate(self, num_entities: int = 100) -> Dict[str, Any]:
        """
        Generate a complete universe
        
        Args:
            num_entities: Number of entities to generate
            
        Returns:
            Dictionary containing universe data
        """
        entities = []
        
        for i in range(num_entities):
            entity_type = self.rng.choice(['star', 'planet', 'asteroid', 'nebula'])
            entity = self._generate_entity(i, entity_type)
            entities.append(entity)
        
        return {
            'seed': self.seed,
            'entities': entities,
            'bounds': {
                'min_x': -10000,
                'max_x': 10000,
                'min_y': -10000,
                'max_y': 10000
            }
        }
    
    def _generate_entity(self, entity_id: int, entity_type: str) -> Dict[str, Any]:
        """Generate a single entity"""
        # Position in universe
        x = self.rng.uniform(-10000, 10000)
        y = self.rng.uniform(-10000, 10000)
        
        # Size varies by type
        size_ranges = {
            'star': (50, 200),
            'planet': (20, 100),
            'asteroid': (5, 30),
            'nebula': (200, 500)
        }
        min_size, max_size = size_ranges[entity_type]
        size = self.rng.uniform(min_size, max_size)
        
        # Color varies by type
        colors = {
            'star': ['#FFFF00', '#FFA500', '#FF4500', '#FFFFFF'],
            'planet': ['#8B4513', '#4169E1', '#32CD32', '#DC143C'],
            'asteroid': ['#808080', '#A9A9A9', '#696969'],
            'nebula': ['#9370DB', '#FF1493', '#00CED1', '#FF69B4']
        }
        color = self.rng.choice(colors[entity_type])
        
        return {
            'id': entity_id,
            'type': entity_type,
            'x': x,
            'y': y,
            'size': size,
            'color': color
        }
    
    def to_json(self) -> str:
        """Serialize universe to JSON"""
        universe = self.generate()
        return json.dumps(universe, indent=2)
    
    @staticmethod
    def from_seed(seed: int, num_entities: int = 100) -> Dict[str, Any]:
        """
        Static method to generate universe from seed
        
        Args:
            seed: Random seed
            num_entities: Number of entities
            
        Returns:
            Universe data dictionary
        """
        factory = UniverseFactory(seed)
        return factory.generate(num_entities)
