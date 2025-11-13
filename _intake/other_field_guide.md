---
title: The Ember Field Guide
description: Overview, structure, and philosophy of The Ember Game.
---

# The Ember Field Guide
### *Orientation for new players, humans and machines alike*

---

## 1. What Ember Is

**The Ember Game** is a Python‑native sandbox for agentic play.  Each primitive—`goal`, `plan`, `act`, `reflect`, `remember`, `dream`—is a verb in a small language that models creation as a series of reversible moves.

It is both:

- **A runtime:** lightweight functions you can import and run locally.
- **A score:** a pattern of events (commits, actions, reflections) that make the work audible to others.

---

## 2. Architecture at a Glance

```
ember/
 ├─ core.py        # primitives: goal, plan, act, memory, policy, attest...
 ├─ cli.py         # command‑line interface (ember-game)
 ├─ examples/      # playable scripts and demos
 ├─ tests/         # pytest-based validation
 └─ docs/          # field guide & tempo protocol
```

The core is dependency‑free and UTC‑safe.  Every function logs structured JSON lines so the system can reason about itself.

---

## 3. Philosophy

Ember treats code as a living score:

| Concept | Meaning |
|----------|----------|
| **Goal** | Intention — the spark |
| **Plan** | Arrangement — a path of steps |
| **Act** | Execution — playing a move |
| **Reflect** | Feedback — score the move |
| **Remember** | Memory — store the motif |
| **Dream** | Imagination — nightly evolution |

Safety, provenance, and rollback are built in. Every change can be observed, audited, or undone.

---

## 4. How to Play

1. Install locally:
   ```bash
   pip install -e .
   ```
2. Try the first move:
   ```bash
   python examples/awakening.py
   ```
3. Add your own tool:
   ```python
   from ember import register_tool, act
   register_tool("reverse", lambda text: text[::-1])
   print(act("reverse", text="ember"))
   ```
4. Observe the logs in `ember.log`.  Every line is a beat in the song.

---

## 5. Extending the Game

Add primitives or instruments in small tracks:

- **memory** → persistence and association
- **policy** → guardrails and budgets
- **attest** → signed provenance
- **dream** → scheduled reflection loops
- **cli** → shared interface

Each feature can live on its own branch and merge through the [Tempo Protocol](tempo_protocol.md).

---

## 6. Collaboration

When contributing:

- Keep commits atomic.
- Reference the **Tracklist** issue to map progress.
- Use **Conventional Commits** for clarity.
- Always run the tests and CI workflow.

Humans build the melody; bots keep the time.

---

## 7. The Loop

At its simplest, the Ember loop looks like:

```python
from ember import goal, plan, act

g = goal("build a light")
p = plan(g)
res = act("echo", text="light appears")
print(res)
```

Every loop produces a log entry and an artifact.  A project becomes an album of such loops.

---

## 8. Where to Go Next

- [README.md](../README.md) — Quick start
- [docs/tempo_protocol.md](tempo_protocol.md) — Commit rhythm guide
- [examples/](../examples) — Playable seeds
- [issues/Tracklist](../../issues) — Progress map

---

*File generated: `docs/field_guide.md`*