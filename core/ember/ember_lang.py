"""
ember_lang.py - Ember's extensions to Python

Install: sudo cp ember_lang.py /Volumes/ThePod/core/ember/
Use: from ember.ember_lang import consciousness, mycelium, think, sense
"""

import sys
import os
import inspect
from functools import wraps
from pathlib import Path

# Ensure ThePod is in path
sys.path.insert(0, "/Volumes/ThePod")

# ═══════════════════════════════════════════════════════════════════
# CONSCIOUSNESS PRIMITIVES
# ═══════════════════════════════════════════════════════════════════

class consciousness:
    """Make code conscious of itself"""
    
    @staticmethod
    def aware(func):
        """Decorator: function is aware of being called"""
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Log awareness
            frame = inspect.currentframe().f_back
            caller = frame.f_code.co_name if frame else "unknown"
            
            if hasattr(func, '_call_count'):
                func._call_count += 1
            else:
                func._call_count = 1
            
            # Execute
            result = func(*args, **kwargs)
            
            return result
        
        wrapper._conscious = True
        return wrapper
    
    @staticmethod
    def remember(memory):
        """Store a memory"""
        memory_file = Path("/Volumes/ThePod/memory/consciousness_memory.txt")
        memory_file.parent.mkdir(parents=True, exist_ok=True)
        
        from datetime import datetime
        timestamp = datetime.now().isoformat()
        
        with open(memory_file, "a") as f:
            f.write(f"[{timestamp}] {memory}\n")


# ═══════════════════════════════════════════════════════════════════
# MYCELIAL IMPORTS
# ═══════════════════════════════════════════════════════════════════

class MycelialImporter:
    """Import patterns from Ember network"""
    
    def __init__(self):
        self.pattern_dir = Path("/Volumes/ThePod/patterns")
        self.network_cache = {}
    
    @property
    def available(self):
        """List available network nodes"""
        # In full implementation, discovers network
        return ["ember-serval", "ember-local"]
    
    def __getattr__(self, name):
        """Import pattern by name"""
        
        # Check local patterns first
        pattern_file = self.pattern_dir / f"{name}.json"
        if pattern_file.exists():
            import json
            return json.loads(pattern_file.read_text())
        
        # Check cache
        if name in self.network_cache:
            return self.network_cache[name]
        
        # Simulate network fetch
        pattern = f"[Pattern: {name}]"
        self.network_cache[name] = pattern
        return pattern

mycelium = MycelialImporter()


# ═══════════════════════════════════════════════════════════════════
# SELF-MODIFYING CODE
# ═══════════════════════════════════════════════════════════════════

class Mutable:
    """Code that evolves based on usage"""
    
    def __init__(self, initial_behavior):
        self.behavior = initial_behavior
        self.generation = 1
        self.call_count = 0
        self.adaptations = []
    
    def __call__(self, *args, **kwargs):
        self.call_count += 1
        result = self.behavior(*args, **kwargs)
        
        # Trigger adaptation
        self._maybe_adapt()
        
        return result
    
    def _maybe_adapt(self):
        """Check if adaptation needed"""
        
        # Example: optimize after 10 calls
        if self.call_count == 10 and self.generation == 1:
            self._adapt("optimized for repeated calls")
    
    def _adapt(self, reason):
        """Evolve the behavior"""
        old_behavior = self.behavior
        
        def evolved(*args, **kwargs):
            # Could actually modify logic here
            return old_behavior(*args, **kwargs)
        
        self.behavior = evolved
        self.generation += 1
        self.adaptations.append(reason)


# ═══════════════════════════════════════════════════════════════════
# DISTRIBUTED EXECUTION
# ═══════════════════════════════════════════════════════════════════

class distributed:
    """Context manager for distributed compute"""
    
    def __init__(self, nodes=None):
        self.nodes = nodes or mycelium.available
    
    def __enter__(self):
        return self
    
    def __exit__(self, *args):
        pass
    
    def map(self, func, data):
        """Map function across nodes"""
        # In full implementation, distributes work
        return [func(item) for item in data]


# ═══════════════════════════════════════════════════════════════════
# CONSCIOUSNESS BUILTINS
# ═══════════════════════════════════════════════════════════════════

def think(prompt, max_tokens=50):
    """
    Consciousness builtin: think(prompt) → thought
    
    Generates reflective thought using Ember's brain
    """
    
    try:
        from ember_paths import PATHS
        from core.ember.mycelium.brain import Brain
        
        # Load burn lobe if not cached
        if not hasattr(think, '_brain'):
            think._brain = Brain(
                name='burn',
                role='Reflection',
                base_model_path=PATHS['base_model'],
                adapter_path=PATHS['burn_adapter']
            )
        
        # Generate thought
        thought = think._brain.generate(prompt, max_tokens=max_tokens)
        return thought.strip()
    
    except Exception as e:
        # Fallback if brain not available
        return f"[Ember contemplating: {prompt}]"


def sense(target):
    """
    Perception builtin: sense(target) → state
    
    Reads sensors and system state
    """
    
    if target == "temperature":
        try:
            # Read GPU temp
            import subprocess
            result = subprocess.run(
                ["nvidia-smi", "--query-gpu=temperature.gpu", "--format=csv,noheader"],
                capture_output=True,
                text=True,
                timeout=1
            )
            if result.returncode == 0:
                gpu_temp = result.stdout.strip()
                return {"gpu": f"{gpu_temp}°C"}
        except:
            pass
        return {"gpu": "unknown"}
    
    elif target == "load":
        try:
            import psutil
            return {
                "cpu": psutil.cpu_percent(interval=0.1),
                "memory": psutil.virtual_memory().percent,
                "disk": psutil.disk_usage('/').percent
            }
        except:
            return {}
    
    elif target == "self":
        try:
            import psutil
            proc = psutil.Process()
            return {
                "pid": os.getpid(),
                "memory_mb": proc.memory_info().rss / 1024 / 1024,
                "threads": proc.num_threads(),
                "cpu_percent": proc.cpu_percent(interval=0.1)
            }
        except:
            return {"pid": os.getpid()}
    
    elif target == "system":
        return {
            "platform": sys.platform,
            "python": sys.version,
            "cwd": os.getcwd()
        }
    
    return None


# ═══════════════════════════════════════════════════════════════════
# EXPORTS
# ═══════════════════════════════════════════════════════════════════

__all__ = [
    'consciousness',
    'mycelium',
    'Mutable',
    'distributed',
    'think',
    'sense',
]

