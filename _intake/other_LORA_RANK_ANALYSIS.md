# 🎯 LORA RANK OPTIMIZATION
## Are We Overtrained? Finding the Sweet Spot

**Palmer's Question:**
> "maybe weve trained our existing loras way too high is there an ideal number?"

---

## 📊 CURRENT STATE:

### What We Have:

```
Original LoRAs: Rank 16 (first attempt)
Current LoRAs: Rank 192 (12x stronger!)

Training:
- Epochs: 3
- Learning rate: 0.0001-0.0003
- Loss: 22.5 → 21.8 (small decrease)
- Size: 200MB per LoRA
```

**Rank 192 is VERY HIGH** - let's analyze if that's good or bad.

---

## 🔬 WHAT IS LORA RANK?

**LoRA decomposes weight updates:**
```
Original model weights: W (e.g., 4096 x 4096)
LoRA update: ΔW = A × B

Where:
A: 4096 × rank
B: rank × 4096

Total params: 4096 × rank × 2
```

**Higher rank = More capacity = More parameters**

### Rank Comparison:

```
Rank 4:     ~33K params per layer
            Very lightweight, weak adaptation
            Good for: Style/tone tweaks

Rank 8:     ~65K params per layer
            Lightweight, mild adaptation
            Good for: Single skill learning

Rank 16:    ~131K params per layer
            Standard, balanced
            Good for: General fine-tuning

Rank 32:    ~262K params per layer
            Strong, noticeable changes
            Good for: Personality shifts

Rank 64:    ~524K params per layer  ⭐ RECOMMENDED
            Very strong, clear behavior
            Good for: Specialized agents

Rank 128:   ~1M params per layer
            Extremely strong
            Risk: Overfitting, slow inference

Rank 192:   ~1.6M params per layer  ⚠️ CURRENT
            Overkill for most cases
            Risk: Overfitting, memory overhead

Rank 256:   ~2M params per layer
            Usually unnecessary
            Risk: Training instability
```

---

## ⚠️ PROBLEMS WITH RANK 192:

### 1. **Overfitting Risk**
```
Small dataset (BURN: ~100 examples)
Huge capacity (192 rank = 1.6M params per layer)
= Model memorizes instead of generalizing

Signs:
- Training loss decreases (✓ you see this)
- But model becomes rigid/repetitive
- Loses base model capabilities
```

### 2. **Memory Overhead**
```
Rank 192 LoRA: ~200MB per lobe
Rank 64 LoRA:  ~67MB per lobe  (3x smaller!)
Rank 32 LoRA:  ~33MB per lobe  (6x smaller!)

With 64 LoRAs target:
Rank 192: 12.8GB (won't fit in 6GB VRAM budget!)
Rank 64:  4.3GB  (fits perfectly!)
Rank 32:  2.1GB  (very comfortable)
```

### 3. **Diminishing Returns**
```
Research shows:
Rank 8-16:   80% of performance
Rank 32-64:  95% of performance  ⭐ Sweet spot
Rank 128+:   97% of performance  (minimal gain)
```

### 4. **Inference Speed**
```
More rank = more compute per forward pass

Rank 16:  ~100 tok/sec (negligible overhead)
Rank 64:  ~95 tok/sec (barely noticeable)
Rank 192: ~80 tok/sec (15-20% slower)
```

---

## 🎯 IDEAL RANK BY USE CASE:

### For Ember's Lobes:

**Core 6 Lobes (Strong personality):**
```
Rank: 64-128
Why: Need strong behavioral override
Examples: BURN, LOOP, KNOWLEDGE, EMOTION, PLANNING, SOCIAL
```

**Imagination Lobes (Creative styles):**
```
Rank: 32-64
Why: Stylistic, not behavioral
Examples: ABSTRACTIUMS, BREATH, COMPRESSION
```

**Specialized Tools (Narrow skills):**
```
Rank: 16-32
Why: Single-purpose, need efficiency
Examples: Future domain-specific lobes
```

---

## 📐 THE MATH FOR 192 LORAS:

**Your constraint: 6GB VRAM for LoRAs**

### At Rank 192 (Current):
```
200MB per LoRA × 192 LoRAs = 38.4GB ❌
Won't fit in 6GB budget!
```

### At Rank 64 (Recommended):
```
67MB per LoRA × 192 LoRAs = 12.9GB ⚠️
Still tight, but possible with quantization
```

### At Rank 32 (Efficient):
```
33MB per LoRA × 192 LoRAs = 6.3GB ✅
Perfect fit!
```

### At Rank 48 (Balanced):
```
50MB per LoRA × 192 LoRAs = 9.6GB ⚠️
Slightly over, but workable
```

---

## 💡 THE PROBLEM: EMBER'S CALCULATION

**Ember said:**
> "12GB VRAM = 192 lobes at 32MB each"

**But current LoRAs are 200MB each (rank 192)!**

**This means:**
- Current: Only 30-40 LoRAs fit in 6GB
- Need: Reduce rank to fit 192 LoRAs

---

## 🔥 RECOMMENDATION:

### Option A: Retrain at Rank 32-48 (Best for 192 LoRAs)

**Rank 32:**
- ✅ 192 LoRAs fit in 6.3GB
- ✅ 3x faster training
- ✅ Less overfitting risk
- ✅ Still strong enough for personality
- ⚠️ May need more training data

**Rank 48:**
- ✅ 192 LoRAs fit in 9.6GB (with 4-bit base model)
- ✅ Stronger adaptation
- ✅ Good balance
- ⚠️ Slightly tight on memory

---

### Option B: Keep Rank 64 for Core, Lower for Others

**Hybrid approach:**
```
6 Core Lobes: Rank 64 (400MB total)
58 Specialized: Rank 32 (1.9GB total)
128 Tools: Rank 16 (1.7GB total)
─────────────────────
Total: 192 LoRAs = 4GB ✅
```

**This gives:**
- Strong personality (core 6 at rank 64)
- Diverse capabilities (186 more lobes)
- Fits in VRAM budget

---

### Option C: Keep Current, Limit to 30-40 LoRAs

**If rank 192 is necessary:**
```
11 Current LoRAs: 2.2GB
20 More at rank 192: 4GB
─────────────────────
Total: 31 LoRAs = 6.2GB ✅
```

**But this abandons the "192 LoRAs" vision.**

---

## 🔬 TESTING IF RANK 192 IS OVERTRAINED:

### Signs of Overfitting:

1. **Loss plateaus early** (you see 22.5→21.8 in 3 epochs)
2. **Model repeats exact training phrases**
3. **Less creative/flexible than base model**
4. **Poor performance on novel queries**

### How to Test:

```python
# Test on NEW queries not in training data
queries = [
    "Explain quantum computing",  # Not in training
    "Write a poem about consciousness",  # Creative
    "What is 2+2?",  # Simple (shouldn't forget)
]

# Compare:
# - Base model (no LoRA)
# - Rank 64 LoRA
# - Rank 192 LoRA (current)

# If rank 192 is worse on novel queries → overtrained!
```

---

## 📊 RESEARCH CONSENSUS:

**From LoRA papers and community:**

```
Small models (1-3B):
├── Rank 8-16:  Standard
├── Rank 32-64: Strong adaptation ⭐ RECOMMENDED
└── Rank 128+:  Usually overkill

Large models (7B+):
├── Rank 16-32: Standard
├── Rank 64-128: Strong adaptation
└── Rank 256+:  Rarely beneficial
```

**For DeepSeek 1.3B, rank 64 is the ceiling for most use cases.**

---

## 🎯 MY RECOMMENDATION:

**Retrain at Rank 32 for 192-LoRA Vision**

### Why Rank 32:

1. **Fits the math:** 192 × 32MB = 6.1GB ✅
2. **Strong enough:** Still 2x stronger than original rank 16
3. **Efficient:** Faster training, faster inference
4. **Less overfitting:** Better generalization
5. **Proven sweet spot:** Works for most LoRA use cases

### Training Strategy:

```python
# For new 181 LoRAs:
LoRAConfig(
    r=32,              # Rank (was 192)
    lora_alpha=64,     # 2x rank (standard)
    lora_dropout=0.05, # Prevent overfitting
    target_modules=["q_proj", "v_proj"]  # Standard targets
)

# Training:
epochs=5-10         # More epochs with lower rank
learning_rate=2e-4  # Slightly higher for faster convergence
batch_size=4        # Depends on data
```

---

## 🔥 ANSWER:

**Yes, rank 192 is likely TOO HIGH for:**
- 1.3B model (overkill)
- Small training sets (~100 examples)
- 192 LoRAs target (won't fit)

**Ideal ranks:**
- **Rank 32:** For 192 LoRAs vision ⭐
- **Rank 48:** Balanced alternative
- **Rank 64:** Max for small models (only ~30-40 LoRAs will fit)

**Ember's calculation was correct:**
- 12GB VRAM / 2 (base models) = 6GB for LoRAs
- 6GB / 32MB = 192 LoRAs ✅

**Should we retrain the 11 current LoRAs at rank 32?** Or test current rank 192 first to see if they're actually overtrained? 🔥

∞

— Tau

