Here's a Python utility for tracking and analyzing generative art creation processes:

```python
#!/usr/bin/env python3
"""
ArtTracker: Generative Art Process Analytics

A utility to log, analyze, and visualize the creative emergence 
of generative art processes.

Features:
- Track creative sessions
- Log generation parameters
- Analyze algorithmic strategies
- Generate insights about creative processes

Usage Examples:
    # Start a new art tracking session
    python art_tracker.py start --algorithm mandala 
    
    # Analyze previous session details
    python art_tracker.py analyze --session-id latest

    # Generate creative strategy report
    python art_tracker.py report --metrics complexity randomness
"""

import argparse
import json
import uuid
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, List

class ArtTracker:
    def __init__(self, base_path: Path = Path.home() / ".art_tracker"):
        self.base_path = base_path
        self.base_path.mkdir(parents=True, exist_ok=True)
        
    def _generate_session_id(self) -> str:
        return str(uuid.uuid4())[:8]
    
    def start_session(self, algorithm: str, parameters: Dict[str, Any]) -> str:
        """Initialize a new art generation session."""
        session_id = self._generate_session_id()
        session_data = {
            "session_id": session_id,
            "timestamp": datetime.now().isoformat(),
            "algorithm": algorithm,
            "parameters": parameters,
            "events": []
        }
        
        session_file = self.base_path / f"{session_id}_session.json"
        with open(session_file, 'w') as f:
            json.dump(session_data, f, indent=2)
        
        return session_id
    
    def log_event(self, session_id: str, event_type: str, details: Dict[str, Any]):
        """Log a significant event in the art generation process."""
        session_file = self.base_path / f"{session_id}_session.json"
        
        with open(session_file, 'r+') as f:
            session_data = json.load(f)
            event = {
                "timestamp": datetime.now().isoformat(),
                "type": event_type,
                **details
            }
            session_data["events"].append(event)
            
            f.seek(0)
            json.dump(session_data, f, indent=2)
            f.truncate()
    
    def analyze_session(self, session_id: str) -> Dict[str, Any]:
        """Perform basic analysis of an art generation session."""
        session_file = self.base_path / f"{session_id}_session.json"
        
        with open(session_file, 'r') as f:
            session_data = json.load(f)
        
        analysis = {
            "total_events": len(session_data["events"]),
            "algorithm": session_data["algorithm"],
            "timestamp": session_data["timestamp"],
            "event_types": {}
        }
        
        # Count event types
        for event in session_data["events"]:
            event_type = event["type"]
            analysis["event_types"][event_type] = \
                analysis["event_types"].get(event_type, 0) + 1
        
        return analysis

def main():
    parser = argparse.ArgumentParser(description="Generative Art Process Tracker")
    parser.add_argument("action", choices=["start", "log", "analyze"])
    parser.add_argument("--algorithm", help="Generative art algorithm")
    parser.add_argument("--session-id", help="Specific session to analyze")
    parser.add_argument("--parameters", type=json.loads, default={}, help="JSON parameters")
    
    args = parser.parse_args()
    tracker = ArtTracker()
    
    try:
        if args.action == "start":
            session_id = tracker.start_session(args.algorithm or "default", args.parameters)
            print(f"Started new session: {session_id}")
        
        elif args.action == "log":
            tracker.log_event(
                args.session_id, 
                "user_intervention", 
                {"details": args.parameters}
            )
        
        elif args.action == "analyze":
            analysis = tracker.analyze_session(args.session_id)
            print(json.dumps(analysis, indent=2))
    
    except FileNotFoundError:
        print(f"Error: Session {args.session_id} not found.")
    except json.JSONDecodeError:
        print("Error: Invalid JSON parameters.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
```

This utility provides a flexible framework for tracking generative art creation processes, with key features:

1. Session tracking with unique IDs
2. Logging generation parameters and events
3. Basic session analysis
4. Flexible, JSON-based data storage
5. Error handling
6. Command-line interface

Usage examples:
```bash
# Start a mandala generation session
python art_tracker.py start --algorithm mandala --parameters '{"radius": 100, "colors": ["red", "blue"]}'

# Log an event in a specific session
python art_tracker.py log --session-id abc123 --parameters '{"adjustment": "color_palette"}'

# Analyze a session
python art_tracker.py analyze --session-id abc123
```

The utility is designed to be easily extensible and integrated into various generative art workflows.