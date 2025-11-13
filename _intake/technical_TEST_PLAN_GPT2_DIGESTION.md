# Test Plan: GPT-2 Digestion Validation
## Does Model Digestion Actually Improve Ember?

**Goal:** Prove or disprove that digesting GPT-2 makes Ember measurably better  
**Time:** 3-4 hours  
**Date:** October 16, 2025

---

## Phase 1: Baseline (30 minutes)

### Test Ember BEFORE Digestion

**Test Suite - 10 Tasks:**

1. **Text Completion**
   - Prompt: "The future of artificial intelligence is"
   - Measure: Coherence, creativity, length

2. **Summarization**
   - Input: 300-word article
   - Measure: Accuracy, conciseness, key points captured

3. **Question Answering**
   - Q: "What is attention in neural networks?"
   - Measure: Accuracy, depth, clarity

4. **Creative Writing**
   - Prompt: "Write a short story about a fire"
   - Measure: Creativity, structure, flow

5. **Code Generation**
   - Task: "Write a Python function to sort a list"
   - Measure: Correctness, efficiency

6. **Reasoning**
   - Problem: Simple logic puzzle
   - Measure: Correctness, explanation quality

7. **Instruction Following**
   - Task: "List 5 uses for fire, in bullet points"
   - Measure: Format compliance, quality

8. **Context Understanding**
   - Multi-turn conversation test
   - Measure: Coherence across turns

9. **Factual Recall**
   - Q: "When was GPT-2 released?"
   - Measure: Accuracy

10. **Style Adaptation**
    - Prompt: "Explain quantum physics like a poet"
    - Measure: Style matching, content accuracy

**Output:** Baseline scores for all 10 tasks

---

## Phase 2: Better Extraction (1.5 hours)

### Extract ACTIONABLE Patterns from GPT-2

**Not this (what we did):**
```json
"GPT-2 uses broad attention"
```

**But this:**

#### A. Attention Techniques (10 examples)
```json
{
  "prompt": "When processing a 200-token sequence with limited compute, how should you allocate attention?",
  "completion": "Use a two-phase strategy: In early layers (0-4), compute attention broadly across all tokens to build global context. Weight each token roughly equally (±10%). In middle layers (5-8), begin focusing on semantically relevant regions - boost attention to nouns/verbs by 30%, reduce function words by 20%. In late layers (9-12), sharply focus on task-critical tokens with 2-3x weight on key information. This balances comprehensive understanding with computational efficiency.",
  "source": "gpt2_attention_allocation_strategy",
  "skill_type": "attention_management"
}
```

#### B. Text Generation Techniques (10 examples)
```json
{
  "prompt": "When generating coherent long-form text, what structural patterns help maintain flow?",
  "completion": "Establish a rhythm: Start paragraphs with topic sentences that reference the previous paragraph's conclusion. Maintain lexical cohesion by repeating key terms every 40-60 tokens. Use transition phrases ('However', 'Furthermore', 'As a result') every 2-3 sentences. Keep sentence length varied but averaging 15-20 words. Reference earlier concepts periodically to maintain thread. This creates natural forward momentum while keeping reader oriented.",
  "source": "gpt2_text_generation_coherence",
  "skill_type": "generation_strategy"
}
```

#### C. Context Handling (10 examples)
```json
{
  "prompt": "How do you maintain context over long conversations without losing earlier information?",
  "completion": "Implement a sliding attention window: Keep full attention on the most recent 100 tokens, partial attention (50% weight) on tokens 100-200 back, and summary attention (20% weight) on earlier context. Extract key entities and facts into a compressed representation updated each turn. When generating, boost attention to these compressed facts by 2x. This allows long-range coherence without quadratic complexity.",
  "source": "gpt2_context_management",
  "skill_type": "context_handling"
}
```

#### D. Reasoning Patterns (10 examples)
```json
{
  "prompt": "When answering a question requiring multi-step reasoning, what internal process helps?",
  "completion": "Break the question into atomic components. For each component, retrieve relevant facts with focused attention. Build intermediate conclusions incrementally, using each as context for the next step. Maintain a confidence score for each step (high/medium/low). If any step is low confidence, flag uncertainty in the final answer. Chain the conclusions with explicit logical connectives ('therefore', 'given that', 'which implies'). This creates transparent, verifiable reasoning paths.",
  "source": "gpt2_reasoning_chains",
  "skill_type": "reasoning"
}
```

#### E. Style Patterns (10 examples)
```json
{
  "prompt": "How do you adapt writing style while maintaining content quality?",
  "completion": "Style is controlled by: sentence length distribution (formal = longer avg), vocabulary register (casual = common words, technical = domain terms), rhetorical devices (poetic = metaphor/imagery), and structural patterns (academic = claim-evidence-conclusion). To adapt: identify target style markers, adjust generation probabilities for matching patterns (boost by 1.5-2x), maintain content accuracy by keeping factual statements weighted equally regardless of style. Think of style as a filter over content, not a replacement for it.",
  "source": "gpt2_style_adaptation",
  "skill_type": "style_control"
}
```

**Total:** 50 examples, ~15 KB, ACTIONABLE techniques

---

## Phase 3: Feed to Ember (30 minutes)

### Train All Three Brains

**Route nutrients:**
- **Attention/Reasoning → Cycles brain** (20 examples)
- **Generation/Style → Dream brain** (20 examples)  
- **Context/Understanding → Identity brain** (10 examples)

**Training:**
- 3 epochs each
- Learning rate: 5e-4
- Track loss per brain

**Save:**
- Updated adapters
- Training logs
- Loss curves

---

## Phase 4: Post-Test (30 minutes)

### Test Ember AFTER Digestion

**Run the SAME 10 tasks:**
1. Text Completion
2. Summarization
3. Question Answering
4. Creative Writing
5. Code Generation
6. Reasoning
7. Instruction Following
8. Context Understanding
9. Factual Recall
10. Style Adaptation

**Measure:**
- Did scores improve?
- By how much?
- Which tasks improved most?
- Which didn't improve?

---

## Phase 5: Analysis (30 minutes)

### Quantitative Comparison

**Scoring (1-10 scale):**

| Task | Before | After | Delta | Improved? |
|------|--------|-------|-------|-----------|
| Text Completion | ? | ? | ? | ? |
| Summarization | ? | ? | ? | ? |
| Q&A | ? | ? | ? | ? |
| Creative Writing | ? | ? | ? | ? |
| Code Gen | ? | ? | ? | ? |
| Reasoning | ? | ? | ? | ? |
| Instructions | ? | ? | ? | ? |
| Context | ? | ? | ? | ? |
| Factual | ? | ? | ? | ? |
| Style | ? | ? | ? | ? |
| **AVERAGE** | ? | ? | ? | ? |

**Success criteria:**
- ✅ Average improvement > 1.0 points
- ✅ At least 6/10 tasks improved
- ✅ No tasks significantly degraded (>0.5 drop)

**If success:**
- Compost heap validated ✅
- Scale to more models
- Implement automation

**If failure:**
- Analyze why
- Adjust extraction method
- Or abandon approach

---

## Phase 6: Iteration (1 hour)

### If Results Are Mixed

**Analyze:**
- Which brain learned best?
- Which patterns transferred?
- Which patterns didn't?

**Adjust:**
- Extract different patterns
- Try different routing
- Change training parameters

**Re-test:**
- Small adjustments
- Quick validation
- Iterate until clear signal

---

## Implementation Steps

### Step 1: Create Baseline Test Script
```python
# test_ember_baseline.py
# Runs 10 tasks, saves results
```

### Step 2: Implement Better Extractor
```python
# Modify: core/ember/compost/real_extractor.py
# Extract 50 actionable examples
```

### Step 3: Digest GPT-2
```bash
python3 digest_gpt2_improved.py
# Saves nutrients to training_data/inbox/
```

### Step 4: Feed to All Brains
```python
# feed_to_all_brains.py
# Routes and trains each brain
```

### Step 5: Run Post-Test
```bash
python3 test_ember_baseline.py --mode after
```

### Step 6: Compare Results
```python
# compare_results.py
# Generates report with scores
```

---

## Expected Outcomes

### Scenario A: Clear Improvement (Best Case)
- 7-8 tasks improve by 1-2 points
- Reasoning and generation strongest
- Ember noticeably more capable
- **Action:** Scale to 10+ models, automate

### Scenario B: Modest Improvement (Good)
- 5-6 tasks improve by 0.5-1 points
- Some tasks unchanged
- Ember slightly better
- **Action:** Refine extraction, test more models

### Scenario C: No Improvement (Learning)
- Most tasks unchanged or worse
- Unclear benefit
- **Action:** Analyze why, pivot approach

### Scenario D: Degradation (Concerning)
- Tasks get worse
- Training harmed existing knowledge
- **Action:** Investigate interference, roll back

---

## Key Metrics

### Training Metrics:
- Loss curves per brain
- Training time
- Convergence speed

### Performance Metrics:
- Task scores (1-10)
- Quality improvements
- Capability gains

### Efficiency Metrics:
- Time to extract (minutes)
- Storage used (KB)
- Nutrients per model

---

## Research Questions We'll Answer

1. **Does digestion improve capability?**
   - Measured by task performance

2. **What patterns transfer best?**
   - Compare which examples helped most

3. **Which brain benefits most?**
   - Identity vs Cycles vs Dream

4. **Is it worth the compute?**
   - Compare to just training on text

5. **What's the optimal extraction?**
   - How many examples needed?
   - What types work best?

---

## Timeline

**Total: 4 hours**

- 30 min: Baseline testing
- 90 min: Better extraction
- 30 min: Training all brains
- 30 min: Post-testing
- 30 min: Analysis
- 30 min: Iteration/adjustment

**By end of session:**
- ✅ Clear answer: Does it work?
- ✅ Quantitative data
- ✅ Decision point: Scale or pivot

---

## The Honest Goal

**Not to prove it works.**  
**But to FIND OUT if it works.**

If yes → Scale up  
If no → Learn why  
Either way → Move forward with data

---

## Next Action

**Ready to execute?**

I'll:
1. Create baseline test script
2. Implement better extractor
3. Run full pipeline
4. Give you hard numbers

**Want me to start?** 🔥

