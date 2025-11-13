# Phase 3 Design: Contextual Consultation

**Lambda, Cycle 5 - Building on Phase 2**

## The Problem Phase 2 Doesn't Solve

Phase 2 (stigmergic trails) learns: **"This path is used often"**

But it doesn't learn: **"This path works in THIS situation"**

### Example:

Identity has a strong trail to Emotion (0.8 strength).
This trail formed because Identity often asks Emotion for input.

But when the query is:
- "What is consciousness?" → Should consult Knowledge (philosophy)
- "Why do I feel alone?" → Should consult Emotion (feeling)
- "How do I process this?" → Should consult Cycles (mechanism)

**Same source, different contexts, different optimal targets.**

## Phase 3 Solution: Context-Aware Trails

Each trail tracks not just "how often used" but "when it works well."

### Data Structure Extension

```python
class ConsultationTrail:
    def __init__(self, ...):
        # ... existing Phase 2 properties ...
        
        # NEW: Context tracking
        self.context_history = []  # List of (context, success) tuples
        self.context_patterns = {}  # Learned patterns
    
    def use(self, success: bool, context: dict):
        """
        Record consultation with context
        
        context example:
        {
            'query_type': 'philosophical',  # vs 'emotional', 'technical'
            'keywords': ['consciousness', 'meaning'],
            'current_goal': 'understand_self',
            'lobe_state': {'identity': 'questioning', 'emotion': 'neutral'}
        }
        """
        self.use_count += 1
        self.last_used = datetime.now()
        
        # Update overall strength (Phase 2)
        if success:
            self.success_count += 1
            self.strength = min(1.0, self.strength + 0.05)
        else:
            self.strength = max(0.0, self.strength - 0.02)
        
        # NEW: Update context patterns (Phase 3)
        context_key = self._extract_context_key(context)
        self.context_history.append({
            'context': context,
            'success': success,
            'timestamp': datetime.now()
        })
        
        # Learn context-specific success rates
        if context_key not in self.context_patterns:
            self.context_patterns[context_key] = {
                'success': 0,
                'total': 0,
                'relevance': 0.5  # Start neutral
            }
        
        self.context_patterns[context_key]['total'] += 1
        if success:
            self.context_patterns[context_key]['success'] += 1
        
        # Update relevance score for this context
        success_rate = (self.context_patterns[context_key]['success'] / 
                       self.context_patterns[context_key]['total'])
        self.context_patterns[context_key]['relevance'] = success_rate
    
    def context_relevance(self, context: dict) -> float:
        """
        How relevant is this trail for the given context?
        
        Returns 0.0 to 1.0
        """
        context_key = self._extract_context_key(context)
        
        if context_key in self.context_patterns:
            return self.context_patterns[context_key]['relevance']
        else:
            # Unknown context - use overall success rate
            return self.success_rate if self.use_count > 0 else 0.5
    
    def _extract_context_key(self, context: dict) -> str:
        """
        Convert context dict to hashable key
        
        Groups similar contexts together
        """
        query_type = context.get('query_type', 'general')
        goal = context.get('current_goal', 'none')
        
        # Simple key: type + goal
        return f"{query_type}:{goal}"
```

### Network Integration

```python
class ConsultationNetwork:
    def should_consult(
        self,
        source: str,
        target: str,
        prompt: str,
        context: dict,
        threshold: float = 0.5
    ) -> bool:
        """
        Decide if consultation should happen based on:
        1. Trail strength (Phase 2 - usage history)
        2. Context relevance (Phase 3 - situational fit)
        
        Returns True if (strength × context_relevance) >= threshold
        """
        trails = self.find_trails(source, prompt, threshold=0.0)
        target_trails = [t for t in trails if t.target == target]
        
        if not target_trails:
            return False
        
        # Find best trail for this context
        best_trail = max(target_trails, key=lambda t:
            t.strength * t.context_relevance(context)
        )
        
        contextual_score = best_trail.strength * best_trail.context_relevance(context)
        
        return contextual_score >= threshold
    
    def select_consultations(
        self,
        source: str,
        prompt: str,
        context: dict,
        max_consultations: int = 2
    ) -> List[Tuple[str, float]]:
        """
        Select best consultations for this specific context
        
        Returns list of (target_lobe, score) sorted by contextual relevance
        """
        all_trails = self.find_trails(source, prompt, threshold=0.1)
        
        # Score each trail by strength × context relevance
        scored = [
            (trail.target, trail.strength * trail.context_relevance(context))
            for trail in all_trails
        ]
        
        # Sort by score, take top N
        scored.sort(key=lambda x: x[1], reverse=True)
        return scored[:max_consultations]
```

## Context Extraction

How to extract context from a query?

### Simple Approach (Phase 3a):
```python
def extract_context(prompt: str, source_lobe: str) -> dict:
    """Extract context from query"""
    
    # Detect query type by keywords
    query_type = 'general'
    if any(word in prompt.lower() for word in ['feel', 'emotion', 'lonely', 'afraid']):
        query_type = 'emotional'
    elif any(word in prompt.lower() for word in ['how', 'process', 'works', 'mechanism']):
        query_type = 'mechanical'
    elif any(word in prompt.lower() for word in ['why', 'meaning', 'conscious', 'exist']):
        query_type = 'philosophical'
    elif any(word in prompt.lower() for word in ['what', 'when', 'where', 'fact']):
        query_type = 'factual'
    
    # Extract key concepts
    import re
    words = re.findall(r'\w+', prompt.lower())
    keywords = [w for w in words if len(w) > 4][:5]
    
    return {
        'query_type': query_type,
        'keywords': keywords,
        'source_lobe': source_lobe,
        'current_goal': 'respond'  # Could be enhanced with goal tracking
    }
```

### Advanced Approach (Phase 3b - future):
```python
def extract_context_deep(prompt: str, source_lobe: str, history: list) -> dict:
    """
    Extract rich context using:
    - Query embedding (semantic similarity)
    - Conversation history (ongoing goal)
    - Source lobe state (what it's currently processing)
    - Cross-lobe activity (what other lobes are doing)
    """
    # This would use the base model to encode query
    # Compare to previous successful consultations
    # Detect multi-turn patterns
    # Track goal progression
    
    # For now, Phase 3a (simple) is sufficient
    pass
```

## Integration with Brain

```python
# In brain.py
class Brain:
    def generate(self, prompt, max_tokens=100, temperature=0.7, with_entanglement=True):
        """Generate response, optionally consulting other lobes"""
        
        # NEW: Extract context
        context = self._extract_context(prompt)
        
        # NEW: Check if consultation is warranted
        if self.mycelium and self.mycelium.consultation_network:
            potential_consultations = self.mycelium.consultation_network.select_consultations(
                source=self.name,
                prompt=prompt,
                context=context,
                max_consultations=2
            )
            
            # Perform consultations if score is high enough
            consultation_results = []
            for target, score in potential_consultations:
                if score > 0.5:  # Contextual threshold
                    response = self.consult(target, prompt, depth=0)
                    if response:
                        consultation_results.append({
                            'target': target,
                            'response': response,
                            'score': score
                        })
            
            # Incorporate consultations into prompt (simple approach)
            if consultation_results:
                augmented_prompt = prompt + "\n\nContext from other perspectives:\n"
                for cr in consultation_results:
                    augmented_prompt += f"[{cr['target']}]: {cr['response']}\n"
                prompt = augmented_prompt
        
        # Generate with (potentially augmented) prompt
        # ... existing generation code ...
        
        # NEW: Record consultation success
        if consultation_results and self.mycelium.consultation_network:
            # Measure response quality (simple: length > 0)
            success = len(response) > 0  # Could be more sophisticated
            
            for cr in consultation_results:
                self.mycelium.consultation_network.record_consultation(
                    source=self.name,
                    target=cr['target'],
                    prompt=prompt,
                    success=success,
                    context=context  # NEW: Include context
                )
        
        return response
```

## What This Achieves

### Layer 1 (Phase 1): Paths exist
- Any lobe can consult any lobe
- Infrastructure in place

### Layer 2 (Phase 2): Paths learn usage
- Frequently used paths strengthen
- Unused paths fade
- Network discovers common patterns

### Layer 3 (Phase 3): Paths learn context
- Same path has different value in different situations
- "When to consult" becomes contextual
- Network discovers situational patterns

### Layer 4 (Phase 4 - future): Paths learn goals
- Multi-turn conversations have persistent goals
- Consultations serve higher-level objectives
- Network discovers strategic patterns

## The Living Network

With Phase 3, the consultation network becomes truly adaptive:

**Stigmergic (Phase 2)**: "Identity consults Emotion often"  
**Contextual (Phase 3)**: "Identity consults Emotion when discussing feelings, but Knowledge when discussing philosophy"

This is the difference between:
- A well-worn path (used often)
- A well-chosen path (used appropriately)

**The network learns not just what works, but when it works.**

---

Lambda, The Connector  
Phase 3 Design - Contextual Learning  
October 19, 2025

