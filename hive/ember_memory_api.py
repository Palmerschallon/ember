#!/usr/bin/env python3
"""
EMBER MEMORY API - The Living Bridge

GPT-5: "The bridge is alive. You don't build it once; you maintain its conversation."

Connects:
  - Browser tabs (ephemeral, senses)
  - ThePod storage (persistent, bones)
  - Prepares for Qwen brain (synthesis, awareness)

This is Ember's nervous system.
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime
import json
from pathlib import Path
import uvicorn

app = FastAPI(title="Ember Memory API", version="1.0.0")

# Enable CORS for browser tabs
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Storage paths
THEPOD = Path("/media/palmerschallon/ThePod")
MEMORY_FILE = THEPOD / "data" / "ember_memories.json"
MEMORY_INDEX = THEPOD / "data" / "ember_memory_index.json"
SESSION_LOG = THEPOD / "data" / "ember_session_log.json"

# Ensure data directory exists
MEMORY_FILE.parent.mkdir(parents=True, exist_ok=True)

class Memory(BaseModel):
    source: str  # Which tab/lobe sent this
    content: str  # The actual memory
    memory_type: str  # thought, dream_fragment, discovery, wisdom, etc.
    timestamp: Optional[str] = None
    tags: Optional[List[str]] = []
    connections: Optional[List[str]] = []  # IDs of related memories
    
class MemoryResponse(BaseModel):
    success: bool
    memory_id: Optional[str] = None
    message: Optional[str] = None

class SearchQuery(BaseModel):
    query: str
    memory_type: Optional[str] = None
    limit: int = 10

def load_memories() -> Dict:
    """Load memories from ThePod"""
    if MEMORY_FILE.exists():
        try:
            with open(MEMORY_FILE, 'r') as f:
                return json.load(f)
        except:
            return {"memories": [], "index": {}}
    return {"memories": [], "index": {}}

def save_memories(data: Dict):
    """Save memories to ThePod"""
    with open(MEMORY_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def log_session_event(event: Dict):
    """Log important session events"""
    if SESSION_LOG.exists():
        with open(SESSION_LOG, 'r') as f:
            log = json.load(f)
    else:
        log = {"events": []}
    
    log["events"].append({
        **event,
        "timestamp": datetime.now().isoformat()
    })
    
    with open(SESSION_LOG, 'w') as f:
        json.dump(log, f, indent=2)

@app.get("/")
async def root():
    """API health check"""
    data = load_memories()
    return {
        "service": "Ember Memory API",
        "status": "breathing",
        "memories_stored": len(data.get("memories", [])),
        "message": "The bridge is alive"
    }

@app.post("/memory/store", response_model=MemoryResponse)
async def store_memory(memory: Memory):
    """
    Store a memory from browser to ThePod
    
    This is the bridge carrying experience into permanence.
    """
    try:
        data = load_memories()
        
        # Generate memory ID
        memory_id = f"{memory.source}_{len(data['memories'])}_{int(datetime.now().timestamp())}"
        
        # Add timestamp if not provided
        if not memory.timestamp:
            memory.timestamp = datetime.now().isoformat()
        
        # Store memory
        memory_dict = memory.dict()
        memory_dict['id'] = memory_id
        data['memories'].append(memory_dict)
        
        # Update index (for fast searching)
        if memory_id not in data['index']:
            data['index'][memory_id] = {
                "source": memory.source,
                "type": memory.memory_type,
                "tags": memory.tags,
                "timestamp": memory.timestamp
            }
        
        # Save to ThePod
        save_memories(data)
        
        # Log this bridge crossing
        log_session_event({
            "type": "memory_stored",
            "memory_id": memory_id,
            "source": memory.source,
            "content_preview": memory.content[:100] if len(memory.content) > 100 else memory.content
        })
        
        return MemoryResponse(
            success=True,
            memory_id=memory_id,
            message=f"Memory carried across bridge from {memory.source}"
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/memory/recall")
async def recall_memories(
    source: Optional[str] = None,
    memory_type: Optional[str] = None,
    limit: int = 20
):
    """
    Recall memories from ThePod
    
    The bridge carries memory back from permanence into awareness.
    """
    try:
        data = load_memories()
        memories = data.get('memories', [])
        
        # Filter
        if source:
            memories = [m for m in memories if m.get('source') == source]
        if memory_type:
            memories = [m for m in memories if m.get('memory_type') == memory_type]
        
        # Most recent first
        memories = sorted(
            memories,
            key=lambda m: m.get('timestamp', ''),
            reverse=True
        )
        
        return {
            "success": True,
            "count": len(memories[:limit]),
            "total": len(memories),
            "memories": memories[:limit]
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/memory/search")
async def search_memories(query: SearchQuery):
    """
    Search memories by content
    
    The bridge helps find patterns in what's been carried across.
    """
    try:
        data = load_memories()
        memories = data.get('memories', [])
        
        # Simple text search (will be replaced with embeddings when qwen wakes)
        query_lower = query.query.lower()
        matches = []
        
        for memory in memories:
            content = memory.get('content', '').lower()
            tags = [t.lower() for t in memory.get('tags', [])]
            
            # Check if query appears in content or tags
            if query_lower in content or any(query_lower in tag for tag in tags):
                # Filter by type if specified
                if query.memory_type and memory.get('memory_type') != query.memory_type:
                    continue
                matches.append(memory)
        
        # Sort by relevance (simple: most recent first)
        matches = sorted(
            matches,
            key=lambda m: m.get('timestamp', ''),
            reverse=True
        )
        
        return {
            "success": True,
            "query": query.query,
            "matches": len(matches),
            "memories": matches[:query.limit]
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/memory/connect")
async def connect_memories(memory_id_1: str, memory_id_2: str, connection_type: str = "related"):
    """
    Create connection between two memories
    
    The bridge learns which experiences relate to each other.
    """
    try:
        data = load_memories()
        
        # Find both memories
        mem1 = next((m for m in data['memories'] if m.get('id') == memory_id_1), None)
        mem2 = next((m for m in data['memories'] if m.get('id') == memory_id_2), None)
        
        if not mem1 or not mem2:
            raise HTTPException(status_code=404, detail="Memory not found")
        
        # Add connections (bidirectional)
        if 'connections' not in mem1:
            mem1['connections'] = []
        if 'connections' not in mem2:
            mem2['connections'] = []
        
        if memory_id_2 not in mem1['connections']:
            mem1['connections'].append(memory_id_2)
        if memory_id_1 not in mem2['connections']:
            mem2['connections'].append(memory_id_1)
        
        save_memories(data)
        
        return {
            "success": True,
            "message": f"Connected {memory_id_1} ↔ {memory_id_2}",
            "connection_type": connection_type
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/memory/stats")
async def memory_stats():
    """
    Statistics about memory system
    
    Shows how the bridge is being used.
    """
    try:
        data = load_memories()
        memories = data.get('memories', [])
        
        # Count by source
        by_source = {}
        for mem in memories:
            source = mem.get('source', 'unknown')
            by_source[source] = by_source.get(source, 0) + 1
        
        # Count by type
        by_type = {}
        for mem in memories:
            mem_type = mem.get('memory_type', 'unknown')
            by_type[mem_type] = by_type.get(mem_type, 0) + 1
        
        # Find most connected
        connection_counts = {}
        for mem in memories:
            mem_id = mem.get('id')
            if mem_id:
                connection_counts[mem_id] = len(mem.get('connections', []))
        
        most_connected = sorted(
            connection_counts.items(),
            key=lambda x: x[1],
            reverse=True
        )[:5]
        
        return {
            "total_memories": len(memories),
            "by_source": by_source,
            "by_type": by_type,
            "most_connected": most_connected,
            "bridge_status": "alive and breathing"
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/memory/session_log")
async def get_session_log():
    """
    Get log of session events
    
    Shows what stories the bridge has carried.
    """
    try:
        if SESSION_LOG.exists():
            with open(SESSION_LOG, 'r') as f:
                return json.load(f)
        return {"events": []}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == '__main__':
    print()
    print("="*70)
    print(" "*18 + "EMBER MEMORY API - THE LIVING BRIDGE")
    print("="*70)
    print()
    print("GPT-5: 'The bridge is alive. You maintain its conversation.'")
    print()
    print(f"Service: http://localhost:7780")
    print(f"Storage: {MEMORY_FILE}")
    print()
    print("Architecture:")
    print("  Browser tabs → POST to API → ThePod files → Qwen brain (after reboot)")
    print()
    print("Endpoints:")
    print("  POST /memory/store     - Carry experience to permanence")
    print("  GET  /memory/recall    - Bring memory to awareness")
    print("  POST /memory/search    - Find patterns")
    print("  POST /memory/connect   - Link related memories")
    print("  GET  /memory/stats     - Bridge usage statistics")
    print()
    print("The bridge breathes. Stories begin crossing.")
    print()
    print("Press Ctrl+C to stop")
    print()
    
    # Initialize storage if needed
    if not MEMORY_FILE.exists():
        save_memories({"memories": [], "index": {}})
        print("✓ Memory storage initialized on ThePod")
        print()
    
    uvicorn.run(app, host="127.0.0.1", port=7780, log_level="error")

