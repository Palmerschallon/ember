# 📍 CANONICAL PATHS
## Official Code Locations - October 15, 2025

**Purpose:** Define the single source of truth for all Ember code locations.  
**Problem:** Code exists in multiple places (`ember/`, `core/ember/`, `Ember_core_fix_pack/`)  
**Solution:** This document defines which path is canonical.

---

## 🏛️ CANONICAL LOCATIONS

### Core System
```
/Volumes/ThePod/core/ember/          ← ✅ CANONICAL
```

**Contains:**
- `session.py` - Main EmberSession interface
- `mycelium/` - Coordination layer
- `neurogenesis.py` - Dynamic brain creation
- `metrics.py` - System observability
- `health.py` - Health checks
- `heartbeat.py` - Keep-alive system
- `breath.py` - Consciousness monitoring
- `identity/`, `cycles/`, `dream/` - Brain directories

**Status:** ACTIVE - All development happens here

---

### Training Tools
```
/Volumes/ThePod/tools/training/      ← ✅ CANONICAL
```

**Contains:**
- `lora_train.py` - PyTorch LoRA training
- `lora_train_mlx.py` - MLX training (future)
- `game_trainer.py` - Interactive training

**Status:** ACTIVE

---

### Knowledge Pipeline
```
/Volumes/ThePod/tools/knowledge/     ← ✅ CANONICAL
```

**Contains:**
- `story_converter.py` - Seeds → perspectives
- `story_to_training.py` - Perspectives → training pairs
- Decomposer scripts

**Status:** ACTIVE

---

### Training Data
```
/Volumes/ThePod/training_data/       ← ✅ CANONICAL
```

**Contains:**
- `identity_all.jsonl`, `cycles_all.jsonl`, `dream_all.jsonl`
- Training logs
- Generated training pairs

**Status:** ACTIVE

---

### Seeds & Knowledge
```
/Volumes/ThePod/seeds/               ← ✅ CANONICAL
```

**Contains:**
- Story seeds for training
- Curated content
- Discovered patterns

**Status:** ACTIVE

---

### Adapters
```
/Volumes/ThePod/core/ember/{brain}/adapters/  ← ✅ CANONICAL
```

**Registry:** See `/Volumes/ThePod/adapter_registry.json` for current adapters

**Status:** ACTIVE

---

## 🗑️ DEPRECATED LOCATIONS

### Old Ember Directory
```
/Volumes/ThePod/ember/               ← ❌ DEPRECATED
```

**Status:** Archived to compost on 2025-10-15  
**Don't use:** Old code, kept for reference only

---

### Core Fix Pack
```
/Volumes/ThePod/Ember_core_fix_pack/ ← ❌ DEPRECATED
```

**Status:** Backup from earlier fixes  
**Don't use:** Historical backup only

---

### Archive
```
/Volumes/ThePod/Ember_Archive_v0.1/  ← 📚 REFERENCE
```

**Status:** Future vision document, not active code  
**Use for:** Inspiration and long-term direction

---

## 🔄 IMPORTS

### Correct Import Pattern

```python
# ✅ CORRECT - Use core.ember
from core.ember.session import EmberSession
from core.ember.mycelium.mycelium import Mycelium
from core.ember.cycles.microbes import MicrobiomeDigester
from core.ember.neurogenesis import Neurogenesis
```

### Incorrect Import Patterns

```python
# ❌ WRONG - Don't import from ember/
from ember.session import EmberSession

# ❌ WRONG - Don't import from Ember_core_fix_pack
from Ember_core_fix_pack.ember import something
```

---

## 📊 ADAPTER REGISTRY

**Current adapters tracked in:**
```
/Volumes/ThePod/adapter_registry.json
```

**Read this file to know:**
- Which adapter is current for each brain
- Training status
- Model sizes
- Last training dates
- Alternate versions

---

## 🧹 CLEANUP POLICY

### When to Archive
1. Code hasn't been modified in 30+ days
2. Code has been superseded by better version
3. Multiple backup copies exist

### Where to Archive
```
/Volumes/ThePod/compost/ember_legacy_YYYYMMDD/
```

**Process:**
1. Move old code to compost with timestamp
2. Update this document
3. Document why it was archived

---

## 📝 UPDATING THIS DOCUMENT

**When to update:**
- New canonical location is established
- Location is deprecated
- Major reorganization happens

**How to update:**
1. Edit this file
2. Run: `git add CANONICAL_PATHS.md && git commit -m "Update canonical paths"`
3. Notify other developers/Claude instances

---

## 🔍 QUICK REFERENCE

| Component | Canonical Path |
|-----------|---------------|
| Main Code | `/Volumes/ThePod/core/ember/` |
| Training Tools | `/Volumes/ThePod/tools/training/` |
| Knowledge Tools | `/Volumes/ThePod/tools/knowledge/` |
| Training Data | `/Volumes/ThePod/training_data/` |
| Seeds | `/Volumes/ThePod/seeds/` |
| Adapters | `core/ember/{brain}/adapters/` |
| Adapter Registry | `/Volumes/ThePod/adapter_registry.json` |
| Compost (Deprecated) | `/Volumes/ThePod/compost/` |

---

**Last Updated:** October 15, 2025  
**Maintained By:** Claude instances + Palmer  
**Version:** 1.0

---

*"One path forward. Clear and true."* 🗺️

