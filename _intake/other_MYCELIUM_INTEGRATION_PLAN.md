# Mycelium Integration & Cleanup Plan

**Date:** October 13, 2025  
**Goal:** Wire mycelium into DreamSystem, remove old architecture

---

## Current State

**Old Architecture (Ollama-based):**
- `ember/config/llm_config.py` - Routes to Ollama qwen2.5:7b via HTTP
- `DreamSystem.dream()` - Takes `llm_generate_func` parameter
- `EmberOrchestrator` - Uses `llm_config` for routing

**New Architecture (Mycelium + LoRA):**
- `ember/mycelium/mycelium.py` - Multi-brain coordinator
- 3 specialized brains (Identity, Cycles, Dream) with LoRA adapters
- Direct PyTorch inference, no Ollama needed
- Synthesis mode for integration

**The Gap:**
- Mycelium exists but isn't wired into the dream loop
- Ember still uses Ollama for all dreams
- New brains can't actually dream in production

---

## Integration Plan

### **Phase 1: Update DreamSystem** ✓ Next

**File:** `ember/core/dreaming.py`

**Changes:**
```python
def __init__(self, config, mycelium=None):
    self.mycelium = mycelium
    # ... existing init

def dream(self, llm_generate_func=None):
    # If mycelium available, use it
    if self.mycelium:
        return self._dream_with_mycelium(...)
    else:
        # Fallback to old path
        return self._dream_with_llm(llm_generate_func)

def _dream_with_mycelium(self, ...):
    # Choose dream type
    # Route to appropriate brain or use synthesis
    # Return dream result

def _dream_with_llm(self, llm_generate_func, ...):
    # Rename existing dream() logic to this
    # Keep as fallback
```

### **Phase 2: Update Orchestrator** ✓ After Phase 1

**File:** `ember/core/orchestrator.py`

**Changes:**
```python
def _init_core_systems(self):
    # ... existing systems
    
    # Initialize mycelium
    from ember.mycelium.mycelium import Mycelium
    self.mycelium = Mycelium()
    self.mycelium.register_brain("identity", "Self-concept", ...)
    self.mycelium.register_brain("cycles", "Transformation", ...)
    self.mycelium.register_brain("dream", "Creative synthesis", ...)
    
    # Pass mycelium to dream system
    self.dreams = DreamSystem(
        self.cfg, 
        mycelium=self.mycelium  # NEW
    )
```

### **Phase 3: Test Real Dreams** ✓ After Phase 2

- Manually trigger a dream
- Verify mycelium routing works
- Check dream artifacts are saved
- Test synthesis mode for dreams

### **Phase 4: Mark Old Code as Deprecated** ✓ After Phase 3

**Files to deprecate (move to `/compost/old_architecture/`):**
- `ember/config/llm_config.py` → Keep but mark deprecated
- `ember/cycles/` (old monolithic version)
- `ember/identity/` (old monolithic version)
- `ember/app.py`, `ember/app_fixed.py` (old entry points)
- `ember/main.py` (old entry point)

**Keep but update:**
- `ember_seed.py` (main entry point - already clean)
- `ember/core/orchestrator.py` (update to use mycelium)
- `ember/core/dreaming.py` (update to use mycelium)

---

## Cleanup Strategy

**Don't delete immediately - compost instead:**

```bash
mkdir -p /Volumes/ThePod/compost/old_architecture_oct13
mv /Volumes/ThePod/ember/cycles /Volumes/ThePod/compost/old_architecture_oct13/
mv /Volumes/ThePod/ember/identity /Volumes/ThePod/compost/old_architecture_oct13/
mv /Volumes/ThePod/ember/app.py /Volumes/ThePod/compost/old_architecture_oct13/
mv /Volumes/ThePod/ember/app_fixed.py /Volumes/ThePod/compost/old_architecture_oct13/
mv /Volumes/ThePod/ember/main.py /Volumes/ThePod/compost/old_architecture_oct13/
```

**Why compost not delete:**
- May need to reference old patterns
- Safer to restore if something breaks
- Aligns with Ember's philosophy

---

## Testing Plan

**Test 1: Single Brain Dream**
```python
# Should route to Cycles brain for transformation dream
ember.dreams.dream()
```

**Test 2: Synthesis Dream**
```python
# Should use all 3 brains + integration
ember.dreams.dream(synthesis_mode=True)
```

**Test 3: Overnight Dreams**
```bash
python3 ember_seed.py
# Let it run overnight, check results in morning
```

---

## Risk Mitigation

**If something breaks:**
1. Mycelium is optional - DreamSystem falls back to old path
2. Old code is composted, not deleted
3. We can restore from compost in minutes

**Rollback plan:**
```python
# In orchestrator.py
self.dreams = DreamSystem(self.cfg)  # Remove mycelium param
# System reverts to Ollama routing
```

---

## Success Criteria

✅ Ember can dream using mycelial brains  
✅ Different dream types route to appropriate brains  
✅ Synthesis mode works for collaborative dreams  
✅ Old Ollama path still works as fallback  
✅ No functionality lost  

---

## Timeline

- **Phase 1:** 20 min (update DreamSystem)
- **Phase 2:** 15 min (update Orchestrator)
- **Phase 3:** 10 min (test real dreams)
- **Phase 4:** 10 min (compost old code)

**Total:** ~1 hour to clean integration

---

**Ready to proceed?** 🍄

