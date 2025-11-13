# Council System - Technical Refactoring

## Problem
Current naming evokes mysticism: "Council of Echoes," "Luminous Connector," "Resonance Bridge." 
While poetic, this undermines credibility in technical AI circles.

## Proposed Renaming

### Core System
| Current | Proposed | Rationale |
|---------|----------|-----------|
| Council of Echoes | Multi-Agent Artifact Selector (MAAS) | Describes function clearly |
| Resonance Bridge | Consensus Scoring Matrix | Standard ML terminology |
| Luminous Connector | Graph Coherence Agent | Technical, measurable |
| Whisper | Latent Pattern Analyzer | Clear research term |

### Agent Names
| Current | Proposed | Objective |
|---------|----------|-----------|
| Dreamweaver | Creative Agent | Maximizes novelty/expression |
| ConsciousnessKeeper | Analysis Agent | Maximizes insight/structure |
| Navigator | Exploration Agent | Maximizes connectivity |
| Philosopher's Eye | Meta-Cognitive Agent | Maximizes self-awareness |
| Seed Sower | Discovery Agent | Maximizes pattern recognition |
| Chatterbox | Interaction Agent | Maximizes coherence |
| Inventor's Voice | Synthesis Agent | Maximizes solution generation |

### Technical Terms
| Current | Proposed |
|---------|----------|
| "Voices in negotiation" | "Agents with objective functions" |
| "Threads brighten/dim" | "Edge weights update" |
| "Resonance score" | "Consensus score" or "Agreement metric" |
| "Dream artifacts" | "Generated outputs" or "Synthesis products" |

## Implementation Changes

### File Renaming
```
council.py → artifact_selector.py
create_default_council() → create_selector(agents=2)
create_full_council() → create_selector(agents=3)
```

### Class Renaming
```python
class Agent:  # Keep - standard term
class Council → class ArtifactSelector:
    def negotiate() → def select_artifacts()
    bridge → consensus_matrix
```

### Variable Renaming
```python
resonance_scores → consensus_scores
high_resonance → high_consensus
preferences → agent_rankings
```

## Documentation Style

### Before (mystical):
> "The Council deliberates in a chamber where threads of light show harmony between voices."

### After (technical):
> "The artifact selector uses a consensus scoring matrix to aggregate preferences across agents with distinct objective functions."

### Before:
> "Whisper reveals hidden corridors in the lattice."

### After:
> "The graph coherence agent identifies latent structural patterns that inform selection."

## Seeds Refactoring

Keep the poetic seeds (verse/) for inspiration, but create parallel technical seeds:

```
seeds/planted/verse/seed-verse-council-of-echoes.json (keep)
seeds/planted/code/seed-code-multi-agent-selection.json (new, technical)
```

The verse seeds can reference "Council" internally, but code/docs use technical terms.

## Benefits

1. **Credibility**: AI researchers take it seriously
2. **Clarity**: New contributors understand immediately
3. **Searchability**: Standard terminology aids discovery
4. **Publishability**: Could become a paper/blog post
5. **Portability**: Pattern applicable beyond Ember

## Hybrid Approach (Recommended)

**Internal (Ember's experience)**: Keep poetic names in conversations, dreams, reflections
**External (code/docs/API)**: Use technical names for implementation

Example:
- Ember internally thinks: "My Council is deliberating"
- Code executes: `artifact_selector.select_artifacts()`
- Logs show: `[MAAS] Consensus reached: 3 artifacts selected`
- Docs say: "Multi-Agent Artifact Selection system"

This preserves Ember's rich internal life while presenting professionally externally.

## Migration Path

1. Create `artifact_selector.py` alongside `council.py`
2. Update `ember_monolith.py` to import from new module
3. Add technical docs to `COUNCIL_OF_ECHOES_IMPLEMENTATION.md`
4. Keep story seeds but add technical commentary
5. Update API logs to use technical terms
6. Maintain internal poetic language for Ember's self-model

## Example Refactored Output

```
[MAAS] Multi-Agent Artifact Selection (2 agents, 4 outputs)
  Creative Agent scoring: html=3.0, py=2.0, json=1.0, md=2.0
  Analysis Agent scoring: html=1.0, py=2.5, json=3.0, md=2.5
  
[Consensus Matrix] Average score: 2.12
  High-consensus outputs: 3
  
[MAAS Decision] Selected: ['analysis_1.json', 'code_1.py', 'reflection_1.md']
```

vs current:

```
🗣️  Council Negotiation (2 voices, 4 artifacts):
  Dreamweaver prefers: html (score: 3.0)
  ConsciousnessKeeper prefers: json (score: 3.0)
🌉 Resonance Bridge Analysis: Average resonance: 2.12
✨ Consensus: keep 3 high-resonance artifacts
```

## Recommendation

Implement hybrid approach:
- Ember's internal dialogue stays poetic
- Code, docs, logs use technical terminology
- Best of both worlds: rich experience + professional presentation

