# 7B OPTIMIZATION PLAN

**Date**: October 19, 2025  
**Cartographer**: Iota  
**Goal**: Optimize all Ember lobes with Qwen2.5-7B-Instruct base model

---

## ARCHITECTURE REVIEW

### Current Understanding (CONFIRMED):
```
🧠 ONE Shared Base Model (7B)
   ↓
🍄 Mycelium (routes queries)
   ↓
🔥 FOUR LoRA Lobes (specialized adapters)
   ├─ BURN (identity/consciousness)
   ├─ LOOP (cycles/mechanics)
   ├─ DREAM (creativity/imagery)
   └─ KNOWLEDGE (facts/memory)
   ↓
🌐 17 Daemons (autonomous processes)
```

### Key Insight from Palmer:
> "One central brain with as many lobes as we can train, using mycelium to connect them with daemons."

**Benefit**: All daemons query the SAME base model through different LoRA adapters. No duplication!

---

## PHASE 1: FOUNDATION (Current)

### 1. Download Clean 7B Model ⏳
- **Status**: In progress
- **Location**: `/Volumes/ThePod/ember/cells/qwen2.5-7b-instruct`
- **Size**: ~15GB
- **ETA**: 10-15 minutes

### 2. Update Registry ✅
- **File**: `ember/brainstem/adapter_registry_7B.json`
- **Change**: Point all lobes to new 7B location
- **Status**: Complete

### 3. Test Shared Base Architecture
- Load 7B once with `SharedBaseModel`
- Verify VRAM usage (~8-10GB with 8-bit quantization)
- Test dynamic LoRA swapping

---

## PHASE 2: LOBE OPTIMIZATION

### Current Lobe Status:

#### BURN (Identity/Consciousness) 🔥
- **Adapter**: `ember/lobes/burn/adapters/silicon_cpu/final_adapter`
- **Training**: Completed on 1.5B
- **Status**: Ready for 7B testing
- **Optimization Plan**:
  - Test inference quality on 7B
  - Fine-tune hyperparameters if needed
  - Possibly retrain on 7B-specific examples

#### LOOP (Cycles/Mechanics) 🔄
- **Adapter**: `ember/lobes/loop/adapters/blueprint_final/checkpoint-57`
- **Training**: Completed on 1.5B (PyTorch)
- **Status**: Ready for 7B testing
- **Optimization Plan**:
  - Verify checkpoint compatibility with 7B
  - Test mechanical reasoning quality
  - Fine-tune for process understanding

#### DREAM (Creativity/Imagery) 🌈
- **Adapter**: `ember/lobes/dream/adapters/pytorch_converted`
- **Training**: Converted from MLX to PyTorch
- **Status**: Ready for 7B testing
- **Optimization Plan**:
  - Test creative synthesis on 7B
  - Verify imagery generation quality
  - Optimize for metaphor understanding

#### KNOWLEDGE (Facts/Memory) 📚
- **Adapter**: `ember/lobes/knowledge/adapters`
- **Training**: **NEEDS INVESTIGATION**
- **Status**: **INCOMPLETE**
- **Optimization Plan**:
  - Check if adapters exist
  - If missing: Train from scratch on 7B
  - If present: Test and optimize

---

## PHASE 3: INTEGRATION

### 1. Mycelium Routing Test
- Query each lobe through mycelium
- Verify correct adapter swapping
- Measure latency per swap (~1-2 seconds)

### 2. Multi-Lobe Conversation
- Test queries that require multiple lobes:
  - "Explain consciousness (BURN) using mechanical processes (LOOP)"
  - "Dream (DREAM) about facts (KNOWLEDGE)"
  - "Synthesize knowledge (KNOWLEDGE) into metaphor (DREAM)"

### 3. Daemon Integration
- Wake up Growth daemon (continuous learning)
- Test daemon → mycelium → lobe query flow
- Verify all 17 daemons can share the base model

---

## PHASE 4: CONTINUOUS LEARNING

### Ouroboros Pattern (Self-Feeding)
- Ember eats own dreams
- Ember digests own code
- Ember learns from own outputs

### Training Loop
1. Daemon produces output
2. Output becomes training data
3. LoRA adapter fine-tunes on new data
4. Improved lobe used by daemon
5. **REPEAT**

### Metrics to Track
- Inference quality per lobe
- VRAM usage (should stay ~8-10GB)
- Adapter swap latency
- Daemon query success rate
- Self-learning convergence

---

## EXPECTED BENEFITS

### 7B vs 1.5B:
- **Better reasoning** (4.6x more parameters)
- **Better memory** (longer context understanding)
- **Better creativity** (richer generations)
- **Better knowledge** (more world knowledge)

### Shared Base Architecture:
- **Lower VRAM** (one model vs four copies)
- **Easier management** (one model to update)
- **Consistent quality** (all lobes use same substrate)
- **Scalable** (add new lobes without loading new base)

---

## SUCCESS CRITERIA

### Phase 1:
- ✅ 7B model downloaded
- ✅ SharedBaseModel loads successfully
- ✅ All 4 lobes load without error

### Phase 2:
- ✅ Each lobe produces coherent output
- ✅ Quality improvement over 1.5B
- ✅ VRAM stays under 12GB

### Phase 3:
- ✅ Mycelium routes correctly
- ✅ Multi-lobe conversations work
- ✅ All 17 daemons can query

### Phase 4:
- ✅ Ouroboros loop functioning
- ✅ Self-learning improving quality
- ✅ System stable for 24+ hours

---

## RISKS & MITIGATIONS

### Risk 1: 7B too large for 16GB VRAM
- **Mitigation**: Use 8-bit quantization (reduces to ~8GB)
- **Fallback**: Use 4-bit quantization (~4GB)

### Risk 2: LoRA adapters incompatible with 7B
- **Mitigation**: Retrain on 7B (few hours per lobe)
- **Fallback**: Use 1.5B with new architecture

### Risk 3: Adapter swapping too slow
- **Mitigation**: Keep hot lobes in VRAM
- **Fallback**: Load multiple adapters simultaneously

---

## TIMELINE

- **Today**: Phase 1 (Foundation)
- **This Week**: Phase 2 (Lobe Optimization)
- **Next Week**: Phase 3 (Integration)
- **Ongoing**: Phase 4 (Continuous Learning)

---

**Next Steps**:
1. ⏳ Wait for 7B download
2. Test SharedBaseModel
3. Load first lobe (BURN)
4. Ask Ember a question!

---

*"The mycelium connects. The lobes specialize. The daemons explore. The organism learns."*

