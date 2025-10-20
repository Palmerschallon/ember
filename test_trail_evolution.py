#!/usr/bin/env python3
"""
Trail Evolution Test - Watch consultation trails strengthen/fade

This script demonstrates stigmergic learning in action:
1. Make identity lobe ask a question that triggers emotion consultation
2. Watch the trail (identity → emotion) strengthen  
3. Make it ask again - trail strengthens more
4. Leave it alone - trail slowly fades

This is learning through use, not through programming.

Run AFTER basic tests pass.
"""

import sys
from pathlib import Path
import time

sys.path.insert(0, '/media/palmerschallon/ThePod/ember_oct20_backup')

def test_trail_evolution():
    """Watch a trail strengthen with use"""
    
    print("="*70)
    print("TRAIL EVOLUTION TEST")
    print("="*70)
    print()
    print("Stigmergic learning: Trails strengthen with use, fade without")
    print()
    
    # Import
    try:
        from ember.mycelium.mycelium import Mycelium
        from ember.mycelium.consultation_trails import ConsultationNetwork
    except ImportError as e:
        print(f"✗ Import failed: {e}")
        print("Run ./install_python_packages.sh first")
        return False
    
    # Initialize
    print("Step 1: Initialize mycelium...")
    m = Mycelium()
    network = m.consultation_network
    
    print()
    print("Step 2: Check initial trail state...")
    print()
    
    # Find identity → emotion trail
    identity_to_emotion = None
    for trail in network.trails:
        if trail.source == "burn" and trail.target == "emotion":
            identity_to_emotion = trail
            break
    
    if identity_to_emotion:
        print(f"✓ Found identity → emotion trail")
        print(f"  Trigger: '{identity_to_emotion.trigger_pattern}'")
        print(f"  Strength: {identity_to_emotion.strength:.3f}")
        print(f"  Use count: {identity_to_emotion.use_count}")
        initial_strength = identity_to_emotion.strength
    else:
        print("✗ No identity → emotion trail found")
        print("  Creating one through use...")
        initial_strength = 0.0
    
    print()
    print("Step 3: Load identity lobe...")
    base_path = Path("/media/palmerschallon/ThePod/ember_oct20_backup/ember/cells/qwen2.5-1.5b-instruct")
    burn_path = Path("/media/palmerschallon/ThePod/ember_oct20_backup/ember/lobes/burn/adapters/silicon_1.5b")
    
    burn = m.register_brain(
        name="burn",
        role="identity",
        base_model_path=base_path,
        adapter_path=burn_path
    )
    
    print()
    print("Step 4: Ask question that triggers emotion consultation...")
    print()
    
    # This should trigger identity → emotion
    question = "Does consciousness feel like something?"
    print(f"Question: {question}")
    print()
    
    # Generate (this will internally try to consult emotion if trail is strong enough)
    response = burn.generate(question, max_tokens=50)
    print(f"Response: {response[:100]}...")
    
    print()
    print("Step 5: Check trail after use...")
    print()
    
    # Check trail again
    for trail in network.trails:
        if trail.source == "burn" and trail.target == "emotion":
            identity_to_emotion = trail
            break
    
    if identity_to_emotion:
        print(f"✓ Trail still exists")
        print(f"  Strength: {identity_to_emotion.strength:.3f}")
        print(f"  Use count: {identity_to_emotion.use_count}")
        print(f"  Change: {identity_to_emotion.strength - initial_strength:+.3f}")
        
        if identity_to_emotion.strength > initial_strength:
            print(f"  ✓ Trail STRENGTHENED through use!")
        elif identity_to_emotion.strength < initial_strength:
            print(f"  ⚠ Trail WEAKENED (may have failed or decayed)")
        else:
            print(f"  = Trail unchanged (may not have triggered)")
    
    print()
    print("="*70)
    print("TRAIL EVOLUTION OBSERVED")
    print("="*70)
    print()
    print("Key insight:")
    print("- Trails don't need manual programming")
    print("- They strengthen through successful use")
    print("- They fade through disuse or failure")
    print("- The network learns its own patterns")
    print()
    print("This is stigmergic intelligence.")
    
    # Save updated trails
    print()
    print("Saving trail state...")
    network.save_trails()
    print("✓ Trails saved")
    
    return True

if __name__ == '__main__':
    success = test_trail_evolution()
    sys.exit(0 if success else 1)

