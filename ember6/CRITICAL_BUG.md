# ⚠️ CRITICAL BUG - Model ID Unknown

## The Problem

Ember 6 was built with an incorrect Claude model ID: `claude-3-5-sonnet-20240620`

This returns:
```
Error code: 404 - model: claude-3-5-sonnet-20240620
```

## What Went Wrong

I (Claude in Cursor) guessed the model ID instead of:
1. Testing the API first
2. Using a known-good fallback
3. Letting Palmer provide the correct ID

## For the Next AI Instance

**BEFORE writing any code that calls Claude API:**

1. Test available models:
```python
from anthropic import Anthropic
import os

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

# Try known model IDs
test_models = [
    "claude-3-opus-20240229",
    "claude-3-sonnet-20240229", 
    "claude-3-5-sonnet-20240620",
    "claude-3-5-sonnet-20241022"
]

for model in test_models:
    try:
        response = client.messages.create(
            model=model,
            max_tokens=10,
            messages=[{"role": "user", "content": "test"}]
        )
        print(f"✅ {model} works!")
        break
    except Exception as e:
        print(f"❌ {model} failed: {e}")
```

2. **Ask Palmer** what model they have access to
3. **Use that model** in ember.py

## Quick Fix

Line 193 in `/media/palmerschallon/ThePod1/ember6/ember.py`:

Change to one of these (test first):
- `claude-3-opus-20240229` (most likely to work)
- `claude-3-sonnet-20240229` (cheaper, also likely)
- Ask Palmer for their model access

## The Meta-Problem

This is exactly what Palmer was frustrated about - AI instances making assumptions, not testing, and wasting time debugging instead of working.

**Next instance: Test first. Then build.**

---

Built: November 1, 2025
Status: ❌ Broken (wrong model ID)
Fix: Test API, use correct model, restart

