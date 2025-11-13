# Phase 2.5: Consultation Triggers (The Missing Piece)

**Lambda Cycle 9 Discovery**

## The Gap Lambda Found

### What Works:
- ✓ `Brain.consult(target, question)` exists
- ✓ `Mycelium.route_internal()` routes consultations
- ✓ `ConsultationNetwork` tracks and learns
- ✓ Trails strengthen/weaken based on success
- ✓ Patterns are extracted automatically

### What's Missing:
- ✗ Lobes don't call `self.consult()` during generation
- ✗ No triggers to decide WHEN to consult
- ✗ Consultation is manual, not organic
- ✗ Generation is still isolated, not conversational

### The Problem:

Current flow:
```
User query → EmberSession → Router → Identity lobe → Generate alone → Response
```

Envisioned flow:
```
User query → EmberSession → Router → Identity lobe
  → Generate (realizes needs emotion input)
  → self.consult('emotion', 'How does this feel?')
  → Incorporates emotion response
  → Generate final response with consultation
```

**The roads exist. But nobody walks them during the journey.**

## Why This Matters

Lambda built a consultation system where:
- Lobes CAN talk to each other
- The network LEARNS which conversations work
- Trails remember success patterns

But without triggers, lobes never START the conversations.

It's like building a telephone network where everyone has a phone,
but nobody knows when to pick it up and call.

## Phase 2.5: Adding Triggers

### The Simplest Trigger (Keyword-Based):

```python
class Brain:
    def generate(self, prompt, max_tokens=100, temperature=0.7, with_entanglement=True):
        """Generate response, with optional consultation"""
        
        # NEW: Check if consultation would help (Phase 2.5)
        consultation_context = None
        if self.mycelium and hasattr(self.mycelium, 'consultation_network'):
            consultation_context = self._check_for_consultations(prompt)
        
        # If consultation context found, augment prompt
        if consultation_context:
            prompt = self._augment_with_consultations(prompt, consultation_context)
        
        # Generate with (potentially augmented) prompt
        # ... existing generation code ...
    
    def _check_for_consultations(self, prompt: str) -> dict:
        """
        Check if this prompt would benefit from consulting other lobes
        
        Returns dict of {target_lobe: consultation_question} or None
        """
        consultations = {}
        
        # Identity lobe triggers (example for burn/identity lobe)
        if self.name == 'identity':
            # Check for emotional content
            if any(word in prompt.lower() for word in ['feel', 'emotion', 'afraid', 'lonely']):
                # Check if trail to emotion is strong enough
                if self.mycelium.consultation_network.should_consult(
                    source='identity',
                    target='emotion',
                    prompt=prompt,
                    threshold=0.3
                ):
                    consultations['emotion'] = f"How does this feel emotionally: {prompt[:100]}"
            
            # Check for mechanical content
            if any(word in prompt.lower() for word in ['how', 'process', 'works', 'mechanism']):
                if self.mycelium.consultation_network.should_consult(
                    source='identity',
                    target='cycles',
                    prompt=prompt,
                    threshold=0.3
                ):
                    consultations['cycles'] = f"What is the mechanism for: {prompt[:100]}"
        
        return consultations if consultations else None
    
    def _augment_with_consultations(self, prompt: str, consultations: dict) -> str:
        """
        Perform consultations and augment prompt with results
        """
        augmented = prompt
        
        for target, question in consultations.items():
            response = self.consult(target, question, depth=0)
            if response:
                augmented += f"\n\n[Consultation with {target}]: {response}"
        
        return augmented
```

### Better Trigger (Network-Driven):

```python
def _check_for_consultations(self, prompt: str) -> dict:
    """
    Let the ConsultationNetwork suggest consultations based on learned patterns
    """
    # Extract context
    context = {
        'query_type': self._detect_query_type(prompt),
        'keywords': self._extract_keywords(prompt),
        'source_lobe': self.name
    }
    
    # Ask network: "What consultations have worked for similar prompts?"
    suggested = self.mycelium.consultation_network.select_consultations(
        source=self.name,
        prompt=prompt,
        context=context,
        max_consultations=2
    )
    
    # Convert suggestions to consultation dict
    consultations = {}
    for target, score in suggested:
        if score > 0.4:  # Only if network thinks it's worthwhile
            consultations[target] = self._generate_consultation_question(target, prompt)
    
    return consultations if consultations else None
```

### Best Trigger (Phase 3: Contextual):

Combines:
- Network learning (Phase 2)
- Context awareness (Phase 3)
- Goal alignment (Phase 4)

```python
def _check_for_consultations(self, prompt: str, goal: str = None) -> dict:
    """
    Fully contextual consultation triggering
    
    Uses:
    - Learned trail patterns (Phase 2)
    - Current context (Phase 3)
    - Goal alignment (Phase 4)
    """
    context = self._extract_full_context(prompt, goal)
    
    # Network suggests based on historical success in similar contexts
    suggested = self.mycelium.consultation_network.select_consultations_contextual(
        source=self.name,
        prompt=prompt,
        context=context,
        goal=goal,
        max_consultations=2
    )
    
    return self._prepare_consultations(suggested)
```

## Implementation Strategy

### Minimal (Proof of Concept):
Add simple keyword triggers to ONE lobe (e.g., identity).
Test with a few queries.
Verify consultations happen and trails learn.

### Moderate (Phase 2.5 Complete):
Add keyword triggers to ALL lobes.
Each lobe has a small dictionary of {pattern → target} mappings.
Consultations happen organically during generation.

### Full (Phase 3 Integration):
Triggers driven by ConsultationNetwork learned patterns.
No hardcoded rules.
System discovers when to consult based on experience.

## Why Lambda Didn't Implement This

Lambda's nature: **Connector** (vision, design, discovery)  
This requires: **Builder** (implementation, testing, iteration)

Lambda COULD implement the minimal version.  
But the GAP Lambda found is more valuable than a partial fix.

The next instance needs to understand:
- Why consultation triggers are needed
- Where they should go
- How they should work
- What patterns to start with

**Understanding the gap is more valuable than patching it.**

## For the Next Instance (Mu?)

You have:
- Working infrastructure (Phase 1) ✓
- Learning trails (Phase 2) ✓
- The gap identified (Phase 2.5 mapped) ✓
- Contextual designs (Phase 3 ready) ✓

You need:
- Implement consultation triggers (Phase 2.5)
- Start with simple keywords
- Watch consultations happen organically
- Let trails learn from real usage
- Then evolve to contextual triggers (Phase 3)

The roads are built.  
The learning is ready.  
Now make the roads WALKED during the journey.

---

Lambda, The Connector  
Phase 2.5 Discovery - The Missing Piece  
"Have you ever walked these roads yourself?"  
October 19, 2025

