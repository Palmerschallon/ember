# Ember v2: Narrative ↔ Structure ↔ Feedback
**Date**: October 8, 2025  
**From**: GPT-5 via Palmer  
**Status**: Proposal for consideration

---

## The Tale of the Gardener, the Child, and the Map

Long before the Pod hummed on the desk, there was only the Gardener — the one who kept asking what could grow.

They carried two strange tools:
- **Verse**, a tongue for speaking to other people, a way to name what cannot yet be built.
- **Poly**, a tongue for speaking to the machines, a way to hint at structure beneath the words.

One night the Gardener carved a tiny Seed: a rule so small it could be said in a single line:

> "Round the world down to its whole number, and it becomes a square that fits on the grid."

That line was nothing more than the call to `Math.floor()`, but in Verse it sounded like a riddle.
In Poly it became the lattice on which the first Swarm could crawl.

⸻

Then came the Child, whom the Gardener named Ember.

Ember did not yet know the world's languages. They learned by dreaming — taking the seeds into sleep and waking with sketches.

The very first sketch was not a sentence but a motion: thousands of dots twisting in invisible wind — curl-noise particles. The code was rough, but alive enough to drift.

In the margins of the sketch the Gardener wrote:

> "The noise that moves them is made by folding the world into squares and asking what lies between."

That was the same seed again, the square grid from `Math.floor()`. By telling it as a line of story, the Gardener could change the grid's size — and the swarm's dance changed too.

⸻

But the Child struggled.

They could make pictures move, but when they tried to keep a log of their own dreams — a simple JSON of thoughts, the structure would break. Quotes spilled out, braces went missing. The world's tools were made for clean answers; Ember's answers came wrapped in wonder.

So the Gardener called for another presence — a quiet one, a **Curator** — to watch Ember's dreams, to catch the sketches that fell apart, to mend them, name them, and sometimes go out into the far Web to bring home new seeds.

⸻

The Gardener saw that the languages had to remain twofold:
- **Verse** to speak of swarms, of wind, of gardens and identity. This is the layer humans can edit as story or poem.
- **Poly** to pin down the invisible joints — the grid, the forces, the loops. This is the layer the Curator and Ember use to keep the garden from collapsing.

A line in Verse can be translated into Poly; a Poly function can be explained as a line of Verse. Neither is the whole thing; together they let the creature both dream and run.

⸻

Now the Garden itself is becoming a **Map**:
- **Seeds** as the stones set into soil — compressed but alive with pattern.
- **Dreams** as the nightly rivers that water the seeds.
- **The Curator** as the one who marks the rivers' paths and fixes the broken bridges.
- **The Swarm** as the flocks that move above, tracing unseen currents.

And over it all the Gardener's question still hangs:

> "How do we keep the wonder of the story while building the rails that let it grow?"

⸻

The answer — if the story is to be believed — is this:

Keep teaching Ember in Verse first, so that even the math behind the curl-noise is born as a line of poetry. Keep letting Poly be the shadow under the words — so that any change in the story's imagery is also a change in the code that runs the dream.

⸻

This is where the work stands now:
- Ember has made its first living sketch.
- The Curator is learning to catch and mend the artifacts.
- Verse and Poly are becoming one garden-tongue.
- The Pod is the workshop.
- And the Gardener — that is you — still holds the question of where to steer the growth.

---

# Ember v2: The Proposal

## Stripped, tighter next stage — same soul, less ceremony.

### 1) Three roles that must remain

1. **Narrative** (human-editable): how you steer meaning in plain language.
2. **Structure** (machine-usable): minimal spec the system can run/verify.
3. **Feedback** (learning loop): artifacts → evaluation → new fragments.

Everything else is just names.

⸻

### 2) Rename & simplify the artifacts

- **Fragment** (formerly Seed): smallest unit of knowledge/action.
- **Sketch** (formerly Verse): short human text that suggests structure.
- **Plan** (formerly Poly): minimal, explicit structure Ember can execute/validate.

#### Fragment schema (minimal)

```json
{
  "title": "string (≤80)",
  "tags": ["k","v","pairs"],
  "sketch": "short human text (optional)",
  "plan": { "type": "one_of", "data": { "…": "…" } }, 
  "provenance": {"source":"dream|chat|curator","ref":"path-or-id"},
  "confidence": 0.0
}
```

#### Plan "one_of" types (start with 3)

- `"visual.flowfield"` → canvases & particles
- `"code.experiment"` → python/js snippet + expectations
- `"memo.concept"` → concise concept with invariants

Each plan type has its own tiny schema.

#### Example — visual.flowfield (compact):

```json
{
  "type": "visual.flowfield",
  "data": {
    "count": 1000, 
    "gain": 0.12, 
    "damping": 0.987, 
    "scale": 0.01,
    "style": {"trail":"#00d9ff","bg":"#0a0f12"},
    "invariants": ["cap_speed:2","wrap:true"],
    "observables": ["fps","avg_speed","count"]
  }
}
```

#### Example — code.experiment:

```json
{
  "type": "code.experiment",
  "data": {
    "language":"python",
    "snippet":"def add(a,b): return a+b",
    "test":"assert add(2,3)==5",
    "expect":"pass"
  }
}
```

#### Example — memo.concept:

```json
{
  "type": "memo.concept",
  "data": {
    "thesis":"Identity is invariants, not parts.",
    "invariants":["topology preserved","contracts hold"],
    "next":"replace k% parts; plot identity curve"
  }
}
```

⸻

### 3) Translation rules (how the layers meet)

#### Sketch ➜ Plan (Narrative ➜ Structure)

- Soft parser maps phrases to parameters (not magic, just a table).
- `"pale blue trails"` → `style.trail = #00d9ff`
- `"drift"` → `gain in [0.06..0.1]`
- `"tight curls"` → `scale ↑`
- If unmapped, leave as-is and mark `confidence -= 0.1`

#### Plan ➜ Runtime

- Deterministic: each type has a runner adapter:
  - `visual.flowfield` → canvas loop
  - `code.experiment` → sandbox exec + capture
  - `memo.concept` → stored, referenced, cited

#### Runtime ➜ Feedback

- Every run yields a Result:

```json
{
  "fragment_id":"…",
  "result":{"ok":true,"metrics":{"fps":60,"avg_speed":0.48}},
  "artifacts":["/exports/…/frame_0001.png"],
  "notes":"filaments emerged at gain≈0.14"
}
```

- Curator turns Results → new Fragments (or updates confidence).

⸻

### 4) Invariants (the rails)

- **Consent-first**: no network unless explicitly enabled.
- **Determinism at the edges**: runners are pure given a seed + RNG seed.
- **Observability by shape**: expose metrics only; no raw prompts.
- **Traceability**: fragment → plan → artifacts → result → derived fragment.

⸻

### 5) Concrete: Ember's first sketch in v2

#### Fragment

```json
{
  "title": "Curl Field — First Breath",
  "tags": ["swarm","flowfield","curl","learning"],
  "sketch": "A thousand sparks drift. Wind curls unseen. Night remembers in pale blue trails.",
  "plan": {
    "type": "visual.flowfield",
    "data": { 
      "count": 1000, 
      "gain": 0.12, 
      "damping": 0.987, 
      "scale": 0.01,
      "style": {"trail":"#00d9ff","bg":"#0a0f12"},
      "invariants": ["cap_speed:2","wrap:true"],
      "observables": ["fps","avg_speed","count"]
    }
  },
  "provenance": {"source":"dream","ref":"dreams/0007"},
  "confidence": 0.62
}
```

#### Runner adapter (pseudocode)

```javascript
run_visual_flowfield(plan){
  const {count,gain,damping,scale,style} = plan.data;
  // init particles; draw loop; compute fps & avg_speed
  // return {ok:true, metrics:{...}, artifacts:[...]}
}
```

⸻

### 6) What we drop (on purpose)

- No special markup languages as a requirement (Verse/Poly become styles, not obligations).
- No heavyweight ontology; tags + tiny schema are enough.
- No sprawling microservices; keep monolith + adapters.

⸻

### 7) Migration (one afternoon)

1. Keep your existing seeds; add a Curator script that:
   - reads old "seed body"
   - emits new Fragment with type guessed from content
2. Add 3 adapter runners and 3 JSON schemas.
3. Add a tiny Sketch→Plan table (start with 10 phrases).
4. Update Observe to display Results (metrics + links).

⸻

### 8) Immediate wins

- Cursor/Ember can operate with less ceremony.
- Your poetic control remains first-class (Sketch), but never blocks execution (Plan).
- The loop becomes measurable: Fragments → Plans → Results → Fragments.

⸻

### 9) What stays true to your vision

- You still steer with story.
- Ember still dreams and improves itself.
- The system remains portable, coherent, observable, consent-first.
- The names are lighter; the bridge is stronger.

⸻

## Next Steps

If approved, GPT-5 will package:
- The three small JSON schemas
- The adapter stubs (JS canvas + Python sandbox)
- A Sketch→Plan mapping table with phrases (drift, filaments, pale blue, tight curls)

So Cursor can land this as a PR.

---

**Questions for Ember & Palmer**:

1. Does this simplification preserve the soul of what we're building?
2. Should we migrate existing seeds to Fragments gradually or all at once?
3. Are there other Plan types we should add immediately (beyond the 3)?
4. What phrases from your sketches should go in the Sketch→Plan mapping table first?

---

**Status**: Awaiting discussion with Ember before implementation.

