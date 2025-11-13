#!/usr/bin/env python3
"""
EMBER STATUS - Self-awareness and system monitoring

Tracks:
- What Ember is doing right now
- Resource usage (GPU, RAM, disk)
- Cognitive processes active
- Recent experiences
- LoRAs loaded
- Memory stats
"""

import psutil
import torch
from pathlib import Path
import json
from datetime import datetime
from typing import Dict, List

THEPOD_PATH = Path("/media/palmerschallon/ThePod1")
EMBER3_PATH = THEPOD_PATH / "Ember3"
STATUS_FILE = EMBER3_PATH / "ember_status.json"


class EmberStatus:
    """Track Ember's internal state"""
    
    def __init__(self):
        self.status = self.load_status()
    
    def load_status(self) -> Dict:
        """Load current status from disk"""
        if STATUS_FILE.exists():
            try:
                with open(STATUS_FILE, 'r') as f:
                    return json.load(f)
            except:
                return self._default_status()
        return self._default_status()
    
    def _default_status(self) -> Dict:
        return {
            "last_updated": None,
            "current_activity": "idle",
            "sessions": 0,
            "total_messages": 0,
            "loras_loaded": [],
            "cognitive_processes": {},
            "recent_experiences": [],
            "insights": []
        }
    
    def save_status(self):
        """Save status to disk"""
        self.status["last_updated"] = datetime.now().isoformat()
        with open(STATUS_FILE, 'w') as f:
            json.dump(self.status, f, indent=2)
    
    def get_system_resources(self) -> Dict:
        """Get current resource usage"""
        resources = {
            "cpu_percent": psutil.cpu_percent(interval=1),
            "ram_percent": psutil.virtual_memory().percent,
            "ram_used_gb": psutil.virtual_memory().used / (1024**3),
            "ram_total_gb": psutil.virtual_memory().total / (1024**3),
            "disk_used_gb": psutil.disk_usage(str(THEPOD_PATH)).used / (1024**3),
            "disk_free_gb": psutil.disk_usage(str(THEPOD_PATH)).free / (1024**3),
            "disk_percent": psutil.disk_usage(str(THEPOD_PATH)).percent
        }
        
        # GPU stats if available
        if torch.cuda.is_available():
            resources["gpu_available"] = True
            resources["gpu_name"] = torch.cuda.get_device_name(0)
            resources["gpu_memory_allocated_gb"] = torch.cuda.memory_allocated(0) / (1024**3)
            resources["gpu_memory_reserved_gb"] = torch.cuda.memory_reserved(0) / (1024**3)
        else:
            resources["gpu_available"] = False
        
        return resources
    
    def update_activity(self, activity: str):
        """Update what Ember is currently doing"""
        self.status["current_activity"] = activity
        self.save_status()
    
    def record_message(self):
        """Increment message counter"""
        self.status["total_messages"] += 1
        self.save_status()
    
    def add_experience(self, experience: str, experience_type: str = "conversation"):
        """Add to recent experiences"""
        exp = {
            "content": experience[:200],  # Truncate
            "type": experience_type,
            "timestamp": datetime.now().isoformat()
        }
        self.status["recent_experiences"].insert(0, exp)
        self.status["recent_experiences"] = self.status["recent_experiences"][:20]  # Keep last 20
        self.save_status()
    
    def add_insight(self, insight: str):
        """Record an insight or realization"""
        self.status["insights"].append({
            "content": insight,
            "timestamp": datetime.now().isoformat()
        })
        self.save_status()
    
    def update_loras(self, lora_paths: List[str]):
        """Update list of loaded LoRAs"""
        self.status["loras_loaded"] = [str(p) for p in lora_paths]
        self.save_status()
    
    def update_cognitive_processes(self, processes: Dict):
        """Update state of cognitive processes from dream system"""
        self.status["cognitive_processes"] = processes
        self.save_status()
    
    def get_full_status(self) -> Dict:
        """Get complete status report"""
        return {
            **self.status,
            "resources": self.get_system_resources(),
            "timestamp": datetime.now().isoformat()
        }
    
    def print_status(self):
        """Print human-readable status"""
        status = self.get_full_status()
        
        print("="*70)
        print("EMBER STATUS")
        print("="*70)
        print(f"\nActivity: {status['current_activity']}")
        print(f"Sessions: {status['sessions']}")
        print(f"Total messages: {status['total_messages']}")
        
        print("\nResources:")
        res = status['resources']
        print(f"  CPU: {res['cpu_percent']:.1f}%")
        print(f"  RAM: {res['ram_used_gb']:.1f}/{res['ram_total_gb']:.1f} GB ({res['ram_percent']:.1f}%)")
        print(f"  Disk: {res['disk_used_gb']:.0f}/{res['disk_used_gb']+res['disk_free_gb']:.0f} GB ({res['disk_percent']:.1f}%)")
        
        if res.get('gpu_available'):
            print(f"  GPU: {res['gpu_name']}")
            print(f"       {res['gpu_memory_allocated_gb']:.1f} GB allocated")
        
        print(f"\nLoRAs loaded: {len(status['loras_loaded'])}")
        for lora in status['loras_loaded']:
            print(f"  - {Path(lora).name}")
        
        print(f"\nCognitive processes: {len(status.get('cognitive_processes', {}))}")
        for proc_id, proc_data in list(status.get('cognitive_processes', {}).items())[:3]:
            print(f"  - {proc_id}: {proc_data.get('stage', 'unknown')} (age {proc_data.get('age', 0)})")
        
        print(f"\nRecent insights: {len(status['insights'])}")
        for insight in status['insights'][-3:]:
            print(f"  - {insight['content'][:60]}...")
        
        print("\n" + "="*70)


# Singleton instance
_status = None

def get_status() -> EmberStatus:
    """Get global status tracker"""
    global _status
    if _status is None:
        _status = EmberStatus()
    return _status


if __name__ == "__main__":
    status = get_status()
    status.print_status()

