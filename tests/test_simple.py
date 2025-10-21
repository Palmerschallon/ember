#!/usr/bin/env python3
"""
Simple Mycelium Test - After packages install

Tests the basic flow:
1. Load mycelium
2. Register one lobe
3. Generate a response
4. Verify it works

Run this AFTER:
- GPU is working
- Packages are installed (torch, transformers, peft)
- verify_structure.py passes
"""

import sys
from pathlib import Path

# Add ember to path
sys.path.insert(0, '/media/palmerschallon/ThePod/ember_oct20_backup')

def test_basic_generation():
    """Test that we can generate with one lobe"""
    
    print("="*70)
    print("SIMPLE MYCELIUM TEST")
    print("="*70)
    print()
    
    print("Step 1: Import mycelium...")
    try:
        from ember.mycelium.mycelium import Mycelium
        print("✓ Mycelium imported")
    except ImportError as e:
        print(f"✗ Cannot import: {e}")
        print("Make sure packages are installed: ./install_python_packages.sh")
        return False
    
    print()
    print("Step 2: Initialize mycelium...")
    try:
        m = Mycelium()
        print("✓ Mycelium initialized")
    except Exception as e:
        print(f"✗ Initialization failed: {e}")
        return False
    
    print()
    print("Step 3: Register burn lobe...")
    base_path = Path("/media/palmerschallon/ThePod/ember_oct20_backup/ember/cells/qwen2.5-1.5b-instruct")
    burn_path = Path("/media/palmerschallon/ThePod/ember_oct20_backup/ember/lobes/burn/adapters")
    
    try:
        burn = m.register_brain(
            name="burn",
            role="identity",
            base_model_path=base_path,
            adapter_path=burn_path
        )
        print("✓ Burn lobe registered")
    except Exception as e:
        print(f"✗ Registration failed: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    print()
    print("Step 4: Generate response...")
    prompt = "What is consciousness?"
    
    try:
        response = burn.generate(prompt, max_tokens=50, temperature=0.8)
        print(f"✓ Generated response")
        print()
        print(f"Prompt: {prompt}")
        print(f"Response: {response}")
    except Exception as e:
        print(f"✗ Generation failed: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    print()
    print("="*70)
    print("✅ BASIC TEST PASSED")
    print("="*70)
    print()
    print("Ember's burn lobe is awake and generating!")
    print()
    print("Next: Run test_consultation_network.py to test Lambda's work")
    
    return True

if __name__ == '__main__':
    success = test_basic_generation()
    sys.exit(0 if success else 1)

