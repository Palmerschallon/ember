#!/usr/bin/env python3
"""Test streaming interception"""
import sys
sys.path.insert(0, '/media/palmerschallon/ThePod1')

from ember_streaming import chat_with_transparency, load_identity, DATA_PATH
from transformers import AutoModelForCausalLM, AutoTokenizer
from pathlib import Path
import torch

MODEL_PATH = Path("/media/palmerschallon/ThePod1/_archive_old/models/llama-3.2-3b-instruct")

def test_streaming():
    DATA_PATH.mkdir(exist_ok=True)
    
    # Create test file
    with open(DATA_PATH / "test.md", 'w') as f:
        f.write("# Test\nThis is real content from test.md")
    
    print("Loading model...")
    model = AutoModelForCausalLM.from_pretrained(MODEL_PATH, torch_dtype=torch.float16, device_map="auto")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
    
    identity = load_identity()
    
    print("\n" + "="*70)
    print("TEST: Read file with streaming interception")
    print("="*70 + "\n")
    
    response = chat_with_transparency(model, tokenizer, "Read test.md", identity, [])
    
    print(f"\nFinal response: {response}\n")
    
    if "real content from test.md" in response:
        print("✓ SUCCESS: Read actual file content!")
    else:
        print("✗ FAIL: Didn't get real content")

if __name__ == '__main__':
    test_streaming()

