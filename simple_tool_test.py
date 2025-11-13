#!/usr/bin/env python3
"""
Simple test: Does model generate tool calls at all without stopping criteria?
"""
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from pathlib import Path

MODEL_PATH = Path("/media/palmerschallon/ThePod1/_archive_old/models/llama-3.2-3b-instruct")

print("Loading model...")
model = AutoModelForCausalLM.from_pretrained(MODEL_PATH, torch_dtype=torch.float16, device_map="auto")
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)

# Simple prompt
messages = [
    {'role': 'system', 'content': 'You have a tool: <tool>read(path="file")</tool>. Use it when asked to read.'},
    {'role': 'user', 'content': 'Read test.md'}
]

prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

print("\nGenerating WITHOUT stopping criteria...")
with torch.no_grad():
    outputs = model.generate(**inputs, max_new_tokens=200, temperature=0.7)

response = tokenizer.decode(outputs[0][inputs['input_ids'].shape[1]:], skip_special_tokens=True)

print(f"\nResponse:\n{response}\n")
print("="*70)

if '<tool>' in response:
    print("✓ Model generated tool tags")
    if '</tool>' in response:
        print("✓ Model completed tool call")
    else:
        print("✗ Model started but didn't finish tool call")
else:
    print("✗ Model didn't generate tool tags at all")

