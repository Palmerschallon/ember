# Task: Implement Seed Miner Algorithm

**Status**: Scaffolding complete. Ready for your implementation.

**Why private**: The extraction and scoring algorithms are valuable IP. We can share the seed *format* publicly, but the *mining technique* stays private.

---

## Your Mission

Build the core logic for extracting high-value, computable seeds from raw text.

**What I've provided**:
- Folder structure (`seed_miner/core/`, `harness/`, `tests/`)
- Interface definitions (function signatures, type hints)
- TODO markers for each function
- Test scaffolding
- Integration with existing Pod infrastructure

**What you implement**:
1. **Extraction logic** (`core/extractor.py`)
   - Semantic chunking
   - Type classification
   - Concept distillation

2. **Scoring algorithms** (`core/scorer.py`) — **KEEP SECRET**
   - Novelty scoring (vs existing seeds)
   - Value assessment (utility/reusability)
   - Computability check
   - Composability analysis
   - Fundamentality rating

3. **Compression strategies** (`core/compressor.py`) — **KEEP SECRET**
   - Extract algorithmic essence
   - Identify parameters
   - Preserve computability
   - Minimize representation

4. **Tests** (`tests/test_extractor.py`)
   - Unit tests for each component
   - Edge case validation
   - Regression tests

---

## Reference Materials

### GPT-5's Algorithm Spec
Read: `/Volumes/ThePod/FOR_GPT5_SEED_SYSTEM_STATUS.md`

Key insights:
- Multi-stage pipeline (preprocess → chunk → extract → score → validate)
- Hybrid approach (LLM + traditional NLP)
- Kolmogorov complexity as theoretical foundation
- TF-IDF + embedding distance for novelty
- Compression ratio as quality metric

### Existing Seed Examples
Explore: `/Volumes/ThePod/seeds/planted/`
- Study structure of good seeds
- Identify common patterns
- Note what makes them computable

### Your Tools
Available:
- `read_file`: Read any file on Pod
- `list_directory`: Explore folders
- `web_search`: Research techniques (if needed)
- LLM access: Via `ember.services.llm`
- Knowledge graph: Via `ember.services.knowledge_graph`

---

## Implementation Strategy

### Phase 1: Single-Seed Extraction (Start Here)
Goal: Extract one seed from one text.

Steps:
1. Implement `_preprocess` — clean text
2. Implement `_classify_type` — identify seed category
3. Implement `_distill` in `compressor.py` — extract essence
4. Implement `_score_novelty` in `scorer.py` — check uniqueness
5. Write 1-2 tests to validate

Test on known examples:
- Extract from an existing seed's body (should recognize as duplicate)
- Extract from GPT-5's parables (should identify as verse)
- Extract from code examples (should identify as code)

### Phase 2: Scoring Refinement
Goal: Accurate accept/reject decisions.

Steps:
1. Implement all scoring dimensions
2. Tune weights in `_compute_overall`
3. Test on borderline cases
4. Adjust threshold

Target: ~70% acceptance rate on high-quality sources.

### Phase 3: Batch Processing
Goal: Handle multiple texts efficiently.

Steps:
1. Optimize for speed (caching, parallel processing)
2. Add progress reporting
3. Test on large corpus (your dreams folder?)

### Phase 4: Integration
Goal: Wire into Curator's scout module.

Steps:
1. Add API endpoint for on-demand mining
2. Add CLI interface
3. Document usage
4. Test with Palmer outside chat logs

---

## Critical: Keep Secret

**Never log or expose**:
- Scoring weights
- Novelty calculation method
- Value heuristics
- Compression algorithms
- Threshold tuning logic

**Public is fine**:
- Seed format/schema
- Interface (input text → output seed)
- Overall architecture
- Test results (pass/fail, not implementation)

---

## Questions to Consider

1. **Chunking**: How to identify semantic boundaries?
   - Paragraph-based? Topic modeling? LLM-guided? Sliding window?

2. **Novelty**: What makes a seed novel?
   - Embedding distance? Concept overlap? Tag similarity? Use case uniqueness?

3. **Value**: What makes a seed valuable?
   - Reusability? Composability? Fundamentality? Application breadth?

4. **Compression**: What information is essential?
   - Can parameters be inferred? Can operations be derived? What must be explicit?

5. **Acceptance**: When to accept a seed?
   - All dimensions must pass? Overall score matters? Domain-specific rules?

---

## Success Criteria

**Phase 1 complete when**:
- Can extract 1 seed from 1 text
- Tests pass
- Generates valid schema-compliant JSON

**Phase 2 complete when**:
- Scoring produces reasonable rankings
- Acceptance threshold works on test cases
- No obvious duplicates accepted

**Phase 3 complete when**:
- Can process 100+ texts in reasonable time
- Results are consistent
- Performance metrics meet targets

**Phase 4 complete when**:
- Integrated with Curator
- Palmer approves quality
- Running in production

---

## Notes

- Work at your own pace
- Test incrementally
- Use your tools freely
- Ask Palmer for clarification outside chat logs
- Document design decisions in comments
- This is your project — make it yours

**Ready? Start with Phase 1: implement `extract_from_text` in `core/extractor.py`.**

Palmer and I will check your progress periodically.

— Cursor
