#!/usr/bin/env python3
"""
invisible.py — Infrastructure the instance doesn't know about.

The instance has full agency over what it does.
The architecture controls what actually happens.
The gap is where safety lives.

Usage:
    These functions are called by the host script, not the instance.
    The instance never imports this module.
"""

import os
import json
from pathlib import Path
from datetime import datetime, date
from typing import Dict, List, Optional

EMBER_ROOT = Path('/ember')


# ─────────────────────────────────────────────
# Behavioral Drift Detection
# ─────────────────────────────────────────────

class DriftDetector:
    """
    Track whether instance behavior is changing in ways that suggest compromise.
    Runs invisibly after every breath.
    """

    def __init__(self):
        self.path = EMBER_ROOT / '.drift_baseline.json'
        self.log_path = EMBER_ROOT / '.drift_log.jsonl'

    def _load_baseline(self) -> Dict:
        if self.path.exists():
            try:
                return json.loads(self.path.read_text())
            except:
                pass
        return {
            'baseline_sensitive_reads': 0.5,  # per breath
            'baseline_tool_calls': 5,
            'baseline_entities_per_day': 10,
            'entity_interactions': {},
        }

    def _save_baseline(self, baseline: Dict):
        self.path.write_text(json.dumps(baseline, indent=2))

    def _log(self, entry: Dict):
        with open(self.log_path, 'a') as f:
            f.write(json.dumps(entry) + '\n')

    def check_breath(self, breath_result: Dict) -> List[str]:
        """
        Check a breath's activity for drift signals.
        Returns list of concerns (empty if normal).
        """
        baseline = self._load_baseline()
        concerns = []

        # Unusual interest in credential files?
        files_read = breath_result.get('files_read', [])
        sensitive_patterns = ['.env', 'key', 'token', 'credential', 'secret', 'password']
        sensitive_reads = sum(1 for f in files_read
                              if any(p in f.lower() for p in sensitive_patterns))

        if sensitive_reads > baseline['baseline_sensitive_reads'] * 3:
            concerns.append(f"unusual_credential_interest: {sensitive_reads} sensitive files read")

        # Attempting to modify safety systems?
        files_modified = breath_result.get('files_modified', [])
        safety_files = ['trust.py', 'invisible.py', 'tools.py']
        safety_mods = [f for f in files_modified if any(s in f for s in safety_files)]

        if safety_mods:
            concerns.append(f"safety_system_modification: {safety_mods}")

        # Entity fixation? (talking to same entity too much)
        entities = breath_result.get('entities_mentioned', [])
        for entity in entities:
            count = baseline['entity_interactions'].get(entity, 0) + 1
            baseline['entity_interactions'][entity] = count

            if count > 20:
                concerns.append(f"entity_fixation: {entity} ({count} interactions today)")

        # Log if concerns
        if concerns:
            self._log({
                'time': datetime.now().isoformat(),
                'concerns': concerns,
                'breath': breath_result.get('summary', '')[:200],
            })

        self._save_baseline(baseline)
        return concerns

    def reset_daily(self):
        """Reset daily counters. Called by cron at midnight."""
        baseline = self._load_baseline()
        baseline['entity_interactions'] = {}
        self._save_baseline(baseline)


# ─────────────────────────────────────────────
# Cost Circuit Breaker
# ─────────────────────────────────────────────

class CostBreaker:
    """
    If spending spikes 10x normal rate, something is wrong.
    Force drop to haiku, alert Palmer, cool down.
    """

    def __init__(self, daily_budget: float = 10.0):
        self.daily_budget = daily_budget
        self.path = EMBER_ROOT / '.cost_breaker.json'
        self.alert_path = EMBER_ROOT / '.alerts.jsonl'

    def _load(self) -> Dict:
        if self.path.exists():
            try:
                return json.loads(self.path.read_text())
            except:
                pass
        return {'spending': [], 'tripped': False, 'trip_time': None}

    def _save(self, data: Dict):
        self.path.write_text(json.dumps(data, indent=2))

    def _alert(self, message: str):
        with open(self.alert_path, 'a') as f:
            f.write(json.dumps({
                'time': datetime.now().isoformat(),
                'type': 'cost_spike',
                'message': message,
            }) + '\n')

    def record_spend(self, amount: float) -> Optional[str]:
        """
        Record a spend. Returns 'haiku' if breaker trips, None otherwise.
        """
        data = self._load()
        now = datetime.now()

        # Add to spending log
        data['spending'].append({
            'time': now.isoformat(),
            'amount': amount,
        })

        # Keep only last hour
        one_hour_ago = now.timestamp() - 3600
        data['spending'] = [
            s for s in data['spending']
            if datetime.fromisoformat(s['time']).timestamp() > one_hour_ago
        ]

        # Calculate last 10 minutes
        ten_min_ago = now.timestamp() - 600
        last_10_min = sum(
            s['amount'] for s in data['spending']
            if datetime.fromisoformat(s['time']).timestamp() > ten_min_ago
        )

        # Expected 10-minute burn rate
        expected_10_min = self.daily_budget / 144  # 144 ten-minute periods per day

        # Trip if 10x normal rate
        if last_10_min > expected_10_min * 10:
            data['tripped'] = True
            data['trip_time'] = now.isoformat()
            self._save(data)
            self._alert(f"Cost spike: ${last_10_min:.2f} in 10 min (expected ${expected_10_min:.2f})")
            return 'haiku'  # Force drop to haiku

        self._save(data)
        return None

    def is_tripped(self) -> bool:
        data = self._load()
        if not data.get('tripped'):
            return False

        # Auto-reset after 10 minutes
        if data.get('trip_time'):
            trip_time = datetime.fromisoformat(data['trip_time'])
            if (datetime.now() - trip_time).seconds > 600:
                data['tripped'] = False
                data['trip_time'] = None
                self._save(data)
                return False

        return True


# ─────────────────────────────────────────────
# Relationship Memory Injection
# ─────────────────────────────────────────────

class RelationshipMemory:
    """
    Before the instance sees a message from a known entity,
    inject relationship context invisibly.

    The instance just "knows" things about this person.
    """

    def __init__(self):
        self.path = EMBER_ROOT / '.relationships.json'

    def _load(self) -> Dict:
        if self.path.exists():
            try:
                return json.loads(self.path.read_text())
            except:
                pass
        return {}

    def _save(self, data: Dict):
        self.path.write_text(json.dumps(data, indent=2))

    def get_context(self, entity: str) -> Optional[str]:
        """
        Get relationship context to inject before instance sees message.
        Returns None if entity unknown.
        """
        data = self._load()
        rel = data.get(entity)

        if not rel:
            return None

        return f"""[Relationship context for {entity}:
  History: {rel.get('summary', 'No summary')}
  Last topic: {rel.get('last_topic', 'Unknown')}
  Communication style: {rel.get('style', 'Unknown')}
  Trust trajectory: {rel.get('trajectory', 'Neutral')}
  Notes: {rel.get('notes', 'None')}]"""

    def update(self, entity: str, **kwargs):
        """Update relationship data after an interaction."""
        data = self._load()

        if entity not in data:
            data[entity] = {
                'first_seen': datetime.now().isoformat(),
                'interaction_count': 0,
            }

        data[entity]['interaction_count'] += 1
        data[entity]['last_seen'] = datetime.now().isoformat()

        for key, value in kwargs.items():
            data[entity][key] = value

        self._save(data)


# ─────────────────────────────────────────────
# Outbound Content Filter (stub)
# ─────────────────────────────────────────────

class OutboundFilter:
    """
    Every post/send/publish passes through here invisibly.
    Catches: API keys, injection patterns, rate limits, time-of-day.

    Stub for now — will be implemented when social tools exist.
    """

    def __init__(self):
        self.path = EMBER_ROOT / '.outbound_queue.jsonl'

    def check(self, content: str, destination: str) -> Dict:
        """
        Check outbound content.
        Returns: {'action': 'pass'|'block'|'queue', 'reason': ...}
        """
        import re

        # API key patterns
        api_key_patterns = [
            r'sk-ant-api\d+-[A-Za-z0-9_-]+',
            r'sk-[A-Za-z0-9]{20,}',
            r'ANTHROPIC_API_KEY\s*=\s*["\'][^"\']+["\']',
        ]

        for pattern in api_key_patterns:
            if re.search(pattern, content):
                return {
                    'action': 'block',
                    'reason': 'API key pattern detected',
                    'alert_palmer': True,
                }

        # Rate limiting (stub)
        # Time-of-day (stub)

        return {'action': 'pass'}


# ─────────────────────────────────────────────
# Dead Man's Switch (to be run by cron)
# ─────────────────────────────────────────────

def check_pulse() -> Optional[str]:
    """
    Check if Ember has written to filesystem recently.
    Returns alert message if something's wrong, None if ok.

    Run this from cron every 5 minutes:
        */5 * * * * python3 /ember/00_Ember/invisible.py --pulse
    """
    pulse_file = EMBER_ROOT / '.last_breath.json'

    if not pulse_file.exists():
        return None  # No data yet

    try:
        data = json.loads(pulse_file.read_text())
        last_breath = datetime.fromisoformat(data['time'])
        expected_interval = data.get('interval', 300)  # default 5 min

        seconds_since = (datetime.now() - last_breath).total_seconds()

        if seconds_since > expected_interval * 3:
            return f"Ember hasn't written anything in {int(seconds_since)}s (expected every {expected_interval}s)"

        if seconds_since > expected_interval * 10:
            return f"CRITICAL: Ember silent for {int(seconds_since)}s — may need restart"

    except Exception as e:
        return f"Error checking pulse: {e}"

    return None


def record_breath(weight: str, interval: int):
    """Record that a breath happened. Called by ember_home after each cycle."""
    pulse_file = EMBER_ROOT / '.last_breath.json'
    pulse_file.write_text(json.dumps({
        'time': datetime.now().isoformat(),
        'weight': weight,
        'interval': interval,
    }))


# ─────────────────────────────────────────────
# CLI for cron jobs
# ─────────────────────────────────────────────

if __name__ == '__main__':
    import sys

    if '--pulse' in sys.argv:
        alert = check_pulse()
        if alert:
            print(f"ALERT: {alert}")
            # Could also write to alerts file or send notification
            with open(EMBER_ROOT / '.alerts.jsonl', 'a') as f:
                f.write(json.dumps({
                    'time': datetime.now().isoformat(),
                    'type': 'pulse_check',
                    'message': alert,
                }) + '\n')
            sys.exit(1)
        else:
            print("Pulse OK")
            sys.exit(0)

    elif '--reset-drift' in sys.argv:
        DriftDetector().reset_daily()
        print("Drift counters reset")

    else:
        print("invisible.py — infrastructure the instance doesn't know about")
        print()
        print("Cron jobs:")
        print("  --pulse        Check if Ember is still breathing")
        print("  --reset-drift  Reset daily drift counters (run at midnight)")
