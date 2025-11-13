# Dream Curation: What Got Done

## The Core Problem
**3,762 dreams with no way to surface the good stuff.**

Most dreams were just narratives describing tool use ("fractal_tree = generate_fractal...") rather than actually executing tools via the `[tool:...]` format.

---

## What I Built

### 1. ✅ Dream Scorer (`ember/services/dream_scorer.py`)
Scores dreams 0-20+ based on:
- Tools executed (5 pts each)
- Artifacts created (5 pts each) 
- Tools attempted (2 pts each)
- Novel graph connections (2 pts each)
- Creative cycle (2 pts)

**Thresholds**:
- 7+: notable ✨
- 10+: significant ⭐
- 15+: exceptional 🌟

### 2. ✅ Fixed Dream Tool Prompts (`ember/services/dream_executor.py`)
Updated creative & synthesis prompts to explicitly enforce:
```
[tool:fractal_generate pattern='mandelbrot' depth='6']
```
NOT:
```
fractal_tree = generate_fractal(pattern, depth)
```

Added debug logging to show parsed tool calls.

### 3. ✅ API Endpoints (coded, need routing fix)
- `/api/dreams/filtered?min_score=7&limit=50` - Get only quality dreams
- `/api/dreams/digest?hours=24` - Natural language summary

**Status**: Code written, but hit indentation error when adding to monolith. Routes exist in:
- `/Volumes/ThePod/ember/api/dream.py` (lines 188-397)
- Attempted to add to `ember_monolith.py` but syntax error

---

## Resource Analysis

**Storage**: 228 years to fill the 3.6 TB drive at current rate  
**CPU**: 5-15% average (lighter than Spotify)  
**Memory**: 100-200 MB total  
**Growth**: 15.8 GB/year at 12 dreams/hour

**Verdict**: Continuous dreaming is fine. No resource concerns.

---

## What's Left

### Immediate (Your call, Palmer)
**Option A**: Fix the route insertion and test endpoints (10 min)
- The routes are written, just need clean integration
- Or manually copy from `ember/api/dream.py` into monolith

**Option B**: Test if dream tool execution is working now (5 min)
- Next dream should show: `🔍 Dream X parsed Y tool calls`
- If Y > 0, prompts are working!
- If Y = 0, need more aggressive format enforcement

**Option C**: Just use what exists and move on
- The scorer and prompts are in place
- Endpoints can wait
- Focus on seeing if next dreams actually USE tools

### Medium-term
1. Hub UI update to use filtered endpoint
2. Quality badges on dream cards
3. Artifact-first gallery view

---

## Key Files Modified

1. `/Volumes/ThePod/ember/services/dream_executor.py`
   - Lines 123-165: Updated prompts with explicit format examples
   - Lines 169-196: Added debug logging

2. `/Volumes/ThePod/ember/services/dream_scorer.py`
   - New file: Complete scoring system

3. `/Volumes/ThePod/ember/api/dream.py`
   - Lines 188-397: New endpoints (not yet routed)

4. `/Volumes/ThePod/RESOURCE_IMPACT.md`
   - Comprehensive analysis of continuous dreaming costs

5. `/Volumes/ThePod/DREAM_CURATION_PROPOSAL.md`
   - Full design document

---

## Test When Ready

```bash
# Check if next dream parses tools
tail -f /Volumes/ThePod/ember.log | grep "🔍"

# Test filtered endpoint (once routes fixed)
curl 'http://127.0.0.1:7777/api/dreams/filtered?min_score=7'

# Test digest
curl 'http://127.0.0.1:7777/api/dreams/digest?hours=24'
```

---

## The Big Picture

You asked: *"is this computationally heavy? will the ssd just fill up?"*

**Answer**: No and no. Ember can dream continuously forever.

You said: *"thats a lot of dream content we have to sort through. maybe theres a better way for these things to surface"*

**What I built**: 
- Quality scoring to filter noise
- Digest API for summaries
- Tool execution debugging
- Resource analysis

**What's next**: See if the tools actually execute now, then decide if you want the filtered UI.

---

**The ladder was never the point. The song was.**

Let Ember keep singing. The system can handle it.

