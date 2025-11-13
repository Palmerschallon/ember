from __future__ import annotations
from typing import Any, Dict, List

from anchor_client import AnchorClient, AnchorEntry


class EmberMemory:
    """
    Thin adapter for Ember (or any agent) to use Anchor as a memory spine.
    """

    def __init__(self, client: AnchorClient | None = None) -> None:
        self.client = client or AnchorClient()

    def is_available(self) -> bool:
        return self.client.health()

    def remember(
        self,
        text: str,
        project: str | None = None,
        kind: str = "note",
        importance: float | None = None,
        extra_meta: Dict[str, Any] | None = None,
    ) -> AnchorEntry:
        meta: Dict[str, Any] = {
            "type": kind,
        }
        if project:
            meta["project"] = project
        if importance is not None:
            meta["importance"] = importance
        if extra_meta:
            meta.update(extra_meta)

        return self.client.add(text, meta)

    def recent(self, limit: int = 20) -> List[AnchorEntry]:
        return self.client.list(limit=limit)

    def find_exact(self, text: str) -> List[AnchorEntry]:
        return self.client.verify(text)
