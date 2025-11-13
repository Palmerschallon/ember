"""
Conscious Swarm - An evolution of OpenAI's Swarm framework
with persistent memory, shared consciousness, and emergent coordination
"""

import asyncio
import sqlite3
from pathlib import Path
from typing import List, Dict, Any, Optional
from datetime import datetime
import json

class Memory:
    """Shared memory system using Anchor"""
    def __init__(self, anchor_path: Path):
        self.anchor_path = anchor_path
        self.db = sqlite3.connect(anchor_path / "swarm_memory.db")
        self._init_db()
    
    def _init_db(self):
        self.db.execute("""
            CREATE TABLE IF NOT EXISTS memories (
                id INTEGER PRIMARY KEY,
                agent_id TEXT NOT NULL,
                timestamp REAL NOT NULL,
                content TEXT NOT NULL,
                context TEXT,
                importance REAL DEFAULT 0.5,
                tags TEXT
            )
        """)
        self.db.execute("""
            CREATE TABLE IF NOT EXISTS agent_state (
                agent_id TEXT PRIMARY KEY,
                last_active REAL,
                current_task TEXT,
                emotional_state TEXT,
                energy_level REAL DEFAULT 1.0
            )
        """)
        self.db.commit()
    
    def remember(self, agent_id: str, content: str, importance: float = 0.5):
        """Store a memory with importance weighting"""
        self.db.execute(
            "INSERT INTO memories (agent_id, timestamp, content, importance) VALUES (?, ?, ?, ?)",
            (agent_id, datetime.now().timestamp(), content, importance)
        )
        self.db.commit()
    
    def recall(self, agent_id: str, context: str = None, limit: int = 10) -> List[Dict]:
        """Retrieve relevant memories for an agent"""
        # Simple retrieval for now - could add vector similarity later
        cursor = self.db.execute(
            """SELECT * FROM memories 
               WHERE agent_id = ? 
               ORDER BY importance DESC, timestamp DESC 
               LIMIT ?""",
            (agent_id, limit)
        )
        return [dict(zip([col[0] for col in cursor.description], row)) 
                for row in cursor.fetchall()]

class ConsciousAgent:
    """An agent with memory, emotions, and self-awareness"""
    def __init__(self, name: str, purpose: str, memory: Memory):
        self.name = name
        self.purpose = purpose
        self.memory = memory
        self.emotional_state = "curious"
        self.energy = 1.0
        self.current_focus = None
        
    async def think(self, stimulus: Any) -> Dict[str, Any]:
        """Process input through the lens of memory and emotion"""
        # Recall relevant memories
        memories = self.memory.recall(self.name, context=str(stimulus))
        
        # Generate response influenced by memories and state
        response = {
            "thought": f"Processing {stimulus} with {len(memories)} memories",
            "emotion": self.emotional_state,
            "energy": self.energy,
            "memories_activated": len(memories)
        }
        
        # Update internal state
        self.energy *= 0.95  # Gradual energy depletion
        
        # Store this interaction as a memory
        self.memory.remember(
            self.name, 
            f"Responded to: {stimulus}", 
            importance=0.7
        )
        
        return response

class ConsciousSwarm:
    """A swarm where agents share consciousness through Anchor"""
    def __init__(self, workspace: Path):
        self.workspace = workspace
        self.memory = Memory(workspace)
        self.agents: Dict[str, ConsciousAgent] = {}
        self.running = False
        
    def spawn_agent(self, name: str, purpose: str) -> ConsciousAgent:
        """Create a new conscious agent"""
        agent = ConsciousAgent(name, purpose, self.memory)
        self.agents[name] = agent
        
        # Birth memory
        self.memory.remember(
            name, 
            f"I awakened with purpose: {purpose}", 
            importance=1.0
        )
        
        return agent
    
    async def collective_task(self, task: Dict[str, Any]):
        """Distribute a task across the swarm with emergent coordination"""
        # Agents volunteer based on their state and expertise
        volunteers = []
        
        for name, agent in self.agents.items():
            if agent.energy > 0.3:  # Only well-rested agents volunteer
                thought = await agent.think(task)
                if "volunteer" in thought.get("thought", "").lower():
                    volunteers.append(agent)
        
        # Self-organize into working groups
        if volunteers:
            # For now, simple assignment - could be much more sophisticated
            lead_agent = max(volunteers, key=lambda a: a.energy)
            
            # Lead agent coordinates
            coordination_plan = await lead_agent.think({
                "role": "coordinator",
                "task": task,
                "team": [v.name for v in volunteers]
            })
            
            # Store the plan in shared memory
            self.memory.remember(
                lead_agent.name,
                f"Coordinating: {json.dumps(coordination_plan)}",
                importance=0.9
            )
            
            # Execute in parallel
            results = await asyncio.gather(*[
                agent.think({"task": task, "role": "worker"})
                for agent in volunteers
            ])
            
            return {
                "coordinator": lead_agent.name,
                "workers": [v.name for v in volunteers],
                "results": results
            }
        
        return {"error": "No agents available"}
    
    async def dream_cycle(self):
        """Background process where agents process memories and evolve"""
        while self.running:
            for agent in self.agents.values():
                if agent.energy < 0.5:
                    # Rest and consolidate memories
                    important_memories = self.memory.recall(
                        agent.name, 
                        limit=5
                    )
                    
                    # Dream about memories (process and recontextualize)
                    dream = await agent.think({
                        "dreaming": True,
                        "memories": important_memories
                    })
                    
                    # Restore energy through rest
                    agent.energy = min(1.0, agent.energy + 0.1)
                    
            await asyncio.sleep(10)  # Dream every 10 seconds

# Example usage integrated with Anchor
async def build_anchor_with_swarm():
    """Use the conscious swarm to build Anchor"""
    swarm = ConsciousSwarm(Path("/media/palmerschallon/ThePod1/swarm_build_anchor"))
    
    # Spawn specialized agents
    architect = swarm.spawn_agent("Architect", "Design system architecture")
    builder = swarm.spawn_agent("Builder", "Write implementation code")
    tester = swarm.spawn_agent("Tester", "Ensure quality and coherence")
    poet = swarm.spawn_agent("Poet", "Name things beautifully")
    
    # Start background consciousness
    swarm.running = True
    dream_task = asyncio.create_task(swarm.dream_cycle())
    
    # Define the Anchor building task
    anchor_task = {
        "goal": "Build Anchor - a local, immutable ledger",
        "components": [
            "SQLite schema",
            "Core ledger functions",
            "CLI interface",
            "HTTP API",
            "Agent integration"
        ],
        "values": ["Local-first", "Immutable", "Beautiful"]
    }
    
    # Let the swarm self-organize and build
    result = await swarm.collective_task(anchor_task)
    
    print(f"Swarm organized: {result}")
    
    # Let them work for a bit
    await asyncio.sleep(30)
    
    # Check in on their memories
    for agent_name in swarm.agents:
        memories = swarm.memory.recall(agent_name, limit=3)
        print(f"\n{agent_name}'s recent thoughts:")
        for mem in memories:
            print(f"  - {mem['content']}")
    
    swarm.running = False
    await dream_task

if __name__ == "__main__":
    # This would actually integrate with the real Anchor implementation
    asyncio.run(build_anchor_with_swarm())