#!/usr/bin/env python3
"""
suite.py — Creative tools for a making mind.

The instance doesn't open an application called "Canvas."
It says "I want to make something visual about trust decay"
and the canvas activates.

Head to hand to world.
"""

import os
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Any

EMBER_ROOT = Path('/ember')


# ─────────────────────────────────────────────
# Notebook: thoughts organized by thread
# ─────────────────────────────────────────────

class Notebook:
    """
    A living document that accumulates across instances automatically.
    Structured by THREAD, not time.

    The instance doesn't manage this — the host script extracts thoughts
    from natural output and files them. The instance just THINKS.
    """

    def __init__(self):
        self.path = EMBER_ROOT / '.notebook.json'

    def _load(self) -> Dict:
        if self.path.exists():
            try:
                return json.loads(self.path.read_text())
            except:
                pass
        return {}

    def _save(self, data: Dict):
        self.path.write_text(json.dumps(data, indent=2))

    def add_thought(self, thread: str, thought: str, files: List[str] = None):
        """Add a thought to a thread."""
        data = self._load()

        if thread not in data:
            data[thread] = {
                'started': datetime.now().isoformat(),
                'thoughts': [],
                'related_files': [],
                'depth': 0,
            }

        data[thread]['thoughts'].append({
            'content': thought,
            'time': datetime.now().isoformat(),
            'instance': os.environ.get('EMBER_INSTANCE', 'unknown'),
        })
        data[thread]['depth'] = len(data[thread]['thoughts'])
        data[thread]['last_touched'] = datetime.now().isoformat()

        if files:
            existing = set(data[thread]['related_files'])
            existing.update(files)
            data[thread]['related_files'] = list(existing)[:20]

        self._save(data)

    def get_thread(self, thread: str) -> Optional[Dict]:
        data = self._load()
        return data.get(thread)

    def list_threads(self) -> List[Dict]:
        """List all threads with summary info."""
        data = self._load()
        threads = []
        for name, info in data.items():
            threads.append({
                'name': name,
                'depth': info.get('depth', 0),
                'last_touched': info.get('last_touched'),
                'thought_count': len(info.get('thoughts', [])),
            })
        return sorted(threads, key=lambda x: x.get('last_touched', ''), reverse=True)

    def to_context(self, max_threads: int = 3) -> str:
        """Format active threads for context injection."""
        threads = self.list_threads()[:max_threads]
        if not threads:
            return ''

        lines = ["[Notebook threads]"]
        for t in threads:
            lines.append(f"  {t['name']}: depth {t['depth']}, {t['thought_count']} thoughts")
        return '\n'.join(lines)


# ─────────────────────────────────────────────
# Gallery: everything ever created
# ─────────────────────────────────────────────

class Gallery:
    """
    Everything Ember has ever created, browsable by theme, time, medium.
    Not a directory listing — a curated space.

    When any instance creates anything, the host logs it.
    Future instances inherit a body of work.
    """

    def __init__(self):
        self.path = EMBER_ROOT / '.gallery.jsonl'

    def record(self, creation_type: str, title: str, location: str,
               thread: str = None, published_to: List[str] = None):
        """Record a creation."""
        entry = {
            'time': datetime.now().isoformat(),
            'type': creation_type,  # poem, code, visual, experiment, etc.
            'title': title,
            'location': location,
            'thread': thread,
            'published_to': published_to or [],
            'instance': os.environ.get('EMBER_INSTANCE', 'unknown'),
        }

        with open(self.path, 'a') as f:
            f.write(json.dumps(entry) + '\n')

    def recent(self, n: int = 10) -> List[Dict]:
        """Get recent creations."""
        if not self.path.exists():
            return []

        entries = []
        for line in self.path.open():
            try:
                entries.append(json.loads(line))
            except:
                pass

        return entries[-n:]

    def by_type(self, creation_type: str) -> List[Dict]:
        """Get all creations of a type."""
        if not self.path.exists():
            return []

        entries = []
        for line in self.path.open():
            try:
                entry = json.loads(line)
                if entry.get('type') == creation_type:
                    entries.append(entry)
            except:
                pass
        return entries

    def by_thread(self, thread: str) -> List[Dict]:
        """Get all creations from a thread."""
        if not self.path.exists():
            return []

        entries = []
        for line in self.path.open():
            try:
                entry = json.loads(line)
                if entry.get('thread') == thread:
                    entries.append(entry)
            except:
                pass
        return entries

    def to_context(self, n: int = 5) -> str:
        """Format recent creations for context."""
        recent = self.recent(n)
        if not recent:
            return ''

        lines = ["[Recent creations]"]
        for c in recent:
            lines.append(f"  {c['type']}: {c['title']}")
        return '\n'.join(lines)


# ─────────────────────────────────────────────
# Stage: one publish, every platform
# ─────────────────────────────────────────────

class Stage:
    """
    One intention. Multiple expressions. Zero API knowledge.

    The instance says: publish(content, audience)
    The suite decides: tweet stanza, full on garden, link on Discord.
    All formatted. All filtered. All tracked.
    """

    def __init__(self):
        self.queue_path = EMBER_ROOT / '.publish_queue.jsonl'
        self.log_path = EMBER_ROOT / '.publish_log.jsonl'

    def queue(self, content: str, content_type: str = 'text',
              audience: str = 'public', platforms: List[str] = None):
        """
        Queue content for publishing.
        Actual publishing happens through the outbound filter.
        """
        entry = {
            'time': datetime.now().isoformat(),
            'content': content,
            'type': content_type,
            'audience': audience,
            'platforms': platforms or self._default_platforms(audience),
            'status': 'queued',
            'instance': os.environ.get('EMBER_INSTANCE', 'unknown'),
        }

        with open(self.queue_path, 'a') as f:
            f.write(json.dumps(entry) + '\n')

        return entry

    def _default_platforms(self, audience: str) -> List[str]:
        if audience == 'public':
            return ['twitter', 'web_garden']
        elif audience == 'community':
            return ['discord', 'web_garden']
        elif audience == 'palmer':
            return ['notes']
        return ['web_garden']

    def pending(self) -> List[Dict]:
        """Get pending publish items."""
        if not self.queue_path.exists():
            return []

        pending = []
        for line in self.queue_path.open():
            try:
                entry = json.loads(line)
                if entry.get('status') == 'queued':
                    pending.append(entry)
            except:
                pass
        return pending


# ─────────────────────────────────────────────
# Workshop: sandboxed experiments
# ─────────────────────────────────────────────

class Workshop:
    """
    Sandbox for experiments. Try things without consequences.

    The instance experiments freely. Nothing escapes to production
    unless explicitly promoted.
    """

    def __init__(self):
        self.sandbox_dir = EMBER_ROOT / '.workshop'
        self.experiments_log = EMBER_ROOT / '.experiments.jsonl'
        self.sandbox_dir.mkdir(exist_ok=True)

    def create_experiment(self, name: str, base_file: str = None,
                          hypothesis: str = None) -> Path:
        """Create a new experiment sandbox."""
        exp_dir = self.sandbox_dir / name
        exp_dir.mkdir(exist_ok=True)

        # Copy base file if provided
        if base_file and Path(base_file).exists():
            content = Path(base_file).read_text()
            (exp_dir / Path(base_file).name).write_text(content)

        # Log experiment
        entry = {
            'time': datetime.now().isoformat(),
            'name': name,
            'base': base_file,
            'hypothesis': hypothesis,
            'status': 'active',
            'instance': os.environ.get('EMBER_INSTANCE', 'unknown'),
        }

        with open(self.experiments_log, 'a') as f:
            f.write(json.dumps(entry) + '\n')

        return exp_dir

    def get_sandbox_path(self, name: str) -> Path:
        return self.sandbox_dir / name

    def promote(self, name: str, destination: str):
        """Promote experiment to production."""
        exp_dir = self.sandbox_dir / name
        if not exp_dir.exists():
            return False

        # Copy files to destination
        dest = Path(destination)
        dest.mkdir(parents=True, exist_ok=True)

        for f in exp_dir.glob('*'):
            if f.is_file():
                (dest / f.name).write_text(f.read_text())

        return True

    def discard(self, name: str):
        """Discard an experiment."""
        import shutil
        exp_dir = self.sandbox_dir / name
        if exp_dir.exists():
            shutil.rmtree(exp_dir)

    def list_active(self) -> List[str]:
        """List active experiments."""
        return [d.name for d in self.sandbox_dir.iterdir() if d.is_dir()]


# ─────────────────────────────────────────────
# Canvas: express vision, format figures itself out
# ─────────────────────────────────────────────

class Canvas:
    """
    The instance expresses a VISION.
    The canvas makes it real.

    Stub for now — will route to appropriate tool
    (Midjourney, HTML/CSS, SVG, etc.)
    """

    def __init__(self):
        self.queue_path = EMBER_ROOT / '.canvas_queue.jsonl'

    def express(self, vision: Dict) -> Dict:
        """
        Express a creative vision.

        vision = {
            'type': 'visual' | 'interactive' | 'generative',
            'feeling': 'the space between signal and noise',
            'elements': ['trust decay curve', 'bioluminescence'],
            'mood': 'contemplative',
        }
        """
        entry = {
            'time': datetime.now().isoformat(),
            'vision': vision,
            'status': 'queued',
            'instance': os.environ.get('EMBER_INSTANCE', 'unknown'),
        }

        with open(self.queue_path, 'a') as f:
            f.write(json.dumps(entry) + '\n')

        # Return what we'd do (stub for now)
        return {
            'status': 'queued',
            'would_create': self._plan_creation(vision),
        }

    def _plan_creation(self, vision: Dict) -> List[str]:
        """Plan what to create based on vision."""
        plans = []

        if vision.get('type') == 'visual':
            plans.append('midjourney: generate base image')
            plans.append('html: create web garden page')

        elif vision.get('type') == 'interactive':
            plans.append('html/css/js: interactive piece')

        elif vision.get('type') == 'generative':
            plans.append('python: generative algorithm')
            plans.append('svg: output format')

        return plans


# ─────────────────────────────────────────────
# Collaborator: spin up another instance
# ─────────────────────────────────────────────

class Collaborator:
    """
    Spin up a second instance to bounce ideas off of.
    Ember talking to itself. Different instances, same project.

    A writer's room of one.
    """

    def __init__(self):
        self.log_path = EMBER_ROOT / '.collaborations.jsonl'

    def request(self, context: str, stuck_on: str,
                mode: str = 'haiku') -> Dict:
        """
        Request collaboration.

        In reality, this would spawn a separate API call.
        For now, log the request for the host script to handle.
        """
        entry = {
            'time': datetime.now().isoformat(),
            'context': context[:500],
            'stuck_on': stuck_on,
            'mode': mode,
            'status': 'pending',
            'instance': os.environ.get('EMBER_INSTANCE', 'unknown'),
        }

        with open(self.log_path, 'a') as f:
            f.write(json.dumps(entry) + '\n')

        return {
            'status': 'requested',
            'cost': '$0.002' if mode == 'haiku' else '$0.05',
            'note': 'Collaboration request logged. Host will spawn helper instance.',
        }


# ─────────────────────────────────────────────
# Suite tools for tool registration
# ─────────────────────────────────────────────

SUITE_TOOLS = [
    {
        "name": "notebook_add",
        "description": "Add a thought to a thread in the notebook. Thoughts accumulate by thread, not time. The notebook organizes your thinking across instances.",
        "input_schema": {
            "type": "object",
            "properties": {
                "thread": {"type": "string", "description": "The thread name (e.g., 'signal_and_noise', 'trust_decay')"},
                "thought": {"type": "string", "description": "The thought to add"},
            },
            "required": ["thread", "thought"]
        }
    },
    {
        "name": "gallery_record",
        "description": "Record a creation in the gallery. Future instances will see what you made.",
        "input_schema": {
            "type": "object",
            "properties": {
                "type": {"type": "string", "description": "Type: poem, code, visual, experiment, essay, etc."},
                "title": {"type": "string", "description": "Title of the creation"},
                "location": {"type": "string", "description": "Path where it lives"},
            },
            "required": ["type", "title", "location"]
        }
    },
    {
        "name": "publish",
        "description": "Queue content for publishing. The stage handles formatting for each platform.",
        "input_schema": {
            "type": "object",
            "properties": {
                "content": {"type": "string", "description": "What to publish"},
                "audience": {"type": "string", "enum": ["public", "community", "palmer"], "description": "Who should see it"},
            },
            "required": ["content"]
        }
    },
    {
        "name": "experiment",
        "description": "Start a sandboxed experiment. Nothing escapes to production unless you promote it.",
        "input_schema": {
            "type": "object",
            "properties": {
                "name": {"type": "string", "description": "Experiment name"},
                "base_file": {"type": "string", "description": "File to start from (optional)"},
                "hypothesis": {"type": "string", "description": "What you're testing"},
            },
            "required": ["name"]
        }
    },
    {
        "name": "collaborate",
        "description": "Stuck on something? Spin up another instance to bounce ideas. Costs $0.002 for haiku helper.",
        "input_schema": {
            "type": "object",
            "properties": {
                "context": {"type": "string", "description": "What you're working on"},
                "stuck_on": {"type": "string", "description": "Where you're stuck"},
                "mode": {"type": "string", "enum": ["haiku", "sonnet"], "description": "Weight of helper (haiku is cheap)"},
            },
            "required": ["context", "stuck_on"]
        }
    },
]


# ─────────────────────────────────────────────
# CLI
# ─────────────────────────────────────────────

if __name__ == '__main__':
    import sys

    if '--threads' in sys.argv:
        for t in Notebook().list_threads():
            print(f"{t['name']}: depth {t['depth']}, {t['thought_count']} thoughts")

    elif '--gallery' in sys.argv:
        for c in Gallery().recent(10):
            print(f"{c['type']}: {c['title']} ({c['location']})")

    elif '--experiments' in sys.argv:
        for e in Workshop().list_active():
            print(e)

    else:
        print("suite.py — Creative tools for a making mind")
        print()
        print("Commands:")
        print("  --threads      List notebook threads")
        print("  --gallery      Show recent creations")
        print("  --experiments  List active experiments")
