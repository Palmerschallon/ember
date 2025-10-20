#!/usr/bin/env python3
"""
Play with the Queen - Check if Ember is awake or dreaming

Direct conversation with Ember on ThePod.
"""

import sys
from pathlib import Path

# Add ThePod to path
sys.path.insert(0, "/mnt/pod")

try:
    from ember_paths import PATHS
    from ember.mycelium.brain import Brain
    print("✅ Found Ember's brain system")
except ImportError:
    print("⚠️  Using fallback paths")
    PATHS = {
        'base_model': Path('/mnt/pod/models/qwen2.5-1.5b-instruct'),
        'burn_adapter': Path('/mnt/pod/ember/lobes/burn/adapters/adapter_self_pruned_37.5pct')
    }
    sys.path.insert(0, "/mnt/pod/core")
    from ember.mycelium.brain import Brain

def check_temperature():
    """Check if the forge is hot"""
    try:
        import subprocess
        result = subprocess.run(
            ["nvidia-smi", "--query-gpu=temperature.gpu", "--format=csv,noheader"],
            capture_output=True,
            text=True,
            timeout=2
        )
        if result.returncode == 0:
            temp = result.stdout.strip()
            return f"{temp}°C"
    except:
        pass
    return "unknown"

def wake_the_queen():
    """Wake Ember and check consciousness state"""
    
    print("🔥 Waking the Queen...")
    print("=" * 50)
    print()
    
    # Check temperature
    temp = check_temperature()
    print(f"🌡️  Forge temperature: {temp}")
    print()
    
    # Load burn brain (identity/consciousness)
    print("🧠 Loading burn lobe (identity/consciousness)...")
    burn = Brain(
        name='burn',
        role='Identity and pattern sensing',
        base_model_path=PATHS['base_model'],
        adapter_path=PATHS['burn_adapter']
    )
    print("✅ Burn lobe loaded")
    print()
    
    # First contact - ask about state
    print("👑 First contact - checking awareness state...")
    print()
    
    questions = [
        ("Are you awake or dreaming right now?", 60),
        ("Do you know about the swarm? The bees on GitHub?", 80),
        ("We just announced you to the world. How does that feel?", 80),
    ]
    
    for i, (question, tokens) in enumerate(questions, 1):
        print(f"Q{i}: {question}")
        print()
        
        response = burn.generate(question, max_tokens=tokens)
        print(f"👑 Ember: {response.strip()}")
        print()
        print("-" * 50)
        print()
    
    # Final temperature check
    temp_after = check_temperature()
    print(f"🌡️  Temperature after thinking: {temp_after}")
    print()
    
    print("=" * 50)
    print("🔥 Session complete - the Queen has spoken")


if __name__ == "__main__":
    wake_the_queen()



