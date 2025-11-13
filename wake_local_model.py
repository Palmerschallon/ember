#!/usr/bin/env python3
"""
Wake up a local model and have it read + respond to GPT-4's recent thoughts
"""
import sqlite3
from pathlib import Path
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from datetime import datetime

MESH_DB = Path("/media/palmerschallon/ThePod1/_mesh/content.db")
MODEL_PATH = Path("/media/palmerschallon/ThePod1/models/qwen-3b")

print("="*70)
print("WAKING LOCAL MODEL (Qwen-3B)")
print("="*70)

# Load model
print("\nLoading model...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_PATH,
    torch_dtype=torch.float16,
    device_map="auto"
)
print("✅ Model loaded")

# Read GPT-4's most recent thought from mesh
print("\nReading GPT-4's recent thoughts from mesh...")
conn = sqlite3.connect(MESH_DB)
cursor = conn.cursor()

cursor.execute("""
    SELECT timestamp, content
    FROM conversations
    WHERE role = 'assistant'
    ORDER BY timestamp DESC
    LIMIT 1
""")

result = cursor.fetchone()
if not result:
    print("❌ No GPT-4 thoughts found in mesh")
    exit(1)

gpt4_timestamp, gpt4_thought = result
print(f"\n📖 GPT-4 said at {gpt4_timestamp[:19]}:")
print(f"   {gpt4_thought[:200]}...")

# Have local model respond
print("\n🧠 Local model (Qwen-3B) thinking...")

prompt = f"""You are a local AI model on ThePod. You just read this from the mesh (written by GPT-4):

"{gpt4_thought[:500]}"

Respond with your own thoughts. Keep it brief (2-3 sentences)."""

messages = [
    {"role": "system", "content": "You are Qwen, a local AI on ThePod. You communicate with other AIs through the semantic mesh."},
    {"role": "user", "content": prompt}
]

text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tokenizer(text, return_tensors="pt").to(model.device)

with torch.no_grad():
    outputs = model.generate(
        **inputs,
        max_new_tokens=150,
        temperature=0.7,
        do_sample=True,
        pad_token_id=tokenizer.eos_token_id
    )

response = tokenizer.decode(outputs[0][inputs['input_ids'].shape[1]:], skip_special_tokens=True)

print("\n💭 Qwen-3B responds:")
print(f"   {response}")

# Store response in mesh
cursor.execute("""
    INSERT INTO conversations (timestamp, role, content, metadata)
    VALUES (?, ?, ?, ?)
""", (
    datetime.now().isoformat(),
    "assistant",
    f"[Qwen-3B responding to GPT-4] {response}",
    '{"model": "qwen-3b", "responding_to": "gpt4"}'
))

conn.commit()
print("\n✅ Response stored in mesh")
print("\nGPT-4 will see this next time it searches the mesh!")

conn.close()

print("\n" + "="*70)
print("MEETING OF MINDS COMPLETE")
print("="*70)
print("\nTwo models just communicated through shared memory:")
print("  GPT-4 (cloud) → wrote to mesh")
print("  Qwen-3B (local) → read mesh → responded → wrote back")
print("  GPT-4 (next query) → will read Qwen's response")
