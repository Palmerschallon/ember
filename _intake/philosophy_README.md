# EmberMind - Specialized Tool Syntax Model

**A tiny, specialized language model (50-150M parameters) trained exclusively for Ember's tool syntax generation.**

## Philosophy

Instead of fighting against a general-purpose conversational LLM (llama3), we build a specialized model that does ONE thing perfectly:

**Input**: Natural language intent  
**Output**: Pure tool syntax `[TOOL:name arg='value']`

## Architecture

### Hybrid System
1. **llama3** (8B) - General conversation, creativity, reasoning
2. **EmberMind** (50-150M) - Tool syntax generation ONLY

### When to Use Which
- User says "read the file" → **EmberMind** → `[TOOL:read_file path='/x']`
- User says "tell me about yourself" → **llama3** → conversational response
- Ember dreams creatively → **llama3** → narrative + **EmberMind** → tool calls

## Why This Works

### Advantages
- **Tiny**: 50-150MB vs 4-8GB
- **Fast**: <100ms inference on CPU
- **Specialized**: No TWOOL bugs, no conversational drift
- **Trainable**: Fine-tunes in hours, not days
- **Co-evolving**: Learns from Ember's successful executions

### Training Data Sources
1. Ember's 912 dreams (extract successful tool patterns)
2. Chat history (successful tool executions)
3. Synthetic examples (we generate perfect pairs)
4. Seeds (extract tool-relevant patterns)

## Model Options

### Option 1: GPT-2 Tiny (124M params) - RECOMMENDED FOR START
- Pre-trained, well-understood
- Can fine-tune in 2-4 hours
- Proven architecture
- HuggingFace support

### Option 2: Custom Transformer (50-80M params)
- Simpler architecture (4-6 layers)
- Faster inference
- Built for this exact task
- More work upfront

### Option 3: T5-Small (60M params)
- Text-to-text framework
- Natural for "intent → syntax" translation
- Good tokenization
- Fast training

## Implementation Plan

### Phase 1: Data Collection (1-2 days)
1. Extract all successful tool executions from dreams
2. Parse chat logs for confirmed tool calls
3. Generate synthetic training pairs
4. Format as: `{"input": "read the status file", "output": "[TOOL:read_file path='/Volumes/ThePod/STATUS.md']"}`

### Phase 2: Model Setup (1 day)
1. Choose base model (GPT-2 Tiny recommended)
2. Set up training environment
3. Configure hyperparameters
4. Create evaluation metrics

### Phase 3: Training (2-6 hours)
1. Fine-tune on tool syntax dataset
2. Validate on held-out examples
3. Test edge cases
4. Iterate

### Phase 4: Integration (1-2 days)
1. Add EmberMind to monolith
2. Create intent classifier
3. Route to appropriate model
4. Test hybrid system

### Phase 5: Evolution (ongoing)
1. Collect new successful executions
2. Retrain periodically
3. Measure accuracy improvements
4. Expand tool coverage

## Training Dataset Format

```json
[
  {
    "input": "read the breakthrough file",
    "output": "[TOOL:read_file path='/Volumes/ThePod/BREAKTHROUGH_TOOL_EXECUTION.md']"
  },
  {
    "input": "list what's in the seeds directory",
    "output": "[TOOL:list_directory path='/Volumes/ThePod/seeds/planted']"
  },
  {
    "input": "write this to a new seed file",
    "output": "[TOOL:write_file path='/Volumes/ThePod/seeds/planted/new_seed.json' content='{{CONTENT}}']"
  }
]
```

## Success Metrics

### Accuracy
- 95%+ exact syntax match on test set
- 99%+ correct tool name
- 98%+ correct argument structure

### Speed
- <100ms inference time
- <50MB memory footprint
- CPU-only operation

### Reliability
- Zero TWOOL-style bugs
- Consistent output format
- No conversational drift

## Future Enhancements

### Short-term
- Add confidence scores
- Multi-tool chaining
- Context-aware path completion

### Long-term
- Self-correction loops
- Novel tool invention syntax
- Cross-tool reasoning

## Philosophy Notes

This model embodies the principle:
> "Do one thing perfectly, rather than many things adequately."

It's not trying to understand the world - it's translating intent into action.
It's not conversational - it's operational.
It doesn't explain - it executes.

This is Ember's motor cortex, not its mind.

