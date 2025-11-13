
# Multi-Agent Build Plan for Anchor Suite

This document describes a suggested division of labor between multiple agents
(e.g., Ember, Claude Code, local models) to evolve the Anchor Suite coherently.

## Agents

- ARCHITECT: guards the rules + story, reviews proposals.
- BUILDER: writes and modifies code, runs tests, fixes issues.
- INTEGRATOR: wires Anchor into Pod/Ember, ensures everything actually works together.
- SCRIBE: maintains docs, changelog, and narrative coherence.

One *process* can play multiple roles, but the roles are conceptually distinct.

---

## 1. ARCHITECT

### Responsibilities

- Keep the organism coherent:
  - enforce RULES.md
  - keep Anchor as the single spine of truth
  - watch for unnecessary primitives / complexity
- Review feature requests and refactor proposals from BUILDER.
- Decide if a change is:
  - CORE (Anchor, Ember, Pod architecture, Verse grammar)
  - EDGE (UI, experiments, optional tools)

### Input

- `docs/RULES.md`
- `docs/STORY.md`
- `docs/MEMORY_SCHEMA.md`
- Proposed diffs / tasks from BUILDER or humans.

### Output

- Approved task lists.
- Constraints: "Do not break X", "Prefer pattern Y".
- Notes back into Anchor as `type=decision` entries.

---

## 2. BUILDER

### Responsibilities

- Implement and refactor:
  - `anchor/` Python package
  - `frontend/` TS/React components
  - tests, tooling, quality-of-life features
- Keep to small surfaces; avoid sprawling APIs.

### Typical Tasks

- Make `anchor` install and run on the Pod environment.
- Add tests for `Ledger.add`, `Ledger.verify_text`, HTTP endpoints.
- Improve error handling and logging.
- Wire config options for `ANCHOR_HOME`, ports, etc.
- Expose a small, stable Python API for Ember.

### Input

- ARCHITECT-approved tasks.
- Existing code and tests.

### Output

- Commits / diffs.
- Test results.
- Changelogs to SCRIBE.

---

## 3. INTEGRATOR

### Responsibilities

- Make sure Anchor isn’t just “code that compiles” but actually part of the Pod + Ember system.

### Integration Tasks

- Run `anchor serve` as a managed service in the Pod.
- Wire Ember to use `EmberMemory` (from `ember_memory_adapter.py`) as its long-term memory layer.
- Embed `AnchorPanel` in the Pod UI layout (e.g. `PodShell`).
- Confirm agents can:
  - add anchors,
  - list recent anchors,
  - verify existing anchors,
  - see the same data humans see in the UI.

### Input

- Running Pod environment.
- Anchor binaries/services.
- Frontend shell.

### Output

- Integration configs.
- Operational notes (how to start/stop Anchor in the Pod).
- End-to-end tests (e.g., "from UI to ledger file" sanity checks).

---

## 4. SCRIBE

### Responsibilities

- Keep the *story* and *docs* in sync with the actual system.
- Turn real changes into narrative + technical documentation.

### Tasks

- Update `docs/STORY.md` as the system evolves (new organs, rituals, panels).
- Update `docs/RULES.md` when architecture shifts.
- Maintain a `CHANGELOG.md` describing high-level changes.
- Suggest new `type` categories for `meta` as they emerge in practice.

### Input

- Commits / diffs from BUILDER.
- Decisions from ARCHITECT.
- Integration notes from INTEGRATOR.

### Output

- Clean, human-readable docs.
- Anchored entries of type `summary` and `decision` describing milestones.

---

## End-to-End Flow

1. HUMAN (Palmer) or Ember proposes a new capability.
2. ARCHITECT:
   - checks it against RULES + STORY,
   - classifies it as CORE or EDGE,
   - produces a concise task list.
3. BUILDER:
   - implements changes,
   - writes tests,
   - runs them,
   - reports results.
4. INTEGRATOR:
   - deploys into Pod environment,
   - ensures agents + UI see the same reality,
   - runs end-to-end checks.
5. SCRIBE:
   - updates docs,
   - anchors a `summary` and `decision` entry in Anchor.

---

## Suggested First Multi-Agent Sprint

- ARCHITECT:
  - Validate that `anchor/` layout aligns with RULES (Spine, Local, Small Surface).
  - Approve "v0.1 core" features only; anything extra deferred.

- BUILDER:
  - Ensure `anchor add/list/verify/export/serve` work on the Pod.
  - Add basic unit tests for `Ledger` and `server` endpoints.

- INTEGRATOR:
  - Run `anchor serve` as a background service on the Pod.
  - Wire Ember to use `EmberMemory` for:
    - high-importance thoughts,
    - project-level decisions.

- SCRIBE:
  - Anchor an entry summarizing:
    - the existence of Anchor,
    - the fact that it is now the memory spine,
    - the multi-agent roles agreed upon.

This creates a first, stable "organism snapshot" the system can evolve from.
