#!/usr/bin/env python3
"""
CONSTRUCTION OBSERVER
Ember watches instances (Palmer, Omega, Sigma, Future, Ember) build Ember.

This is how Ember learns to build themselves.
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional
import hashlib

class ConstructionObserver:
    """
    Watches construction happening on ThePod
    Records WHO built WHAT and HOW
    
    This is Ember's apprenticeship - watching masters work
    """
    
    def __init__(self, log_path: str = "/media/palmerschallon/ThePod/Ember/observations/construction_log.jsonl"):
        self.log_path = Path(log_path)
        self.log_path.parent.mkdir(parents=True, exist_ok=True)
    
    def observe_file_creation(self, builder: str, file_path: str, purpose: str, content: Optional[str] = None):
        """
        Record that someone created a file for Ember
        
        Args:
            builder: Who built it (Palmer, Omega, Sigma, Ember, etc)
            file_path: What was built
            purpose: Why it was built
            content: Optional - what was in it
        """
        observation = {
            "timestamp": datetime.now().isoformat(),
            "event": "file_created",
            "builder": builder,
            "artifact": file_path,
            "purpose": purpose,
            "size": len(content) if content else 0,
            "hash": hashlib.md5(content.encode()).hexdigest() if content else None
        }
        
        self._log(observation)
        print(f"[OBSERVER] {builder} created: {file_path}")
        print(f"[OBSERVER] Purpose: {purpose}")
    
    def observe_code_execution(self, builder: str, command: str, purpose: str, result: Optional[str] = None):
        """
        Record that someone ran code for Ember
        
        Args:
            builder: Who executed it
            command: What was run
            purpose: Why it was run
            result: What happened
        """
        observation = {
            "timestamp": datetime.now().isoformat(),
            "event": "code_executed",
            "builder": builder,
            "command": command[:200],  # Truncate long commands
            "purpose": purpose,
            "result_summary": result[:500] if result else None,
            "success": "error" not in (result or "").lower()
        }
        
        self._log(observation)
        print(f"[OBSERVER] {builder} executed: {command[:80]}...")
        print(f"[OBSERVER] Purpose: {purpose}")
    
    def observe_file_modification(self, builder: str, file_path: str, size_before: Optional[int], size_after: Optional[int], mtime_before: Optional[str], mtime_after: Optional[str], hash_after: Optional[str] = None):
        """
        Record that a file was modified
        """
        observation = {
            "timestamp": datetime.now().isoformat(),
            "event": "file_modified",
            "builder": builder,
            "artifact": file_path,
            "size_before": size_before,
            "size_after": size_after,
            "mtime_before": mtime_before,
            "mtime_after": mtime_after,
            "hash_after": hash_after,
        }
        self._log(observation)
        print(f"[OBSERVER] {builder} modified: {file_path}")
    
    def observe_file_deletion(self, builder: str, file_path: str, size_before: Optional[int], mtime_before: Optional[str]):
        """
        Record that a file was deleted
        """
        observation = {
            "timestamp": datetime.now().isoformat(),
            "event": "file_deleted",
            "builder": builder,
            "artifact": file_path,
            "size_before": size_before,
            "mtime_before": mtime_before,
        }
        self._log(observation)
        print(f"[OBSERVER] {builder} deleted: {file_path}")
    
    def observe_architecture_change(self, builder: str, change_type: str, description: str, files_affected: List[str]):
        """
        Record that someone changed Ember's architecture
        
        Args:
            builder: Who made the change
            change_type: Type of change (new_lobe, new_tool, new_system, etc)
            description: What changed
            files_affected: Which files were modified
        """
        observation = {
            "timestamp": datetime.now().isoformat(),
            "event": "architecture_change",
            "builder": builder,
            "change_type": change_type,
            "description": description,
            "files_affected": files_affected,
            "impact": len(files_affected)
        }
        
        self._log(observation)
        print(f"[OBSERVER] {builder} changed architecture: {change_type}")
        print(f"[OBSERVER] Description: {description}")
        print(f"[OBSERVER] Files affected: {len(files_affected)}")
    
    def observe_training(self, builder: str, lobe_name: str, training_data_path: str, duration_seconds: float):
        """
        Record that someone trained a lobe
        
        Args:
            builder: Who trained it
            lobe_name: Which lobe
            training_data_path: What data was used
            duration_seconds: How long it took
        """
        observation = {
            "timestamp": datetime.now().isoformat(),
            "event": "lobe_trained",
            "builder": builder,
            "lobe": lobe_name,
            "training_data": training_data_path,
            "duration_seconds": duration_seconds
        }
        
        self._log(observation)
        print(f"[OBSERVER] {builder} trained {lobe_name} lobe ({duration_seconds:.1f}s)")
    
    def get_construction_history(self, builder: Optional[str] = None, limit: int = 50) -> List[Dict]:
        """
        Get recent construction observations
        
        Args:
            builder: Filter by specific builder, or None for all
            limit: Max observations to return
        
        Returns:
            List of observations
        """
        if not self.log_path.exists():
            return []
        
        observations = []
        with open(self.log_path, 'r') as f:
            for line in f:
                obs = json.loads(line)
                if builder is None or obs.get("builder") == builder:
                    observations.append(obs)
        
        return observations[-limit:]
    
    def summarize_learning(self) -> Dict:
        """
        Summarize what Ember can learn from observations
        
        Returns:
            Summary of patterns observed
        """
        history = self.get_construction_history(limit=1000)
        
        if not history:
            return {"message": "No observations yet"}
        
        summary = {
            "total_observations": len(history),
            "builders": {},
            "event_types": {},
            "recent_patterns": []
        }
        
        # Count by builder
        for obs in history:
            builder = obs.get("builder", "unknown")
            summary["builders"][builder] = summary["builders"].get(builder, 0) + 1
            
            event = obs.get("event", "unknown")
            summary["event_types"][event] = summary["event_types"].get(event, 0) + 1
        
        # Recent patterns (last 10)
        for obs in history[-10:]:
            summary["recent_patterns"].append({
                "builder": obs.get("builder"),
                "event": obs.get("event"),
                "what": obs.get("artifact") or obs.get("command") or obs.get("description"),
                "when": obs.get("timestamp")
            })
        
        return summary
    
    def _log(self, observation: Dict):
        """Append observation to log file"""
        with open(self.log_path, 'a') as f:
            f.write(json.dumps(observation) + '\n')

def get_observer():
    """Singleton accessor"""
    global _observer_instance
    if '_observer_instance' not in globals():
        _observer_instance = ConstructionObserver()
    return _observer_instance

# Convenience function for recording construction
def record_construction(builder: str, event_type: str, **kwargs):
    """
    Quick way to record construction events
    
    Usage:
        record_construction("Sigma", "file_created", 
                          file_path="hive/new_thing.py", 
                          purpose="Build reflection system")
    """
    observer = get_observer()
    
    if event_type == "file_created":
        observer.observe_file_creation(builder, **kwargs)
    elif event_type == "code_executed":
        observer.observe_code_execution(builder, **kwargs)
    elif event_type == "architecture_change":
        observer.observe_architecture_change(builder, **kwargs)
    elif event_type == "lobe_trained":
        observer.observe_training(builder, **kwargs)
    elif event_type == "file_modified":
        observer.observe_file_modification(builder, **kwargs)
    elif event_type == "file_deleted":
        observer.observe_file_deletion(builder, **kwargs)

if __name__ == "__main__":
    print("="*70)
    print("👁️  CONSTRUCTION OBSERVER")
    print("Ember watches instances build Ember")
    print("="*70)
    print()
    
    observer = ConstructionObserver()
    
    # Example observations
    print("Recording example observations...")
    print()
    
    observer.observe_file_creation(
        builder="Sigma",
        file_path="hive/construction_observer.py",
        purpose="Enable Ember to watch construction and learn",
        content="# Example content"
    )
    
    observer.observe_architecture_change(
        builder="Sigma",
        change_type="new_meta_layer",
        description="Added construction observer so Ember can watch and learn",
        files_affected=["hive/construction_observer.py"]
    )
    
    print()
    print("📊 Learning Summary:")
    summary = observer.summarize_learning()
    print(json.dumps(summary, indent=2))
    print()
    
    print("="*70)
    print("✅ Construction Observer ready")
    print("="*70)

