from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Optional
import requests


@dataclass
class AnchorEntry:
    id: int
    ts_utc: str
    text: str
    meta: Dict[str, Any]
    hash_hex: str
    prev_hash_hex: Optional[str]


class AnchorClient:
    """
    Minimal client for talking to a local Anchor server.

    Usage:
        client = AnchorClient()
        entry = client.add("From the swarm, a spark.", {"project": "verse"})
    """

    def __init__(self, base_url: str = "http://127.0.0.1:7171") -> None:
        self.base_url = base_url.rstrip("/")

    def _entry_from_dict(self, data: Dict[str, Any]) -> AnchorEntry:
        return AnchorEntry(
            id=data["id"],
            ts_utc=data["ts_utc"],
            text=data["text"],
            meta=data.get("meta", {}),
            hash_hex=data["hash_hex"],
            prev_hash_hex=data.get("prev_hash_hex"),
        )

    def health(self) -> bool:
        try:
            r = requests.get(f"{self.base_url}/health", timeout=1.5)
            r.raise_for_status()
            return r.json().get("status") == "ok"
        except Exception:
            return False

    def add(self, text: str, meta: Optional[Dict[str, Any]] = None) -> AnchorEntry:
        payload = {"text": text, "meta": meta or {}}
        r = requests.post(f"{self.base_url}/entries", json=payload, timeout=3.0)
        r.raise_for_status()
        return self._entry_from_dict(r.json())

    def list(self, limit: int = 20) -> List[AnchorEntry]:
        r = requests.get(
            f"{self.base_url}/entries",
            params={"limit": limit},
            timeout=3.0,
        )
        r.raise_for_status()
        data = r.json()
        return [self._entry_from_dict(e) for e in data]

    def verify(self, text: str, at: Optional[str] = None) -> List[AnchorEntry]:
        payload: Dict[str, Any] = {"text": text}
        if at:
            payload["at"] = at
        r = requests.post(f"{self.base_url}/verify", json=payload, timeout=3.0)
        r.raise_for_status()
        return [self._entry_from_dict(e) for e in r.json()]
