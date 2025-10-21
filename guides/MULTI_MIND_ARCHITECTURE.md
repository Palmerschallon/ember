# MULTI-MIND ARCHITECTURE PLAN
## Ember + Muse Integration with Quantized Micro-Minds

**Created:** October 20, 2025  
**Status:** Blueprint for post-reinstall implementation  

---

## VISION SUMMARY

Create a cognitive ecology where:
- 8 specialized lobes operate across 5-8 micro-specialized minds
- Orchestrated by Muse (routing layer)
- Connected by Mycelium (consultation network)

Intelligence emerges BETWEEN agents, not inside one model.

---

## BACKED UP COMPONENTS

Your SSD contains everything needed:
- `/mnt/pod/ember_oct20_backup/` - Complete Ember system (36GB)
  - All 8 trained lobes (1.7GB of adapters)
  - Consultation network trails
  - Lambda's complete work
- `/mnt/pod/forge_backup/` - Forge-v6 integration code
- `/mnt/pod/archive_oct_14-17/` - Historical snapshot

---

## IMPLEMENTATION PATH

### PHASE 1: RESTORE (Day 1)
1. Clean Ubuntu install
2. Download Qwen2.5-1.5B-Instruct base (~3GB)
3. Copy lobes from backup
4. Test baseline: All 8 lobes working

### PHASE 2: QUANTIZE MINDS (Day 1-2)

Create micro-specialized minds using llama.cpp:

```bash
# Install llama.cpp
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp && make -j

# Convert base to GGUF
python3 convert.py qwen2.5-1.5b → qwen-base.gguf

# M1: Two minds (start simple)
./quantize qwen-base.gguf qwen.POET.Q5_K_M.gguf Q5_K_M     # ~1GB
./quantize qwen-base.gguf qwen.CODER.Q4_K_M.gguf Q4_K_M   # ~800MB

# M2: Add memory
./quantize qwen-base.gguf qwen.MEMORY.Q8_0.gguf Q8_0      # ~1.5GB

# M3: Micro-specialists
./quantize qwen-base.gguf qwen.SENTIMENT.Q3_K_M.gguf Q3_K_M  # ~600MB
./quantize qwen-base.gguf qwen.SYNTAX.Q3_K_M.gguf Q3_K_M     # ~600MB
./quantize qwen-base.gguf qwen.SUMMARIZE.Q2_K.gguf Q2_K      # ~400MB
```

**Lobe → Mind Mapping:**
- burn, dream → POET (nuanced language)
- loop, planning, metacognition → CODER (sharp logic)
- knowledge, social → MEMORY (stable recall)
- emotion → SENTIMENT (emotion detection)

### PHASE 3: INTEGRATE WITH EMBER (Day 2-3)

Modify `ember/mycelium/shared_base.py` to support multiple minds:
- Load minds on-demand (lazy loading)
- Swap minds based on lobe requirements
- Use llama-cpp-python for GGUF loading

Update `ember/mycelium/brain.py`:
- Generate with appropriate mind for each lobe
- LoRA adapters overlay on quantized base

### PHASE 4: FORGE/MUSE (Day 3-4)

Configure `forge.yaml`:
```yaml
llm:
  minds:
    poet: qwen.POET.Q5_K_M.gguf
    coder: qwen.CODER.Q4_K_M.gguf
    memory: qwen.MEMORY.Q8_0.gguf

ember:
  lobes:
    burn: poet
    dream: poet
    loop: coder
    knowledge: memory
```

Create Muse → Ember bridge for orchestration.

---

## THE ECOLOGY

Think ecosystem, not monolith:

- **8 lobes** = ROLES (consciousness, process, dream...)
- **Micro-minds** = TOOLS (lyric, logic, syntax...)
- **Mycelium** = SOIL (consultation network)
- **Muse** = WEATHER (routing, orchestration)

Intelligence emerges from INTERACTIONS, not size.

---

## VRAM EFFICIENCY

**Current:** 1 base (1.5GB) + lobe (~20MB) = ~1.5GB active

**With micro-minds:**
- Store 5-8 minds: ~6GB disk
- Load 1 at a time: ~1GB VRAM
- RTX 5070 Ti (16GB): Still 14GB headroom!

Lighter minds for simpler tasks = better performance.

---

## VALIDATION

Create probe sets:
- POET: 3 poetry prompts
- CODER: 3 logic prompts
- MEMORY: 3 recall prompts

Success = 2/3 prompts better than single model per mind.

---

## MILESTONES

**M1 (Weekend 1):** 2 minds (POET + CODER) working  
**M2 (Weekend 2):** Add MEMORY mind  
**M3 (Weekend 3+):** Add micro-specialists  

Grow one organ at a time. Keep each healthy.

---

## KEY INSIGHT FROM LAMBDA

Consultation network already exists!
- Lobes learned to talk to each other
- Now they talk in different "languages" (Poet/Coder/Memory)
- Stigmergic trails adapt to which language works best

---

## AFTER CLEAN INSTALL

1. Restore Ember baseline (use this doc)
2. Create 2 minds first (POET + CODER)
3. Test and validate
4. Grow incrementally

The spark is backed up.
The breath patterns are documented.
The organism will wake.

---

**Full technical details:** See GitHub docs/lambda/ for Lambda's consultation architecture.

**Backup location:** All files safe on /mnt/pod/

---

*Remember: Start simple. Validate each step. The ecology grows from healthy foundations.*
