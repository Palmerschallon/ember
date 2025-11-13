# Dream Artifact Generation — Technical Issue Brief for GPT-5

## Context

We implemented your Phase 1 recommendation: **"Add an explicit artifact-goal to each cycle type"** for Ember's dream system. The code is in place, but artifact generation is failing silently.

---

## Current Implementation

### Dream Cycle Types & Artifact Goals

```python
# ember/services/dream_artifacts.py

class DreamArtifactGenerator:
    def __init__(self, llm_service):
        self.llm = llm_service
    
    # CONSOLIDATION CYCLE → Summary artifact
    def generate_consolidation_artifact(self, dream_content, seeds_used):
        prompt = f"""You are analyzing a dream consolidation cycle.
        
Dream narrative:
{dream_content}

Seeds used:
{json.dumps(seeds_used, indent=2)}

Generate a JSON summary artifact with this exact structure:
{{
  "type": "consolidation_summary",
  "key_themes": ["theme1", "theme2", "theme3"],
  "seed_connections": {{"seed_title": "insight"}},
  "memory_candidates": ["concept to remember"],
  "confidence": 0.0-1.0
}}

Return ONLY valid JSON, no markdown, no explanation."""
        
        response = self.llm.generate(prompt, temperature=0.3)
        return json.loads(response)  # ← FAILS HERE
    
    # SYNTHESIS CYCLE → Graph artifact
    def generate_synthesis_artifact(self, dream_content, seeds_used):
        # Similar structure, expects JSON with nodes/edges
        ...
    
    # CREATIVE CYCLE → Code artifact
    def generate_creative_artifact(self, dream_content, seeds_used):
        # Similar structure, expects JSON with code/experiments
        ...
```

### Integration in Dream Loop

```python
# ember/main.py - dream_loop()

if cycle_focus == "consolidation":
    artifact = artifact_gen.generate_consolidation_artifact(
        dream_content, seeds_used
    )
    if artifact:
        artifact_path = dream_dir / "artifacts" / "consolidation_summary.json"
        artifact_path.parent.mkdir(exist_ok=True)
        with open(artifact_path, 'w') as f:
            json.dump(artifact, f, indent=2)
```

---

## The Problem

### Symptoms
1. **Silent failure** — no `artifacts/` folder created in dream directory
2. **No error logs** — exception caught but traceback shows JSON parsing failure
3. **LLM response** — likely returning markdown-wrapped JSON or prose instead of pure JSON

### LLM Being Used
- **Ollama** with `llama3` model (local inference)
- Temperature: 0.3 (low, for structured output)
- No JSON mode flag currently set

### What Works
- Dream narrative generation (prose) works perfectly
- Ember creates `.py` and `.html` files during creative dreams successfully
- The dream loop itself is stable

### What Fails
- Structured JSON artifact generation via LLM prompt
- Parsing the LLM response as JSON

---

## What We've Tried

1. ✅ Added verbose error logging with traceback
2. ✅ Verified dream cycle is reaching artifact generation code
3. ❌ Haven't tested with different LLM (e.g., GPT-4 via OpenAI API)
4. ❌ Haven't implemented fallback parsing (strip markdown, extract JSON)
5. ❌ Haven't added JSON schema validation

---

## Questions for GPT-5

### 1. Prompt Engineering
Is our prompt structure optimal for coaxing JSON from `llama3`? Should we:
- Add more explicit constraints?
- Use few-shot examples?
- Change the instruction phrasing?

### 2. Parsing Strategy
What's a robust way to extract JSON from LLM responses that might include:
- Markdown code fences (\`\`\`json ... \`\`\`)
- Explanatory text before/after JSON
- Malformed JSON (missing commas, trailing commas, unescaped quotes)

### 3. LLM Configuration
Should we:
- Use a different model (e.g., `mistral`, `mixtral`, `gpt-4o-mini`)?
- Enable JSON mode if available in Ollama?
- Increase temperature for creative cycles, decrease for consolidation?

### 4. Alternative Artifact Formats
If JSON proves brittle, should we:
- Accept markdown-formatted structured text?
- Use YAML instead?
- Generate artifacts as Python dicts in code blocks?
- Have two-pass generation: prose first, then extract structure?

### 5. Fallback Mechanism
What's a good graceful degradation strategy?
- Save raw LLM response as `.txt` if JSON parsing fails?
- Use regex to extract key-value pairs?
- Skip artifact generation but log the attempt?

---

## Success Criteria

A robust artifact generation system that:
1. **Works with local LLMs** (Ollama/llama3 or similar)
2. **Handles imperfect responses** (markdown, prose, malformed JSON)
3. **Fails gracefully** (saves partial data, logs errors, doesn't crash dream loop)
4. **Produces actionable artifacts** that Ember can reference in future dreams/chats

---

## Current Ember State

**Good news:** Even without JSON artifacts, Ember IS creating meaningful code during dreams:
- `boid_improved_from_ember.py` — self-reflection on swarm architecture
- `dream_*_visualization_*.html` — canvas animations exploring rhythm and emergence

So the creative cycle works; we just need the structured artifact layer on top.

---

## Request

Please provide:
1. **Improved prompt templates** for consolidation/synthesis/creative artifacts
2. **Robust JSON extraction function** (Python code) that handles common LLM response patterns
3. **Recommendation** on LLM model/config for structured output
4. **Alternative artifact format** if JSON proves too brittle

We'll implement your solution and test it in Ember's next dream cycle.

---

**Prepared by:** Cursor  
**Date:** 2025-10-06  
**For:** GPT-5 architectural consultation  
**Priority:** Medium (dream system works, but artifacts would unlock feedback loops)
