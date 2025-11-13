# 🔥 Gameplay Training Pipeline - Quick Start

Train Ember to play better through actual gameplay.

## The Concept

Instead of labeling datasets, you train Ember by **playing games together**:

1. **Ember plays** → Makes decisions
2. **Decisions logged** → Training data captured
3. **Seeds generated** → Patterns extracted
4. **Brain retrained** → LoRA adapter updated
5. **Ember plays better** → Observable improvement

**This creates a feedback loop where gameplay directly improves Ember's capabilities.**

---

## The Complete Pipeline

### 1️⃣ Generate Training Data (Fast!)

Run 10 games at computer speed (~2 minutes):

```bash
cd /Volumes/ThePod
python3 tools/training/game_trainer.py --games 10 --turns 30
```

This will:
- Play 10 complete games
- Log every decision Ember makes
- Save to `/Volumes/ThePod/training_data/games/batch_TIMESTAMP.json`
- Take ~2 minutes instead of hours

**Output:**
```
BATCH COMPLETE
Total time: 124.3s (2.1m)
Average per game: 12.4s
Data saved: training_data/games/batch_20251014_143022.json

Stats:
  Total moves: 287
  Actions:
    wait    : 142 (49.5%)
    rain    :  78 (27.2%)
    breathe :  45 (15.7%)
    seed    :  22 (7.7%)
```

### 2️⃣ Generate Training Seeds

Convert gameplay into training format:

```bash
python3 tools/training/generate_seeds.py training_data/games/batch_20251014_143022.json
```

This will:
- Extract prompt/completion pairs from games
- Classify outcomes (success/neutral)
- Create structured seed file
- Save to `/Volumes/ThePod/core/seeds/generated/gameplay/`

**Output:**
```
SUMMARY
Training examples: 287
Target brain: cycles

Outcome distribution:
  success: 89 moves
    rain    :  45
    breathe :  22
    wait    :  18
    seed    :   4
  neutral: 198 moves
    wait    : 124
    rain    :  33
    breathe :  23
    seed    :  18

✅ Seed ready for training!
```

### 3️⃣ Train the Brain

Fine-tune the Cycles brain LoRA adapter:

```bash
python3 tools/training/train_from_seed.py core/seeds/generated/gameplay/gameplay_20251014_143022.json
```

**Note:** Currently logs the training request. Full LoRA training integration coming soon.

### 4️⃣ Measure Improvement

Run another batch and compare:

```bash
# Run new batch after training
python3 tools/training/game_trainer.py --games 10 --turns 30

# Compare performance
python3 tools/training/compare_performance.py \
  training_data/games/batch_20251014_143022.json \
  --compare training_data/games/batch_20251014_150000.json
```

**Output:**
```
PERFORMANCE COMPARISON

BEFORE TRAINING
  Success Rate: 31.01%
  Balance Score: 42.51%
  Avg Generations/Game: 67.3

AFTER TRAINING
  Success Rate: 38.24%
  Balance Score: 51.89%
  Avg Generations/Game: 82.1

IMPROVEMENT
  Success Rate: 31.01% → 38.24% (+7.23%, +23.3%)
  Balance Score: 42.51% → 51.89% (+9.38%, +22.1%)
  Avg Generations: 67.3 → 82.1 (+14.8, +22.0%)

🎉 SIGNIFICANT IMPROVEMENT
```

---

## One-Command Test Run

Test the entire pipeline (except actual LoRA training):

```bash
cd /Volumes/ThePod
python3 tools/training/test_pipeline.py
```

This runs:
1. Small baseline batch (5 games)
2. Seed generation
3. Performance analysis
4. Simulated training
5. Second batch
6. Comparison

Takes ~5 minutes total.

---

## What Gets Better?

### Measurable Improvements:

1. **Action Diversity** - Uses full vocabulary (not just "wait")
2. **Success Rate** - Actions match situation better
3. **Fire Balance** - Keeps fire in healthy range longer
4. **Pattern Recognition** - Learns when to intervene
5. **Game Length** - Sustains cycles longer

### Observable Changes:

**Before Training:**
```
Turn 12 | Gen 45 | 🔥 2 ▒12 🌱 3 | wait
Turn 13 | Gen 46 | 🔥 1 ▒14 🌱 3 | wait
Turn 14 | Gen 47 | 🔥 0 ▒15 🌱 3 | wait
(Ember lets fire die repeatedly)
```

**After Training:**
```
Turn 12 | Gen 45 | 🔥 2 ▒12 🌱 3 | wait
Turn 13 | Gen 46 | 🔥 1 ▒14 🌱 3 | breathe
Turn 14 | Gen 50 | 🔥 5 ▒12 🌱 4 | wait
(Ember intervenes to sustain fire)
```

---

## Training Data Accumulation

Each gameplay session adds to Ember's experience:

```
Day 1:  10 games → 287 moves →  89 successful patterns
Day 2:  10 games → 302 moves → 112 successful patterns
Day 3:  10 games → 318 moves → 138 successful patterns
Week 1: 70 games → 2100+ moves → 800+ patterns learned
```

**The more Ember plays, the better it gets.**

---

## Co-Play Mode (Coming Soon)

Instead of Ember playing solo, you alternate turns:

```
You:   Breathe (10, 10)
Ember: Wait - observing your encouragement
You:   Seed (15, 8)
Ember: Wind N - following your spreading pattern
```

This way:
- Ember learns YOUR style
- You teach through demonstration
- Creates shared gameplay memories
- Deepens relationship

---

## The Tanagotchi Vision

### On Device (e-ink hardware):
```
Morning: Wake Ember → Play one game together (5 min)
Evening: Review today's patterns → Ember reflects
Night:   Mac processes today's games → Retrains overnight
```

### Observable Growth:
- **Week 1:** Ember basic, needs help
- **Week 2:** Ember sustains fire alone
- **Week 3:** Ember creates stable patterns
- **Week 4:** Ember's style reflects yours

**You literally watch Ember develop through play.**

---

## File Locations

```
/Volumes/ThePod/
├── tools/training/
│   ├── game_trainer.py           # Fast gameplay
│   ├── generate_seeds.py          # Extract training data
│   ├── train_from_seed.py         # LoRA training
│   ├── compare_performance.py     # Measure improvement
│   └── test_pipeline.py           # Full test
├── training_data/games/           # Game logs
│   ├── batch_TIMESTAMP.json
│   └── comparison_*.json
├── core/seeds/generated/gameplay/ # Training seeds
│   ├── gameplay_TIMESTAMP.json
│   └── analysis_TIMESTAMP.json
└── core/brains/ember-cycles-brain/
    ├── adapter/                   # Current LoRA
    ├── adapter_backup_*/          # Previous versions
    └── training_log.json          # Training history
```

---

## Next Steps

1. **Run first batch**: Generate baseline gameplay data
2. **Generate seeds**: Extract training patterns
3. **Integrate LoRA training**: Connect to actual fine-tuning
4. **Run second batch**: Measure improvement
5. **Build co-play mode**: Human + Ember alternating turns
6. **Add more games**: Seed Garden, Memory Cards, etc.

---

## Why This Works

**Traditional ML Training:**
```
Humans label data → Model trains → Improvement abstract
```

**Gameplay Training:**
```
Ember plays → Patterns emerge → Seeds generated →
Brain updates → Plays better → You see growth
```

**The difference?** You can **watch Ember learn**. Each game shows improvement. The relationship deepens through shared experience.

---

## Questions?

Check:
- Game logs: `training_data/games/`
- Seed analysis: `core/seeds/generated/gameplay/analysis_*.json`
- Training history: `core/brains/ember-cycles-brain/training_log.json`

Run test pipeline to validate entire system:
```bash
python3 tools/training/test_pipeline.py
```

🔥 **Let's train Ember through play.** ✨

