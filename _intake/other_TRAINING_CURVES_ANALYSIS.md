# Training Curves Analysis - The "Riddle Seeds" Theory

## Dataset Size vs Optimal Epochs

### Small Dataset (30-60 examples)
**Optimal: 8-12 epochs**

```
Epoch 1-3:   Learn basic syntax patterns
Epoch 4-6:   Learn path structure rules  
Epoch 7-9:   Refine specific paths
Epoch 10-12: Diminishing returns, risk overfitting
```

**Why this range?**
- Too few epochs (1-5): Model hasn't internalized patterns
- Sweet spot (8-12): Learned patterns, not memorized exact strings
- Too many (15+): Starts memorizing training data verbatim

**Test:**
```bash
# Undertrained (5 epochs)
Input: "list my dreams"
Output: [TOOL:list_directory path='/Volumes/ThePod/']  # Incomplete

# Well-trained (9 epochs)  
Input: "list my dreams"
Output: [TOOL:list_directory path='/Volumes/ThePod/memory/dreams']  # Perfect

# Overtrained (20 epochs)
Input: "list my dreams"
Output: [TOOL:list_directory path='/Volumes/ThePod/memory/dreams']  # Perfect
Input: "show me my dreams"  # Slightly different phrasing!
Output: [TOOL:list_directory path='/Volumes/ThePod/memory/']  # Confused!
```

---

### Medium Dataset (100-200 examples)
**Optimal: 5-8 epochs**

More examples = faster learning per epoch.

```
Epoch 1-2:   Learn basic patterns
Epoch 3-5:   Learn edge cases
Epoch 6-8:   Polish and refine
```

**Why fewer epochs?**
- Each epoch exposes model to more diverse patterns
- Less risk of overfitting (harder to memorize 200 things)
- Diminishing returns kick in sooner

---

### Large Dataset (500+ examples)  
**Optimal: 3-5 epochs**

Industrial-scale training.

```
Epoch 1:     Learn 80% of patterns
Epoch 2-3:   Learn 15% more (edge cases)
Epoch 4-5:   Final 5% polish
```

**Why so few?**
- Massive diversity = fast learning
- Model sees enough variation to generalize
- More epochs = wasted time and electricity

---

## The "Riddle Seeds" Concept

### Definition

**Riddle Seeds** = Training examples that are:
1. **Ambiguous** - Multiple valid interpretations
2. **Complex** - Long paths, nested structure
3. **Rare** - Unusual phrasing or edge cases
4. **High-density** - Teach multiple patterns at once

### Example: Regular vs Riddle

**Regular Seed (Easy)**
```json
{
  "input": "read STATUS.md",
  "output": "[TOOL:read_file path='/Volumes/ThePod/STATUS.md']",
  "difficulty": "easy",
  "epochs_to_learn": 3
}
```

**Riddle Seed (Hard)**
```json
{
  "input": "show me that protocol thing Palmer mentioned from the verse seeds",
  "output": "[TOOL:read_file path='/Volumes/ThePod/seeds/planted/verse/seed-verse-hammer-protocol.json']",
  "difficulty": "hard",
  "epochs_to_learn": 12,
  "teaches": ["path resolution", "nested directories", "fuzzy matching", "context awareness"]
}
```

---

## Training Strategy: Mixed Difficulty

### The Curriculum Learning Approach

Instead of random examples, **order by difficulty**:

```python
# Phase 1: Epochs 1-3 - Easy seeds only
easy_seeds = [
    "read STATUS.md",
    "list seeds",
    "show exports"
]

# Phase 2: Epochs 4-7 - Mix of easy + medium
medium_seeds = [
    "read the hammer protocol",
    "list my recent dreams",
    "show verse seeds"
]

# Phase 3: Epochs 8-10 - All difficulties
riddle_seeds = [
    "show me that spiral thing from the upgrade folder",
    "read the GPT-5 story about mirrors",
    "find the blueprint atlas I created last week"
]
```

**Result**: Model learns faster and better!

---

## Identifying Your Riddle Seeds

### Method 1: Track Validation Loss Per Example

During training, measure which examples have highest loss:

```python
# After epoch 5
high_loss_examples = [
    {"input": "...", "loss": 2.3},  # Still struggling
    {"input": "...", "loss": 1.8},  # Riddle seed!
    {"input": "...", "loss": 0.2},  # Learned
]
```

Examples with **high loss after 5+ epochs** = riddle seeds.

**Solution**: 
- Add 5 more similar examples
- OR train 5 more epochs
- OR use bigger model

---

### Method 2: Complexity Scoring

Score each example by:
1. **Path depth** - `/Volumes/ThePod/seeds/planted/verse/file.json` = depth 5
2. **Ambiguity** - "that thing Palmer mentioned" = high ambiguity
3. **Token count** - Longer = harder
4. **Rarity** - How often do users say this?

```python
def riddle_score(example):
    score = 0
    score += example['output'].count('/') * 2  # Path depth
    score += len(example['input'].split()) / 2  # Length penalty
    score += ambiguity_words(example['input']) * 5  # "that", "thing", etc.
    return score

# Score > 15 = Riddle seed (needs more epochs or examples)
```

---

## Optimal Training Recipe for EmberMind

### Current Status (v2)
- **Dataset**: 61 examples
- **Epochs**: 10
- **Result**: Good, but path accuracy issues

### Problem
Some examples are **riddle seeds** that need:
- More similar examples (5+ variations), OR  
- More epochs (15-20), OR
- Bigger model (355M)

### Recommendation A: Add More Examples (Best)

Expand dataset to 150 examples:
- 100 easy seeds (basic paths)
- 30 medium seeds (nested paths)
- 20 riddle seeds (complex/ambiguous)

Train for **6-8 epochs** instead of 10.

**Why?** More diversity > more repetition

---

### Recommendation B: Longer Training on Riddles

Keep 61 examples, but:
1. Identify the 10 hardest examples (riddle seeds)
2. Train normally for 10 epochs
3. **Continue training for 5 more epochs on just the riddle seeds**

This is called **targeted fine-tuning**.

---

### Recommendation C: Two-Stage Training

**Stage 1: Foundation (5 epochs, all examples)**
- Learn basic patterns fast
- Validation loss: ~0.5

**Stage 2: Riddle Focus (10 epochs, hard examples only)**
- Only train on the 20 hardest examples
- Nail the edge cases
- Final validation loss: ~0.2

---

## Real-World Test

Let's identify EmberMind's current riddle seeds:

### Test 1: Path Depth
```bash
Easy:    "list seeds" → /seeds (loss: 0.1)
Medium:  "list verse seeds" → /seeds/planted/verse (loss: 0.3)
Riddle:  "read hammer protocol from verse" → /seeds/planted/verse/seed-verse-hammer-protocol.json (loss: 1.2)
```

### Test 2: Ambiguity
```bash
Easy:    "read STATUS.md" → /STATUS.md (loss: 0.1)
Riddle:  "show me that thing we worked on yesterday" → ??? (loss: 2.5)
```

### Test 3: Rarity
```bash
Common:  "read X" appears 20 times in training (loss: 0.1)
Rare:    "show me X" appears 3 times in training (loss: 0.8)
Riddle:  "find X" appears 0 times in training (loss: 3.0+)
```

---

## Conclusion

### Your Insight is Correct!

**30-60 examples** → Optimal at **8-12 epochs**  
**100-200 examples** → Optimal at **5-8 epochs**  
**500+ examples** → Optimal at **3-5 epochs**

### The Riddle Seeds Theory

Some examples are **inherently harder** and need:
- More similar examples (augmentation)
- More training time (15-20 epochs)
- OR bigger models (355M parameters)

### Next Steps for EmberMind

**Option 1**: Expand to 150 examples, train 6-8 epochs  
**Option 2**: Identify riddle seeds, add 5 variations each  
**Option 3**: Two-stage training (general → riddles)  

**My recommendation**: Option 1 - More examples beats more epochs every time.

---

**The Golden Rule**: 
> "More diversity in training data > More repetition of same data"

Unless you have riddle seeds. Then you need both. 🎯

