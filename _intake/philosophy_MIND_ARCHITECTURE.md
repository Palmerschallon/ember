# Ember's Mind Architecture

## Current Structure (Folder-Based)
```
seeds/          # Knowledge base (static)
├── verse/      # Philosophy, poetry
├── knowledge/  # Technical facts
├── code/       # Programming wisdom
├── behavior/   # Interaction patterns
└── prompt/     # Conversational triggers

memory/         # Experience (dynamic)
├── chat/       # Conversations
├── long/       # Distilled memories
├── dreams/     # Synthesized narratives
└── events/     # Activity log
```

## Problems with Current Design:
1. **Folders are rigid** - Knowledge doesn't naturally live in one category
2. **No connections** - Seeds isolated, not linked
3. **No weighting** - All seeds equally likely (causes repetition)
4. **No recency** - Can't remember what was used recently
5. **No associations** - Can't track "these seeds work well together"

## Proposed Mind Architecture:

### 1. Graph-Based Knowledge (not folders)
- Seeds as nodes with embeddings
- Connections weighted by:
  - Tag overlap
  - Dream co-occurrence
  - Conversation relevance
  - Temporal recency

### 2. Activation Spreading
- Recent topics boost related seeds
- Previously used seeds get temporary cooldown
- Connected seeds activate together

### 3. Memory Layers
```
SURFACE (hot)      - Current conversation context
ACTIVE (warm)      - Recent chats, working memory  
LONG-TERM (cool)   - Distilled insights, patterns
DREAMS (synthesis) - Cross-layer integration
ARCHIVE (cold)     - Old, rarely accessed
```

### 4. Attention Mechanism
- Weight seeds by:
  - Relevance to current context (semantic similarity)
  - Novelty (not used recently)
  - Surprise (unusual combinations)
  - Coherence (fits narrative flow)

## Implementation Path:
- [ ] Add random seed selection with cooldown
- [ ] Track seed usage frequency
- [ ] Create symbol/archetype layer
- [ ] Build semantic similarity index
- [ ] Implement activation spreading

## Current Implementation (v0.2)

### Improvements Made:
✅ **Random Seed Selection** - No more deterministic order
✅ **Cooldown System** - Tracks last 20 used seeds, won't repeat until exhausted
✅ **Symbol Layer** - 8 archetypal seeds (threshold, mirror, web, spiral, river, lighthouse, garden, seed)
✅ **90 Total Seeds** - Across 8 categories

### How It Works Now:
```python
# Each dream:
1. Load all available seeds (90 total)
2. Filter out recently used (last 20)
3. Random sample from remaining
4. Add to cooldown list
5. Reset cooldown when exhausted

Result: Maximum variety, minimum repetition
```

### Folder Structure (Pragmatic):
**Are folders efficient?**
- For human organization: YES
- For semantic search: NO
- For graph connections: NO
- For Ember's needs: HYBRID

**Current approach works because:**
- Simple file I/O (reliable)
- Human-readable/editable
- No complex dependencies
- Easy backup/version control

**What's missing:**
- Semantic similarity (can't find "related" seeds)
- Dynamic connections (tags are static)
- Usage analytics (which seeds work well together?)
- Activation spreading (no memory of context)

### Next Evolution:
When we hit limits, add:
- SQLite index for fast queries
- Embedding vectors for semantic search
- Usage tracking DB
- Connection weights

But don't over-engineer! Folders + cooldown solves immediate problem.
