#!/usr/bin/env python3
"""
Test script for stopping criteria.
Simulates a conversation to verify tool execution works.
"""

import sys
sys.path.insert(0, '/media/palmerschallon/ThePod1')

from ember_with_stopping import chat_with_stopping, load_identity, TOOLS, DATA_PATH
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from pathlib import Path

MODEL_PATH = Path("/media/palmerschallon/ThePod1/_archive_old/models/llama-3.2-3b-instruct")

def test_stopping_criteria():
    print("="*70)
    print("TESTING STOPPING CRITERIA FOR TOOL EXECUTION")
    print("="*70)
    
    # Setup
    DATA_PATH.mkdir(exist_ok=True)
    
    print("\n1. Loading model...")
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_PATH,
        torch_dtype=torch.float16,
        device_map="auto"
    )
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
    print("   ✓ Model loaded")
    
    print("\n2. Loading identity...")
    identity = load_identity()
    print(f"   ✓ Identity loaded ({len(identity)} chars)")
    
    print("\n3. Creating test files...")
    test_file = DATA_PATH / "test.md"
    with open(test_file, 'w') as f:
        f.write("# Test File\n\nThis is a test file for verifying tool execution.")
    print("   ✓ Created test.md")
    
    # Test 1: List files
    print("\n" + "="*70)
    print("TEST 1: List files (should use tools, not hallucinate)")
    print("="*70)
    
    user_msg = "What files do you have?"
    print(f"\nYou: {user_msg}")
    
    history = []
    response = chat_with_stopping(model, tokenizer, user_msg, identity, history)
    
    print(f"\nEmber: {response}")
    
    # Check if it actually listed files vs hallucinated
    if "test.md" in response or "identity.md" in response:
        print("\n✓ PASS: Ember listed actual files")
    else:
        print("\n✗ FAIL: Ember may have hallucinated file list")
    
    # Test 2: Read file
    print("\n" + "="*70)
    print("TEST 2: Read file (should execute read tool)")
    print("="*70)
    
    user_msg = "Read test.md"
    print(f"\nYou: {user_msg}")
    
    response = chat_with_stopping(model, tokenizer, user_msg, identity, history)
    
    print(f"\nEmber: {response}")
    
    # Check if it read actual content
    if "Test File" in response or "test file for verifying" in response:
        print("\n✓ PASS: Ember read actual file content")
    else:
        print("\n✗ FAIL: Ember may have hallucinated file content")
    
    # Test 3: Write file
    print("\n" + "="*70)
    print("TEST 3: Write file (should execute write tool)")
    print("="*70)
    
    user_msg = "Write a thought about tools to thoughts/tools_test.md"
    print(f"\nYou: {user_msg}")
    
    response = chat_with_stopping(model, tokenizer, user_msg, identity, history)
    
    print(f"\nEmber: {response}")
    
    # Check if file was actually written
    written_file = DATA_PATH / "thoughts" / "tools_test.md"
    if written_file.exists():
        print("\n✓ PASS: File was actually written")
        with open(written_file, 'r') as f:
            print(f"\n   Content: {f.read()[:200]}...")
    else:
        print("\n✗ FAIL: File was not written (may have hallucinated)")
    
    print("\n" + "="*70)
    print("TESTING COMPLETE")
    print("="*70)

if __name__ == '__main__':
    try:
        test_stopping_criteria()
    except KeyboardInterrupt:
        print("\n\nTest interrupted by user")
    except Exception as e:
        print(f"\n\nTest failed with error: {e}")
        import traceback
        traceback.print_exc()

