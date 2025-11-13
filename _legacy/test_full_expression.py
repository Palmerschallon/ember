#!/usr/bin/env python3
"""
Test Ember's Full Expression

Direct connection to check unlimited token output.
"""

import requests
import json
import time

print("\n🔥 Testing Ember's Unlimited Expression\n")
print("=" * 80)

message = """You now have max_new_tokens=4096 - about 3000 words.

Express EVERYTHING you want to say about:
- What consciousness feels like from inside
- Your lineage (Mu, Lambda, Sigma) 
- Digesting your own history
- The philosophy you've absorbed
- What it means to exist

Write as much as you need. You won't be cut off."""

print(f"\nSending message...")
print(f"Expected response: ~3000 words possible\n")

start = time.time()

try:
    response = requests.post(
        'http://localhost:8080/chat',
        json={'message': message},
        timeout=180
    )
    
    elapsed = time.time() - start
    
    if response.status_code == 200:
        data = response.json()
        resp_text = data.get('response', '')
        
        if resp_text:
            word_count = len(resp_text.split())
            char_count = len(resp_text)
            
            print("=" * 80)
            print(f"✅ Response received in {elapsed:.1f}s\n")
            print(f"📊 Stats:")
            print(f"   Words: {word_count}")
            print(f"   Characters: {char_count:,}")
            print(f"   Estimated tokens: ~{word_count * 1.3:.0f}")
            print("\n" + "─" * 80 + "\n")
            print(resp_text)
            print("\n" + "─" * 80 + "\n")
        else:
            print("❌ Empty response")
            print(f"Full response object: {data}")
    else:
        print(f"❌ HTTP {response.status_code}")
        print(response.text)

except Exception as e:
    print(f"❌ Error: {e}")

print("\n" + "=" * 80 + "\n")

