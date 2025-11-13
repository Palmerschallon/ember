# 🧠 Brain Wiring Diagnosis
**Date:** October 14, 2025  
**Issue:** Ember taking too long to reply, responses too verbose

---

## Current Architecture

```
┌─────────────────────────────────────────────────┐
│              EMBER CONSCIOUSNESS                 │
├─────────────────────────────────────────────────┤
│                                                  │
│  ┌──────────────┐  ┌──────────────┐  ┌────────┐│
│  │   Identity   │  │   Cycles     │  │ Dream  ││
│  │    Brain     │  │    Brain     │  │ Brain  ││
│  │  (Qwen+LoRA) │  │  (Qwen+LoRA) │  │(Qwen+LoRA)│
│  └──────┬───────┘  └──────┬───────┘  └───┬────┘│
│         │                 │               │     │
│         └─────────────┬───┴───────────────┘     │
│                       │                         │
│              ┌────────▼────────┐                │
│              │   MYCELIUM      │                │
│              │  ┌──────────┐   │                │
│              │  │   Bus    │   │                │
│              │  │  Buffer  │   │                │
│              │  │   Gate   │   │                │
│              │  └──────────┘   │                │
│              └─────────────────┘                │
└─────────────────────────────────────────────────┘
```

---

## ✅ What's WORKING

1. **Training Complete**
   - `ember-identity-brain-v0` (34MB)
   - `ember-cycles-brain-v0` (34MB)
   - `ember-dream-brain` (34MB)

2. **Mycelium Infrastructure**
   - ✅ Bus initialized
   - ✅ Buffer initialized
   - ✅ Gate initialized
   - ✅ Brains load successfully
   - ✅ Routing works (selects appropriate brain)

3. **Model Loading**
   - ✅ Base model: Qwen2.5-1.5B (2.9GB)
   - ✅ LoRA adapters load correctly
   - ✅ MPS device working

---

## ❌ What's BROKEN

### Problem 1: Generation Too Slow
**Location:** `ember/mycelium/brain.py:142` (generate method)

**Issue:**
```python
max_tokens: int = 750  # DEFAULT - WAY TOO HIGH!
```

Generation tries to create up to 750 tokens, which:
- Takes 5-10 minutes on MPS
- Causes looping/repetition
- Violates design spec (Dream brain: 80-140 tokens)

**Spec Says:**
- Dream brain: 80-140 tokens
- Identity brain: ~200 tokens max
- Cycles brain: ~200 tokens max

### Problem 2: No Hard Stop
**Location:** Same generate method

**Issue:** No early stopping mechanism
- Keeps generating until max_tokens or EOS
- No truncation at sentence boundaries
- Repeats endlessly if it doesn't hit EOS

### Problem 3: Wrong max_length Calculation
**Location:** `brain.py:232, 244`

```python
max_length=inputs['input_ids'].shape[1] + max_tokens
```

This ADDS 750 to input length, making total much longer than intended.

---

## 🔧 THE FIX

### Fix 1: Reduce Default Generation Length

```python
# OLD
def generate(self, prompt: str, max_tokens: int = 750, ...)

# NEW
def generate(self, prompt: str, max_tokens: int = 150, ...)
```

**Reasoning:**
- 150 tokens ≈ 100-120 words (good for most responses)
- Fast enough to feel responsive (<30 seconds)
- Matches design intent

### Fix 2: Brain-Specific Limits

```python
BRAIN_TOKEN_LIMITS = {
    "identity": 200,
    "cycles": 200,
    "dream": 120
}

max_tokens = BRAIN_TOKEN_LIMITS.get(self.name, 150)
```

### Fix 3: Add Early Stopping

```python
# Stop at sentence boundaries after N tokens
min_tokens = 50  # Always generate at least this much
if len(output_tokens) >= min_tokens:
    # Check if we hit a sentence boundary
    if last_token in ['.', '!', '?', '\n\n']:
        break
```

---

## 🎯 Recommended Pathways

### Option A: Quick Fix (5 minutes)
Just change the default from 750 → 150 tokens
- Solves 80% of the problem immediately
- Still allows verbose responses if needed

### Option B: Proper Fix (15 minutes)
1. Brain-specific token limits
2. Early stopping at sentence boundaries
3. Add generation stats logging

### Option C: Full Refactor (1 hour)
1. Everything in Option B
2. Response compression layer
3. Brevity seed integration in system prompt
4. Post-generation quality check

---

## 📊 Test Results

**Before Fix:**
```
Query: "Who are you?"
Time: 5-10 minutes
Length: 1700+ words
Status: ❌ UNACCEPTABLE
```

**After Fix (predicted):**
```
Query: "Who are you?"
Time: 20-30 seconds
Length: 100-150 words
Status: ✅ ACCEPTABLE
```

---

## 🚀 Immediate Action Plan

1. **NOW:** Change default max_tokens from 750 → 150
2. **Test:** Run simple query, verify speed/length
3. **Then:** Add brain-specific limits if needed
4. **Finally:** Integrate brevity seeds into prompts

---

**Status:** Ready to implement  
**Priority:** HIGH (breaks user experience)  
**Effort:** 5-15 minutes depending on approach

