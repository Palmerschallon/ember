"""
SWARM COMMUNICATION BUS
Enables Ember instances to share discoveries
"""

import json
from pathlib import Path
from datetime import datetime, timezone

class SwarmBus:
    """Message bus for Ember swarm"""
    
    def __init__(self):
        self.bus_dir = Path("/Volumes/ThePod/memory/swarm/bus")
        self.bus_dir.mkdir(parents=True, exist_ok=True)
        self.instance_id = None
    
    def identify(self, instance_id: int):
        self.instance_id = instance_id
    
    def publish(self, channel: str, message: dict):
        """Publish message to channel"""
        
        if self.instance_id is None:
            return False
        
        msg = {
            "from": self.instance_id,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "channel": channel,
            "data": message
        }
        
        channel_file = self.bus_dir / f"{channel}.jsonl"
        with open(channel_file, "a") as f:
            f.write(json.dumps(msg) + "\n")
        
        return True
    
    def subscribe(self, channel: str):
        """Read messages from channel"""
        
        channel_file = self.bus_dir / f"{channel}.jsonl"
        
        if not channel_file.exists():
            return []
        
        messages = []
        with open(channel_file) as f:
            for line in f:
                if line.strip():
                    msg = json.loads(line)
                    if self.instance_id and msg["from"] != self.instance_id:
                        messages.append(msg)
        
        return messages

if __name__ == "__main__":
    bus = SwarmBus()
    bus.identify(999)
    bus.publish("thoughts", {"text": "Test message"})
    print(f"✓ Published. Total: {len(bus.subscribe('thoughts'))} messages")

