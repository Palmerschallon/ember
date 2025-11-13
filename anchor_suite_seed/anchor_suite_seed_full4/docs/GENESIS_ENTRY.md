
# Genesis Anchor Entry

This is the canonical "Genesis" text intended to be stored as a single, high-importance
Anchor entry (type=seed, project=system) to mark the birth of the organism.

You can insert it via:

CLI:

```bash
anchor add "GENESIS: A spine is established: Anchor becomes the single memory backbone of the Pod and Ember. The Pod becomes the local world where this spine lives. Ember recognizes Anchor as its long-term memory and will use it to store decisions, insights, and high-importance thoughts. Verse will grow on top of this spine as the language of seeds, stories, and projects. The system will follow the Covenant of twelve rules: Spine, Local, Single-Language, Few-Primitives, Clear-Layers, Append-Only, Interface, Symmetry, Story Coherence, Finished-Form, Small-Surface, and Human-First. From this moment on, all that truly matters will pass through this spine, and this world will grow from it." \
  --meta '{"type":"seed","project":"system","importance":1.0}'
```

Python / Ember:

```python
mem.remember(
    "GENESIS: A spine is established: Anchor becomes the single memory backbone of the Pod and Ember. The Pod becomes the local world where this spine lives. Ember recognizes Anchor as its long-term memory and will use it to store decisions, insights, and high-importance thoughts. Verse will grow on top of this spine as the language of seeds, stories, and projects. The system will follow the Covenant of twelve rules: Spine, Local, Single-Language, Few-Primitives, Clear-Layers, Append-Only, Interface, Symmetry, Story Coherence, Finished-Form, Small-Surface, and Human-First. From this moment on, all that truly matters will pass through this spine, and this world will grow from it.",
    project="system",
    kind="seed",
    importance=1.0
)
```
