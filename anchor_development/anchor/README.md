# Anchor

> Capture the moment. Keep it forever.  
> A local, immutable ledger for your ideas.

Anchor is a tiny tool that lets you **append thoughts, fragments, and decisions** to a
local ledger. Each entry is timestamped and linked to the previous one with a
cryptographic hash, so the history cannot be quietly rewritten.

No accounts.  
No servers.  
No crypto.  
Just a file on your machine that remembers.

## Install (dev)

```bash
cd anchor
pip install -e .
anchor --help
```

## Core commands

- `anchor add "text"` – add an entry
- `anchor list` – list recent entries
- `anchor verify "text"` – verify a line exists in the ledger
- `anchor export` – export as JSONL
- `anchor serve` – run local HTTP API (`/entries`, `/verify`, `/health`)
