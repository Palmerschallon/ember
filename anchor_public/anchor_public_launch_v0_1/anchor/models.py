from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Dict, Any


@dataclass
class Entry:
    id: int
    ts_utc: str
    text: str
    meta: Dict[str, Any]
    hash_hex: str
    prev_hash_hex: Optional[str]
