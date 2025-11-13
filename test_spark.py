#!/usr/bin/env python3
"""
Test Spark - Can it read, analyze, and fix code?
"""
from pathlib import Path
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load DeepSeek Coder
MODEL_PATH = Path("/media/palmerschallon/ThePod1/models/coder/deepseek-6.7b")
if not MODEL_PATH.exists():
    MODEL_PATH = Path("/media/palmerschallon/ThePod1/_archive_old/models/deepseek-coder-6.7b-instruct")

print("Loading DeepSeek Coder...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_PATH,
    torch_dtype=torch.float16,
    device_map="auto"
)
print("✅ Loaded")

# Create a buggy file
buggy_code = """
def divide(a, b):
    return a / b

result = divide(10, 0)
print(result)
"""

Path("/tmp/buggy.py").write_text(buggy_code)

# Ask Spark to fix it
prompt = f"""You are Spark, a code analysis and fixing AI.

Here is a buggy Python file:

```python
{buggy_code}
```

Task: Find the bug and write the fixed version. Output ONLY the corrected code, no explanation.

Fixed code:
```python"""

messages = [{"role": "user", "content": prompt}]
inputs = tokenizer.apply_chat_template(messages, return_tensors="pt", add_generation_prompt=True).to(model.device)

print("\n" + "="*70)
print("ASKING SPARK TO FIX THE BUG")
print("="*70)

outputs = model.generate(
    inputs,
    max_new_tokens=300,
    temperature=0.3,
    do_sample=True,
    pad_token_id=tokenizer.eos_token_id
)

response = tokenizer.decode(outputs[0][inputs.shape[1]:], skip_special_tokens=True).strip()

print("\n" + "="*70)
print("SPARK'S RESPONSE:")
print("="*70)
print(response)
print("\n" + "="*70)

# Extract code from response
if "```python" in response:
    code = response.split("```python")[1].split("```")[0].strip()
elif "```" in response:
    code = response.split("```")[1].split("```")[0].strip()
else:
    code = response

print("\nEXTRACTED CODE:")
print("="*70)
print(code)

# Save it
Path("/tmp/fixed.py").write_text(code)
print("\n✅ Saved to /tmp/fixed.py")

# Test it
print("\n" + "="*70)
print("TESTING FIXED CODE:")
print("="*70)
try:
    exec(code)
    print("✅ Code executed successfully!")
except Exception as e:
    print(f"❌ Error: {e}")

