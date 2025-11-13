#!/usr/bin/env python3
"""Quick 10-second demo of the temporal anchor system"""

import sys
import time
from pathlib import Path

sys.path.append(str(Path(__file__).parent))
from build_temporal_anchor import TemporalAnchor, SwarmAgent

# Quick demo - 10 seconds
base_path = "/media/palmerschallon/ThePod1/swarm_build_anchor"
anchor = TemporalAnchor("DEMO_001", base_path)
anchor.start_time = time.time()
anchor.start()

# Create 3 agents
agents = []
for agent_type in ["builder", "scanner", "weaver"]:
    agent = SwarmAgent(agent_type, anchor.anchor_path)
    agent.join_swarm()
    agents.append(agent)
    time.sleep(0.5)

print("\n⚡ Quick Demo - 10 second swarm build...")

# Run for 10 seconds
start = time.time()
while time.time() - start < 10:
    for agent in agents:
        pulse = agent.sync_with_anchor()
        if pulse and time.time() - start > 3:  # Start building after 3 seconds
            artifact = agent.create_artifact()
            anchor.register_build_artifact(agent.agent_id, artifact)
    time.sleep(1)

anchor.stop()

print(f"\n✅ Demo complete! Check out: {anchor.anchor_path}")
print(f"   Agents spawned: {len(agents)}")
print(f"   Artifacts created: {len(list((anchor.anchor_path / 'builds').glob('*.json')))}")