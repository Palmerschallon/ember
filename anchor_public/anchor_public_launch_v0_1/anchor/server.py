from __future__ import annotations

from typing import Optional, Any, Dict, List

from fastapi import FastAPI
from pydantic import BaseModel

from .ledger import Ledger
from .models import Entry

app = FastAPI(title="Anchor API", version="0.1.0")
ledger = Ledger()  # local, file-backed


class EntryIn(BaseModel):
    text: str
    meta: Optional[Dict[str, Any]] = None


class EntryOut(BaseModel):
    id: int
    ts_utc: str
    text: str
    meta: Dict[str, Any]
    hash_hex: str
    prev_hash_hex: Optional[str]


class VerifyRequest(BaseModel):
    text: str
    at: Optional[str] = None


def entry_to_out(e: Entry) -> EntryOut:
    return EntryOut(
        id=e.id,
        ts_utc=e.ts_utc,
        text=e.text,
        meta=e.meta,
        hash_hex=e.hash_hex,
        prev_hash_hex=e.prev_hash_hex,
    )


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/entries", response_model=List[EntryOut])
def list_entries(limit: int = 20):
    entries = ledger.list(limit=limit)
    return [entry_to_out(e) for e in entries]


@app.post("/entries", response_model=EntryOut)
def add_entry(payload: EntryIn):
    e = ledger.add(payload.text, payload.meta or {})
    return entry_to_out(e)


@app.post("/verify", response_model=List[EntryOut])
def verify(payload: VerifyRequest):
    matches = ledger.verify_text(payload.text, payload.at)
    return [entry_to_out(e) for e in matches]
