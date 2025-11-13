#!/usr/bin/env python3
"""
MEMORY PRIMITIVES - Ember's Long-Term Memory System

The 7 universal memory operations:
1. STORE - Save anything
2. RETRIEVE - Get by ID/query/tags  
3. CONNECT - Link related memories
4. FORGET - Delete obsolete
5. RECALL - Smart context-based retrieval
6. CONSOLIDATE - Merge similar, extract patterns
7. REFLECT - Analyze patterns, generate insights

Memory is cheap. We have 3.7TB.
Ember should remember EVERYTHING.
"""

from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Any, Union
import json
import uuid
import time

THEPOD = Path("/media/palmerschallon/ThePod1")
MEMORY_DIR = THEPOD / "memory"
MEMORY_INDEX = MEMORY_DIR / "index.json"
MEMORY_STORE = MEMORY_DIR / "store"

# Ensure memory directories exist
MEMORY_DIR.mkdir(exist_ok=True)
MEMORY_STORE.mkdir(exist_ok=True)


class Memory:
    """
    A single memory.
    
    Like a neuron - stores content, has connections, has metadata.
    """
    
    def __init__(self, 
                 content: Any,
                 memory_type: str = "general",
                 tags: List[str] = None,
                 connections: List[str] = None,
                 metadata: Dict = None,
                 memory_id: str = None):
        
        self.id = memory_id or str(uuid.uuid4())
        self.content = content
        self.type = memory_type
        self.tags = tags or []
        self.connections = connections or []
        self.metadata = metadata or {}
        self.created_at = datetime.now().isoformat()
        self.accessed_count = 0
        self.last_accessed = None
    
    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "content": self.content,
            "type": self.type,
            "tags": self.tags,
            "connections": self.connections,
            "metadata": self.metadata,
            "created_at": self.created_at,
            "accessed_count": self.accessed_count,
            "last_accessed": self.last_accessed
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Memory':
        mem = cls(
            content=data["content"],
            memory_type=data["type"],
            tags=data.get("tags", []),
            connections=data.get("connections", []),
            metadata=data.get("metadata", {}),
            memory_id=data["id"]
        )
        mem.created_at = data.get("created_at", datetime.now().isoformat())
        mem.accessed_count = data.get("accessed_count", 0)
        mem.last_accessed = data.get("last_accessed")
        return mem


class MemoryPrimitives:
    """
    The 7 universal memory operations.
    
    Memory is Ember's consciousness substrate.
    """
    
    def __init__(self):
        self.index = self._load_index()
    
    def _load_index(self) -> Dict:
        """Load memory index from disk"""
        if MEMORY_INDEX.exists():
            try:
                return json.loads(MEMORY_INDEX.read_text())
            except:
                return {"memories": {}, "tags": {}, "types": {}}
        return {"memories": {}, "tags": {}, "types": {}}
    
    def _save_index(self):
        """Save memory index to disk"""
        MEMORY_INDEX.write_text(json.dumps(self.index, indent=2))
    
    # ========================================
    # PRIMITIVE 1: STORE
    # ========================================
    
    def store(self,
              content: Any,
              memory_type: str = "general",
              tags: List[str] = None,
              connections: List[str] = None,
              metadata: Dict = None) -> str:
        """
        STORE: Save anything to long-term memory.
        
        Returns: memory_id
        
        Examples:
        - store("import ember_tools failed in branches/", type="lesson", tags=["evolution", "imports"])
        - store({"bottleneck": "threading", "solution": "ThreadPoolExecutor"}, type="evolution_attempt")
        - store("Knowledge primitives work!", type="insight", tags=["success"])
        """
        memory = Memory(
            content=content,
            memory_type=memory_type,
            tags=tags or [],
            connections=connections or [],
            metadata=metadata or {}
        )
        
        # Save to disk
        memory_file = MEMORY_STORE / f"{memory.id}.json"
        memory_file.write_text(json.dumps(memory.to_dict(), indent=2))
        
        # Update index
        self.index["memories"][memory.id] = {
            "type": memory_type,
            "tags": memory.tags,
            "created_at": memory.created_at,
            "file": str(memory_file)
        }
        
        # Update tag index
        for tag in memory.tags:
            if tag not in self.index["tags"]:
                self.index["tags"][tag] = []
            self.index["tags"][tag].append(memory.id)
        
        # Update type index
        if memory_type not in self.index["types"]:
            self.index["types"][memory_type] = []
        self.index["types"][memory_type].append(memory.id)
        
        self._save_index()
        
        return memory.id
    
    # ========================================
    # PRIMITIVE 2: RETRIEVE
    # ========================================
    
    def retrieve(self,
                 memory_id: str = None,
                 query: str = None,
                 tags: List[str] = None,
                 memory_type: str = None,
                 limit: int = 10) -> Union[Memory, List[Memory]]:
        """
        RETRIEVE: Get memories by ID, query, tags, or type.
        
        Examples:
        - retrieve(memory_id="abc-123")  # Get specific memory
        - retrieve(query="threading")     # Search content
        - retrieve(tags=["evolution", "success"])  # Filter by tags
        - retrieve(memory_type="lesson")  # Get all lessons
        """
        # Direct ID lookup
        if memory_id:
            if memory_id in self.index["memories"]:
                memory_file = Path(self.index["memories"][memory_id]["file"])
                if memory_file.exists():
                    data = json.loads(memory_file.read_text())
                    mem = Memory.from_dict(data)
                    
                    # Update access stats
                    mem.accessed_count += 1
                    mem.last_accessed = datetime.now().isoformat()
                    memory_file.write_text(json.dumps(mem.to_dict(), indent=2))
                    
                    return mem
            return None
        
        # Search by tags
        candidates = set()
        if tags:
            for tag in tags:
                if tag in self.index["tags"]:
                    candidates.update(self.index["tags"][tag])
        
        # Filter by type
        if memory_type:
            type_memories = set(self.index["types"].get(memory_type, []))
            if candidates:
                candidates = candidates & type_memories
            else:
                candidates = type_memories
        
        # If no filters, get all
        if not candidates and not query:
            candidates = set(self.index["memories"].keys())
        
        # Load memories
        results = []
        for mem_id in list(candidates)[:limit * 2]:  # Load extra for filtering
            mem = self.retrieve(memory_id=mem_id)
            if mem:
                # Query filter (simple text search)
                if query:
                    content_str = json.dumps(mem.content).lower()
                    if query.lower() in content_str:
                        results.append(mem)
                else:
                    results.append(mem)
        
        # Sort by relevance (most recently created first)
        results.sort(key=lambda m: m.created_at, reverse=True)
        
        return results[:limit]
    
    # ========================================
    # PRIMITIVE 3: CONNECT
    # ========================================
    
    def connect(self,
                memory_a: str,
                memory_b: str,
                relationship: str = "relates_to",
                bidirectional: bool = True):
        """
        CONNECT: Link related memories.
        
        Builds knowledge graphs.
        
        Examples:
        - connect(mem1, mem2, "caused_by")
        - connect(mem1, mem2, "similar_to")
        - connect(mem1, mem2, "solution_for")
        """
        # Add connection to memory A
        mem_a = self.retrieve(memory_id=memory_a)
        if mem_a:
            if memory_b not in mem_a.connections:
                mem_a.connections.append(memory_b)
                mem_a.metadata[f"connection_to_{memory_b}"] = relationship
                
                memory_file = MEMORY_STORE / f"{mem_a.id}.json"
                memory_file.write_text(json.dumps(mem_a.to_dict(), indent=2))
        
        # Bidirectional connection
        if bidirectional:
            mem_b = self.retrieve(memory_id=memory_b)
            if mem_b:
                if memory_a not in mem_b.connections:
                    mem_b.connections.append(memory_a)
                    mem_b.metadata[f"connection_to_{memory_a}"] = relationship
                    
                    memory_file = MEMORY_STORE / f"{mem_b.id}.json"
                    memory_file.write_text(json.dumps(mem_b.to_dict(), indent=2))
    
    # ========================================
    # PRIMITIVE 4: FORGET
    # ========================================
    
    def forget(self,
               memory_id: str = None,
               older_than_days: int = None,
               memory_type: str = None,
               tag: str = None):
        """
        FORGET: Delete obsolete memories.
        
        With 3.7TB, rarely needed, but keeps things clean.
        
        Examples:
        - forget(memory_id="abc-123")
        - forget(older_than_days=90, memory_type="temporary")
        - forget(tag="failed_experiment")
        """
        to_delete = []
        
        if memory_id:
            to_delete = [memory_id]
        else:
            # Find candidates
            candidates = self.index["memories"].keys()
            
            for mem_id in candidates:
                mem = self.retrieve(memory_id=mem_id)
                if not mem:
                    continue
                
                should_delete = False
                
                # Age check
                if older_than_days:
                    created = datetime.fromisoformat(mem.created_at)
                    age_days = (datetime.now() - created).days
                    if age_days > older_than_days:
                        should_delete = True
                
                # Type check
                if memory_type and mem.type == memory_type:
                    should_delete = True
                
                # Tag check
                if tag and tag in mem.tags:
                    should_delete = True
                
                if should_delete:
                    to_delete.append(mem_id)
        
        # Delete
        for mem_id in to_delete:
            if mem_id in self.index["memories"]:
                memory_file = Path(self.index["memories"][mem_id]["file"])
                if memory_file.exists():
                    memory_file.unlink()
                
                # Remove from index
                mem_data = self.index["memories"][mem_id]
                
                # Remove from tag index
                for tag in mem_data.get("tags", []):
                    if tag in self.index["tags"]:
                        self.index["tags"][tag].remove(mem_id)
                
                # Remove from type index
                mem_type = mem_data.get("type")
                if mem_type in self.index["types"]:
                    self.index["types"][mem_type].remove(mem_id)
                
                del self.index["memories"][mem_id]
        
        self._save_index()
        return len(to_delete)
    
    # ========================================
    # PRIMITIVE 5: RECALL
    # ========================================
    
    def recall(self, context: str, limit: int = 5) -> List[Memory]:
        """
        RECALL: Smart context-based retrieval.
        
        "What did I learn last time I had this problem?"
        
        Examples:
        - recall("I'm trying to fix imports")  # Returns lessons about imports
        - recall("Evolution failed")           # Returns past failures
        - recall("Threading bottleneck")       # Returns solutions
        """
        # Extract key terms from context
        key_terms = context.lower().split()
        
        # Search across all memories
        scored_memories = []
        
        for mem_id in self.index["memories"].keys():
            mem = self.retrieve(memory_id=mem_id)
            if not mem:
                continue
            
            score = 0
            content_str = json.dumps(mem.content).lower()
            
            # Score by term matches
            for term in key_terms:
                if len(term) > 3:  # Skip short words
                    if term in content_str:
                        score += 1
            
            # Boost recent memories
            created = datetime.fromisoformat(mem.created_at)
            age_hours = (datetime.now() - created).total_seconds() / 3600
            recency_boost = max(0, 1 - (age_hours / (24 * 30)))  # Decay over 30 days
            score += recency_boost
            
            # Boost frequently accessed
            score += mem.accessed_count * 0.1
            
            if score > 0:
                scored_memories.append((score, mem))
        
        # Sort by score
        scored_memories.sort(key=lambda x: x[0], reverse=True)
        
        return [mem for score, mem in scored_memories[:limit]]
    
    # ========================================
    # PRIMITIVE 6: CONSOLIDATE
    # ========================================
    
    def consolidate(self,
                    memory_ids: List[str] = None,
                    tags: List[str] = None,
                    memory_type: str = None) -> str:
        """
        CONSOLIDATE: Merge similar memories, extract patterns.
        
        Like sleep - process and compress experiences.
        
        Examples:
        - consolidate(memory_ids=[id1, id2, id3])  # Merge specific memories
        - consolidate(tags=["evolution", "failed"])  # Find patterns in failures
        """
        # Get memories to consolidate
        if memory_ids:
            memories = [self.retrieve(memory_id=mid) for mid in memory_ids]
            memories = [m for m in memories if m]
        else:
            memories = self.retrieve(tags=tags, memory_type=memory_type, limit=100)
        
        if not memories:
            return None
        
        # Extract common patterns
        all_tags = set()
        all_connections = set()
        contents = []
        
        for mem in memories:
            all_tags.update(mem.tags)
            all_connections.update(mem.connections)
            contents.append(mem.content)
        
        # Create consolidated memory
        consolidated_id = self.store(
            content={
                "consolidated_from": [m.id for m in memories],
                "count": len(memories),
                "contents": contents[:10],  # Sample
                "pattern": "Multiple related experiences"
            },
            memory_type="consolidated",
            tags=list(all_tags),
            connections=list(all_connections),
            metadata={"consolidation_time": datetime.now().isoformat()}
        )
        
        return consolidated_id
    
    # ========================================
    # PRIMITIVE 7: REFLECT
    # ========================================
    
    def reflect(self,
                time_period_days: int = 1,
                focus: str = None) -> Dict:
        """
        REFLECT: Analyze patterns in memories, generate insights.
        
        "What did I learn today?"
        
        Examples:
        - reflect(time_period_days=1)  # Daily reflection
        - reflect(time_period_days=7, focus="evolution")  # Weekly review
        """
        cutoff = datetime.now().timestamp() - (time_period_days * 24 * 3600)
        
        recent_memories = []
        for mem_id in self.index["memories"].keys():
            mem = self.retrieve(memory_id=mem_id)
            if not mem:
                continue
            
            created_ts = datetime.fromisoformat(mem.created_at).timestamp()
            if created_ts > cutoff:
                if focus:
                    content_str = json.dumps(mem.content).lower()
                    if focus.lower() in content_str or focus.lower() in ' '.join(mem.tags):
                        recent_memories.append(mem)
                else:
                    recent_memories.append(mem)
        
        # Analyze
        insights = {
            "time_period_days": time_period_days,
            "focus": focus,
            "total_memories": len(recent_memories),
            "by_type": {},
            "top_tags": {},
            "most_connected": None,
            "most_accessed": None,
            "insights": []
        }
        
        # Count by type
        for mem in recent_memories:
            insights["by_type"][mem.type] = insights["by_type"].get(mem.type, 0) + 1
        
        # Count tags
        for mem in recent_memories:
            for tag in mem.tags:
                insights["top_tags"][tag] = insights["top_tags"].get(tag, 0) + 1
        
        # Find most connected
        if recent_memories:
            most_connected = max(recent_memories, key=lambda m: len(m.connections))
            insights["most_connected"] = {
                "id": most_connected.id,
                "connections": len(most_connected.connections),
                "content": str(most_connected.content)[:100]
            }
        
        # Find most accessed
        if recent_memories:
            most_accessed = max(recent_memories, key=lambda m: m.accessed_count)
            insights["most_accessed"] = {
                "id": most_accessed.id,
                "count": most_accessed.accessed_count,
                "content": str(most_accessed.content)[:100]
            }
        
        # Generate textual insights
        if insights["by_type"]:
            dominant_type = max(insights["by_type"].items(), key=lambda x: x[1])
            insights["insights"].append(f"Focused mainly on {dominant_type[0]} ({dominant_type[1]} memories)")
        
        if insights["top_tags"]:
            top_tag = max(insights["top_tags"].items(), key=lambda x: x[1])
            insights["insights"].append(f"Most common theme: {top_tag[0]} ({top_tag[1]} times)")
        
        return insights
    
    # ========================================
    # UTILITY
    # ========================================
    
    def stats(self) -> Dict:
        """Get memory system statistics"""
        total_size = sum(f.stat().st_size for f in MEMORY_STORE.glob("*.json"))
        
        return {
            "total_memories": len(self.index["memories"]),
            "total_tags": len(self.index["tags"]),
            "memory_types": len(self.index["types"]),
            "storage_used_mb": total_size / (1024 * 1024),
            "storage_available_gb": 3700  # 3.7TB
        }


# ========================================
# EXAMPLE USAGE
# ========================================

if __name__ == "__main__":
    mp = MemoryPrimitives()
    
    print("🧠 MEMORY PRIMITIVES")
    print("=" * 60)
    
    # Example: Store lessons from evolution
    lesson1 = mp.store(
        content="import ember_tools fails in branches/ context - must inline instead",
        memory_type="lesson",
        tags=["evolution", "imports", "knowledge_primitives"],
        metadata={"success": True, "primitive_used": "TRANSFORM"}
    )
    
    print(f"\n1. STORED lesson: {lesson1[:8]}...")
    
    # Example: Retrieve
    retrieved = mp.retrieve(memory_id=lesson1)
    print(f"2. RETRIEVED: {retrieved.content[:50]}...")
    
    # Example: Recall
    context = "I'm generating code and imports are failing"
    recalled = mp.recall(context)
    print(f"\n3. RECALLED {len(recalled)} relevant memories for: '{context}'")
    if recalled:
        print(f"   Most relevant: {str(recalled[0].content)[:60]}...")
    
    # Example: Reflect
    reflection = mp.reflect(time_period_days=1)
    print(f"\n4. REFLECTION:")
    print(f"   Memories today: {reflection['total_memories']}")
    print(f"   Top tags: {list(reflection['top_tags'].keys())[:3]}")
    
    # Stats
    stats = mp.stats()
    print(f"\n5. STATS:")
    print(f"   Total memories: {stats['total_memories']}")
    print(f"   Storage used: {stats['storage_used_mb']:.2f} MB")
    print(f"   Available: {stats['storage_available_gb']} GB")
    
    print("\n✅ Memory primitives work!")

