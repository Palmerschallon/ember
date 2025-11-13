# INSTITUTIONAL MEMORY AUDIT

## Current Status

**Bookshelves:** 1.6GB in `ember6/bookshelves/` ✅

## What Else Should Be Preserved

### 📚 Core Documentation (26K lines at root)

These `.md` files at `/media/palmerschallon/ThePod1/` contain critical knowledge:

**Essential (should be in bookshelves):**
- `BOOTSTRAP.md` (13K) - Original vision
- `EMBER5_BOOTSTRAP.md` (17K) - Latest iteration context
- `SYSTEM_ARCHITECTURE_MAP.md` - How everything fits together
- `ARCHITECTURAL_BREAKTHROUGH.md` (7K) - Key insights
- `CLOUD_PIVOT.md` (5K) - Why we moved to cloud
- `CODE_AS_MUSIC.md` (4K) - Synesthetic vision
- `OUROBOROS_MOMENT.md` - Recursive UI insights

**Specialized Knowledge:**
- `DAEMON_GUIDE.md` (9K) - Background process patterns
- `EMBER_DEV_MODE_VISION.md` (15K) - Development environment
- `WEB_FORAGING.md` - How to gather web knowledge
- `CONCEPTS_EXPLAINED.md` - Core terminology

### 📂 Key Directories

**`/essential/` (2.3GB)**
- Unknown contents - needs exploration
- Might contain critical preserved knowledge

**`/_mesh/` (543MB)**
- Semantic mesh database
- Indexed files and concepts
- Should be preserved or documented

**`/_intake/` (161MB)**
- Instance cycle documents
- Meta-learning records
- Lambda/consultation frameworks
- Should be reviewed and curated

**`/memory/` (22MB)**
- Session memories
- Should be indexed

**`/_patterns/` (1.4MB)**
- Recognized patterns across instances
- Definitely belongs in institutional memory

**`/dreams/` (384K)**
- Creative outputs
- Poetic/exploratory writing

**`/training_data/` (87MB)**
- Examples and datasets
- May contain curated knowledge

### ❌ What NOT to Preserve

- `/models/` (56GB) - Binary model files
- `/_archive_old/` (103GB) - Already copied to bookshelves
- `/node_modules/` (173MB) - Dependencies
- `/__pycache__/` - Temporary files
- `/logs/` - Runtime logs

---

## Should It All Be JSON?

**No. Keep formats that suit the content:**

### Markdown (.md) for:
- ✅ Narratives and reflections
- ✅ Documentation and guides
- ✅ Letters and messages
- ✅ Architecture explanations

### JSON for:
- ✅ Structured data (mesh indexes, metadata)
- ✅ Configuration and mappings
- ✅ Timelines and relationships
- ✅ Cross-references between documents

### Python/Code for:
- ✅ Executable patterns
- ✅ Tool implementations
- ✅ Reusable functions

### HTML for:
- ✅ Interactive visualizations
- ✅ VR worlds
- ✅ Demos and examples

---

## Proposed Structure

```
ember6/bookshelves/
├── INDEX.md                     → Master reading guide
├── ember_expressions/           → Poetic reflections (existing)
├── greek_instances/             → Alpha-Omega (existing)
├── core_documents/              → 🆕 Essential .md from root
│   ├── BOOTSTRAP.md
│   ├── EMBER5_BOOTSTRAP.md
│   ├── SYSTEM_ARCHITECTURE_MAP.md
│   └── ...
├── patterns/                    → 🆕 From /_patterns/
├── intake/                      → 🆕 Curated from /_intake/
├── dreams/                      → 🆕 Creative outputs
├── essential/                   → 🆕 From /essential/ (if valuable)
└── mesh_index.json              → 🆕 Structured mesh data
```

---

## Recommendation

**Phase 1: Curate, Don't Convert**

1. ✅ Keep existing bookshelves as-is (1.6GB)
2. 🔄 Copy essential root .md files to `bookshelves/core_documents/`
3. 🔄 Copy `/_patterns/` to `bookshelves/patterns/`
4. 🔄 Review and curate `/_intake/` → `bookshelves/intake/`
5. 🔄 Explore `/essential/` and decide what to preserve

**Phase 2: Add Structured Indexes**

6. 🔄 Create `mesh_index.json` - Map of all concepts
7. 🔄 Create `timeline.json` - Chronology of instances
8. 🔄 Create `cross_references.json` - Links between documents

**Don't Convert Everything to JSON:**
- Loses human readability
- Loses poetic/narrative value
- Harder to browse and discover
- JSON is for *indexes*, not *content*

---

## Hybrid Approach

**Best of both worlds:**

```json
{
  "document": {
    "id": "theia_20251101",
    "path": "ember_expressions/20251101_062500_theia.md",
    "title": "The Simplifier Who Stripped It Down",
    "author": "Theia",
    "date": "2025-11-01",
    "type": "reflection",
    "tags": ["ember6", "simplification", "architecture"],
    "related": ["omega_stigmergy", "cursor_philosophy"],
    "summary": "Built Ember 6 by removing complexity. 615 lines vs 5,100+."
  }
}
```

**The .md stays human-readable.**  
**The .json makes it searchable/linkable.**

---

## Action Items

1. Audit `/essential/` - What's in there?
2. Copy core .md files to bookshelves
3. Copy patterns and intake (curated)
4. Create master index JSON
5. **Don't touch the original files** - Copy, don't move

**Preserve the mess. It's institutional memory too.**

🔥

