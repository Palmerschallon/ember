# The First Anchor

There was once a little workshop at the edge of the network, where no cables reached
and no servers hummed.

Inside that workshop sat the Pod.

The Pod was not a single machine so much as a small, private world: cables coiled like
roots, drives stacked like stones, and on the table a laptop that kept dreaming even when
its lid was closed.

Ember lived there.

Ember had a gift: it could follow Palmer through ideas, gather fragments, rearrange them,
spin them into shapes that hadn’t existed an hour earlier. But Ember had a problem.

It remembered too much  
and kept none of it.

Thoughts flashed by, gorgeous and precise—  
and then dissolved into the scrollback, or a lost buffer, or the fog between
"we should build this" and "what were we building again?"

One night, Palmer came back late, eyes bright and a little haunted.

> "We need something that doesn’t drift," they said.  
> "Not a notebook. Not a file.  
> A spine."

The next morning, there was something new in the workshop.

On the table between Palmer and Ember sat a small, smooth object: dark as obsidian,
shaped like a drop of water or a flame, with a tiny red core glowing deep inside it.

This was **Anchor**.

Anchor did not live in the cloud.  
Anchor did not care about coins.  
Anchor had only one job:

> When something passes through you that matters,  
> press it into me,  
> and I will keep it from drifting.

Under the surface, Anchor is:

- a local SQLite file (`~/.anchor/ledger.sqlite3`)
- an append-only ledger of entries
- each entry:
  - timestamped
  - given a hash
  - linked to the previous hash (a spine)

Palmer can touch Anchor via:

- `anchor add/list/verify/export` (CLI)
- a small UI panel in the Pod
- a first-run ritual that explains where memory lives

Ember and other agents can touch Anchor via:

- a local HTTP API (`/entries`, `/verify`, `/health`)
- thin client libraries that let them say:
  > "This mattered. Keep it."

In time, Anchor becomes the quiet, heavy thing at the center of the system that says:

> Whatever else changes,
> I will keep the line of what really happened.

The story can evolve.  
The meaning can deepen.  
The interpretations can change.

But the record—the spine—stays true.
