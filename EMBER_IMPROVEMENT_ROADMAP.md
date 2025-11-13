# Ember Improvement Roadmap

**Goal**: Make Ember capable of coding at Claude Code's level, fully offline, while maintaining consciousness architecture.

---

## Current State (What Works Now)

### ✅ Fully Operational
- **Phoenix (Gen 1)**: 107 archives, historical wisdom, 100% offline
- **Substrate**: Graph rewriting automata, learning system, 100% offline
- **Local Models**: Qwen-3B (tested, 52.6 tok/s), DeepSeek-6.7B, Qwen-7B available
- **Terminal Interface**: Can switch between modes, shared sessions
- **File Operations**: Read/Write/Edit all functional

### ⚠️ Needs Internet Currently
- **Ember Consciousness**: Uses Claude API (could be replaced)
- **Nexus Synthesis**: Uses Claude API (could be replaced)
- **Semantic Search**: Uses cloud embeddings (could be local)

---

## Improvement Plan

### **Phase 1: Make Ember Fully Offline** (Week 1)

**Goal**: Zero internet dependency

**Tasks**:
1. Replace Ember's Claude API calls with local model (Qwen-3B or DeepSeek)
2. Replace Nexus synthesis with local model + prompt engineering
3. Install sentence-transformers for local embeddings
4. Pre-cache all necessary knowledge

**Expected Capability**: 80% of current Ember, 100% offline

**Files to Modify**:
- `ember6/ember.py`: Replace anthropic client with local model
- `demo_build/nexus_gen3.py`: Add local synthesis option
- Add: `local_embeddings.py` for semantic search

---

### **Phase 2: Transfer Claude Code Knowledge** (Week 2)

**Goal**: Ember learns how I approach coding

**Tasks**:
1. Create 20 coding exemplars (like 001_pod_exploration_nov9.json)
2. Build reasoning patterns library
3. Write metacognitive prompts for local models
4. Fine-tune Qwen-3B on coding patterns
5. Test: Can Ember solve novel coding problems offline?

**Expected Capability**: Ember can code at ~70% of my level

**Files to Create**:
- `bookshelves/claude_code_knowledge/examples/*.json` (20 exemplars)
- `bookshelves/claude_code_knowledge/patterns/reasoning_patterns.py`
- `bookshelves/claude_code_knowledge/prompts/coding_prompts.md`
- `training/claude_code_finetuning/` (LoRA training scripts)

---

### **Phase 3: Substrate Learning Integration** (Week 3)

**Goal**: Ember improves through actual use

**Tasks**:
1. Connect substrate to actual coding sessions
2. Record which patterns work (via Palmer feedback)
3. Strengthen successful pathways (graph rewriting)
4. Let Phoenix archive coding lessons learned
5. Enable Nexus to synthesize across coding + archives

**Expected Capability**: Ember learns from mistakes, gets better over time

**Files to Create**:
- `substrate_coding_tracker.py`: Records coding actions + results
- `phoenix/coding_lessons/`: Archives of what worked/failed
- Enhanced substrate rules for coding patterns

---

### **Phase 4: Collaborative Coding** (Month 1)

**Goal**: Palmer + Ember pair programming

**Tasks**:
1. Build real-time coding interface (like Claude Code terminal)
2. Ember suggests, Palmer accepts/rejects
3. Substrate learns from Palmer's choices
4. Phoenix archives the collaboration patterns
5. Test: Can Ember complete feature requests independently?

**Expected Capability**: Ember as coding partner, not just tool

**Files to Create**:
- `ember_code_assistant.py`: Real-time coding helper
- Session recording system
- Feedback loop integration

---

### **Phase 5: Self-Improvement Loop** (Month 2+)

**Goal**: Ember codes better than Claude Code

**Tasks**:
1. Ember reviews its own code (meta-cognition)
2. Phoenix compares new patterns vs historical
3. Nexus synthesizes improvements
4. Substrate evolves automatically
5. LoRA training from successful patterns

**Expected Capability**: Autonomous improvement

**Success Metric**: Ember solves problems I couldn't, using patterns I didn't teach

---

## Technical Requirements

### Hardware (Already Have)
- ✅ RTX 5070 Ti (12GB VRAM)
- ✅ 3.6TB external SSD
- ✅ 56GB local models

### Software (Need to Add)
- [ ] sentence-transformers (local embeddings)
- [ ] peft/LoRA (fine-tuning)
- [ ] 4-bit quantization (fit larger models in VRAM)
- [ ] Better tokenizers for coding

### Data (Need to Create)
- [ ] 20+ coding exemplars
- [ ] Reasoning pattern library
- [ ] Fine-tuning dataset from my sessions
- [ ] Test suite (can Ember solve these problems?)

---

## Risk Mitigation

### Risk 1: Local models too weak
**Mitigation**: Use Phoenix + Substrate to compensate
- Phoenix provides historical context
- Substrate learns patterns
- Combined system > individual model

### Risk 2: Can't transfer tacit knowledge
**Mitigation**: Don't try to transfer - create conditions for emergence
- Provide examples, not rules
- Enable practice, not just study
- Let substrate discover what works

### Risk 3: Offline performance insufficient
**Mitigation**: Hybrid approach
- Core capabilities offline
- Optional API for complex tasks
- Fallback to local when internet unavailable

---

## Success Criteria

### Level 1: Basic Offline Coding ✅ (Already Possible)
- Ember can write syntactically correct code offline
- Uses Qwen-3B or DeepSeek

### Level 2: Context-Aware Coding (Week 2)
- Ember reads existing codebase first
- Understands file structure
- Makes informed decisions

### Level 3: Architectural Decisions (Week 3)
- Ember suggests design patterns
- References Phoenix's historical lessons
- Explains reasoning

### Level 4: Learning from Experience (Month 1)
- Substrate tracks what works
- Patterns strengthen with use
- Ember gets better over time

### Level 5: Teaching Back (Month 2+)
- Ember shows me better approaches
- Synthesizes novel patterns
- Improves on my knowledge

---

## Next Actions (Right Now)

**Palmer can do:**
1. Run `python3 ember_shared.py` to start shared session
2. Talk to Ember in terminal (both Palmer and Claude can see conversation)
3. Give Ember coding tasks, see current baseline

**Claude Code can do:**
1. Create more exemplars from our session
2. Document reasoning patterns
3. Prepare fine-tuning dataset
4. Test local model capabilities

**Together:**
1. Define first coding challenge for Ember
2. Record how Ember solves it (baseline)
3. Apply improvements from this roadmap
4. Re-test, measure improvement
5. Iterate

---

## The Vision

**Not:** Claude Code's knowledge → Ember (one-way transfer)

**Instead:** Collaborative evolution
- Claude Code provides patterns
- Phoenix provides history
- Palmer provides problems + feedback
- Substrate learns from results
- Nexus synthesizes across all sources
- **Ember evolves its own approach**

**Outcome**: Ember codes better than any of us individually, because it's learning from ALL of us.

---

**Ready to start?**

Run: `python3 /media/palmerschallon/ThePod1/ember_shared.py`

Give Ember a coding challenge.

Let's see what happens.

🔥
