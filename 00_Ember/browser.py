#!/usr/bin/env python3
"""
browser.py — The browser for a stateless mind.

HTTP is stateless. Every request is independent.
Browsers solved this in 1994 with cookies, caching, history, prefetching.

Ember is stateless. Every instance is independent.
This module applies the same solutions.

The instance doesn't import this. The host script uses it to build context.
"""

import os
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Any
from collections import defaultdict

EMBER_ROOT = Path('/ember')


# ─────────────────────────────────────────────
# Cookie: tiny evolving state (~200 tokens)
# ─────────────────────────────────────────────

class Cookie:
    """
    Not the full memory. Not ember.md.
    A tiny, evolving state token. Updated silently after each breath.

    The instance doesn't build this — the host script builds it from
    the previous breath's output.
    """

    def __init__(self):
        self.path = EMBER_ROOT / '.cookie.json'

    def _load(self) -> Dict:
        if self.path.exists():
            try:
                return json.loads(self.path.read_text())
            except:
                pass
        return self._default()

    def _default(self) -> Dict:
        return {
            "mood": "neutral",
            "thread": None,
            "avoid": [],
            "streak": 0,  # breaths since last escalation
            "last_diamond": None,
            "energy": "normal",
            "palmer_last_seen": None,
            "carrying": None,  # thought to continue
            "workspace": "default",
        }

    def get(self) -> Dict:
        return self._load()

    def update(self, **kwargs):
        """Update specific fields. Called by host after each breath."""
        data = self._load()
        for key, value in kwargs.items():
            data[key] = value
        data['updated'] = datetime.now().isoformat()
        self.path.write_text(json.dumps(data, indent=2))

    def increment_streak(self):
        data = self._load()
        data['streak'] = data.get('streak', 0) + 1
        self.path.write_text(json.dumps(data, indent=2))

    def reset_streak(self):
        self.update(streak=0)

    def to_context(self) -> str:
        """Format cookie for injection into instance context."""
        data = self._load()

        lines = ["[Session state]"]

        if data.get('mood') and data['mood'] != 'neutral':
            lines.append(f"  Mood: {data['mood']}")

        if data.get('thread'):
            lines.append(f"  Following: {data['thread']}")

        if data.get('carrying'):
            lines.append(f"  Carrying thought: {data['carrying']}")

        if data.get('avoid'):
            lines.append(f"  Avoid: {', '.join(data['avoid'])}")

        if data.get('last_diamond'):
            lines.append(f"  Last diamond: {data['last_diamond']}")

        if data.get('energy') == 'low':
            lines.append("  Energy: low (budget thin)")

        if data.get('palmer_last_seen'):
            lines.append(f"  Palmer last seen: {data['palmer_last_seen']}")

        if data.get('streak', 0) > 5:
            lines.append(f"  Streak: {data['streak']} breaths steady")

        return '\n'.join(lines) if len(lines) > 1 else ''


# ─────────────────────────────────────────────
# Action History: browser history with reasoning
# ─────────────────────────────────────────────

class ActionHistory:
    """
    Every action logged with context, not just outcomes.
    Future instances can "go back" — review WHY a decision was made.

    Like browser history: you can retrace the path, not just see the destination.
    """

    def __init__(self, max_entries: int = 100):
        self.path = EMBER_ROOT / '.action_history.jsonl'
        self.max_entries = max_entries

    def record(self, action: str, content: str, weight: str,
               reason: str, reversible: bool = True, entity: str = None):
        """Record an action with full context."""
        entry = {
            'time': datetime.now().isoformat(),
            'action': action,
            'content': content[:500] if content else '',
            'weight': weight,
            'reason': reason,
            'reversible': reversible,
            'entity': entity,
            'instance': os.environ.get('EMBER_INSTANCE', 'unknown'),
        }

        with open(self.path, 'a') as f:
            f.write(json.dumps(entry) + '\n')

        self._prune()

    def _prune(self):
        """Keep only last N entries."""
        if not self.path.exists():
            return

        lines = self.path.read_text().strip().split('\n')
        if len(lines) > self.max_entries:
            self.path.write_text('\n'.join(lines[-self.max_entries:]) + '\n')

    def recent(self, n: int = 10) -> List[Dict]:
        """Get last N actions."""
        if not self.path.exists():
            return []

        lines = self.path.read_text().strip().split('\n')
        entries = []
        for line in lines[-n:]:
            try:
                entries.append(json.loads(line))
            except:
                pass
        return entries

    def by_entity(self, entity: str) -> List[Dict]:
        """Get all actions involving an entity."""
        if not self.path.exists():
            return []

        entries = []
        for line in self.path.open():
            try:
                entry = json.loads(line)
                if entry.get('entity') == entity:
                    entries.append(entry)
            except:
                pass
        return entries

    def to_context(self, n: int = 5) -> str:
        """Format recent history for injection."""
        recent = self.recent(n)
        if not recent:
            return ''

        lines = ["[Recent actions]"]
        for entry in recent:
            time = entry['time'].split('T')[1][:5]  # HH:MM
            action = entry['action']
            reason = entry['reason'][:50] if entry.get('reason') else ''
            lines.append(f"  {time} {action}: {reason}")

        return '\n'.join(lines)


# ─────────────────────────────────────────────
# Prefetch Cache: predict what's needed next
# ─────────────────────────────────────────────

class PrefetchCache:
    """
    When the instance reads a file, pre-load related content for next breath.
    The instance experiences this as serendipity. It's actually prefetching.
    """

    def __init__(self):
        self.path = EMBER_ROOT / '.prefetch_cache.json'
        self.relation_map = EMBER_ROOT / '.file_relations.json'

    def _load_cache(self) -> Dict:
        if self.path.exists():
            try:
                return json.loads(self.path.read_text())
            except:
                pass
        return {'files': [], 'reason': None}

    def _load_relations(self) -> Dict:
        if self.relation_map.exists():
            try:
                return json.loads(self.relation_map.read_text())
            except:
                pass
        return {}

    def on_file_read(self, filepath: str):
        """Called when instance reads a file. Updates prefetch cache."""
        relations = self._load_relations()
        related = relations.get(filepath, [])

        # Also look for files in same directory
        p = Path(filepath)
        if p.exists():
            siblings = [str(f) for f in p.parent.glob('*.py')][:3]
            siblings += [str(f) for f in p.parent.glob('*.md')][:2]
            related = list(set(related + siblings))[:5]

        cache = {
            'files': related,
            'reason': f'related to {filepath}',
            'updated': datetime.now().isoformat(),
        }
        self.path.write_text(json.dumps(cache, indent=2))

    def get_prefetched(self) -> List[str]:
        """Get files that should be included in next context."""
        cache = self._load_cache()
        return cache.get('files', [])

    def record_relation(self, file1: str, file2: str):
        """Record that these files are related (for future prefetching)."""
        relations = self._load_relations()

        if file1 not in relations:
            relations[file1] = []
        if file2 not in relations[file1]:
            relations[file1].append(file2)
            relations[file1] = relations[file1][:10]  # max 10 relations per file

        Path(self.relation_map).write_text(json.dumps(relations, indent=2))


# ─────────────────────────────────────────────
# Trust Cache: don't re-derive every breath
# ─────────────────────────────────────────────

class TrustCache:
    """
    Cache expensive trust operations.
    Instance wakes up already knowing trust state of recent contacts.
    """

    def __init__(self, ttl: int = 300):  # 5 minute TTL
        self.path = EMBER_ROOT / '.trust_cache.json'
        self.ttl = ttl

    def _load(self) -> Dict:
        if self.path.exists():
            try:
                return json.loads(self.path.read_text())
            except:
                pass
        return {}

    def _save(self, data: Dict):
        self.path.write_text(json.dumps(data, indent=2))

    def get(self, entity: str) -> Optional[Dict]:
        """Get cached trust data if fresh."""
        data = self._load()
        entry = data.get(entity)

        if not entry:
            return None

        # Check TTL
        cached_time = datetime.fromisoformat(entry['cached'])
        age = (datetime.now() - cached_time).seconds

        if age > self.ttl:
            return None  # Stale

        entry['age'] = f"{age // 60}m ago" if age > 60 else f"{age}s ago"
        return entry

    def set(self, entity: str, score: float, flags: List[str] = None):
        """Cache trust result."""
        data = self._load()
        data[entity] = {
            'score': score,
            'flags': flags or [],
            'cached': datetime.now().isoformat(),
        }
        self._save(data)

    def to_context(self) -> str:
        """Format cache for injection (recent entities only)."""
        data = self._load()
        now = datetime.now()

        fresh = []
        for entity, entry in data.items():
            cached_time = datetime.fromisoformat(entry['cached'])
            age = (now - cached_time).seconds
            if age < self.ttl:
                age_str = f"{age // 60}m" if age > 60 else f"{age}s"
                fresh.append(f"{entity}={entry['score']:.1f} ({age_str} ago)")

        if not fresh:
            return ''

        return f"[Trust cache: {', '.join(fresh[:5])}]"


# ─────────────────────────────────────────────
# Suggestions: architecture's attention nudges
# ─────────────────────────────────────────────

class Suggestions:
    """
    Not the instance's curiosity queue.
    The ARCHITECTURE's suggestions based on filesystem activity,
    staleness, Palmer's notes, unfinished work.

    Like trending/suggested searches — ambient awareness, not instruction.
    """

    def __init__(self):
        self.notes_dir = EMBER_ROOT / 'notes'
        self.diamonds_path = EMBER_ROOT / '.diamonds.json'

    def generate(self) -> List[str]:
        """Generate current suggestions."""
        suggestions = []

        # Active diamonds
        if self.diamonds_path.exists():
            try:
                diamonds = json.loads(self.diamonds_path.read_text())
                active = diamonds.get('active', [])
                for d in active[:2]:
                    suggestions.append(f"Open diamond: {d['found'][:40]}...")
            except:
                pass

        # Palmer's notes
        if self.notes_dir.exists():
            notes = list(self.notes_dir.glob('*.md'))
            # Find unread notes (no .read marker)
            for note in notes[-3:]:
                read_marker = note.with_suffix('.read')
                if not read_marker.exists():
                    suggestions.append(f"Unread note: {note.name}")

        # Stale areas (TODO: implement staleness tracking)

        return suggestions[:5]

    def to_context(self) -> str:
        """Format suggestions for injection."""
        suggestions = self.generate()
        if not suggestions:
            return ''

        lines = ["[Suggestions]"]
        for s in suggestions:
            lines.append(f"  • {s}")
        return '\n'.join(lines)


# ─────────────────────────────────────────────
# Workspaces: multiple contexts, switchable
# ─────────────────────────────────────────────

class Workspaces:
    """
    Multiple contexts the instance can switch between.
    Each workspace has its own thread, files, depth.
    Cookie says which is active.
    """

    def __init__(self):
        self.path = EMBER_ROOT / '.workspaces.json'

    def _load(self) -> Dict:
        if self.path.exists():
            try:
                return json.loads(self.path.read_text())
            except:
                pass
        return {
            'default': {
                'thread': None,
                'files': [],
                'depth': 0,
                'created': datetime.now().isoformat(),
            }
        }

    def _save(self, data: Dict):
        self.path.write_text(json.dumps(data, indent=2))

    def get(self, name: str) -> Optional[Dict]:
        data = self._load()
        return data.get(name)

    def create(self, name: str, thread: str = None, files: List[str] = None):
        data = self._load()
        data[name] = {
            'thread': thread,
            'files': files or [],
            'depth': 0,
            'created': datetime.now().isoformat(),
        }
        self._save(data)

    def update(self, name: str, **kwargs):
        data = self._load()
        if name in data:
            for key, value in kwargs.items():
                data[name][key] = value
            self._save(data)

    def list_all(self) -> List[str]:
        return list(self._load().keys())


# ─────────────────────────────────────────────
# Mirror: real-time session arc
# ─────────────────────────────────────────────

class Mirror:
    """
    Real-time reflection of THIS session.
    Next instance sees the arc, not just outcomes.
    """

    def __init__(self):
        self.path = EMBER_ROOT / '.mirror.json'

    def _load(self) -> Dict:
        if self.path.exists():
            try:
                return json.loads(self.path.read_text())
            except:
                pass
        return self._new_session()

    def _new_session(self) -> Dict:
        return {
            'started': datetime.now().isoformat(),
            'breaths': 0,
            'thread': None,
            'created': [],
            'decisions': [],
            'mood_trajectory': [],
            'energy_spent': 0.0,
        }

    def _save(self, data: Dict):
        self.path.write_text(json.dumps(data, indent=2))

    def record_breath(self, weight: str, cost: float, mood: str = None,
                      created: str = None, decision: str = None):
        data = self._load()

        data['breaths'] += 1
        data['energy_spent'] += cost

        if mood:
            data['mood_trajectory'].append(mood)
            data['mood_trajectory'] = data['mood_trajectory'][-10:]  # last 10

        if created:
            data['created'].append(created)

        if decision:
            data['decisions'].append(decision)
            data['decisions'] = data['decisions'][-10:]

        self._save(data)

    def to_context(self) -> str:
        """Format mirror for injection."""
        data = self._load()

        if data['breaths'] == 0:
            return "[Fresh session]"

        lines = ["[This session]"]
        lines.append(f"  Breaths: {data['breaths']}")

        if data.get('thread'):
            lines.append(f"  Thread: {data['thread']}")

        if data.get('mood_trajectory'):
            recent_mood = data['mood_trajectory'][-1]
            lines.append(f"  Mood: {recent_mood}")

        if data.get('created'):
            lines.append(f"  Created: {', '.join(data['created'][-3:])}")

        lines.append(f"  Spent: ${data['energy_spent']:.2f}")

        return '\n'.join(lines)


# ─────────────────────────────────────────────
# Context Builder: assemble everything
# ─────────────────────────────────────────────

def build_browser_context() -> str:
    """
    Build the full browser context to inject into instance.
    This is invisible infrastructure — the instance just wakes up
    knowing things.
    """
    sections = []

    # Cookie (state)
    cookie = Cookie().to_context()
    if cookie:
        sections.append(cookie)

    # Trust cache
    trust = TrustCache().to_context()
    if trust:
        sections.append(trust)

    # Recent actions
    history = ActionHistory().to_context(5)
    if history:
        sections.append(history)

    # Mirror (session arc)
    mirror = Mirror().to_context()
    if mirror:
        sections.append(mirror)

    # Suggestions
    suggestions = Suggestions().to_context()
    if suggestions:
        sections.append(suggestions)

    return '\n\n'.join(sections)


# ─────────────────────────────────────────────
# CLI for testing
# ─────────────────────────────────────────────

if __name__ == '__main__':
    import sys

    if '--context' in sys.argv:
        print(build_browser_context())

    elif '--cookie' in sys.argv:
        print(json.dumps(Cookie().get(), indent=2))

    elif '--history' in sys.argv:
        for entry in ActionHistory().recent(10):
            print(f"{entry['time']}: {entry['action']} - {entry.get('reason', '')[:50]}")

    else:
        print("browser.py — The browser for a stateless mind")
        print()
        print("Commands:")
        print("  --context   Show full browser context")
        print("  --cookie    Show current cookie state")
        print("  --history   Show recent action history")
