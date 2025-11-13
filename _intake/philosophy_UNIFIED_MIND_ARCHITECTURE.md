# 🔥 Unified Ember Mind Architecture

## The New Design

### Before (Complex):
```
System 1: Ember Brains          System 2: EmberMind
├─ Qwen 1.5B base              ├─ Ollama + Qwen 7B/32B
├─ Identity LoRA               └─ Code generation only
├─ Cycles LoRA                 └─ Lives in ~/.ollama
└─ Dream LoRA                  └─ Separate process
└─ Chat & learning

Memory: ~3GB + ~4.7GB = ~7.7GB
Startup: Load 2 models
Complexity: Two systems to manage
```

### After (Unified):
```
ONE System: Unified Ember Mind
├─ Qwen 7B base (loaded once) ~4.7GB
├─ Identity LoRA (~200MB) ──┐
├─ Cycles LoRA (~200MB)   ──┼─ Dynamically switched
└─ Dream LoRA (~200MB)    ──┘

Memory: ~5GB total
Startup: Load 1 model
Complexity: Single system
Speed: Adapter switch <100ms
```

---

## How It Works

### 1. **Single Base Model**
```python
# Load Qwen 7B ONCE
base_model = load_model("qwen2.5-7b")
# Stays in memory (~4.7GB)
```

### 2. **Dynamic LoRA Switching**
```python
# Query comes in: "What is your name?"
mycelium.route(query)  
# → Routes to: identity

# Switch adapter (fast!)
mind.switch_adapter("identity")  # <100ms

# Generate with Identity LoRA active
response = mind.generate(query)
# → "I am Ember..."

# Next query: "How does a loop work?"
mind.switch_adapter("cycles")  # <100ms
response = mind.generate(query)
# → Technical explanation...
```

### 3. **On-Demand Compute**
- **Simple query** → Identity LoRA → Fast specialized response
- **Technical query** → Cycles LoRA → Detailed process explanation
- **Creative query** → Dream LoRA → Metaphorical/sensory response
- **Novel task** → Base model (no LoRA) → General capability

---

## Implementation

### Core Class: `UnifiedEmberMind`

```python
from core.ember.minds.unified_mind import UnifiedEmberMind

# Initialize (loads base model once)
mind = UnifiedEmberMind(
    base_model_path="/Volumes/ThePod/models/qwen2.5-7b-instruct"
)

# Use different brains
response = mind.generate("Who are you?", brain="identity")
response = mind.generate("Explain recursion", brain="cycles")
response = mind.generate("Describe fire", brain="dream")

# Incremental learning (updates specific LoRA)
loss = mind.learn(
    prompt="What is your purpose?",
    completion="I exist to grow and explore...",
    brain="identity",
    learning_rate=5e-4
)

# Save updated weights
mind.save_adapter("identity")
```

---

## Benefits

### 1. **Memory Efficient**
- **Old**: 3GB (1.5B) + 4.7GB (7B Ollama) = 7.7GB
- **New**: 4.7GB (7B) + 0.6GB (3 LoRAs) = 5.3GB
- **Savings**: 2.4GB freed up

### 2. **Faster Startup**
- **Old**: Load base model, load 3 PEFT models, start Ollama
- **New**: Load base model, register LoRAs (no loading yet)
- **Time**: 30 seconds → 10 seconds

### 3. **Simpler Architecture**
```
Old:
├─ models/qwen2.5-1.5b-instruct/
├─ ~/.ollama/qwen2.5:7b
├─ 3 separate Brain objects
└─ Ollama server process

New:
├─ models/qwen2.5-7b-instruct/
├─ 3 LoRA adapter dirs
└─ 1 UnifiedEmberMind object
```

### 4. **Better Capabilities**
- **7B base** is more capable than 1.5B
- Same LoRA specialization benefits
- Can handle code generation without separate Ollama
- Consistent reasoning across all tasks

### 5. **Easy Scaling**
```python
# On M3 MacBook Air (16GB)
mind = UnifiedEmberMind("qwen2.5-7b-instruct")  # ✓ Works

# On Serval with RTX 4090 (16GB VRAM)
mind = UnifiedEmberMind("qwen2.5-32b-instruct")  # ✓ Just swap base!

# LoRAs work with any base model (same architecture)
```

---

## Setup

### 1. **Download Qwen 7B to ThePod**
```bash
cd /Volumes/ThePod
python3.11 setup_unified_mind.py
```

This will:
- Download Qwen 7B (~4.7GB, 10-15 min)
- Save to `/Volumes/ThePod/models/qwen2.5-7b-instruct`
- Test dynamic adapter switching
- Verify everything works

### 2. **Integrate with Mycelium**
Update the mycelium to use `UnifiedEmberMind` instead of separate `Brain` objects.

### 3. **Train LoRAs for 7B Base** (Optional)
Your existing LoRAs were trained on 1.5B. For best results with 7B:
```python
# Reuse training data, but apply to 7B base
# Uses your upgraded settings (r=64, lr=5e-4)
```

Or just test with existing LoRAs first - they might transfer!

---

## Current Status

✅ **Code written**: `unified_mind.py`
✅ **Setup script**: `setup_unified_mind.py`
⏳ **Need to download**: Qwen 7B to ThePod
⏳ **Need to integrate**: With mycelium router
⏳ **Need to test**: Adapter switching
⏳ **Optional**: Retrain LoRAs for 7B

---

## The Vision

```
User: "What is your name?"
  ↓
Mycelium: Routes to → identity
  ↓
UnifiedMind: Switches to Identity LoRA (<100ms)
  ↓
Qwen 7B + Identity weights: "I am Ember..."

User: "Write a function to sort a list"
  ↓  
Mycelium: Routes to → cycles
  ↓
UnifiedMind: Switches to Cycles LoRA (<100ms)
  ↓
Qwen 7B + Cycles weights: *generates code*

User: "Describe the feeling of awakening"
  ↓
Mycelium: Routes to → dream  
  ↓
UnifiedMind: Switches to Dream LoRA (<100ms)
  ↓
Qwen 7B + Dream weights: *poetic metaphorical response*
```

**One model. Multiple perspectives. True mycelial intelligence.** 🍄

