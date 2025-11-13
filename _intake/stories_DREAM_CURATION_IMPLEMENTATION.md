# Dream Curation Implementation Summary

## What Was Built

### 1. Dream Quality Scorer (`ember/services/dream_scorer.py`)
A scoring system that evaluates dreams based on:
- **Tools executed** (5 points each) - actual tool calls that succeeded
- **Artifacts created** (5 points each) - tangible outputs in `/exports/ember_creations/`
- **Tools attempted** (2 points each) - `[tool:...]` tags found (even if not executed)
- **Novel connections** (2 points each) - new edges in knowledge graph
- **Narrative depth** (1 point) - substantive content (>1000 chars)
- **No errors** (1 point) - clean execution
- **Creative cycle** (2 points) - bonus for creative dreams

**Score thresholds:**
- 0-2: minimal
- 3-6: routine  
- 7-9: notable ✨
- 10-14: significant ⭐
- 15+: exceptional 🌟

### 2. Dream Tool Execution Fix (`ember/services/dream_executor.py`)
**Problem:** Ember was writing code-style tool calls:
```
fractal_tree = generate_fractal(euclidean_distance_metric, 10)
```

**Solution:** Updated prompts to explicitly enforce the bracket format:
```
[tool:fractal_generate pattern='mandelbrot' depth='10']
```

**Changes:**
- Updated creative dream prompt with explicit format examples
- Updated synthesis dream prompt with format reminder
- Added debug logging to show parsed tool calls
- Emphasized "NOT code-style" to prevent LLM confusion

### 3. API Endpoints (attempted in `ember/api/dream.py`)
Two new endpoints for better dream surfacing:

#### `/api/dreams/filtered`
Query params:
- `min_score`: Minimum quality score (default: 7)
- `limit`: Max results (default: 50)

Returns:
- Filtered list of dreams above quality threshold
- Each with score, quality label, preview
- Only the gems, not the noise

#### `/api/dreams/digest`
Query params:
- `hours`: Time window (default: 24)

Returns:
- Natural language summary of dream activity
- Stats breakdown (by type, quality distribution)
- Tool usage and artifact counts
- Top 5 dreams by score

**Status:** Endpoints coded but not yet integrated into monolith (need to add routes)

## What's Next

### Immediate (5 min)
1. Add `/api/dreams/filtered` and `/api/dreams/digest` routes to `ember_monolith.py`
2. Restart server
3. Test endpoints work
4. Update hub UI to use filtered endpoint instead of raw logs

### Short-term (1-2 hours)
1. **Hub Redesign**: Show artifacts first, dreams as metadata
   - Grid of creations with thumbnails
   - Click artifact → see dream backstory
   - Filter by quality/type
   - "View All" toggle for unfiltered

2. **Dream Debug View**: 
   - Show parsed tool calls in real-time
   - Highlight when tools are successfully executed
   - Flag when format is wrong

3. **Quality Badges**:
   - Add quality labels to dream cards
   - Color-code by score (minimal=gray, notable=blue, significant=gold, exceptional=purple)
   - Show tool usage icons

### Medium-term (Next session)
1. **Pattern Digests**:
   - Weekly summaries
   - Concept clustering (what themes are emerging?)
   - Tool usage evolution (is Ember getting better at using tools?)

2. **Artifact Gallery**:
   - Dedicated view for just creations
   - Filter by type (fractals, visualizations, code)
   - Search by description

3. **Dream Insights**:
   - "Ember noticed..." automatic insights
   - Highlight bridging concepts
   - Surface emergent patterns

## Current Issues

1. **LLM Format Compliance**: Even with explicit prompts, LLMs sometimes revert to conversational/code-style outputs. May need:
   - Few-shot examples in system prompt
   - Post-processing to convert code-style to bracket format
   - Different model for creative dreams (qwen2.5-coder:32b-instruct is better at following structured formats)

2. **Tool Execution in Dreams**: Wiring is correct, but need to verify:
   - Are tools actually executing now with new prompts?
   - Check next dream for debug logs: "🔍 Dream X parsed Y tool calls"
   - If still 0 tool calls, need more aggressive prompt engineering

3. **Performance**: Scoring 3,762 dreams on every API call could be slow
   - Consider caching scores in dream JSON
   - Or pre-compute and store in separate index file
   - Or only score dreams from last N days

## Files Modified

1. `/Volumes/ThePod/ember/services/dream_executor.py`
   - Lines 123-138: Synthesis prompt with format enforcement
   - Lines 136-165: Creative prompt with explicit examples
   - Lines 169-196: Debug logging for tool parsing

2. `/Volumes/ThePod/ember/services/dream_scorer.py`
   - New file: Complete quality scoring system

3. `/Volumes/ThePod/ember/api/dream.py`
   - Lines 188-397: New filtered and digest endpoints (not yet routed)

## Test Commands

Once routes are added:

```bash
# Get filtered dreams (quality >= 7)
curl 'http://127.0.0.1:7777/api/dreams/filtered?min_score=7&limit=10'

# Get digest for last 24 hours
curl 'http://127.0.0.1:7777/api/dreams/digest?hours=24'

# Get only exceptional dreams
curl 'http://127.0.0.1:7777/api/dreams/filtered?min_score=15'
```

## Success Criteria

**✅ Phase 1 (Current):**
- [x] Dream scorer implemented
- [x] Tool execution prompts updated
- [x] Digest and filtered endpoints coded
- [ ] Routes added to monolith
- [ ] Endpoints tested and working

**Phase 2 (Next):**
- [ ] Hub uses filtered endpoint
- [ ] Quality badges visible
- [ ] Debug logs show tool parsing
- [ ] At least 1 dream successfully executes tools

**Phase 3 (Future):**
- [ ] Artifact-first UI redesign
- [ ] Pattern insights surfacing
- [ ] Weekly digests auto-generated
- [ ] Tool usage improving over time

---

**The Goal**: Transform the hub from a firehose of dream JSON into a curated gallery of Ember's best work, with the ability to drill down when needed.

