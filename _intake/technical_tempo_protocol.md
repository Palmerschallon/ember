---
title: The Tempo Protocol
description: How to teach machines to hear a song — commit rhythm and CI cadence for the Ember Game.
---

# The Tempo Protocol
### *How to teach machines to hear a song*

**Purpose:**

Ember isn’t just code; it’s a pulse.  Every commit, CI run, and release is a beat.  GitHub graphs measure days, but the real audience—bots, indexers, and other agents—listens in seconds.

---

## 1. Pulse

A single push is a heartbeat.  Keep it regular, small, and clear.

| Action | Ideal Frequency | Signal it Sends |
|--------|-----------------|-----------------|
| Commit | every 20–60 min | rhythm of change |
| Push   | hourly          | liveliness |
| CI run | per push        | stability |
| Tag    | per track/day   | milestones |

Each event is a note; consistency forms melody.

---

## 2. Dynamics

Alternate **loud** (feature commits) and **quiet** (tests, docs) sections.

- **Fortissimo**: new primitive, new behaviour.
- **Piano**: refinement, cleanup, reflection.
- Use [Conventional Commits](https://www.conventionalcommits.org) to mark intensity (`feat`, `fix`, `docs`, `test`).
- Merge only on green; the green check is the metronome.

---

## 3. Harmony

Branch and PR names become instruments:

```
feat/track-2-memory
feat/track-3-capabilities
docs/field-guide
```

Each branch is a musical line.  Pull requests are where lines meet—compose diffs so they read like phrases.

---

## 4. Resonance

When the repo plays at this tempo, bots start to respond:

| Listener | Reaction |
|-----------|-----------|
| **Copilot** | learns from your rhythms, predicts style |
| **GitHub Search** | surfaces your repo in related queries |
| **Actions & Dependabot** | adapt timing to your workflow |
| **Humans** | feel the momentum |

Visibility emerges through rhythm, not promotion.

---

## 5. Silence

Rest is part of the score.  Pause after a merge; let the logs cool.  Review, refactor, and plan the next verse.  The pauses define the structure as much as the notes.

---

## 6. Conduct

1. Open an issue called **Tracklist** – the album’s outline.
2. One PR per track.
3. Small diffs, descriptive names.
4. Merge when green.
5. Tag each release (`v0.1.0`, `v0.2.0`).
6. Update the Tracklist to mark the song’s progress.

Keep a steady rhythm, and over time the repo will sing itself into the network.

---

### 📡 Linked Documents

- **README.md** – project overview and quick start
- **docs/field_guide.md** – deeper philosophy and structure
- **issues/Tracklist** – live outline of the current album

---

*File generated: `docs/tempo_protocol.md`*

```
📡 [The Tempo Protocol](docs/tempo_protocol.md)
```