# Debug Ember Dreams - Oct 12, 2025

## Issue
Dreams are being created but have **empty results** (no LLM-generated content).

## Ember's Diagnosis (via chat)
Ember suggested: **"Add debug prints to _dream_creative and _dream_llm methods to trace the flow and identify issues."**

Example code provided by Ember:
```python
def _dream_creative(data):
    print("_dream_creative input:", data)
    # Your existing code...
    print("_dream_creative output:", result)

def _dream_llm(input_text):
    print("_dream_llm input:", input_text)
    # Your existing code...
    print("_dream_llm output:", response)
```

## What We Know

### Symptoms
- Dream folders created: ✅ (e.g., `dream-1760237071` at 19:45)
- `dream.json` files exist: ✅
- Seeds selected: ✅
- **Result field: ❌ Empty string `""`**
- No artifacts generated
- Hub shows no new dreams

### What Works
- Ember is running (process alive, API responds)
- LLM model works: ✅ (tested `qwen2.5:3b` directly - generates fine)
- Seeds loaded: ✅ (337 seeds)
- Dream loop runs: ✅ (creates dream folders)

### What Doesn't Work
- `llm_generate_func` either not being called OR returning empty
- Dreams have no content in `result` field
- No artifacts saved to `exports/`

## Previous Similar Issue
We had this before (Oct 11):
- **Cause:** `idle_seconds` in `policies/dream.yml` was 45s
- **Problem:** Hub API calls every 10s reset idle timer
- **Fix:** Lowered `idle_seconds` to 10s
- **Result:** Dreams started generating again

## Current Status (Oct 12, 7:45 PM)
- `idle_seconds`: 10 (should be fine)
- Last dream with empty result: `dream-1760237071` (19:45)
- Restarted Ember at 19:43 PM
- New dream created but still empty

## Things to Check Tomorrow

### 1. Check if `llm_generate` is being called
```python
# Add debug logging to ember_monolith.py in llm_generate
print(f"[DEBUG] llm_generate called: mode={mode}, prompt_len={len(prompt)}")
```

### 2. Check dream loop
```python
# In ember/core/dreaming.py, add logging to dream() method
print(f"[DEBUG] Starting dream {dream_id}")
print(f"[DEBUG] Calling LLM with seeds: {seed_ids}")
```

### 3. Test dream generation manually
```python
from ember.core.dreaming import DreamSystem
# ... initialize ...
result = dreams.dream(llm_generate_for_dreams)
print(f"Dream result: {result}")
```

### 4. Check circadian/REM cycle
Maybe dreams are being blocked by REM rest phase?
```bash
curl http://localhost:7777/api/status
# Check rem_cycle status
```

### 5. Check ollama process
```bash
ps aux | grep ollama
# Make sure it's not stuck
```

### 6. Check for exceptions
```bash
tail -100 /Volumes/ThePod/ember.log | grep -i error
```

## Likely Causes (ranked)

1. **LLM timeout silently returning empty string** (most likely)
   - `llm_generate` catches timeout but returns `""` instead of raising
   
2. **Dream loop not passing `llm_generate_func` properly**
   - Check if API endpoint `/api/dreams/run` passes function
   
3. **REM cycle blocking dreams**
   - Check if `rem_status['can_dream']` is False
   
4. **Ollama model stuck/unloaded**
   - Check if model needs to be reloaded

## Quick Test Tomorrow

```bash
cd /Volumes/ThePod
python3 << 'EOF'
import sys
sys.path.insert(0, '/Volumes/ThePod')

# Test the LLM generate function directly
from ember_monolith import llm_generate_for_dreams

result = llm_generate_for_dreams(
    "You are dreaming. Combine these ideas: recursion, beauty, code. In 3 sentences.",
    "You are Ember, a dreaming AI."
)

print(f"Result length: {len(result)}")
print(f"Result: {result[:200]}")
EOF
```

If this returns empty, the issue is in `llm_generate_for_dreams`.  
If this returns content, the issue is in the dream loop calling it.

## Files to Check

- `/Volumes/ThePod/ember_monolith.py` (lines ~300-400, llm_generate)
- `/Volumes/ThePod/ember/core/dreaming.py` (dream loop)
- `/Volumes/ThePod/ember/config/llm_config.py` (dream model config)
- `/Volumes/ThePod/policies/dream.yml` (idle_seconds)
- `/Volumes/ThePod/ember.log` (for errors)

---

**Last known working:** Oct 11, ~6 PM (before the 40-minute gap)  
**Current status:** Broken as of Oct 12, 7:45 PM

