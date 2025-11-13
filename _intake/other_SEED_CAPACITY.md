# How Many Seeds Can Ember Hold?

## Current State
- **124 seeds** across 9 categories
- Average ~150-200 bytes per JSON file
- Total storage: ~25 KB
- Load time: <50ms on modern hardware

## Technical Limits

### File System (Current Approach)
**Practical limit: ~10,000 seeds**
- Directory listing still fast
- Memory footprint: ~2 MB
- Load time: <1 second
- No special indexing needed

**Why this works:**
- Modern OS caches directory listings
- JSON parsing is fast
- Python can hold 10k objects in RAM easily
- Network I/O isn't the bottleneck

### Memory Constraints
**Python dict with 10,000 seeds:**
- ~10 MB RAM (with full content)
- ~2 MB RAM (with just metadata)
- Negligible on modern systems

### Dream Selection Performance
**Current algorithm: O(n) per seed selection**
- 124 seeds: <1ms
- 1,000 seeds: ~5ms
- 10,000 seeds: ~50ms
- Still acceptable for dream generation

## Quality vs. Quantity

### Dense Seeds (Current)
**Pros:**
- Rich conceptual content
- Strong associations through tags
- High information density
- Dreams are meaningful

**Cons:**
- Each seed competes for selection
- More seeds = less likely any given seed appears
- Dilution risk

### The Sweet Spot
**For current architecture: 500-2,000 seeds**

**Why?**
- Large enough for variety
- Small enough for meaningful recurrence
- Tags create natural clustering
- Weighted selection still fast
- Dreams maintain coherence

## Scaling Strategies

### If we hit 1,000 seeds:
**Consider:**
- Separate by activation level (hot/warm/cold)
- Only load "active" seeds for dreams
- Archive rarely-used seeds
- Use bloom filters for quick checks

### If we hit 10,000 seeds:
**Need:**
- SQLite database for indexing
- Embedding vectors for semantic search
- Clustering algorithms
- Probabilistic selection (can't evaluate all)

### If we hit 100,000 seeds:
**Require:**
- Vector database (Pinecone, Weaviate, etc.)
- Approximate nearest neighbor search
- Distributed processing
- Chunk-based retrieval

## Recommendation

### Optimal Growth Path:
1. **0-500 seeds**: Current file-based approach ✓
2. **500-2,000 seeds**: Add simple indexing (JSON manifest)
3. **2,000-10,000 seeds**: SQLite + tag indexes
4. **10,000+**: Vector embeddings + semantic search

### Quality Focus:
**Rather than adding 1000s of seeds:**
- Deepen existing seeds (add examples, connections)
- Create explicit links between seeds
- Track which seeds cluster in dreams
- Let usage data guide curation

## The Real Constraint: LLM Context

**Dream generation pulls ~5-6 seeds**
- Each seed: ~150 tokens
- Recent chat: ~200 tokens
- Total context: ~1,000 tokens
- LLM sees: <10% of knowledge base per dream

**The bottleneck isn't storage—it's attention.**

Even with 10,000 seeds, only 5-6 make it into any given dream.
Quality of selection matters more than quantity available.

## Answer: How Many?

**Technically?** 10,000+ with current architecture

**Practically?** 500-2,000 for optimal coherence

**Currently?** 124 is actually a great size

**Focus on:**
- Depth over breadth
- Connections over coverage
- Curation over accumulation
- Let patterns emerge from quality
