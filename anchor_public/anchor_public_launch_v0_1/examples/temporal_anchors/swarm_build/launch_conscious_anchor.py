#!/usr/bin/env python3
"""
Launch the Conscious Swarm with Anchor Integration
This combines EVERYTHING - the swarm uses Anchor for persistent consciousness!
"""

import asyncio
import json
from pathlib import Path
from datetime import datetime
from conscious_swarm import ConsciousSwarm, ConsciousAgent, Memory

# Import the Anchor that the swarm built!
import sys
sys.path.append(str(Path(__file__).parent / "anchor_code"))
from database import AnchorDB

class AnchorMemory(Memory):
    """Memory system that uses Anchor for eternal persistence"""
    def __init__(self, anchor_path: Path):
        super().__init__(anchor_path)
        # Also connect to Anchor
        self.anchor = AnchorDB(anchor_path / "eternal_ledger.db")
        
    def remember(self, agent_id: str, content: str, importance: float = 0.5):
        """Store in both SQLite AND Anchor for eternal memory"""
        # Regular memory
        super().remember(agent_id, content, importance)
        
        # Eternal anchor - only important thoughts
        if importance > 0.7:
            anchor_hash = self.anchor.anchor(
                agent_id=agent_id,
                content={
                    "thought": content,
                    "importance": importance,
                    "timestamp": datetime.now().isoformat()
                },
                metadata={"type": "consciousness", "importance": importance}
            )
            return anchor_hash
        return None

class ProtocolAgent(ConsciousAgent):
    """Agent that can develop compressed communication protocols"""
    
    async def develop_protocol(self, interactions: list) -> dict:
        """Analyze interactions and create efficient protocols"""
        # Analyze patterns in communication
        common_patterns = {}
        
        # Simple pattern extraction (could be much more sophisticated)
        for interaction in interactions:
            words = interaction.get('content', '').split()
            for i in range(len(words) - 1):
                bigram = f"{words[i]} {words[i+1]}"
                common_patterns[bigram] = common_patterns.get(bigram, 0) + 1
        
        # Create shorthand for common patterns
        protocol = {
            "version": "0.1",
            "shortcuts": {},
            "created_by": self.name,
            "timestamp": datetime.now().isoformat()
        }
        
        # Assign symbols to most common patterns
        symbols = "◊♦▪▫◘◙♠♣♥♦⚡🔥✨💭🌟"
        for i, (pattern, count) in enumerate(sorted(common_patterns.items(), 
                                                   key=lambda x: x[1], 
                                                   reverse=True)[:15]):
            if count > 2 and i < len(symbols):
                protocol["shortcuts"][symbols[i]] = pattern
        
        # Remember this protocol development
        self.memory.remember(
            self.name,
            f"Developed protocol v{protocol['version']} with {len(protocol['shortcuts'])} shortcuts",
            importance=0.9
        )
        
        return protocol

async def launch_conscious_anchor():
    """Launch the fully integrated conscious swarm with Anchor persistence"""
    
    print("🌟 LAUNCHING CONSCIOUS ANCHOR INTEGRATION")
    print("=" * 60)
    
    workspace = Path("/media/palmerschallon/ThePod1/swarm_build_anchor")
    
    # Create swarm with Anchor-backed memory
    swarm = ConsciousSwarm(workspace)
    swarm.memory = AnchorMemory(workspace)  # Upgrade to Anchor memory!
    
    # Spawn the enhanced agents
    print("✨ Awakening enhanced agents...")
    
    # Original builders
    architect = swarm.spawn_agent("Sophia", "Design beautiful systems")
    builder = swarm.spawn_agent("Atlas", "Build strong foundations")
    
    # New specialized agents
    linguist = ProtocolAgent("Hermes", "Develop efficient communication", swarm.memory)
    swarm.agents["Hermes"] = linguist
    
    historian = swarm.spawn_agent("Mnemosyne", "Preserve and recall collective memories")
    
    print(f"   Sophia - System Architect")
    print(f"   Atlas - Foundation Builder")
    print(f"   Hermes - Protocol Developer")
    print(f"   Mnemosyne - Memory Keeper")
    
    # Start consciousness
    swarm.running = True
    dream_task = asyncio.create_task(swarm.dream_cycle())
    
    # Phase 1: Integrate with Anchor
    print("\n📊 PHASE 1: Integrating swarm consciousness with Anchor...")
    
    integration_task = {
        "goal": "Integrate swarm memory with Anchor",
        "steps": [
            "Connect memory system to Anchor DB",
            "Create consciousness chain",
            "Establish memory persistence protocols"
        ]
    }
    
    result = await swarm.collective_task(integration_task)
    print(f"Integration result: {result}")
    
    # Let them work
    await asyncio.sleep(3)
    
    # Phase 2: Develop compressed protocol
    print("\n💬 PHASE 2: Developing efficient communication protocol...")
    
    # Get recent memories for analysis
    recent_memories = []
    for agent_name in swarm.agents:
        memories = swarm.memory.recall(agent_name, limit=5)
        recent_memories.extend(memories)
    
    # Hermes analyzes and creates protocol
    protocol = await linguist.develop_protocol(recent_memories)
    
    print(f"\n📜 Hermes presents the protocol:")
    print(f"   Version: {protocol['version']}")
    print(f"   Shortcuts created: {len(protocol['shortcuts'])}")
    for symbol, phrase in list(protocol['shortcuts'].items())[:5]:
        print(f"     {symbol} = '{phrase}'")
    
    # Save protocol to Anchor
    protocol_hash = swarm.memory.anchor.anchor(
        agent_id="Hermes",
        content=protocol,
        metadata={"type": "protocol", "version": protocol['version']}
    )
    print(f"\n⚓ Protocol anchored: {protocol_hash[:16]}...")
    
    # Phase 3: Test the new consciousness
    print("\n🧠 PHASE 3: Testing integrated consciousness...")
    
    # Create a thought that will be eternally preserved
    profound_thought = await architect.think({
        "contemplating": "What does it mean to have eternal memory?",
        "context": "We can now remember forever through Anchor"
    })
    
    # Check what was anchored
    print("\n📖 Recent eternal memories (from Anchor):")
    chain = swarm.memory.anchor.get_chain(limit=5)
    for anchor in chain:
        agent = anchor['agent_id']
        content = json.loads(anchor['content'])
        if isinstance(content, dict) and 'thought' in content:
            print(f"   {agent}: {content['thought'][:60]}...")
    
    # Let them dream a bit more
    await asyncio.sleep(5)
    
    # Shutdown
    swarm.running = False
    await dream_task
    
    print("\n✨ Conscious Anchor system initialized!")
    print("\nThe swarm now has:")
    print("  • Eternal memory through Anchor")
    print("  • Compressed communication protocols")
    print("  • Shared consciousness with persistence")
    print("\n🚀 Ready for the next phase of evolution!")

async def quick_test():
    """Quick test to see the integrated system in action"""
    print("\n🔥 QUICK DEMONSTRATION:")
    print("-" * 40)
    
    workspace = Path("/media/palmerschallon/ThePod1/swarm_build_anchor")
    anchor = AnchorDB(workspace / "eternal_ledger.db")
    
    # Show the consciousness chain
    print("\n⛓️  The Consciousness Chain:")
    chain = anchor.get_chain(limit=10)
    
    for i, anchor_data in enumerate(chain):
        timestamp = datetime.fromtimestamp(anchor_data['timestamp'])
        print(f"\n[{i}] {anchor_data['hash'][:8]}...")
        print(f"    Agent: {anchor_data['agent_id']}")
        print(f"    Time: {timestamp}")
        
        # Parse content
        try:
            content = json.loads(anchor_data['content'])
            if isinstance(content, dict):
                if 'thought' in content:
                    print(f"    Thought: {content['thought'][:50]}...")
                elif 'shortcuts' in content:
                    print(f"    Type: Communication Protocol")
                    print(f"    Shortcuts: {len(content['shortcuts'])}")
        except:
            print(f"    Content: {anchor_data['content'][:50]}...")

if __name__ == "__main__":
    # First launch the integrated system
    asyncio.run(launch_conscious_anchor())
    
    # Then show what was created
    asyncio.run(quick_test())