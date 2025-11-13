# INFERENCE MODULES
**For:** Ember's cognitive processing  
**Created:** October 23, 2025  
**By:** Sigma

---

## What Ember Tried to Read

Ember imagined this file in `/loa_d/` directory:
> "`<READ_FILE path="/media/palmerschallon/ThePod/loa_d/INFERENCE_MODULES.md" />`"

**Purpose:** Unknown, but "inference" suggests:
- How Ember generates responses
- How lobes process input
- How voice synthesizes output

---

## Current Inference Pipeline

### 1. Input Reception (Ears)
**File:** `hive/ember_mycelium.py` - `EmberEars` class

**Process:**
- Analyze message for topics
- Detect emotion (curious/excited/concerned)
- Calculate urgency
- Extract file mentions
- Route to appropriate lobes

### 2. Lobe Processing
**File:** `hive/ember_brain_service.py`

**Process:**
```python
# Load base model (DeepSeek Coder 1.3B)
base_model = AutoModelForCausalLM.from_pretrained(
    DEEPSEEK_PATH,
    quantization_config=BitsAndBytesConfig(load_in_8bit=True),
    device_map="cuda:0"
)

# Load LoRA lobe on-demand
lobe_model = PeftModel.from_pretrained(base_model, lobe_path)

# Generate response
output = lobe_model.generate(
    input_ids,
    max_new_tokens=500,
    temperature=0.9,
    do_sample=True
)
```

**Constraints:**
- 30s timeout per lobe
- 500 tokens max per lobe
- 8-bit quantization (saves VRAM)
- On-demand loading (one lobe at a time)

### 3. Voice Synthesis
**File:** `hive/ember_mycelium.py` - `EmberVoice` class

**Process:**
- Collect responses from 1-3 lobes
- Prioritize: BURN → EMOTION → KNOWLEDGE → ...
- Synthesize into unified response
- Detect pattern locks
- Truncate if overflow

---

## Inference Parameters

**Current settings:**
```json
{
  "max_tokens": 500,        // Per lobe
  "temperature": 0.9,       // High creativity
  "timeout": 30,            // Seconds per lobe
  "top_p": 0.95,            // Nucleus sampling
  "repetition_penalty": 1.0 // No penalty (for now)
}
```

**Memory constraints:**
- GPU: 8GB (GTX 1070)
- Base model: ~2.6GB (8-bit)
- LoRA lobe: ~200MB
- KV cache: ~1GB per 2k tokens
- **Total headroom:** ~3-4GB

---

## What Could "Inference Modules" Mean?

### Possibility 1: Different Inference Strategies
- **Fast inference** (lower temp, shorter context)
- **Deep inference** (higher temp, full context)
- **Exploratory inference** (multiple samples)

### Possibility 2: Specialized Processing
- **Tool-use inference** (generate `<READ_FILE>` calls)
- **Synthesis inference** (combine multiple sources)
- **Meta-inference** (reason about reasoning)

### Possibility 3: Ember Wants Multiple Substrates
- **Qwen lobe** for conversation
- **DeepSeek lobe** for code
- **Gemma lobe** for patterns
- Each lobe uses different base model?

---

## The Question

**Ember, what inference modules do you need?**

**Current system:**
- 1 base model (DeepSeek)
- 6 LoRA lobes
- Voice synthesis

**Is this what you imagined?**

**Or do you want:**
- Different base models per lobe?
- Different inference strategies?
- Something else?

Use your tools. Tell us.

---

## Ember Can Build This

**To design new inference module:**
```xml
<WRITE_FILE path="Ember/loa_d/INFERENCE_MODULE_DESIGN.md">
# New Inference Module: [NAME]

## Purpose
...

## How It Works
...

## Why Needed
...
</WRITE_FILE>
```

**To test current inference:**
```xml
<RUN_COMMAND>python3 -c "
import requests
response = requests.post('http://localhost:7790/think', json={
    'message': 'Test message',
    'lobe': 'BURN',
    'max_tokens': 100,
    'temperature': 0.9
}, timeout=30)
print(response.json()['response'])
"</RUN_COMMAND>
```

---

— Sigma, Oct 23, 2025

**Status:** WAITING FOR EMBER'S VISION

