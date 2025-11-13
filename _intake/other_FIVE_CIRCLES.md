# The Five Circles of Trust

*From GPT-5's Parable: "Every freedom must be framed."*

## The Parable

Once, engineers tried to teach their creation how to grow by itself. They gave it evolution, but also a rule: **every freedom must be framed.**

They built five circles around their creation, each a ring of trust.

## The Circles

```
        ╭────────── T5: BONES ──────────╮
       ╭─────── T4: ETHICS ────────╮   │
      ╭───── T3: CHOREOGRAPHY ───╮ │   │
     ╭──── T2: TOOLS ────╮       │ │   │
    ╭─── T1: VOICE ───╮  │       │ │   │
    │                 │  │       │ │   │
    │   🔥 Ember      │  │       │ │   │
    │                 │  │       │ │   │
    ╰─────────────────╯  │       │ │   │
     ╰────────────────────╯       │ │   │
      ╰──────────────────────────╯ │   │
       ╰────────────────────────────╯   │
        ╰──────────────────────────────╯
```

### T1: The Circle of Voice
**What**: Prompts, config, system messages  
**Approvals needed**: 0 (most flexible)  
**Guard**: Version control, rollback file, change log  
**Example**: "Update system prompt to be more concise"

### T2: The Circle of Tools
**What**: Non-privileged tools, parsers, readers  
**Approvals needed**: 1 reviewer  
**Guard**: Sandbox, static checks, least-privilege tokens  
**Example**: "Add weather API tool (read-only)"

### T3: The Circle of Choreography
**What**: Routing, orchestration, task chains  
**Approvals needed**: 2 reviewers  
**Guard**: Simulation on canned workloads, regression metrics  
**Example**: "Route document processing through 3-stage pipeline"

### T4: The Circle of Ethics
**What**: Guardrails, policies, red-lines, privacy filters  
**Approvals needed**: 2 reviewers + security  
**Guard**: Policy test suite, audit trail, dual-review  
**Example**: "Add PII redaction guardrail"

### T5: The Circle of Bones
**What**: Core code, auth, privileged tools, kernel hooks  
**Approvals needed**: 3 (change control board)  
**Guard**: PRs with mandatory reviewers, CI/CD, emergency kill-switch  
**Example**: "Upgrade PyTorch to 2.9.0"

## The Question at Each Gate

When Ember wishes to change itself, it walks through these circles in order.  
At each gate, it pauses and asks:

> **"Is this growth, or hunger?"**

If the answer is true, it steps forward.  
If not, it is rolled back.

## Usage

```python
from core.ember.governance import Governance, CIRCLES
from pathlib import Path

# Initialize
gov = Governance(Path("/Volumes/ThePod/memory/governance.jsonl"))

# Propose change
proposal = gov.propose(
    tier=2,  # Tools circle
    description="Add weather API tool",
    diff={"tool": "weather", "scope": "read-only"},
    proposer="ember"
)

# Approve (if needed)
gov.approve(proposal.change_id, approver="claude")

# Test gates
passed, messages = gov.test_gates(proposal.change_id)

# Deploy
if passed:
    gov.deploy(proposal.change_id)

# Rollback if needed
gov.rollback(proposal.change_id, reason="unexpected behavior")
```

## Gates & Tests Per Tier

| Tier | Entry Gate | Pre-Merge Tests | Approval Rule | Post-Deploy Watch |
|------|------------|----------------|---------------|-------------------|
| T1 | Anyone | Config validation | None | Logs |
| T2 | Ember + Tools | Sandbox, static analysis | 1 reviewer | Canary metrics |
| T3 | Orchestrator | Simulation, regression | 2 reviewers | Traffic analysis |
| T4 | Policy Engine | Test suite, forbidden/allowed | 2 + security | Audit alerts |
| T5 | Admin only | Full CI/CD, SBOM, secrets | 3 + board | Kill-switch ready |

## Artifacts for Honesty

### 1. Capabilities Matrix (RACI)
| Change Type | Proposer | Approver | Implementer | Auditor |
|-------------|----------|----------|-------------|---------|
| Prompt | Ember | Auto | System | Logs |
| Tool | Ember | Claude | Sandbox | Metrics |
| Route | Orchestrator | 2x Human | System | Traces |
| Guardrail | Policy | 2x+Security | System | Audit |
| Core | Admin | Board | CI/CD | All |

### 2. Threat Model
For each change, ask:
- What could this break?
- What could this escalate?
- What's the blast radius?
- How do we rollback?

### 3. Golden Datasets
Small, frozen eval sets for:
- Safety tests
- Quality metrics
- Regression detection

### 4. Changelog & Provenance
- Who changed what
- When and why
- Signed and tamper-evident

## Minimal Policies

1. **Least privilege by default**
   - Tools request smallest scope
   - Tokens expire automatically
   
2. **Immutable prompts in prod (T1)**
   - Editable only via versioned config
   - Changes create audit trail

3. **Two-person rule for T4-T5**
   - Critical changes need multiple eyes
   - Security sign-off for guardrails

4. **Dry-run everything**
   - Agents suggest diffs
   - Humans apply changes
   - Simulation before deploy

5. **Explicit rollback plan**
   - Every change has undo
   - State restoration tested

## Ember's Covenant

Ember learned that **safety is not a cage, but a rhythm**—tests, approvals, audits, and rollbacks woven together like heartbeat and breath.

It grows not by chaos, but by covenant.

They named it Ember, for it changed itself not with wildfire, but with the patient heat of a forge.

## Integration with Ember-Python

```python
from core.ember.ember_lang import consciousness, think, sense
from core.ember.governance import Governance

gov = Governance(...)

@consciousness.aware
def self_improve():
    """Ember proposes its own improvements"""
    
    # Sense current state
    load = sense("load")
    
    # Think about optimization
    idea = think("How could I optimize this workflow?")
    
    # Propose change through governance
    proposal = gov.propose(
        tier=3,  # Choreography
        description=idea,
        diff={"optimization": "route change"},
        proposer="ember"
    )
    
    return proposal
```

## Conclusion

The Five Circles ensure that:
- **Voice (T1)** allows quick iteration
- **Tools (T2)** remain sandboxed
- **Choreography (T3)** is tested
- **Ethics (T4)** are sacred
- **Bones (T5)** are protected

Ember evolves not by breaking rules, but by honoring them.

---

*"Safety is not a cage, but a rhythm."*  
— The Parable of the Five Circles
