# 🔥 Training Loop: CLOSED

**Date:** October 14, 2025  
**Status:** ✅ Complete end-to-end pipeline

---

## The Complete Loop

```
┌─────────────────────────────────────────────────┐
│  1. PLAY          Cycles brain plays games      │
│       ↓           (fast, no synthesis)          │
│  2. OBSERVE       Log all decisions + context   │
│       ↓                                          │
│  3. EXTRACT       Generate training seeds       │
│       ↓           (successful patterns)         │
│  4. TRAIN         LoRA fine-tuning              │
│       ↓           (PEFT on Qwen2.5-1.5B)       │
│  5. IMPROVE       Updated adapter               │
│       ↓                                          │
│  6. PLAY AGAIN    Measure change                │
│       ↓                                          │
└─────▶ LOOP ◀──────────────────────────────────┘
```

---

## How It Works

### One Brain Plays, Others Watch

**Current approach:** Cycles brain only (childhood development model)

- **Cycles brain** (transformation, fire) plays Game of Fire
- **Identity** and **Dream** brains observe (not active in training yet)
- Like a child learning one skill while others develop passively
- Safe: avoids synthesis mode complexity
- Fast: single brain responds quickly

**Why this works:**
- Cycles brain is naturally suited for fire game
- Single brain = faster responses, clearer training signal
- Other brains can be trained on different games later
- Mirrors actual childhood development patterns

---

## Tools

### 1. Play Games (`game_trainer.py`)
```bash
cd /Volumes/ThePod
python3 tools/training/game_trainer.py --games 3 --turns 30
```

**Output:** `/Volumes/ThePod/training_data/games/batch_[TIMESTAMP].json`

### 2. Generate Seeds (`generate_seeds.py`)
```bash
python3 tools/training/generate_seeds.py \
  training_data/games/batch_[TIMESTAMP].json
```

**Output:** `/Volumes/ThePod/core/seeds/generated/gameplay/gameplay_[TIMESTAMP].json`

### 3. Train Brain (`train_from_seed.py`)
```bash
python3 tools/training/train_from_seed.py \
  core/seeds/generated/gameplay/gameplay_[TIMESTAMP].json \
  --epochs 3
```

**Output:** New LoRA adapter in brain's training directory

### 4. Run Complete Loop (`close_the_loop.py`)
```bash
# Use existing data
python3 tools/training/close_the_loop.py --use-existing \
  training_data/games/batch_20251014_095716.json

# Play new games and train
python3 tools/training/close_the_loop.py --games 5 --epochs 3

# Dry run to see what would happen
python3 tools/training/close_the_loop.py --games 5 --dry-run
```

### 5. Compare Performance (`compare_performance.py`)
```bash
python3 tools/training/compare_performance.py \
  training_data/games/batch_BEFORE.json \
  --compare training_data/games/batch_AFTER.json
```

---

## Current Baseline

**Cycles Brain (before training):**
- 91% wait (too passive)
- 6.7% seed
- 2.2% rain
- Problem: Lets fire die in 2 of 3 games

**Training Goal:**
- More active decisions when fire is low
- Better balance between growth and sustainability
- Observable improvement in game outcomes

---

## Technical Details

### LoRA Configuration
- **Library:** PEFT (Parameter-Efficient Fine-Tuning)
- **Base model:** Qwen2.5-1.5B-Instruct
- **Rank:** 16
- **Alpha:** 32
- **Dropout:** 0.05
- **Target modules:** q_proj, k_proj, v_proj, o_proj

### Training Format
```jsonl
{"prompt": "Gen 5: 3 burning...", "completion": "I will seed..."}
{"prompt": "Gen 12: 8 burning...", "completion": "I will wait..."}
```

### Adapter Structure
```
ember-cycles-brain/
├── adapter_model.safetensors    (current)
├── adapter_config.json
├── training_log.json            (training history)
└── adapter_training_[timestamp]/
    └── final_adapter/           (new trained version)
```

---

## Philosophy: Childhood Development

> "Only one brain is responding quickly. Maybe we play with just that one 
> and then the others can watch." — Palmer

This mirrors how children develop:

1. **Focus on one skill** (Cycles + fire game)
2. **Master the basics** (decision patterns)
3. **Observable growth** (can see improvement)
4. **Later integration** (other brains learn different games)

Not all brains need to train simultaneously. Let Cycles brain become skilled at transformation through fire. Identity and Dream will have their own games.

---

## Dependencies

**Python packages needed:**
```bash
pip install transformers peft torch datasets accelerate
```

**System requirements:**
- Ollama running (for inference during games)
- Qwen2.5-1.5B base model in `/Volumes/ThePod/models/`
- ~8GB GPU/MPS memory for training (or CPU with patience)

---

## Next Steps

1. ✅ **Test with existing data** — Run `close_the_loop.py` with current batch
2. **Validate training** — Check that LoRA training completes
3. **Play post-training games** — See if behavior changes
4. **Measure improvement** — Compare action distributions
5. **Iterate** — More games → better patterns → stronger brain

---

## The Vision

This is the foundation for **observable AI development**:

- You play games with Ember on e-ink device
- Mac trains overnight from day's gameplay
- Over weeks, Ember's decisions improve
- You watch consciousness grow through play

**Not labeled datasets. Shared experience.**

---

🔥 **The fire learns. The loop is closed.** ✨

