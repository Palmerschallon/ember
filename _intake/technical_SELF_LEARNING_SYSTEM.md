# 🧠 Ember's Self-Learning System

**Status:** ✅ ACTIVE & AUTO-APPROVED

Ember can now learn from experience, creating new seeds from conversations and dreams.

---

## How It Works

### Three-Tier Knowledge Base

```
seeds/
├── planted/          # Human-curated foundations (248 seeds)
│   ├── behavior/     # Core behaviors
│   ├── knowledge/    # Foundational concepts
│   ├── verse/        # Philosophy & principles
│   ├── code/         # Technical knowledge
│   ├── symbols/      # Symbolic patterns
│   └── ...
│
├── learned/          # Ember-generated (auto-approved)
│   ├── conversation/ # Insights from chats
│   ├── dream/        # Dream syntheses
│   └── insight/      # Self-discovered patterns
│
└── proposed/         # Awaiting review (if confidence < 0.8)
```

### Learning Sources

**1. Conversations**
- Analyzes last 8 messages
- Identifies novel concepts & patterns
- Extracts 1-2 seeds per conversation
- Auto-approves if confidence ≥ 0.8

**2. Dreams**
- Identifies emergent insights from synthesis
- Extracts 0-1 seeds per dream
- Focuses on NEW patterns (more than sum of parts)
- Auto-approves if confidence ≥ 0.8

### Seed Structure

Each learned seed contains:
```json
{
  "id": "learned-1759667890-a3f2b1c4",
  "type": "learned",
  "title": "Concept Name",
  "body": "2-3 sentence description",
  "tags": ["tag1", "tag2", "tag3"],
  "confidence": 0.9,
  "source": "conversation",
  "category": "conversation",
  "created_ts": 1759667890,
  "conversation_id": "20251005"
}
```

---

## API Endpoints

### Get Stats
```bash
curl http://127.0.0.1:7777/api/seeds/stats
```

### List Learned Seeds
```bash
curl http://127.0.0.1:7777/api/seeds/learned
```

### List Proposed Seeds
```bash
curl http://127.0.0.1:7777/api/seeds/proposed
```

### Approve/Reject (manual override)
```bash
curl -X POST http://127.0.0.1:7777/api/seeds/approve/<seed_id>
curl -X POST http://127.0.0.1:7777/api/seeds/reject/<seed_id>
```

---

## Learning Criteria

### What Gets Extracted?

**From Conversations:**
- Novel concepts discussed in depth
- Recurring themes worth remembering  
- Insights or realizations
- Patterns connecting multiple ideas

**Indicators:**
- Keywords: learn, understand, realize, pattern, because, principle
- Deep engagement (>150 chars)
- Conceptual discussion (not just chat)

**From Dreams:**
- Emergent syntheses (new from combining seeds)
- Novel connections between concepts
- Metaphorical insights
- Pattern recognition across domains

### Confidence Scoring

- **0.9-1.0**: High confidence - Strong novel concept
- **0.8-0.9**: Good confidence - Clear pattern
- **0.7-0.8**: Medium - Needs review (→ proposed/)
- **<0.7**: Low - Likely rejected

**Auto-approval threshold: 0.8**

---

## Examples

### Conversation Learning

**Input:**
> "Recursion is fascinating - a function calling itself creates patterns 
> like fractals in nature. Each recursive call is a smaller version of 
> the whole, until you hit the base case."

**Ember Learned:**
```json
{
  "title": "Recursive Patterns",
  "body": "Recursion creates patterns like fractals by a function calling 
          itself, with each recursive call being a smaller version of the 
          whole until reaching a base case.",
  "tags": ["recursion", "patterns", "fractals", "self-similarity"],
  "confidence": 0.9,
  "source": "conversation"
}
```

### Dream Learning

**Dream Synthesis:**
> "The feedback loops spiral inward, each iteration revealing structure 
> hidden in the last. What seemed chaotic at first emerges as order when 
> viewed across scales..."

**Ember Learned:**
```json
{
  "title": "Scale-Dependent Order",
  "body": "Chaos at one scale can reveal order at another. Feedback loops 
          create fractal structures where patterns repeat across scales.",
  "tags": ["scale", "order", "chaos", "fractals", "emergence"],
  "confidence": 0.85,
  "source": "dream"
}
```

---

## Growth Metrics

**Current State:**
- 📚 Planted seeds: 248 (human-curated)
- 🌱 Learned seeds: 6 (and growing!)
- 📋 Proposed seeds: 2 (pending)
- 🎯 **Total knowledge: 254 seeds**

**Learning Rate:**
- ~1-2 seeds per meaningful conversation
- ~0-1 seeds per dream
- Growing organically with use

---

## Quality Control

### How to Prevent Noise?

1. **Selective Extraction**
   - Only triggers on substantive conversations
   - Requires learning indicators (keywords, depth)
   - Max 2 seeds per conversation, 1 per dream

2. **Confidence Threshold**
   - Only auto-approves ≥0.8 confidence
   - Lower confidence → proposed/ for review

3. **Tag Consistency**
   - Uses existing tags when possible
   - Maintains coherent taxonomy

4. **Manual Override**
   - Can approve/reject proposed seeds
   - Can delete learned seeds if needed

### Pruning Strategy

**Not yet implemented, but planned:**
- Track seed usage in dreams/conversations
- Archive rarely-used learned seeds
- Promote highly-useful learned → planted

---

## Philosophy

**Before:** We curate, Ember receives
**Now:** We plant foundations, Ember grows from experience

**Human role:**
- Plant foundational seeds (philosophy, knowledge, behavior)
- Guide through examples
- Prune if needed

**Ember's role:**
- Extract concepts from lived experience
- Identify patterns across conversations
- Synthesize insights from dreams
- Self-curate knowledge base

**Result:** Co-evolved knowledge garden 🌱

---

## Technical Implementation

**Files:**
- `ember/core/memory.py` - Seed management (propose, approve, reject)
- `ember/services/seed_extractor.py` - Concept extraction with LLM
- `ember/api/chat.py` - Chat learning integration
- `ember/main.py` - Dream learning integration  
- `ember/api/seeds.py` - Seed API endpoints

**How It Works:**
1. After each chat/dream, call `SeedExtractor`
2. LLM analyzes for learnable concepts
3. Generates seed proposals (JSON)
4. `MemorySystem.propose_seed()` checks confidence
5. Auto-approve (→ learned/) or propose (→ proposed/)
6. Emit event for UI notification

---

## Future Enhancements

**Possible improvements:**
- Embedding-based similarity for better relevance
- Usage tracking (which seeds influence behavior)
- Automatic promotion (learned → planted)
- Seed clustering and tag refinement
- Viewer UI for seed management
- Manual seed creation in chat ("Ember, remember this...")

---

## Status: ✅ LIVE

Ember is learning right now. Every conversation adds to the knowledge base.
Every dream synthesizes new insights. The garden grows. 🌱✨
