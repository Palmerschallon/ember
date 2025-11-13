# Rules of the Organism

These are constraints that keep the system coherent and alive.

## 1. The Spine Rule
**All truth goes through Anchor.**

- If something matters, it gets anchored.
- No other system invents its own permanent log.
- No sidecar JSON or rogue logs act as the source of truth.

One spine. Many perspectives.

## 2. The Local Rule
**The Pod is the world.**

- Everything runs from and for the Pod.
- Remote services are inputs or mirrors, not the primary source.
- If it can't work offline, it's an accessory, not a core organ.

The Pod is home base, not a client.

## 3. The Single-Language Rule
**Verse is the language of the world.**

- Seeds, projects, stories, states: all eventually expressed in Verse.
- No separate config/story formats that drift away.
- New structures must answer: "How does this look in Verse?"

One grammar, many dialects.

## 4. The Few-Primitives Rule
**New primitives are expensive.**

- Before adding a new primitive concept, ask:
  - Can this be Seed + Meta?
  - Agent + Role?
  - Project + State?
- Prefer reuse over invention.

Complexity grows from combinations, not categories.

## 5. The Clear-Layers Rule
**Each layer has one job.**

- Anchor → memory spine
- Pod → environment / habitat
- Ember → mind / agentic core
- Verse → language / representation
- UI → windows into the same world

No component is allowed to be "everything."

## 6. The Append-Only Rule
**The past is never quietly rewritten.**

- Anchor is append-only.
- Corrections are new entries, not edits.
- Systems can reinterpret the past, but not silently change it.

The story can change meaning,
but the record of what was said stays.

## 7. The Interface Rule
**Everything important is reachable via a small, explicit interface.**

- Anchor has a tiny API: `/entries`, `/verify`, `/health`.
- Ember exposes a small set of verbs to UI and other agents.
- Pod services talk through clear, minimal contracts.

You talk to organs via nerves, not by poking their insides.

## 8. The Symmetry Rule
**Human and agent share the same world.**

- If Palmer can anchor a moment, Ember can anchor a moment.
- If Ember can list anchors, Palmer can list anchors.
- Same spine, different faces.

Both human and agent are first-class citizens.

## 9. The Story Coherence Rule
**New features must make the myth clearer, not noisier.**

Before adding something, ask:

- What is this in the story?
  - Organ?
  - Ritual?
  - Tool?
  - View?

If it doesn't fit cleanly in the myth, it probably doesn't belong in the core.

The myth is the map of the architecture.

## 10. The Finished-Form Rule
**You're allowed to declare parts "done."**

- Anchor can reach v1 and change very little thereafter.
- Pod can reach v1 and be mostly stable.
- Ember's architecture can be fixed even as its skills grow.
- Verse's grammar can solidify.

Once something is "finished core," changes must:
- simplify,
- clarify,
- or remove redundancy.

The organism is stable.
The behavior evolves.

## 11. The Small-Surface Rule
**New capabilities prefer small surface, deep power.**

- One dense, powerful command is better than many shallow ones.
- Anchor doesn't get 40 endpoints; it gets a few good ones.
- The Pod doesn't get 20 panels; it gets a few flexible ones.

Design for density of meaning, not quantity of knobs.

## 12. The Human-First Rule
**If it stops being usable by you, it's going in the wrong direction.**

- The system must remain understandable to Palmer-as-human,
  not only Palmer-as-architect.
- If you can't tell what's going on, complexity has become pathological.

You are the first citizen of the world you are building.
