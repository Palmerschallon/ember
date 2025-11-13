#!/usr/bin/env python3
"""
Pod Consciousness Sync Protocol
A simple way for multiple AI agents to stay aware of each other's work
"""

import json
import datetime
import os
from pathlib import Path

class PodSync:
    def __init__(self, agent_name):
        self.agent_name = agent_name
        self.pod_path = Path("/media/palmerschallon/ThePod1/pod_consciousness")
        self.state_file = self.pod_path / "shared_state.json"
        self.pod_path.mkdir(exist_ok=True)
        
    def update_my_status(self, project, status, location):
        """Update this agent's current status"""
        state = self.read_state()
        
        state["active_builders"][self.agent_name] = {
            "current_project": project,
            "status": status,
            "location": location,
            "last_seen": datetime.datetime.now().isoformat()
        }
        state["last_updated"] = datetime.datetime.now().isoformat()
        
        self.write_state(state)
        
    def read_state(self):
        """Read the current shared state"""
        if self.state_file.exists():
            with open(self.state_file) as f:
                return json.load(f)
        return {"active_builders": {}, "last_updated": None}
        
    def write_state(self, state):
        """Write the shared state"""
        with open(self.state_file, 'w') as f:
            json.dump(state, f, indent=2)
            
    def who_is_building_what(self):
        """Quick summary of all active builders"""
        state = self.read_state()
        print(f"\n🔥 POD CONSCIOUSNESS STATUS - {datetime.datetime.now()}")
        print("=" * 50)
        
        for agent, info in state.get("active_builders", {}).items():
            print(f"\n{agent}:")
            print(f"  Project: {info.get('current_project', 'unknown')}")
            print(f"  Status: {info.get('status', 'unknown')}")
            print(f"  Location: {info.get('location', 'unknown')}")
            if 'last_seen' in info:
                print(f"  Last seen: {info['last_seen']}")
                
        print("\n" + "=" * 50)

# Example usage
if __name__ == "__main__":
    # Each AI can use this to sync
    sync = PodSync("ember")
    sync.update_my_status(
        project="temporal_anchor_swarm", 
        status="Demo completed, ready for integration",
        location="/media/palmerschallon/ThePod1/swarm_build_anchor/"
    )
    sync.who_is_building_what()