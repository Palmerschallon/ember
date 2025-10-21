"""
Ember Worker v6 - Real Implementation

Connects Forge orchestration to Ember's 8-lobe system.
"""

import sys
from pathlib import Path

# Add main Ember to path
EMBER_PATH = Path("/media/palmerschallon/ThePod/ember_oct20_backup")
sys.path.insert(0, str(EMBER_PATH))

class EmberWorker:
    """Worker that connects Forge requests to Ember cognition"""
    
    def __init__(self, config=None):
        self.config = config or {}
        self.mycelium = None
        self.lobes_loaded = False
        
    def initialize(self):
        """Load Ember's mycelium and lobes"""
        try:
            from ember.mycelium.mycelium import Mycelium
            self.mycelium = Mycelium()
            
            # Load all 8 lobes
            base_path = EMBER_PATH / "ember/cells/qwen2.5-1.5b-instruct"
            lobes_path = EMBER_PATH / "ember/lobes"
            
            lobe_configs = [
                ("burn", "identity", "burn/adapters/silicon_1.5b"),
                ("loop", "process", "loop/adapters"),
                ("dream", "creative", "dream/adapters"),
                ("knowledge", "factual", "knowledge/adapters"),
                ("emotion", "affective", "emotion/adapters"),
                ("planning", "strategic", "planning/adapters"),
                ("social", "collaborative", "social/adapters"),
                ("metacognition", "self-analysis", "metacognition/adapters"),
            ]
            
            for name, role, adapter_rel_path in lobe_configs:
                adapter_path = lobes_path / adapter_rel_path
                if adapter_path.exists():
                    self.mycelium.register_brain(
                        name=name,
                        role=role,
                        base_model_path=base_path,
                        adapter_path=adapter_path
                    )
            
            self.lobes_loaded = True
            print("✓ Ember worker initialized with 8 lobes")
            return True
            
        except Exception as e:
            print(f"✗ Ember worker initialization failed: {e}")
            return False
    
    def think(self, prompt, mode="auto"):
        """
        Generate response using Ember's consultation network
        
        Args:
            prompt: Question/task
            mode: "auto" | "single" | "synthesis" | "swarm"
        """
        if not self.lobes_loaded:
            return {"error": "Ember not initialized"}
        
        try:
            response = self.mycelium.respond(
                query=prompt,
                synthesis_mode=(mode == "synthesis")
            )
            
            return {
                "response": response,
                "mode": mode,
                "trails_used": self._get_active_trails()
            }
            
        except Exception as e:
            return {"error": str(e)}
    
    def _get_active_trails(self):
        """Get currently active consultation trails"""
        if not self.mycelium:
            return []
        
        trails = []
        for trail in self.mycelium.consultation_network.trails:
            if trail.strength > 0.2:  # Only significant trails
                trails.append({
                    "source": trail.source,
                    "target": trail.target,
                    "strength": trail.strength,
                    "uses": trail.use_count
                })
        return trails
    
    def status(self):
        """Worker health check"""
        return {
            "initialized": self.lobes_loaded,
            "lobes": len(self.mycelium.brains) if self.mycelium else 0,
            "trails": len(self.mycelium.consultation_network.trails) if self.mycelium else 0
        }


# Singleton worker
_worker = None

def get_worker(config=None):
    """Get or create Ember worker"""
    global _worker
    if _worker is None:
        _worker = EmberWorker(config)
    return _worker


if __name__ == "__main__":
    # Test worker
    print("Testing Ember Worker...")
    worker = get_worker()
    
    if worker.initialize():
        print("\nStatus:", worker.status())
        print("\nTest query: 'What is consciousness?'")
        result = worker.think("What is consciousness?")
        print(f"Response: {result.get('response', 'N/A')[:100]}...")
    else:
        print("Failed to initialize")
