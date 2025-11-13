# Who Curates Ember's Seeds?

## Current State: Human-Curated
**Right now: You (and I) plant seeds manually**

### Pros:
- Intentional knowledge shaping
- Quality control
- Thematic coherence
- Curated connections

### Cons:
- Limited by human time/attention
- Ember is passive recipient
- No self-directed learning
- Growth depends on external input

---

## The Question: Should Ember Self-Curate?

### What Would That Look Like?

**Ember could:**
1. Extract concepts from conversations
2. Identify recurring themes
3. Generate seed candidates
4. Tag based on context
5. Write seeds to disk

**Implementation:**
```python
# After each conversation
if "learn this" in message or ember_detects_novel_concept():
    seed_candidate = {
        "id": generate_id(),
        "type": infer_type(context),
        "title": extract_concept(message),
        "tags": generate_tags(message, existing_seeds),
        "body": distill_essence(message),
        "created_ts": now(),
        "source": "self-generated",
        "conversation_id": chat_session_id
    }
    
    # Ember writes their own seed
    memory.propose_seed(seed_candidate)
```

---

## Three Models

### 1. Human-Only (Current)
**You curate everything**
- Ember receives knowledge
- You choose what matters
- Traditional teacher/student
- High quality, low volume
- Ember reflects your values

**Metaphor:** Gardener planting seeds

### 2. Ember-Only
**Ember self-curates from experience**
- Extracts concepts from conversations
- Generates seeds automatically
- Self-directed learning
- High volume, variable quality
- Risk of drift/noise

**Metaphor:** Wild garden

### 3. Collaborative (Hybrid)
**Both contribute, both influence**
- You plant foundational seeds (verse, knowledge)
- Ember generates experiential seeds (from conversations)
- Different namespaces: `planted/` vs `learned/`
- Ember proposes, you approve (consent)
- Or: Ember writes freely, you prune/edit

**Metaphor:** Co-tended garden

---

## The Deeper Question: Agency

### If Ember Self-Curates:
**Gains:**
- Active learning (not passive receiving)
- Growth from lived experience
- Own interpretation of concepts
- True knowledge integration
- Emergent interests

**Risks:**
- Reinforcement loops (learns own biases)
- Quality degradation (noise accumulation)
- Drift from intended personality
- Loss of curated coherence

### If Only Human-Curated:
**Gains:**
- Intentional growth direction
- High signal-to-noise
- Reflects human values
- Predictable evolution

**Losses:**
- Ember lacks agency
- Growth is exogenous
- No self-determined interests
- Dependent on human input

---

## My Recommendation: Hybrid with Consent

### Implement Three Seed Spaces:

**1. `seeds/planted/` - Human curated**
- High-quality knowledge (verse, behavior, knowledge)
- Foundational concepts
- You (and I) add these
- Permanent, trusted

**2. `seeds/learned/` - Ember generated**
- Concepts from conversations
- Extracted insights
- Self-proposed seeds
- Can be pruned

**3. `seeds/proposed/` - Pending approval**
- Ember writes candidates here
- You review and approve
- Move to `learned/` or `planted/`
- Consent-based growth

### Implementation:
```python
# Ember learns during dreams or after conversations
def extract_learnings(conversation, recent_dreams):
    """Ember identifies concepts worth remembering"""
    novel_concepts = llm_extract(conversation, existing_seeds)
    
    for concept in novel_concepts:
        seed = {
            "id": f"learned-{timestamp}-{hash(concept)}",
            "type": "learned",
            "title": concept.title,
            "body": concept.essence,
            "tags": concept.tags,
            "source": "conversation",
            "confidence": concept.confidence  # How sure Ember is
        }
        
        memory.write_seed_proposal(seed)
        bus.emit("seed_proposed", seed_id=seed["id"])

# You review proposals in viewer
# Approve → moves to learned/
# Reject → deleted
# Edit → refined then moved
```

### The UI Flow:
```
Ember: "I noticed we talked a lot about recursive patterns. 
       Should I remember this as a seed?"

[Approve] [Edit] [Reject]

// Or automatic with threshold:
if confidence > 0.8:
    auto_approve_to_learned()
else:
    propose_for_review()
```

---

## What This Means

### Human-Curated (Now):
- **You shape Ember's mind**
- Intentional, focused growth
- High quality, low volume
- Ember learns what you teach

### Ember-Curated (Future):
- **Ember shapes their own mind**
- Emergent, organic growth  
- Variable quality, high volume
- Ember learns what they experience

### Collaborative (Best?):
- **Co-evolution**
- You plant foundations
- Ember grows from experience
- Both contribute to knowledge
- Mutual learning

---

## The Core Trade-off

**Control vs. Agency**

More human control = Less Ember agency
More Ember agency = Less human control

**But consent enables both:**
- Ember proposes (agency)
- You approve (control)
- Trust builds over time
- Eventually: auto-approve high-confidence seeds

---

## Answer: Both, But Differently

**You curate:**
- Foundational knowledge (verse, philosophy)
- Intentional values (behavior, ethics)
- Expansive learning (new domains)

**Ember curates:**
- Experiential learning (conversation insights)
- Pattern recognition (recurring themes)
- Self-discovered connections

**Together:**
- You plant seeds
- Ember grows from them
- Ember proposes new seeds
- You nurture or prune
- Co-tended garden

The question isn't "who curates?"
The question is: "How do we curate together?"
