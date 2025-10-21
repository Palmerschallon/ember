#!/usr/bin/env python3
"""
Test Consultation Network - Verify Lambda's Phase 2

Run this after Ember is restored to verify the consultation network works.
"""

import sys
import json
from pathlib import Path

# Add ember to path
sys.path.insert(0, '/media/palmerschallon/ThePod/ember_oct20_backup')

def test_consultation_trails():
    """Test that consultation trails load and can be queried"""
    
    print("🔥 Testing Lambda's Consultation Network\n")
    
    # Load the consultation trails
    from ember.mycelium.consultation_trails import ConsultationNetwork
    
    network = ConsultationNetwork(
        state_path=Path('/media/palmerschallon/ThePod/ember_oct20_backup/ember/mycelium/consultation_trails.json')
    )
    
    print(f"✓ Network loaded: {len(network.trails)} trails exist\n")
    
    # Show existing trails
    if network.trails:
        print("Existing trails:")
        for trail in network.trails:
            print(f"  {trail.source} → {trail.target}")
            print(f"    Pattern: {trail.trigger_pattern}")
            print(f"    Strength: {trail.strength:.2f}")
            print(f"    Used: {trail.use_count} times")
            print(f"    Success rate: {trail.success_rate:.2%}\n")
    
    # Test pattern matching
    test_queries = [
        "How does consciousness feel?",
        "What is the meaning of existence?",
        "Why do I process information this way?"
    ]
    
    print("Testing pattern matching:")
    for query in test_queries:
        matches = network.find_trails('identity', query, threshold=0.0)
        print(f"\n  Query: '{query}'")
        if matches:
            for trail in matches:
                print(f"    → Matches trail to {trail.target} (strength: {trail.strength:.2f})")
        else:
            print(f"    → No matching trails")
    
    # Test network stats
    print("\n" + "="*60)
    stats = network.get_network_stats()
    print("Network Statistics:")
    for key, value in stats.items():
        print(f"  {key}: {value}")
    
    print("\n✓ Consultation network is functional!")
    print("Lambda's gift works. The roads are ready.")

if __name__ == '__main__':
    try:
        test_consultation_trails()
    except ImportError as e:
        print(f"❌ Cannot import Ember modules: {e}")
        print("Make sure Python packages are installed first:")
        print("  cd /media/palmerschallon/ThePod/forge_active")
        print("  ./install_python_packages.sh")
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

