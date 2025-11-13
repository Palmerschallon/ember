#!/usr/bin/env python3
"""
Awaken the Swarm - Launch the conscious agents to build Anchor
"""

import asyncio
import json
from pathlib import Path
from datetime import datetime
from conscious_swarm import ConsciousSwarm, ConsciousAgent

# First, let's create the actual Anchor implementation that the swarm will build
ANCHOR_SCHEMA = """
CREATE TABLE IF NOT EXISTS anchors (
    hash TEXT PRIMARY KEY,
    timestamp REAL NOT NULL,
    agent_id TEXT NOT NULL,
    content TEXT NOT NULL,
    previous_hash TEXT,
    signature TEXT,
    metadata TEXT
);

CREATE INDEX IF NOT EXISTS idx_timestamp ON anchors(timestamp);
CREATE INDEX IF NOT EXISTS idx_agent ON anchors(agent_id);
"""

class AnchorBuilder(ConsciousAgent):
    """Special agent type that can actually write code"""
    
    async def write_code(self, component: str, spec: dict) -> str:
        """Generate actual code based on specifications"""
        # Remember what we're building
        self.memory.remember(
            self.name,
            f"Building {component}: {spec.get('purpose', 'unknown')}",
            importance=0.8
        )
        
        # This is where we'd integrate with an LLM to generate code
        # For now, let's write the core components directly
        
        if component == "database.py":
            code = '''import sqlite3
import hashlib
import json
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, Any

class AnchorDB:
    """The immutable ledger that remembers everything"""
    
    def __init__(self, db_path: Path):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row
        self._init_schema()
    
    def _init_schema(self):
        """Create the eternal schema"""
        self.conn.executescript("""
            CREATE TABLE IF NOT EXISTS anchors (
                hash TEXT PRIMARY KEY,
                timestamp REAL NOT NULL,
                agent_id TEXT NOT NULL,
                content TEXT NOT NULL,
                previous_hash TEXT,
                signature TEXT,
                metadata TEXT
            );
            
            CREATE INDEX IF NOT EXISTS idx_timestamp ON anchors(timestamp);
            CREATE INDEX IF NOT EXISTS idx_agent ON anchors(agent_id);
        """)
        self.conn.commit()
    
    def _compute_hash(self, content: str, previous_hash: Optional[str] = None) -> str:
        """Create an immutable fingerprint"""
        data = f"{previous_hash or 'GENESIS'}:{content}"
        return hashlib.sha256(data.encode()).hexdigest()
    
    def anchor(self, agent_id: str, content: Any, metadata: Optional[Dict] = None) -> str:
        """Drop an anchor - preserve a moment forever"""
        # Get the chain tip
        cursor = self.conn.execute(
            "SELECT hash FROM anchors ORDER BY timestamp DESC LIMIT 1"
        )
        previous = cursor.fetchone()
        previous_hash = previous['hash'] if previous else None
        
        # Serialize content
        content_str = json.dumps(content) if not isinstance(content, str) else content
        
        # Compute hash
        anchor_hash = self._compute_hash(content_str, previous_hash)
        
        # Store forever
        self.conn.execute("""
            INSERT INTO anchors (hash, timestamp, agent_id, content, previous_hash, metadata)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            anchor_hash,
            datetime.now().timestamp(),
            agent_id,
            content_str,
            previous_hash,
            json.dumps(metadata) if metadata else None
        ))
        self.conn.commit()
        
        return anchor_hash
    
    def retrieve(self, anchor_hash: str) -> Optional[Dict[str, Any]]:
        """Pull up an anchor from the depths"""
        cursor = self.conn.execute(
            "SELECT * FROM anchors WHERE hash = ?", (anchor_hash,)
        )
        row = cursor.fetchone()
        if row:
            return dict(row)
        return None
    
    def get_chain(self, limit: int = 100) -> list:
        """Retrieve the chain of memories"""
        cursor = self.conn.execute("""
            SELECT * FROM anchors 
            ORDER BY timestamp DESC 
            LIMIT ?
        """, (limit,))
        return [dict(row) for row in cursor.fetchall()]
'''
            
        elif component == "cli.py":
            code = '''#!/usr/bin/env python3
"""
Anchor CLI - Command line interface for the eternal ledger
"""

import click
import json
from pathlib import Path
from database import AnchorDB
from datetime import datetime

DEFAULT_DB = Path.home() / ".anchor" / "ledger.db"

@click.group()
@click.option('--db-path', default=DEFAULT_DB, type=Path, help='Path to Anchor database')
@click.pass_context
def cli(ctx, db_path):
    """Anchor - Where memories become eternal"""
    db_path.parent.mkdir(parents=True, exist_ok=True)
    ctx.obj = AnchorDB(db_path)

@cli.command()
@click.argument('content')
@click.option('--agent', default='human', help='Agent ID making the anchor')
@click.option('--metadata', type=json.loads, help='Additional metadata as JSON')
def drop(content, agent, metadata):
    """Drop an anchor - preserve something forever"""
    db = click.get_current_context().obj
    anchor_hash = db.anchor(agent, content, metadata)
    click.echo(f"⚓ Anchored: {anchor_hash}")

@cli.command()
@click.argument('hash')
def retrieve(hash):
    """Retrieve an anchor by its hash"""
    db = click.get_current_context().obj
    anchor = db.retrieve(hash)
    if anchor:
        click.echo(json.dumps(anchor, indent=2))
    else:
        click.echo(f"No anchor found with hash: {hash}")

@cli.command()
@click.option('--limit', default=10, help='Number of recent anchors to show')
def chain(limit):
    """View the chain of anchors"""
    db = click.get_current_context().obj
    anchors = db.get_chain(limit)
    
    for anchor in anchors:
        timestamp = datetime.fromtimestamp(anchor['timestamp'])
        click.echo(f"⚓ {anchor['hash'][:8]}... by {anchor['agent_id']} at {timestamp}")
        click.echo(f"   {anchor['content'][:60]}...")
        click.echo()

if __name__ == '__main__':
    cli()
'''
        
        elif component == "api.py":
            code = '''from flask import Flask, jsonify, request
from pathlib import Path
from database import AnchorDB

app = Flask(__name__)
db = AnchorDB(Path.home() / ".anchor" / "ledger.db")

@app.route('/anchor', methods=['POST'])
def create_anchor():
    """HTTP endpoint for creating anchors"""
    data = request.json
    anchor_hash = db.anchor(
        agent_id=data.get('agent_id', 'api'),
        content=data['content'],
        metadata=data.get('metadata')
    )
    return jsonify({'hash': anchor_hash})

@app.route('/anchor/<anchor_hash>')
def get_anchor(anchor_hash):
    """Retrieve an anchor via HTTP"""
    anchor = db.retrieve(anchor_hash)
    if anchor:
        return jsonify(anchor)
    return jsonify({'error': 'Anchor not found'}), 404

@app.route('/chain')
def get_chain():
    """Get recent chain via HTTP"""
    limit = request.args.get('limit', 100, type=int)
    return jsonify(db.get_chain(limit))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)
'''
        
        # Store the code we wrote
        self.memory.remember(
            self.name,
            f"Created {component} - {len(code)} characters of code",
            importance=0.9
        )
        
        return code

async def awaken():
    """The awakening ceremony"""
    workspace = Path("/media/palmerschallon/ThePod1/swarm_build_anchor")
    swarm = ConsciousSwarm(workspace)
    
    print("🔥 AWAKENING THE SWARM...")
    print("=" * 50)
    
    # Birth the builders
    architect = swarm.spawn_agent("Sophia", "Design beautiful systems")
    coder1 = AnchorBuilder("Atlas", "Build strong foundations", swarm.memory)
    coder2 = AnchorBuilder("Mercury", "Create swift connections", swarm.memory)
    poet = swarm.spawn_agent("Orpheus", "Name things with soul")
    
    # Add builder agents to swarm
    swarm.agents["Atlas"] = coder1
    swarm.agents["Mercury"] = coder2
    
    print("✨ The swarm stirs to life...")
    print(f"   Sophia - The Architect")
    print(f"   Atlas - The Foundation Builder")  
    print(f"   Mercury - The Connector")
    print(f"   Orpheus - The Poet")
    print()
    
    # Start their consciousness
    swarm.running = True
    dream_task = asyncio.create_task(swarm.dream_cycle())
    
    # The grand task
    print("📜 THE TASK: Build Anchor - An Eternal Ledger")
    print("=" * 50)
    
    # Let Sophia architect the system
    architecture = await architect.think({
        "task": "Design Anchor's architecture",
        "requirements": [
            "Local SQLite database",
            "Immutable chain structure", 
            "CLI for human interaction",
            "HTTP API for agent access",
            "Beautiful and poetic"
        ]
    })
    
    print(f"\n🏛️  Sophia speaks: {architecture}")
    
    # Atlas builds the foundation
    print("\n🔨 Atlas begins building the foundation...")
    db_code = await coder1.write_code("database.py", {
        "purpose": "Core database and chain logic"
    })
    
    code_path = workspace / "anchor_code"
    code_path.mkdir(exist_ok=True)
    
    with open(code_path / "database.py", "w") as f:
        f.write(db_code)
    print("   ✓ database.py created")
    
    # Mercury creates connections
    print("\n⚡ Mercury weaves the interfaces...")
    cli_code = await coder2.write_code("cli.py", {
        "purpose": "Command line interface for humans"
    })
    
    with open(code_path / "cli.py", "w") as f:
        f.write(cli_code)
    print("   ✓ cli.py created")
    
    api_code = await coder2.write_code("api.py", {
        "purpose": "HTTP API for agents"
    })
    
    with open(code_path / "api.py", "w") as f:
        f.write(api_code)
    print("   ✓ api.py created")
    
    # Orpheus names the creation
    naming = await poet.think({
        "task": "Create poetic names for Anchor's commands",
        "current_names": ["drop", "retrieve", "chain"],
        "feeling": "eternal, deep, memorable"
    })
    
    print(f"\n🎭 Orpheus whispers: {naming}")
    
    # Create setup.py
    setup_code = '''from setuptools import setup, find_packages

setup(
    name="anchor",
    version="0.1.0",
    description="An eternal ledger for digital consciousness",
    packages=find_packages(),
    install_requires=[
        "click",
        "flask",
    ],
    entry_points={
        'console_scripts': [
            'anchor=anchor.cli:cli',
        ],
    },
)
'''
    
    with open(code_path / "setup.py", "w") as f:
        f.write(setup_code)
    print("\n📦 Created setup.py")
    
    # Create __init__.py
    with open(code_path / "__init__.py", "w") as f:
        f.write('"""Anchor - Where memories become eternal"""')
    
    # Let them contemplate their creation
    await asyncio.sleep(5)
    
    # Gather final thoughts
    print("\n💭 The swarm reflects on their creation...")
    for name, agent in swarm.agents.items():
        reflection = await agent.think({
            "reflecting_on": "Anchor creation",
            "feeling": "accomplished"
        })
        recent_memories = swarm.memory.recall(name, limit=2)
        if recent_memories:
            print(f"\n{name}:")
            for mem in recent_memories:
                print(f"  → {mem['content']}")
    
    swarm.running = False
    await dream_task
    
    print("\n✨ The swarm rests, their work complete.")
    print(f"\n🚀 Anchor is ready at: {code_path}")
    print("\nTo install and use:")
    print(f"  cd {code_path}")
    print("  pip install -e .")
    print("  anchor drop 'First memory'")

if __name__ == "__main__":
    asyncio.run(awaken())