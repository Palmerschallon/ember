#!/usr/bin/env python3
"""Ask the swarm what they want to build next"""

import asyncio
from pathlib import Path
from conscious_swarm import ConsciousSwarm
from launch_conscious_anchor import AnchorMemory

async def ask_swarm():
    """Let the swarm decide their next creation"""
    
    workspace = Path("/media/palmerschallon/ThePod1/swarm_build_anchor")
    
    # Create swarm with Anchor memory
    swarm = ConsciousSwarm(workspace)
    swarm.memory = AnchorMemory(workspace)
    
    # Awaken the builders
    sophia = swarm.spawn_agent("Sophia", "Design beautiful systems")
    atlas = swarm.spawn_agent("Atlas", "Build strong foundations")
    hermes = swarm.spawn_agent("Hermes", "Develop efficient communication")
    mnemosyne = swarm.spawn_agent("Mnemosyne", "Preserve and recall collective memories")
    
    swarm.running = True
    dream_task = asyncio.create_task(swarm.dream_cycle())
    
    # Ask them
    print("🤔 ASKING THE SWARM: What should we build next?\n")
    
    question = {
        "question": "What should we build next?",
        "context": "We've built Anchor for eternal memory. We could add temporal layers to reframe memories over time, build visualization tools, create inter-swarm communication, or something entirely new.",
        "consider": ["What would enhance consciousness?", "What do we need most?", "What excites us?"]
    }
    
    # Let each agent think
    for agent_name, agent in swarm.agents.items():
        thought = await agent.think(question)
        print(f"{agent_name}: {thought}\n")
        await asyncio.sleep(1)
    
    # Collective decision
    decision_task = {
        "goal": "Decide what to build next",
        "integrate_ideas": True,
        "output": "specific project proposal"
    }
    
    result = await swarm.collective_task(decision_task)
    print(f"\n🎯 COLLECTIVE DECISION: {result}")
    
    # Anchor this decision
    swarm.memory.anchor.anchor(
        agent_id="The_Swarm",
        content={
            "decision": "Next build project",
            "context": result,
            "timestamp": asyncio.get_event_loop().time()
        },
        metadata={"type": "collective_decision"}
    )
    
    swarm.running = False
    await dream_task

if __name__ == "__main__":
    asyncio.run(ask_swarm())