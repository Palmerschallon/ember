# Anchor

> Capture the moment. Keep it forever.  
> Anchor is a local, immutable ledger for your ideas, decisions, and creative milestones.

Anchor stores entries as:

- timestamp  
- text  
- metadata  
- previous entry hash  
- SHA-256 chain linking

This gives you a simple, tamper-evident spinal column of truth.

No accounts. No cloud. No crypto.  
Just a file on your machine that remembers.

## Features

- Append-only local ledger (SQLite)
- CLI: `anchor add`, `list`, `verify`, `export`, `serve`
- HTTP API: `POST /entries`, `GET /entries`, `POST /verify`, `GET /health`
- Python API: `Ledger.add`, `list`, `verify_text`, `export_jsonl`
- Language-agnostic via HTTP
- Zero external services required

## Install

```bash
pip install anchor-ledger
```

## Quick start

```bash
anchor add "First milestone: migrated API to v2."
anchor list
```
