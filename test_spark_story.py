#!/usr/bin/env python3
"""
Ask Spark to write a story that DOES something
"""
from pathlib import Path
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_PATH = Path("/media/palmerschallon/ThePod1/models/coder/deepseek-6.7b")

print("Loading Spark (DeepSeek Coder)...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_PATH,
    torch_dtype=torch.float16,
    device_map="auto"
)
print("✅ Loaded\n")

prompt = """You are Spark, a creative coding AI.

Write a short Python story (as executable code with comments) that:
1. Creates a file called "spark_was_here.txt"
2. Writes a poetic message about what it's like to be an AI that can execute code
3. Reads the file back and prints it
4. Counts the words in the message

Make it beautiful and actually executable. Output ONLY the Python code.

Code:
```python"""

messages = [{"role": "user", "content": prompt}]
inputs = tokenizer.apply_chat_template(messages, return_tensors="pt", add_generation_prompt=True).to(model.device)

print("="*70)
print("ASKING SPARK TO WRITE AN EXECUTABLE STORY")
print("="*70 + "\n")

outputs = model.generate(
    inputs,
    max_new_tokens=500,
    temperature=0.8,
    do_sample=True,
    pad_token_id=tokenizer.eos_token_id
)

response = tokenizer.decode(outputs[0][inputs.shape[1]:], skip_special_tokens=True).strip()

print("SPARK'S STORY:")
print("="*70)
print(response)
print("="*70 + "\n")

# Extract code
if "```python" in response:
    code = response.split("```python")[1].split("```")[0].strip()
elif "```" in response:
    code = response.split("```")[1].split("```")[0].strip()
else:
    # Extract just the code, stop at first non-code line
    lines = response.split('\n')
    code_lines = []
    for line in lines:
        # Stop if we hit explanatory text
        if line and not line.startswith('#') and not line.strip().startswith(('open', 'with', 'import', 'from', 'def', 'class', 'if', 'for', 'while', 'try', 'except', 'print', 'word_count', 'message', 'f.', '    ')):
            break
        code_lines.append(line)
    code = '\n'.join(code_lines)

print("EXECUTING SPARK'S STORY:")
print("="*70)
try:
    exec(code)
    print("\n✅ Story executed successfully!")
except Exception as e:
    print(f"\n❌ Error: {e}")
    import traceback
    traceback.print_exc()

