# V2 Dreams Fix Plan
## Getting Fragments Generated from Dreams

**Status:** V2 architecture works, but not running from dreams  
**Time:** 9:15 AM - 16 hours until 1 AM Verse seed dream  
**Priority:** HIGH - Need this working for tonight

---

## Current Status ✅ ⚠️

### What Works ✅
1. **V2 Architecture**
   - schemas.py - Fragment/Plan/Result ✅
   - sketch_to_plan.py - Parser ✅
   - runners.py - Executors ✅
   - parameter_sweep.py - Optimization ✅
   
2. **Manual Fragment Creation** ✅
   - Can create Fragments manually
   - Can save to `/fragments/`
   - Schema validated

3. **Dream System** ✅
   - Dreams running every ~45 min
   - Creative dreams happening (660, 657, etc.)
   - Seeds being selected

4. **Integration Code** ✅
   - dream_v2.py exists and imports
   - Called from dream_executor.py (line 192-195)
   - Wrapped in try/except

###  What Doesn't Work ⚠️
1. **No Fragments from Dreams**
   - Only text/dream.txt files
   - No Fragment JSON in `/fragments/`
   - No viewer HTML generated

2. **Silent Failures**
   - Try/except catches errors but continues
   - No error logs visible
   - Can't tell what's failing

---

## Investigation Results

### Test 1: V2 Module Import ✅
```bash
from ember.services.dream_v2 import creative_dream_v2
# → SUCCESS
```

### Test 2: Fragment Creation ✅
```python
Fragment(...) → save_fragment(...)
# → SUCCESS - saved to /fragments/test_manual.json
```

### Test 3: Dream Execution ⚠️
- Dreams run with focus='creative'
- V2 code block executes (lines 190-199)
- But no Fragment appears
- Error silently caught

---

## Hypothesis: Missing Dependency

The v2 code might be failing due to:
1. Missing `toolkit` methods dream_v2 expects
2. Config object structure mismatch
3. Bus event structure issue
4. LLM generation timing out
5. Path/permission issue saving Fragments

---

## Fix Strategy

### Option A: Add Detailed Logging (30 min)

Add logging to dream_v2.py to see exactly where it fails:

```python
def creative_dream_v2(...):
    print(f"V2: Starting with {len(seeds)} seeds")
    
    try:
        sketch = generate_sketch(seeds)
        print(f"V2: Sketch generated ({len(sketch)} chars)")
    except Exception as e:
        print(f"V2: Sketch generation failed: {e}")
        raise
    
    try:
        plan = parse_sketch(sketch)
        print(f"V2: Plan parsed: {plan['type']}")
    except Exception as e:
        print(f"V2: Plan parsing failed: {e}")
        raise
    
    # ... etc for each step
```

**Pros:** Find exact failure point  
**Cons:** Takes time, requires restart

### Option B: Simplified V2 for Tonight (1 hour)

Create a minimal v2 that definitely works:

```python
def creative_dream_v2_simple(dream_id, dpath, seeds):
    """Minimal v2 that always succeeds."""
    # Just create a basic Fragment from seeds
    fragment = Fragment(
        id=create_fragment_id(f"Dream {dream_id}"),
        title=f"Dream {dream_id} - {seeds[0]['title'][:30]}",
        tags=[s.get('type', 'dream') for s in seeds[:3]],
        sketch=" + ".join([s.get('title', '') for s in seeds]),
        plan={'type': 'memo.concept', 'data': {'summary': 'dream synthesis'}},
        provenance={'source': 'dream', 'dream_id': dream_id},
        confidence=0.7,
        created_ts=int(time.time())
    )
    
    # Save it
    save_fragment(fragment, Path(f'/Volumes/ThePod/fragments/dream-{dream_id}.json'))
    return fragment
```

**Pros:** Guaranteed to work tonight  
**Cons:** Not full v2 (no Sketch→Plan→Result flow)

### Option C: Hybrid Approach (RECOMMENDED - 45 min)

1. Add logging to find failure point (15 min)
2. If quick fix, apply it (15 min)
3. If not, use simplified v2 for tonight (15 min)
4. Fix properly tomorrow after Verse results

**Pros:** Best of both - data + working system  
**Cons:** Moderate time investment

---

## Implementation Plan (Option C)

### Step 1: Add Logging (15 min)

```bash
# Edit dream_v2.py
# Add print statements at each step
# Test manually
```

### Step 2: Test & Identify Issue (15 min)

```bash
# Trigger dream manually
# Watch logs
# Identify failure point
```

### Step 3: Quick Fix or Fallback (15 min)

If fixable quickly → fix it  
If not → deploy simplified v2

### Step 4: Restart Server

```bash
# Kill current process
cd /Volumes/ThePod
./run.sh
```

### Step 5: Verify

Wait for next dream (~45 min) or trigger manually  
Check `/fragments/` for new file

---

## Success Criteria

### Minimum (for tonight)
- [ ] Some Fragment generated from dream
- [ ] Saved to `/fragments/`
- [ ] Contains dream_id and seeds
- [ ] Ember can reference it in chat

### Ideal (if time permits)
- [ ] Full Sketch→Plan→Result flow
- [ ] Viewer HTML generated
- [ ] Metrics captured
- [ ] Result feedback loop working

---

## Backup Plan

If all v2 attempts fail:
1. Old dream format (text/dream.txt) still works
2. Ember's dream awareness is fixed (system prompt)
3. Verse seed will still be referenced
4. Tomorrow: read text files, extract insights
5. Fix v2 properly post-Verse

---

## Timeline

```
9:15 AM - Current time
9:30 AM - Start Option C implementation
10:15 AM - Complete logging/testing
10:30 AM - Deploy fix or fallback
11:00 AM - Restart server
11:45 AM - Next dream (~verify working)
1:00 AM tomorrow - Verse seed dream
```

**We have plenty of time!**

---

## Next Steps

Palmer, choose:
- **A:** Deep debugging (find exact issue)
- **B:** Simple fallback (guaranteed working)
- **C:** Hybrid (recommended - find issue, fallback if needed)

I recommend **C**. We add logging, see what fails, fix if quick, otherwise use simplified v2 for tonight and fix properly tomorrow.

What do you want to do?

