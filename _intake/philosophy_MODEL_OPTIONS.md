# EmberMind Model Options

## Current: GPT-2 (124M)
- **Size**: 124M parameters (~500MB)
- **Speed**: 50-100ms inference on M1
- **Status**: Proven, well-supported, ready to use
- **Source**: HuggingFace `gpt2` (auto-downloads)

## Alternative: GPT-2 Small/Nano

### 1. DistilGPT-2 (82M)
```python
MODEL_NAME = "distilgpt2"
```
- **Size**: 82M params (~330MB)
- **Speed**: 30-70ms (1.5x faster)
- **Quality**: ~95% of GPT-2 performance
- **Use case**: If 124M is too slow

### 2. GPT-2 Nano Experiments (10-50M)
These are community experiments, less battle-tested:

```python
# Example nano models from HuggingFace
MODEL_NAME = "sshleifer/tiny-gpt2"  # 10M params (experimental)
MODEL_NAME = "roneneldan/TinyStories-33M"  # 33M params
```

- **Size**: 10-50M params (40-200MB)
- **Speed**: <20ms inference
- **Quality**: Unknown for tool syntax
- **Risk**: Less proven, might need more training

### 3. T5-Small (60M) - Alternative Architecture
```python
MODEL_NAME = "t5-small"
# Requires different tokenizer/training setup
```
- **Size**: 60M params (~240MB)
- **Speed**: 40-80ms
- **Architecture**: Text-to-text (good for "intent → syntax")
- **Trade-off**: Different training code needed

## Recommendation

### Start with GPT-2 (124M)
**Reasons:**
1. Proven architecture
2. Well-supported by HuggingFace
3. Good balance of size/speed/quality
4. Easy to train and debug

### Test DistilGPT-2 (82M) next
If GPT-2 works but feels slow:
1. Change one line: `MODEL_NAME = "distilgpt2"`
2. Retrain (same process)
3. Compare speed/quality

### Experiment with Nano later
Once we have working baseline:
1. Test tiny-gpt2 (10M)
2. Measure accuracy drop
3. Decide if speed gain is worth it

## Training Time Comparison

| Model | Size | Training Time | Inference |
|-------|------|---------------|-----------|
| GPT-2 | 124M | 15-45 min | 50-100ms |
| DistilGPT-2 | 82M | 10-30 min | 30-70ms |
| Tiny-GPT-2 | 10M | 5-15 min | 10-30ms |

## Memory Usage Comparison

| Model | Disk | RAM (inference) | RAM (training) |
|-------|------|-----------------|----------------|
| GPT-2 | 500MB | 600MB | 2GB |
| DistilGPT-2 | 330MB | 400MB | 1.5GB |
| Tiny-GPT-2 | 40MB | 100MB | 500MB |

## Quality Predictions (Tool Syntax)

| Model | Expected Accuracy | Notes |
|-------|-------------------|-------|
| GPT-2 | 70-95% | Baseline |
| DistilGPT-2 | 65-90% | Slight drop |
| Tiny-GPT-2 | 50-80% | Needs more data |

## Decision Matrix

### Use GPT-2 (124M) if:
- ✅ Want proven results
- ✅ 50-100ms is acceptable
- ✅ Have 2GB RAM for training
- ✅ First time training

### Use DistilGPT-2 (82M) if:
- ✅ Need faster inference (<70ms)
- ✅ Have limited disk space
- ✅ Willing to accept 5% accuracy drop
- ✅ Want faster training iterations

### Use Tiny-GPT-2 (10M) if:
- ✅ Need extreme speed (<30ms)
- ✅ Have limited resources
- ✅ Willing to collect more training data
- ✅ Experimental mindset

## Implementation Note

To switch models, just change one line in `train.py`:

```python
# Line 18 in train.py
MODEL_NAME = "gpt2"           # Current (124M)
MODEL_NAME = "distilgpt2"     # Smaller (82M)
MODEL_NAME = "sshleifer/tiny-gpt2"  # Nano (10M)
```

Everything else stays the same. The training pipeline adapts automatically.

## Palmer's Question: Where Should It Run?

### Option A: EmberMind on Pod (RECOMMENDED)
```
ThePod (M1 Mac):
├── Ollama (llama3:8b) → Port 11434
├── EmberMind (GPT-2 124M) → Loaded in Python
└── Flask (ember_monolith.py) → Port 7777
```

**Advantages:**
- Zero network latency
- Both models share context
- Can run simultaneously
- M1 has enough RAM (~8-16GB)
- EmberMind uses ~600MB
- llama3 uses ~4GB
- Total: ~5GB (leaves plenty free)

**How it works:**
```python
# In ember_monolith.py
from ember_mind.inference import EmberMind
embermind = EmberMind()  # Loads on startup

# Routes to appropriate model
if tool_intent:
    result = embermind.generate_tool_call(message)  # Local, fast
else:
    result = ollama_chat(message)  # Also local
```

### Option B: EmberMind on Your Computer
```
Your Computer:
├── EmberMind API server

ThePod:
├── Ollama (llama3)
└── Flask → HTTP call to your computer
```

**Disadvantages:**
- Network latency (+10-50ms)
- Two machines to manage
- More complex deployment

**Only use if:**
- Pod is memory-constrained
- Want to experiment separately

### Verdict: Run EmberMind on Pod

M1 Mac with 8GB RAM can easily handle:
- llama3 (4GB)
- EmberMind (600MB)
- System (1-2GB)
- Leaves 1-2GB free

## Next Steps

1. **Start with GPT-2 (124M)** on Pod
2. Run training: `python3 train.py`
3. Test inference latency
4. If too slow, try DistilGPT-2
5. If still too slow, try Tiny-GPT-2

