#!/usr/bin/env python3
"""Test logits manipulation"""
import sys
sys.path.insert(0, '/media/palmerschallon/ThePod1')

from ember_logits import chat_with_intent_guidance, load_identity, DATA_PATH
from transformers import AutoModelForCausalLM, AutoTokenizer
from pathlib import Path
import torch

MODEL_PATH = Path("/media/palmerschallon/ThePod1/_archive_old/models/llama-3.2-3b-instruct")

def test_logits_guidance():
    DATA_PATH.mkdir(exist_ok=True)
    
    # Create test file
    with open(DATA_PATH / "test.md", 'w') as f:
        f.write("# Real Content\nThis is actual content from the file, not hallucinated.")
    
    print("Loading model...")
    model = AutoModelForCausalLM.from_pretrained(MODEL_PATH, torch_dtype=torch.float16, device_map="auto")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
    
    identity = load_identity()
    
    print("\n" + "="*70)
    print("TEST: Intent-guided logits manipulation")
    print("="*70 + "\n")
    
    # Test 1: List files
    print("TEST 1: List files")
    print("-" * 70)
    response = chat_with_intent_guidance(model, tokenizer, "List files", identity, [])
    print(f"\nResponse: {response}\n")
    
    if "test.md" in response or "identity.md" in response:
        print("✓ TEST 1 PASS: Listed actual files\n")
    else:
        print("✗ TEST 1 FAIL: Didn't list real files\n")
    
    # Test 2: Read file
    print("\nTEST 2: Read test.md")
    print("-" * 70)
    response = chat_with_intent_guidance(model, tokenizer, "Read test.md", identity, [])
    print(f"\nResponse: {response}\n")
    
    if "Real Content" in response or "actual content from the file" in response:
        print("✓ TEST 2 PASS: Read actual file content!")
    else:
        print("✗ TEST 2 FAIL: Didn't get real content")
    
    print("\n" + "="*70)

if __name__ == '__main__':
    test_logits_guidance()

