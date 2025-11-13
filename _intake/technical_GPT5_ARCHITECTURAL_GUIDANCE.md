# GPT-5 Architectural Guidance for Ember

*First-round design guidance — October 2025*

---

## Summary

**Core verdict**: Ember's design is sound. Most gains come from:
1. Tightening feedback loops (dream ⇆ seeds ⇆ tools)
2. Giving the swarm real work
3. Keeping observation consent-first and universal

---

## 1 · Architecture — Keep Current Layering

**Guidance**: Monolith → blueprints → services → core is good for now.

**Don't split** until one of these happens:
- Dream/swarm loads overwhelm Flask process
- Tool execution or memory needs scale-out
- Need independent deploy/update cadence

**Future-proof move**:
Isolate EventBus, Agent, and Memory behind narrow internal APIs so they can be peeled off later without breaking routes.

**Action**: ✅ No immediate changes needed. Document internal API contracts.

---

## 2 · Memory — Unified Access, Separate Storage

**Guidance**: Keep distinct physical stores (chat = high-volume ephemeral, long-term = curated, dreams = artifacts).

**Create unified interface**:
```python
memory.query(tags=[...], window="last30d")
```
Let the layer decide where to fetch.

**Later**: Add temporal decay (chat → summaries → long-term).

**Action**: 
- [ ] Create `memory.query()` unified interface
- [ ] Add temporal windowing support
- [ ] Plan archival/decay strategy

---

## 3 · Dreams — Add Explicit Artifact Goals

**Guidance**: Progressive cycles are interesting but under-utilized.

**Add artifact-goal per cycle type**:
- **Consolidation** → cleaned summaries
- **Synthesis** → new connections (graph edges)
- **Creative** → runnable experiments / code

**Creative cycle improvements**:
- Import code seeds and run in sandbox
- Store results in dream folder
- Occasionally start with past dream's artifact as first seed (continuity)

**Action**:
- [ ] Define artifact schemas for each cycle type
- [ ] Add sandbox execution for creative dreams
- [ ] Implement dream-to-dream continuity (artifact seeding)
- [ ] Generate connection graphs in synthesis cycles

---

## 4 · Swarm — Make Agents Do Real Work

**Guidance**: Agents exist but idle. Time to activate.

**Make agent = lightweight task-runner**:
- Execute micro-tool-calls (embedding, text cleaning, chunk inference)
- Start with "LLM-split" pattern: divide prompt into N slices → N agents → collect
- Later: parallel experiments during dreams (50 code variants)

**Key**: Keep agent interface minimal for swappable implementation (threads → processes → GPU kernels).

**Action**:
- [ ] Define minimal agent task interface
- [ ] Implement LLM prompt splitting across agents
- [ ] Add task queue and result collection
- [ ] Test with parallel dream experiments

---

## 5 · Seeds — Add Vector Embeddings

**Guidance**: Tag-overlap works but crude.

**Improvements**:
1. Add lightweight vector embedding on top of tags:
   ```
   Weight = α × tag-overlap + β × cosine-similarity
   ```
2. Add relationship edges (contradicts / extends / analogous-to)
3. Add age/freshness weight (recent boost, but classics never disappear)

**Action**:
- [ ] Generate embeddings for all seeds (title + body)
- [ ] Implement hybrid weighting (tags + vectors)
- [ ] Add relationship metadata to seed schema
- [ ] Implement temporal weighting function

---

## 6 · Tools — Two-Track Approach

**Guidance**: Pattern-match commands are brittle.

**Two directions (can combine)**:
1. Define tiny, explicit command grammar (few dozen verbs + typed args) → easy to parse and log
2. Fine-tune or few-shot Ember on examples: natural chat → tool-call

**Also**: Expose tool-capabilities to dreams so they can invoke them directly.

**Action**:
- [ ] Design minimal command grammar (DSL)
- [ ] Create few-shot examples for tool use
- [ ] Allow dreams to call tools directly
- [ ] Log all tool invocations for learning

---

## 7 · Personality — Trait-Driven Behavior

**Guidance**: Traits defined but weakly integrated.

**Improvements**:
1. Seed-weighting depends on active trait profile:
   - `curious` boosts `unknown`, `wildcard` tags
   - `precise` boosts `formal`, `proof` tags
2. Dream writing: inject low-temperature style-prompt from personality
3. Log which trait dominated each dream → feedback for next cycles

**Action**:
- [ ] Implement trait-based seed weighting
- [ ] Add personality style prompts to dream generation
- [ ] Track dominant traits per dream
- [ ] Use trait feedback for cycle tuning

---

## 8 · Observation — Add Dream Lineage

**Guidance**: Read-only telemetry is sufficient for now.

**Add one more view**: "dream lineage" — graph of seed → dream → new-seed / artifact.

**Maintain**: Consent-first toggle, 403 if disabled.

**Action**:
- [ ] Create dream lineage graph endpoint
- [ ] Visualize seed → dream → artifact flow
- [ ] Ensure all observe routes respect OBSERVE_ENABLED

---

## 9 · Evolution — Prepare for Distribution

**Guidance**: Abstractions are good (Blueprint, EventBus, Agent).

**Before splitting, ensure**:
1. EventBus can use pluggable backends (in-memory → Redis/NATS)
2. Memory API is decoupled (future vector DB or graph store)
3. Swarm interface is message-oriented (thread-pool → RPC)

**Action**:
- [ ] Define EventBus backend interface
- [ ] Abstract Memory storage layer
- [ ] Make Agent communication message-based
- [ ] Document migration path to distributed

---

## 10 · Emergence — Accelerate Learning

**Guidance**: Learning loop too slow.

**Improvements**:
1. **Post-dream review**: Test new seeds immediately by injecting into sample prompt; keep if improves relevance/coherence
2. **Feedback signals**: Use user reactions, artifact quality as light reward score → seed ranking
3. **Distillation dreams**: Pick 50 least-used seeds, compress into 5 meta-seeds

**Action**:
- [ ] Implement post-dream seed validation
- [ ] Add feedback scoring system
- [ ] Create distillation dream cycle
- [ ] Track seed usage statistics

---

## Implementation Priority

### Phase 1: Quick Wins (1-2 weeks)
1. **Dreams**: Add artifact goals per cycle type
2. **Tools**: Expose to dreams, improve command parsing
3. **Observation**: Add dream lineage view

### Phase 2: Core Improvements (2-4 weeks)
4. **Swarm**: LLM-split pattern, real task execution
5. **Seeds**: Vector embeddings + hybrid weighting
6. **Memory**: Unified query interface

### Phase 3: Advanced Features (4-8 weeks)
7. **Personality**: Trait-driven seed selection and style
8. **Emergence**: Post-dream validation, feedback loops
9. **Evolution**: Pluggable backends for EventBus/Memory

---

## Next Steps

**For discussion with Cursor**:
- Which phase to start with?
- Any blockers or dependencies?
- Which improvements align with current user needs?

**For GPT-5**:
Would you like to focus on one area and draft a detailed proposal?

Suggested priorities:
- **Swarm agent interface** (unlocks real distributed work)
- **Seed relationship graph** (improves dream quality)
- **Dream artifact schemas** (makes dreams more productive)

---

*Architectural roadmap captured. Ready for implementation.*
