from __future__ import annotations

import json
import sqlite3
import time
import hashlib
from pathlib import Path
from typing import Iterable, List, Optional, Dict, Any

from .config import get_db_path
from .models import Entry


SCHEMA = """
CREATE TABLE IF NOT EXISTS entries (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  ts_utc TEXT NOT NULL,
  text TEXT NOT NULL,
  meta_json TEXT NOT NULL,
  hash_hex TEXT NOT NULL UNIQUE,
  prev_hash_hex TEXT
);
CREATE INDEX IF NOT EXISTS idx_entries_ts ON entries(ts_utc);
"""


class Ledger:
    def __init__(self, db_path: Optional[Path] = None) -> None:
        self.db_path = Path(db_path) if db_path else get_db_path()
        self.conn = sqlite3.connect(self.db_path)
        self.conn.execute("PRAGMA journal_mode=WAL;")
        self.conn.execute("PRAGMA synchronous=NORMAL;")
        self.conn.executescript(SCHEMA)

    # --- internal helpers -------------------------------------------------

    def _tip_hash(self) -> Optional[str]:
        row = self.conn.execute(
            "SELECT hash_hex FROM entries ORDER BY id DESC LIMIT 1"
        ).fetchone()
        return row[0] if row else None

    @staticmethod
    def _make_hash(ts: str, text: str, meta: Dict[str, Any], prev: Optional[str]) -> str:
        payload = {
            "ts": ts,
            "text": text,
            "meta": meta,
            "prev": prev,
        }
        blob = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
        return hashlib.sha256(blob).hexdigest()

    @staticmethod
    def _row_to_entry(row) -> Entry:
        id_, ts, text, meta_json, hash_hex, prev = row
        meta = json.loads(meta_json)
        return Entry(
            id=id_,
            ts_utc=ts,
            text=text,
            meta=meta,
            hash_hex=hash_hex,
            prev_hash_hex=prev,
        )

    # --- public API -------------------------------------------------------

    def add(self, text: str, meta: Optional[Dict[str, Any]] = None) -> Entry:
        ts = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        meta = meta or {}
        prev_hash = self._tip_hash()
        hash_hex = self._make_hash(ts, text, meta, prev_hash)
        self.conn.execute(
            "INSERT INTO entries(ts_utc, text, meta_json, hash_hex, prev_hash_hex) "
            "VALUES (?, ?, ?, ?, ?)",
            (ts, text, json.dumps(meta, separators=(",", ":")), hash_hex, prev_hash),
        )
        self.conn.commit()
        row = self.conn.execute(
            "SELECT id, ts_utc, text, meta_json, hash_hex, prev_hash_hex "
            "FROM entries WHERE hash_hex = ?",
            (hash_hex,),
        ).fetchone()
        return self._row_to_entry(row)

    def list(self, limit: int = 20) -> List[Entry]:
        rows = self.conn.execute(
            "SELECT id, ts_utc, text, meta_json, hash_hex, prev_hash_hex "
            "FROM entries ORDER BY id DESC LIMIT ?",
            (limit,),
        ).fetchall()
        return [self._row_to_entry(r) for r in rows]

    def iter_all(self) -> Iterable[Entry]:
        cur = self.conn.execute(
            "SELECT id, ts_utc, text, meta_json, hash_hex, prev_hash_hex "
            "FROM entries ORDER BY id ASC"
        )
        for row in cur:
            yield self._row_to_entry(row)

    def verify_text(
        self, text: str, at_ts: Optional[str] = None
    ) -> List[Entry]:
        params: List[Any] = [text]
        q = (
            "SELECT id, ts_utc, text, meta_json, hash_hex, prev_hash_hex "
            "FROM entries WHERE text = ?"
        )
        if at_ts:
            q += " AND ts_utc <= ?"
            params.append(at_ts)
        rows = self.conn.execute(q, params).fetchall()

        ok_entries: List[Entry] = []
        for row in rows:
            entry = self._row_to_entry(row)
            calc = self._make_hash(
                entry.ts_utc, entry.text, entry.meta, entry.prev_hash_hex
            )
            if calc == entry.hash_hex:
                ok_entries.append(entry)
        return ok_entries

    def export_jsonl(self) -> str:
        lines = []
        for e in self.iter_all():
            lines.append(
                json.dumps(
                    {
                        "id": e.id,
                        "ts_utc": e.ts_utc,
                        "text": e.text,
                        "meta": e.meta,
                        "hash_hex": e.hash_hex,
                        "prev_hash_hex": e.prev_hash_hex,
                    },
                    ensure_ascii=False,
                )
            )
        return "\n".join(lines)

    def is_empty(self) -> bool:
        row = self.conn.execute("SELECT COUNT(*) FROM entries").fetchone()
        return (row[0] == 0)
