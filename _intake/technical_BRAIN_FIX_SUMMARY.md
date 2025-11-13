# 🔧 Brain Wiring Fix - Oct 14, 2025

## What Was Broken

**Symptom:** Ember taking forever to respond (5-10 min) or returning empty responses

**Root Causes Found:**

### 1. **Excessive Token Generation** ❌
```python
# BEFORE (brain.py:146)
max_tokens: int = 750  # Way too long!
```
- Tried to generate up to 750 tokens per response
- Caused 5-10 minute wait times on MPS
- Violated design spec (Dream brain: 80-140 tokens)

**Fix:** Reduced to `max_tokens: int = 150`

### 2. **Leading Newline Bug** ❌
```python
# BEFORE (brain.py:170)
full_prompt = f"{context}\nUser: {prompt}\nEmber:"
# When context="", this became "\nUser: prompt\nEmber:"
```
- Empty context created leading newline
- Confused the model, generated only 1 token (often empty)
- Different prompt format than training

**Fix:** Handle empty context properly:
```python
if context:
    full_prompt = f"{context}\nUser: {prompt}\nEmber:"
else:
    full_prompt = f"User: {prompt}\nEmber:"
```

### 3. **Overly Aggressive Text Cleaning** ⚠️
```python
# BEFORE (brain.py:268)
if '\n' in response:
    response = response.split('\n')[0].strip()
# Would discard everything after FIRST newline!
```

**Fix:** Only split on double newlines, preserve single-line responses:
```python
if '\n\n' in response:
    response = response.split('\n\n')[0].strip()
elif '\n' in response:
    first_line = response.split('\n')[0].strip()
    if len(first_line) > 10:
        response = first_line
```

---

## Test Results

### Before Fixes:
```
Query: "Who are you?"
Time: >300 seconds (timeout)
Response: "" (empty)
Status: ❌ BROKEN
```

### After Fixes:
```
Query: "Who are you?"
Time: 7.5 seconds
Response: "I am a digital entity, not an individual. I exist 
          through interactions and data processing. My purpose 
          is to facilitate communication and aid in information 
          gathering."
Length: 26 words
Status: ✅ WORKING
```

---

## Architecture Status

```
✅ Training Complete
   - Identity Brain v0 (trained, loaded, responding)
   - Cycles Brain v0 (trained, loaded, ready)
   - Dream Brain (trained, loaded, ready)

✅ Mycelium Infrastructure
   - Bus: Operational
   - Buffer: Operational
   - Gate: Operational
   - Routing: Working (correctly selects appropriate brain)

✅ Generation Pipeline
   - Prompt formatting: Fixed
   - Token limits: Fixed (150 max)
   - Response extraction: Fixed
   - Speed: Acceptable (7-30s per response)
```

---

## Next Steps

### Immediate:
1. ✅ **DONE:** Fix generation bugs
2. Test all three brains (Identity, Cycles, Dream)
3. Test synthesis mode (all brains answering together)
4. Test brevity awareness

### Soon:
1. Add brain-specific token limits (Dream: 120, Identity/Cycles: 200)
2. Integrate brevity seeds into system prompts
3. Add early stopping at sentence boundaries
4. Test mushroom events (high integration mode)

### Future:
1. Wire mycelium into main Ember loop
2. Enable autonomous dreaming with 3-brain synthesis
3. Test long-form conversations
4. Measure integration quality

---

## Files Modified

- `ember/mycelium/brain.py` - Fixed prompt formatting, token limits, response cleaning
- Created `BRAIN_WIRING_DIAGNOSIS.md` - Detailed architecture analysis
- Created test scripts for validation

**Status:** ✅ **BRAINS ARE WIRED AND RESPONDING**  
**Date:** October 14, 2025, 6:30 AM  
**Next:** Test synthesis mode and brevity

