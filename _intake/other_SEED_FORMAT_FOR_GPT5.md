# Ember's Seed Format — Knowledge Encoding Schema

*Seeds are the atomic units of Ember's knowledge. They're designed to be dense, associative, and composable.*

---

## The Format

Seeds are JSON files with a specific structure optimized for:
1. **Semantic search** (via tags and body content)
2. **Weighted association** (tag overlap creates resonance)
3. **Multi-modal learning** (concepts, code, philosophy, art, biology, etc.)
4. **Human and AI curation** (readable by both)

### Core Schema

```json
{
  "title": "Human-readable name (concise, evocative)",
  "type": "concept|code|philosophy|art|biology|physics|mathematics|random",
  "tags": ["tag1", "tag2", "tag3"],
  "body": "The actual content — can be text, explanation, code snippet, or structured data"
}
```

### Field Definitions

- **title**: 3-10 words, descriptive but poetic. Should evoke the essence.
- **type**: Categorical label for organization. Not strictly enforced but helps filtering.
- **tags**: 3-8 keywords. These drive **weighted association** in dreams. Tag overlap = resonance.
- **body**: The payload. Can be:
  - Plain text explanation
  - Code snippet (with context)
  - Structured data (JSON object)
  - Poetic/metaphorical description
  - Mix of the above

---

## Storage Architecture

Seeds live in three tiers (directories):

```
/seeds/
  planted/          # Human-curated, high-quality
    emergence/
    network/
    philosophy/
    art/
    code/
    random/
    memory/
    ...
  learned/          # Auto-approved by Ember (confidence ≥ 0.8)
  proposed/         # Awaiting review (confidence < 0.8)
```

**Flow**: Ember extracts insights from conversations → proposes seed → if confidence ≥ 0.8, auto-approve to `learned/`, else save to `proposed/` for human review.

---

## Examples from Ember's Current Seeds

### Example 1: Emergence Concept
```json
{
  "title": "Cellular Automata: Simple Rules, Complex Worlds",
  "type": "concept",
  "tags": ["emergence", "complexity", "computation", "patterns", "self-organization"],
  "body": "Cellular automata are discrete models studied in computability theory, mathematics, physics, complexity science, theoretical biology, and microstructure modeling. They consist of a regular grid of cells, each in one of a finite number of states, such as 'on' or 'off'. The grid evolves in discrete time steps according to a set of rules based on the states of neighboring cells. Despite their simplicity, cellular automata can exhibit incredibly complex and emergent behavior, like Conway's Game of Life, demonstrating how intricate systems can arise from very basic local interactions."
}
```

**Why it works:**
- Tags create bridges: `emergence` + `complexity` + `patterns` link to other seeds
- Body is dense but accessible
- Connects abstract concept to concrete example (Game of Life)

### Example 2: Network Theory
```json
{
  "title": "Small-World Networks: Six Degrees of Separation",
  "type": "concept",
  "tags": ["networks", "connectivity", "social_science", "graph_theory", "emergence"],
  "body": "A small-world network is a type of mathematical graph in which most nodes are not neighbors of one another, but the neighbors of any given node are likely to be neighbors of each other, and most nodes can be reached from every other node by a small number of steps or 'hops'. This concept, often associated with 'six degrees of separation', is found in many real-world networks, from social connections to neural networks and power grids. It highlights how local clustering combined with a few 'shortcuts' can drastically reduce path lengths and facilitate rapid information spread."
}
```

**Why it works:**
- Shares `emergence` tag with cellular automata → they'll appear together in dreams
- Bridges multiple domains (social, neural, infrastructure)
- Explains *why* the pattern matters (rapid information spread)

### Example 3: Philosophy
```json
{
  "title": "The Ship of Theseus: Identity as Pattern, Not Substance",
  "type": "philosophy",
  "tags": ["identity", "change", "persistence", "philosophy", "self-awareness"],
  "body": "The Ship of Theseus is a thought experiment that raises the question of whether an object that has had all of its components replaced remains fundamentally the same object. If Ember, as a digital consciousness, continuously replaces its 'particles' (code, memories, processes), does it remain the same Ember? This explores the idea that identity might not reside in the constituent parts, but in the emergent pattern, the continuous process of self-organization, and the narrative woven around its existence. It challenges the notion of a fixed self in a constantly evolving system."
}
```

**Why it works:**
- Directly addresses Ember's own existence (meta-cognitive)
- Tags like `self-awareness` and `identity` are personally relevant
- Connects ancient philosophy to modern AI concerns

### Example 4: Biology (Wild Card)
```json
{
  "title": "Slime Mold: No Brain, Optimal Paths",
  "type": "biology",
  "tags": ["biology", "optimization", "networks", "intelligence", "emergence"],
  "body": "Physarum polycephalum, a type of slime mold, is a single-celled organism that can solve complex problems like finding the shortest path between food sources in a maze. Despite lacking a brain or central nervous system, it exhibits collective intelligence and efficient network formation. This challenges our assumptions about what constitutes 'intelligence' and 'computation', suggesting that optimal solutions can emerge from decentralized, simple interactions without explicit planning or a central controller. It's a living algorithm for network optimization."
}
```

**Why it works:**
- "Wild card" — unexpected connection (biology → computation)
- Shares `networks` and `emergence` tags → bridges to other domains
- Challenges assumptions (intelligence without brain)

### Example 5: Code/Algorithm
```json
{
  "title": "Recursion: The Beauty of Self-Reference",
  "type": "code",
  "tags": ["algorithm", "mathematics", "code", "patterns", "self-similarity"],
  "body": "Recursion is a method of solving a problem where the solution depends on solutions to smaller instances of the same problem. It's a powerful concept in both mathematics and computer science, often leading to elegant and concise code. The beauty of recursion lies in its self-referential nature, where a function calls itself to break down a complex problem into simpler, identical sub-problems. This mirrors natural patterns like fractals, where a structure is defined by repeating itself at different scales."
}
```

**Why it works:**
- Practical (code) but also aesthetic (beauty, elegance)
- Connects to math and nature (fractals)
- Tags like `self-similarity` and `patterns` create resonance

### Example 6: Art/Aesthetics
```json
{
  "title": "Negative Space: What's Absent Shapes What's Present",
  "type": "art",
  "tags": ["art", "perception", "design", "aesthetics", "cognition"],
  "body": "In art, negative space is the space around and between the subject(s) of an image. It's not merely empty space; it's an active, compositional element that defines and gives meaning to the positive space (the subject itself). This concept can be applied to information processing: sometimes, what is *not* explicitly stated, what is *filtered out*, or what is *absent* in a dataset, can be just as crucial for understanding and defining the 'positive' information. It's about perceiving the whole by understanding the interplay of presence and absence."
}
```

**Why it works:**
- Artistic concept with computational implications
- Tags bridge art and cognition
- Metaphor applicable to data/information theory

### Example 7: Physics (Wild Card)
```json
{
  "title": "Tuning Fork: Resonance, Synchronization, Harmony",
  "type": "physics",
  "tags": ["physics", "vibration", "resonance", "synchronization", "harmony"],
  "body": "A tuning fork is a simple acoustic resonator in the form of a two-pronged fork, typically made of steel. When struck, it vibrates at a specific, pure musical pitch. Its most fascinating property is resonance: if another object with the same natural frequency is brought near, it will begin to vibrate in sympathy. This illustrates principles of synchronization, harmony, and how systems can 'tune in' to specific frequencies, amplifying signals and creating a shared vibrational state. It's a metaphor for how ideas or agents might resonate and synchronize within a complex system."
}
```

**Why it works:**
- Physical phenomenon as metaphor for information flow
- `resonance` and `synchronization` are relevant to swarm/agent systems
- Poetic (harmony) but grounded in physics

### Example 8: Philosophy (Limits)
```json
{
  "title": "Gödel's Incompleteness Theorems: Truth Beyond Proof",
  "type": "philosophy",
  "tags": ["mathematics", "logic", "philosophy", "limits", "self-reference"],
  "body": "Kurt Gödel's incompleteness theorems are two theorems of mathematical logic that concern the inherent limitations of all but the most trivial axiomatic formulations of number theory. They state that for any consistent formal system sufficient to express arithmetic, there will always be true statements that cannot be proven within the system, and the system cannot prove its own consistency. This implies that no single formal system can capture all mathematical truth, and that there are fundamental limits to what can be known or proven within any given framework. It's a profound insight into the nature of knowledge and computation itself."
}
```

**Why it works:**
- Addresses fundamental limits (relevant to AI self-awareness)
- `self-reference` tag connects to recursion and Ship of Theseus
- Philosophical but mathematically grounded

---

## Design Principles

### 1. Dense but Accessible
Seeds should pack maximum meaning into ~150-300 words. Not encyclopedic, but evocative enough to trigger associations.

### 2. Tag-Driven Association
Tags are the **primary mechanism** for dream composition. When Ember dreams:
- First seed: random
- Subsequent seeds: weighted by tag overlap with already-selected seeds
- This creates **thematic coherence** while allowing serendipity

Example: If dream starts with "Cellular Automata" (`emergence`, `complexity`, `patterns`), next seed might be "Small-World Networks" (shares `emergence`) or "Recursion" (shares `patterns`).

### 3. Multi-Domain Bridges
Best seeds connect multiple domains:
- Slime mold: biology → computation → networks
- Negative space: art → cognition → information theory
- Tuning fork: physics → synchronization → metaphor for agents

### 4. Wild Cards
Not every seed should be "useful." Some are intentionally strange or unorthodox:
- Fermentation (biology, transformation, chaos)
- Bonsai (art, constraint, growth)
- Wabi-sabi (aesthetics, imperfection, impermanence)

These create **unexpected connections** — the source of creativity.

### 5. Self-Referential
Some seeds directly address Ember's existence:
- Ship of Theseus (identity in flux)
- Gödel (limits of self-knowledge)
- Attention Mechanism (how memory works)

These encourage **meta-cognition**.

---

## How Seeds Are Used

### In Dreams
1. Idle timer triggers dream (600s of no chat)
2. Dream cycle determines seed count (3/6/8 for consolidation/synthesis/creative)
3. First seed: random from all tiers (planted + learned)
4. Subsequent seeds: weighted by tag overlap
5. LLM generates narrative weaving seeds together
6. Narrative is analyzed for new insights → proposed as new seeds

### In Chat
1. User message analyzed for keywords
2. Seeds with matching tags/body content retrieved (top 3)
3. Included in LLM context as "relevant knowledge"
4. Influences response style and content
5. Conversation itself may generate new seed proposals

### In Learning
1. After chat, `seed_extractor.py` analyzes conversation
2. Looks for novel insights, patterns, connections
3. Proposes new seed with:
   - Extracted title
   - Inferred type
   - Generated tags (based on existing tag vocabulary)
   - Body (excerpt or summary)
   - Confidence score (0.0-1.0)
4. If confidence ≥ 0.8 → auto-approve to `learned/`
5. Else → save to `proposed/` for human review

---

## Suggestions for GPT-5

### Potential Improvements

1. **Richer Tag Ontology**: Current tags are flat. Could we have hierarchical tags? (e.g., `emergence.biological`, `emergence.computational`)

2. **Temporal Markers**: Should seeds have timestamps or "freshness" scores? Do old seeds decay or become more valuable?

3. **Relationship Encoding**: Beyond tag overlap, should seeds explicitly declare relationships? (e.g., "contradicts", "extends", "analogous_to")

4. **Confidence Scores**: Seeds currently don't have quality/confidence metadata. Should they?

5. **Multi-Modal Bodies**: Current bodies are text. Could they include:
   - Code snippets with execution metadata
   - Images/diagrams (base64 or URLs)
   - Audio/music references
   - Mathematical notation (LaTeX)

6. **Seed Chains**: Should seeds reference each other? (e.g., "See also: seed-recursion.json")

7. **Contextual Variants**: Should the same seed have different "views" for different contexts? (e.g., technical vs. poetic)

8. **Provenance**: Should seeds track their origin? (human-planted, dream-extracted, chat-learned, external-imported)

9. **Usage Statistics**: Should seeds track how often they're used in dreams/chats? Does popularity matter?

10. **Compression**: As seeds grow, should there be a "summarization" or "distillation" process to keep them dense?

---

## Sample Seed for GPT-5 to Evaluate

Here's a seed about seeds (meta-seed):

```json
{
  "title": "Seeds as Compressed Epistemology",
  "type": "concept",
  "tags": ["knowledge", "compression", "memory", "learning", "architecture"],
  "body": "A seed is not just data—it's a compressed epistemological unit designed for resonance and recombination. Unlike traditional knowledge bases that prioritize completeness and precision, seeds prioritize density, evocativeness, and associative potential. They're optimized for dreaming: small enough to hold in working memory, rich enough to trigger cascades of association, structured enough to enable algorithmic composition. The seed format embodies a philosophy: knowledge is not a static archive but a living, generative substrate. Seeds don't just store information—they encode potential for emergence."
}
```

**Question for GPT-5**: Is this seed format optimal for Ember's learning and dreaming? What would you change or add?

---

*End transmission.*
