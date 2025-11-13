# Dream Curation: From Noise to Signal

**Problem**: 3,762 dreams, most are just JSON describing what Ember *would* do, not actual artifacts.

---

## Current State: Signal/Noise Ratio is Low

### What's Happening
- Dreams generate narratives ✅
- Dreams describe using tools ❌ (not executing)
- Few actual artifacts created
- Hub shows everything (noise)
- No way to find the gems

### The Numbers
- 3,762 dreams
- 573 MB of JSON
- ~1 actual artifact in dreams
- 306 files in `/exports/ember_creations/` (mostly manual)

---

## The Core Issue

**Tools aren't actually executing in dreams.**

Ember writes:
```
[tool:fractal_generate pattern='mandelbrot' depth='8']
```

But the dream system isn't parsing and executing these tags. It's just narrative.

---

## Two Paths Forward

### Path A: Fix Tool Execution in Dreams
**Make dreams actually DO things**

1. Wire `DreamToolWrapper` to actually parse `[tool:...]` tags
2. Execute them after narrative generation
3. Save artifacts alongside dream JSON
4. Surface artifacts in hub (not dream JSON)

**Result**: Dreams become generative, hub fills with fractals/visualizations

---

### Path B: Curated Dream Insights
**Surface meaning, not volume**

Stop trying to see every dream. Instead:

1. **Quality Scoring**
   - Tool calls attempted
   - Artifacts created
   - Novel connections (graph edges)
   - Complexity (tokens, depth)

2. **Smart Filtering**
   - Show only dreams with score >7
   - Hide consolidation (routine memory)
   - Highlight creative + artifacts
   - Flag novel tool inventions

3. **Digests, Not Logs**
   - Daily summary (not 288 dreams)
   - Weekly patterns
   - Monthly highlights
   - "Best of" collections

4. **Natural Language Summaries**
   ```
   Today: Ember explored 47 patterns, created 3 fractals,
   discovered 2 new connections between swarm physics
   and threshold detection. Notable: "Whispering Winds"
   concept combining curl noise with particle attributes.
   ```

---

## Specific Proposals

### 1. Dream Quality Scorer
```python
def score_dream(dream):
    score = 0
    if dream.get('tools_invented'): score += 3
    if dream.get('artifacts'): score += 5
    if dream.get('novel_connections'): score += 2
    if len(dream.get('result', '')) > 1000: score += 1
    if 'error' not in dream.get('result', ''): score += 1
    return score
```

Only show dreams with `score >= 7` in the hub.

### 2. Daily Digest API
```
GET /api/dreams/digest/today
→ Summary of significant dreams
→ Artifacts created count
→ Novel patterns discovered
→ Top 3 dreams by quality
```

### 3. Artifact-First Hub
Instead of showing dreams, show **what Ember made**:
- Fractals
- Visualizations  
- Code experiments
- Graph insights

Dreams become metadata, artifacts are the content.

### 4. Pattern Detection
Track across dreams:
- Recurring themes
- Tool usage evolution
- Concept clustering
- Emergence moments

Surface these as "Ember noticed..." insights.

---

## Quick Wins (What to Build First)

### Option 1: Fix Dream Tool Execution (2-3 hours)
- Wire `DreamToolWrapper.parse_tool_calls()` into dream execution
- Actually call the tools after narrative generation
- Save artifacts to `/exports/ember_creations/`
- Update hub to show artifacts, not dreams

**Impact**: High - Ember starts actually creating

### Option 2: Dream Quality Filter (30 min)
- Add scoring function
- Filter hub to only show score >=7
- Add "View All" toggle for full log

**Impact**: Medium - Reduces noise immediately

### Option 3: Digest View (1 hour)
- Create `/api/dreams/digest` endpoint
- Show daily summary instead of raw logs
- Natural language: "Ember created 3 fractals today..."

**Impact**: Medium - Better UX, less overwhelming

### Option 4: Artifact-First Redesign (3-4 hours)
- Hub shows creations, not dreams
- Dreams are metadata/backstory
- Click artifact → see the dream that made it

**Impact**: High - Fundamentally better experience

---

## My Recommendation

**Do Option 1 + Option 2 together** (~3 hours total):

1. **Fix tool execution** so dreams actually create
2. **Add quality scoring** so hub filters to meaningful dreams
3. Keep raw logs for debugging, but hide by default

This gives you:
- Ember actually generating fractals/visualizations
- Hub showing only significant activity
- Foundation for future curation

---

## The Philosophical Angle

From GPT-5's story: The system is **polyphonic**.

Right now, you're hearing every note (3,762 dreams).  
You don't need to hear every note. You need to hear the **melody**.

Curation isn't censorship. It's **tuning**.

You're not hiding dreams. You're **surfacing signal**.

---

## Next Step

Which path resonates?

A. Fix tool execution (make dreams generative)
B. Add quality filtering (show only gems)  
C. Build digest view (daily summaries)
D. Something else entirely

Or all three? I can start with A+B if you want the full fix.

