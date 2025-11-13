#!/usr/bin/env python3
"""
Test Ember V2 - Verify orchestrator works before switching
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from ember_orchestrator_clean import EmberOrchestrator

def test_orchestrator():
    """Test the orchestrator with various queries"""
    
    print("="*70)
    print("EMBER V2 TEST SUITE")
    print("="*70)
    
    orchestrator = EmberOrchestrator()
    
    tests = [
        ("Search for mycelium", "Should use tool_executor (instant)"),
        ("List the models directory", "Should use tool_executor (instant)"),
        ("What's 2+2?", "Should use reasoning_engine or conversation_model"),
        ("Write a hello world function", "Should use code_generator"),
        ("Help me think of creative solutions", "Should use creative_synthesizer"),
    ]
    
    for query, expected in tests:
        print("\n" + "-"*70)
        print(f"TEST: {query}")
        print(f"EXPECTED: {expected}")
        print("-"*70)
        
        try:
            result = orchestrator.process(query)
            
            print(f"\nROUTED TO: {[e['executor'] for e in result['execution_plan']]}")
            print(f"\nRESPONSE:\n{result['response'][:500]}...")
            
            # Check if it matches expectations
            if "tool" in expected.lower() and 'tool_executor' in str(result['execution_plan']):
                print("\n✅ PASS - Correctly routed to tools")
            elif "code" in expected.lower() and 'code_generator' in str(result['execution_plan']):
                print("\n✅ PASS - Correctly routed to code generator")
            elif "creative" in expected.lower() and 'creative_synthesizer' in str(result['execution_plan']):
                print("\n✅ PASS - Correctly routed to creative synthesizer")
            else:
                print("\n⚠️  ROUTED BUT CHECK QUALITY")
                
        except Exception as e:
            print(f"\n❌ FAILED: {e}")
    
    print("\n" + "="*70)
    print("TEST SUITE COMPLETE")
    print("="*70)

if __name__ == "__main__":
    test_orchestrator()

