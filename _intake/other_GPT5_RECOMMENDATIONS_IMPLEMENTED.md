# GPT-5 Recommendations: Implemented

**Date**: October 6, 2025  
**Status**: ✅ Code Complete, Awaiting Model Download

---

## What We Implemented

Following GPT-5's guidance for improving creative dream artifact generation.

### 1. Model Switching Architecture ✅

**Implementation**:
- `DreamArtifactGenerator` now accepts optional `creative_model_fn`
- Dream executor checks for `OLLAMA_CREATIVE_MODEL` env var
- If set, uses specialized model for creative dreams only
- Falls back to main model if not configured

**Code Changes**:
- `ember/services/dream_artifacts.py`: Added `creative_model_fn` parameter
- `ember/services/dream_executor.py`: Added model switching logic
- `.env`: Added `OLLAMA_CREATIVE_MODEL=deepseek-coder:6.7b-instruct`

### 2. Improved Creative Prompt ✅

**GPT-5's Recommendations Applied**:
- ✅ Explicit regex validation hint: `^\s*\{[\s\S]*\}\s*$`
- ✅ Two complete few-shot examples with proper escaping
- ✅ Clear instructions: "No triple quotes, all strings double-quoted"
- ✅ Explicit requirements for code safety and length
- ✅ Better system prompt: "You are a code generator. Output ONLY valid JSON..."

**Prompt Structure**:
```
1. Regex requirement for validation
2. Example 1: Particle simulation
3. Example 2: Number transformation
4. User's dream narrative
5. Seeds involved (for context)
6. Explicit requirements
7. Output format template
```

### 3. Enhanced JSON Parsing ✅

**Already Implemented** (from previous GPT-5 guidance):
- Strip markdown fences
- Extract JSON between braces
- Auto-add missing closing braces
- Fallback to raw .txt on failure

### 4. Dual-Location Saving ✅

**Already Implemented**:
- Artifacts stay in `/memory/dreams/*/artifacts/` (provenance)
- Successful artifacts copied to `/exports/ember_creations/` (Curator)
- Timestamped filenames for tracking

---

## Configuration

### Current Setup

```bash
# Main model (consolidation, synthesis, chat)
OLLAMA_MODEL=llama3:latest

# Creative dreams (code generation)
OLLAMA_CREATIVE_MODEL=deepseek-coder:6.7b-instruct
```

### Alternative Models (GPT-5's suggestions)

If DeepSeek-Coder doesn't work well:
- `codellama:7b-instruct` - Good JSON discipline, slightly less creative
- `qwen2.5-coder:7b-instruct` - Balances compliance and creativity
- Leave empty to use `llama3:latest` for all dreams

---

## Next Steps

### 1. Download the Model

```bash
# Pull DeepSeek-Coder 6.7B Instruct
ollama pull deepseek-coder:6.7b-instruct
```

**Size**: ~7-8 GB  
**Time**: 5-15 minutes depending on connection

### 2. Restart Ember

```bash
cd /Volumes/ThePod
python3 -m ember.main
```

Look for: `🎨 Creative dreams will use: deepseek-coder:6.7b-instruct`

### 3. Test Creative Dream

```bash
curl -X POST http://127.0.0.1:7777/api/dream/start \
  -H "Content-Type: application/json" \
  -d '{"cycle": "creative"}'
```

### 4. Check Results

```bash
# Check latest dream artifacts
ls -lht /Volumes/ThePod/memory/dreams/dream-*/artifacts/ | head -20

# Check if copied to ember_creations
ls -lht /Volumes/ThePod/exports/ember_creations/ | head -10

# Check if Curator detected it
curl -s http://127.0.0.1:7778/api/status \
  -H "Authorization: Bearer curator-status-2024" | jq .
```

---

## Expected Results (GPT-5's Predictions)

### Success Metrics

- ✅ **JSON compliance**: ≥95% (up from ~20%)
- ✅ **Dream creativity**: Roughly unchanged (slightly more pragmatic)
- ✅ **Generation time**: 5-20 seconds on M2/M3
- ✅ **Storage**: +7-8 GB for second model

### What Should Happen

1. **Creative dreams generate valid JSON**
   - Proper string escaping
   - No triple quotes
   - No markdown fences
   - Complete closing braces

2. **Code is executable**
   - Proper Python syntax
   - Safe (no network, no file I/O)
   - Self-contained (stdlib only)

3. **Curator can analyze**
   - Artifacts appear in `ember_creations/`
   - Curator classifies as "code"
   - Proposes seeds based on concepts

4. **Knowledge graph grows**
   - Creative experiments linked to seeds
   - Provenance tracked
   - Connections discovered

---

## Fallback Plan

If DeepSeek-Coder doesn't improve results:

1. **Try CodeLlama**:
   ```bash
   # In .env
   OLLAMA_CREATIVE_MODEL=codellama:7b-instruct
   ```

2. **Try Qwen2.5-Coder**:
   ```bash
   OLLAMA_CREATIVE_MODEL=qwen2.5-coder:7b-instruct
   ```

3. **Disable model switching** (use llama3 for all):
   ```bash
   OLLAMA_CREATIVE_MODEL=
   ```

4. **Two-pass generation** (future enhancement):
   - First pass: Generate plain Python code
   - Second pass: Wrap in JSON with strict model

---

## Technical Details

### Model Switching Logic

```python
# In dream_executor.py
if creative_model:
    def creative_generate(prompt, system):
        # Temporarily override model
        original = cfg['llm_model']
        cfg['llm_model'] = creative_model
        try:
            return generate_response(cfg, prompt, system)
        finally:
            cfg['llm_model'] = original
    
    artifact_gen = DreamArtifactGenerator(
        llm_generate_fn=default_generate,
        creative_model_fn=creative_generate
    )
```

### Prompt Engineering

Key improvements from GPT-5:
- **Regex hint**: Models trained on regex respond well
- **Two examples**: Shows pattern more clearly than one
- **Explicit escaping**: "\\n for newlines, \\t for tabs"
- **No triple quotes**: Prevents common failure mode
- **Strict system prompt**: "Output ONLY valid JSON"

---

## Monitoring

### Check Model Usage

```bash
# Watch Ember's logs
tail -f /tmp/ember_*.log | grep "Creative dreams"

# Check which model is active
curl -s http://localhost:11434/api/tags | jq '.models[].name'
```

### Check Success Rate

```bash
# Count successful creative artifacts
find /Volumes/ThePod/memory/dreams -name "creative_experiment.json" | wc -l

# Count failures (raw responses)
find /Volumes/ThePod/memory/dreams -name "raw_creative_response.txt" | wc -l
```

### Calculate Success Rate

```bash
# Success rate = successful / (successful + failed)
# Target: ≥95%
```

---

## Summary

✅ **Code Complete**: All GPT-5 recommendations implemented  
⏳ **Awaiting**: Model download (`ollama pull deepseek-coder:6.7b-instruct`)  
🎯 **Goal**: 95%+ JSON compliance for creative dreams  
📊 **Benefit**: Curator can analyze code artifacts and propose seeds  

**Next action**: Download the model and test!

---

**Credits**: GPT-5 for architectural guidance, Cursor for implementation
