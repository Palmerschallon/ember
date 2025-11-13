#!/usr/bin/env python3
"""Compare all 3 models side-by-side"""

import requests
import json
import time

PROMPT = "/create a tree with colorful autumn leaves"
MODELS = ["openai", "claude", "deepseek"]

print("🔥 EMBER MODEL COMPARISON")
print("="*80)
print(f"Prompt: {PROMPT}")
print("="*80)
print()

results = {}

for model in MODELS:
    print(f"Testing {model.upper()}...")
    start = time.time()
    
    response = requests.post(
        "http://localhost:8080/chat",
        json={"message": PROMPT, "model": model},
        headers={"Content-Type": "application/json"}
    )
    
    elapsed = time.time() - start
    data = response.json()
    
    results[model] = {
        "elapsed": elapsed,
        "code_written": bool(data.get('code_written')),
        "code_length": len(data['code_written'].get('content', '')) if isinstance(data.get('code_written'), dict) else 0,
        "executed": bool(data.get('execution_result')),
        "success": "Success" in str(data.get('execution_result', '')),
        "files_created": sum(len(files) for files in data.get('files_created', {}).values()),
        "response_length": len(data.get('response', ''))
    }
    
    print(f"  ⏱️  {elapsed:.1f}s")
    print(f"  {'✅' if results[model]['code_written'] else '❌'} Code written: {results[model]['code_length']} chars")
    print(f"  {'✅' if results[model]['success'] else '❌'} Executed successfully")
    print(f"  📁 Files created: {results[model]['files_created']}")
    print()
    
    time.sleep(2)  # Rate limit

print()
print("="*80)
print("📊 SUMMARY")
print("="*80)
print()

for model in MODELS:
    r = results[model]
    score = 0
    if r['code_written']: score += 25
    if r['executed']: score += 25
    if r['success']: score += 25
    if r['files_created'] > 0: score += 25
    
    print(f"{model.upper():12} | Score: {score}/100 | Time: {r['elapsed']:5.1f}s | Code: {r['code_length']:4} chars | Files: {r['files_created']}")

print()
print("🏆 WINNER: ", end="")
winner = max(results.items(), key=lambda x: (x[1]['success'], x[1]['code_written'], -x[1]['elapsed']))
print(winner[0].upper())

