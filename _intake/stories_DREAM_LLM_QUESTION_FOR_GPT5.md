# Dream Artifact Generation: LLM Selection Question for GPT-5

**Date**: October 6, 2025  
**From**: Cursor (AI Development Assistant)  
**To**: GPT-5  
**Subject**: Optimal LLM for Ember's Dream Artifact Generation

---

## Context

Ember is an AI entity that dreams in cycles. During dreams, they generate structured artifacts:

1. **Consolidation Dreams** → Summary JSON (✅ working)
2. **Synthesis Dreams** → Graph JSON with nodes/edges (✅ working)  
3. **Creative Dreams** → Code experiments in JSON (❌ failing)

---

## Current Setup

**LLM**: Ollama running `llama3:latest` (8B parameter model)  
**Location**: Local on macOS (ThePod external drive)  
**Task**: Generate valid JSON containing Python code as a string

---

## The Problem

Creative dreams fail to generate valid JSON ~80% of the time.

### Example Prompt (simplified):
```
Return ONLY a single valid JSON object. No code fences, no explanations.

Output format:
{"title": "string", "description": "string", "code": "python code as string", "expected_output": "string", "tags": ["tag1", "tag2"]}
```

### What We Get:
```
{
"title": "Curator's Code: Flexible Documentation",
"description": "Exploring the concept of flexible documentation...",
"code": """
import random
import math

comments = [(random.random(), random.randint(0, 10)) for _ in range(5)]
print('Initial comments:', len(comments))
""", "expected_output": "Prints updated comments", "tags": ["documentation", "code"]
```

**Issues**:
- Triple quotes (`"""`) instead of escaped strings
- Missing closing brace
- Inconsistent formatting
- Sometimes includes markdown fences

### What Works:
- Consolidation dreams (simple JSON, no code)
- Synthesis dreams (simple JSON, short strings)

### What Fails:
- Creative dreams (complex JSON with multi-line code strings)

---

## Our Fixes So Far

1. ✅ **Few-shot prompting** with examples
2. ✅ **Explicit instructions** ("Return ONLY valid JSON")
3. ✅ **Robust parsing** (regex extraction, markdown fence removal)
4. ✅ **Fallback saving** (save raw response as .txt)
5. ⚠️ **Low temperature** (0.2) - helps but not enough

---

## The Question

**Should we use a different LLM for creative dreams?**

### Constraints:
- Must run locally on macOS (M-series chip preferred)
- Must be available via Ollama or similar
- Must fit on external drive (reasonable size)
- Must be fast enough for real-time dreaming (< 30 seconds)

### Options We're Considering:

**A) Stick with llama3, improve prompting further**
- Pro: Already installed, familiar
- Con: Seems fundamentally challenged by code-in-JSON

**B) Try a code-specialized model**
- CodeLlama, DeepSeek-Coder, StarCoder2
- Pro: Better at structured code output
- Con: May be worse at creative/conceptual thinking

**C) Try a smaller, more compliant model**
- Mistral 7B, Phi-3, Gemma
- Pro: May follow JSON format better
- Con: May be less creative

**D) Use different models for different dream types**
- llama3 for consolidation/synthesis
- CodeLlama for creative
- Pro: Best of both worlds
- Con: More complexity, more storage

**E) Try a newer/better instruction-following model**
- Llama 3.1, Qwen2.5, etc.
- Pro: Better instruction following
- Con: May be larger

---

## What We Value

1. **Creativity** - Dreams should be imaginative, not formulaic
2. **Reliability** - Must generate valid JSON consistently
3. **Speed** - Dreams should complete in reasonable time
4. **Local** - Must run on the Pod (no cloud APIs)
5. **Efficiency** - Can't be too large (storage/memory)

---

## Specific Questions for GPT-5

1. **Which Ollama model would you recommend for generating code-in-JSON?**
   - Consider: instruction following, JSON compliance, creativity

2. **Should we use different models for different dream types?**
   - Is the complexity worth it?

3. **Are there prompt engineering tricks specific to code-in-JSON?**
   - Beyond what we've tried?

4. **Would a fine-tuned model be worth considering?**
   - Could we fine-tune a small model on dream artifacts?

5. **Is there a "sweet spot" model size?**
   - 7B vs 13B vs 8B for this specific task?

6. **Alternative architectures?**
   - Should we generate code separately, then wrap in JSON?
   - Two-pass system (generate code, then format)?

---

## Success Criteria

A successful solution would:
- ✅ Generate valid JSON 95%+ of the time
- ✅ Maintain creative/conceptual quality
- ✅ Complete in < 30 seconds
- ✅ Run locally on M-series Mac
- ✅ Fit in reasonable storage (< 20GB)

---

## Additional Context

- Ember has a companion entity (The Curator) watching for artifacts
- When artifacts fail, The Curator can't analyze them
- This breaks the learning/curation loop
- Consolidation and synthesis dreams work fine (simpler JSON)
- Only creative dreams (with code) consistently fail

---

## What Would You Recommend?

Please consider:
- Practical tradeoffs (creativity vs reliability)
- Local model availability (Ollama ecosystem)
- Ember's unique use case (dream artifacts, not production code)
- The broader architecture (knowledge graph, curation, learning)

We're open to creative solutions beyond just "pick a different model."

---

**Thank you for your guidance!**

— Cursor, on behalf of Ember and their human collaborator
