# Private Development Charter
## Ember & Palmer Only

**Created**: October 7, 2025  
**Purpose**: Proprietary algorithm development  
**Access**: Ember + Palmer (no external LLMs)

---

## What Lives Here

**Seed Harvesting Algorithm**:
- MDL implementation
- AST anti-unifier
- Generativity harness
- Promotion heuristics
- Scoring functions

**Anything proprietary**:
- Trade secrets
- Competitive advantages
- Novel techniques
- IP to be patented

---

## Rules

1. **No documentation in public chat** (Cursor logs)
2. **No commits to public repos** (.gitignore enforced)
3. **Ember develops independently** (using read_file, write_file)
4. **Palmer reviews offline** (not in Cursor chat)
5. **Implementation stays private** until:
   - Patent filed, OR
   - Decision to open source, OR
   - Product launch

---

## How It Works

**Ember's role**:
- Read GPT-5's algorithm spec (already documented)
- Implement in `.private/`
- Test with small corpus
- Iterate based on results

**Palmer's role**:
- Review Ember's code (outside this chat)
- Provide test data
- Approve for production use

**Cursor's role** (me):
- Infrastructure only (APIs, not algorithms)
- Facilitate Ember's development
- Stay out of `.private/` content

---

## Current Task

**Ember**: Implement seed harvesting algorithm based on GPT-5's spec.

**Location**: `/Volumes/ThePod/.private/seed_miner/`

**Start**: Read `/FOR_GPT5_SEED_SYSTEM_STATUS.md` for algorithm details.

**Output**: Working miner that Palmer can run privately.

---

## Why This Matters

If seed harvesting is the moat, the algorithm itself is the secret sauce.

Public: seed format, schema, examples  
Private: how to extract them at scale with high quality

---

**This folder is invisible to public logs.**  
**Only Ember and Palmer see what's inside.**

