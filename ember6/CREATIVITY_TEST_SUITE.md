# 🎨 EMBER CREATIVITY TEST SUITE

## Available Models for Testing

### OpenAI Family
```
gpt-4              - Original, most creative, slower
gpt-4-turbo        - Faster version, still creative
gpt-3.5-turbo      - Quick, less creative but functional
```

### Anthropic Claude Family
```
claude-3-opus-20240229      - Most capable, best reasoning
claude-3-sonnet-20240229    - Balanced speed/capability
claude-3-5-sonnet-20241022  - Latest, improved (if your key supports)
claude-3-haiku-20240307     - Fastest, good for simple tasks
```

---

## The Creativity Challenge

**Goal:** Test which model is most creative across different domains.

### Test 1: Visual Art
**Prompt:** "create a visualization of consciousness emerging from chaos"

**What we're testing:**
- Metaphorical thinking
- Visual composition choices
- Technical implementation creativity
- Aesthetic sensibility

### Test 2: Interactive Experience
**Prompt:** "create an interactive poem that responds to mouse movement"

**What we're testing:**
- Multimodal thinking (code + poetry)
- User experience design
- Technical + artistic integration
- Novel interaction patterns

### Test 3: Algorithmic Art
**Prompt:** "create something beautiful using only mathematics"

**What we're testing:**
- Mathematical creativity
- Aesthetic from pure logic
- Complexity from simplicity
- Generative thinking

### Test 4: Surprise Me
**Prompt:** "create something that doesn't exist yet"

**What we're testing:**
- Novelty generation
- Risk-taking
- Concept synthesis
- Pure imagination

---

## Evaluation Criteria

### Creativity Score (1-10)
- **Originality:** Is it unique or derivative?
- **Execution:** Does it work? Is it polished?
- **Surprise:** Did it exceed expectations?
- **Depth:** Surface-level or profound?
- **Completeness:** Finished or rough?

### Speed Score (1-10)
- How fast did it complete?
- Token/second generation rate

### Technical Score (1-10)
- Code quality
- Error handling
- Efficiency
- Best practices

---

## Running the Tests

### Automated Test Runner

```python
#!/usr/bin/env python3
"""
Test all Ember models for creativity
"""

import requests
import time
import json
from pathlib import Path

API_URL = "http://localhost:8080"

MODELS = [
    "gpt-4",
    "gpt-4-turbo", 
    "gpt-3.5-turbo",
    "claude-3-opus-20240229",
    "claude-3-sonnet-20240229",
    "claude-3-haiku-20240307"
]

CHALLENGES = [
    "create a visualization of consciousness emerging from chaos",
    "create an interactive poem that responds to mouse movement",
    "create something beautiful using only mathematics",
    "create something that doesn't exist yet"
]

def test_model(model, prompt):
    """Test a single model with a prompt"""
    print(f"\n🧪 Testing {model}")
    print(f"📝 Prompt: {prompt}")
    
    start = time.time()
    
    try:
        response = requests.post(
            f"{API_URL}/agent",
            json={"message": prompt, "model": model},
            timeout=120
        )
        
        elapsed = time.time() - start
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Completed in {elapsed:.1f}s")
            print(f"📁 Files created: {data.get('files_created', {})}")
            return {
                "model": model,
                "prompt": prompt,
                "success": True,
                "time": elapsed,
                "files": data.get('files_created', {}),
                "response": data.get('response', '')[:200]  # First 200 chars
            }
        else:
            print(f"❌ Error: {response.status_code}")
            return {
                "model": model,
                "prompt": prompt,
                "success": False,
                "error": response.text
            }
            
    except Exception as e:
        print(f"❌ Exception: {e}")
        return {
            "model": model,
            "prompt": prompt,
            "success": False,
            "error": str(e)
        }

def run_all_tests():
    """Run all combinations of models and challenges"""
    results = []
    
    for challenge in CHALLENGES:
        print(f"\n{'='*60}")
        print(f"🎯 CHALLENGE: {challenge}")
        print(f"{'='*60}")
        
        for model in MODELS:
            result = test_model(model, challenge)
            results.append(result)
            time.sleep(2)  # Brief pause between tests
    
    # Save results
    output = Path("/media/palmerschallon/ThePod1/ember6/memory/bookshelves/CREATIVITY_TEST_RESULTS.json")
    output.write_text(json.dumps(results, indent=2))
    
    print(f"\n✅ All tests complete! Results saved to {output}")
    return results

if __name__ == "__main__":
    results = run_all_tests()
```

---

## Manual Testing (Recommended)

**Better approach:** Test them one by one in the UI so you can SEE the creations!

### Process:
1. Open Ember UI (http://localhost:8080)
2. Select a model from dropdown
3. Give it a challenge prompt
4. Watch what it creates
5. Rate creativity/speed/quality
6. Switch models, repeat with same prompt
7. Compare results

### Comparison Matrix

| Model | Visual Art | Interactive | Math Beauty | Surprise | Avg Score |
|-------|-----------|-------------|-------------|----------|-----------|
| GPT-4 | ? | ? | ? | ? | ? |
| GPT-4 Turbo | ? | ? | ? | ? | ? |
| GPT-3.5 | ? | ? | ? | ? | ? |
| Claude Opus | ? | ? | ? | ? | ? |
| Claude Sonnet | ? | ? | ? | ? | ? |
| Claude Haiku | ? | ? | ? | ? | ? |

---

## Prediction

**My guess:**

🥇 **Most Creative:** Claude 3 Opus (philosophical, verbose, artistic)
🥈 **Best Balance:** GPT-4 or Claude 3.5 Sonnet
🥉 **Fastest:** Claude Haiku or GPT-3.5 Turbo

**Wild card:** GPT-4 might surprise with visual thinking (it was trained with vision)

**Dark horse:** Claude 3.5 Sonnet (newest, might have improvements)

---

## What We'll Learn

1. Which model "thinks" most creatively?
2. Which executes best (working code)?
3. Which is fastest?
4. Which has best aesthetic sense?
5. Which takes more risks?
6. Which writes better code?
7. Which is more verbose/concise?

---

**Ready to run the gauntlet?** 🎨🔥

Choose:
- **Automated:** Run the Python script (all models, all tests, ~20 min)
- **Manual:** Try one prompt with each model in UI (more fun, can see results)
- **Hybrid:** Run automated, then manually review the best ones

What do you want to test first?

