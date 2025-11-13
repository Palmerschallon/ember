#!/usr/bin/env python3
"""
Semantic Mesh Query Interface

Fast proprioception for AI - query by concept, not location.
"""

import json
from pathlib import Path
from collections import defaultdict

class MeshQuery:
    def __init__(self, mesh_root="_mesh"):
        self.mesh_root = Path(mesh_root)
        self.load_index()
        
    def load_index(self):
        index_file = self.mesh_root / "index" / "semantic_index.json"
        with open(index_file) as f:
            self.index = json.load(f)
            
    def query(self, concept):
        """Query mesh by concept - returns chunks"""
        chunk_ids = self.index['by_concept'].get(concept, [])
        chunks = []
        for cid in chunk_ids:
            chunk_file = self.mesh_root / "chunks" / f"{cid}.json"
            if chunk_file.exists():
                with open(chunk_file) as f:
                    chunks.append(json.load(f))
        return chunks
    
    def trace_flow(self, start_concept, depth=2):
        """Trace flow between concepts"""
        flows = {start_concept: self.query(start_concept)}
        
        # Find related concepts
        related = set()
        for chunk in flows[start_concept]:
            related.update(chunk.get('concepts', []))
            
        # Get chunks for related concepts
        for concept in related:
            if concept != start_concept:
                flows[concept] = self.query(concept)
                
        return flows
    
    def find_by_name(self, name_part):
        """Find chunks by name substring"""
        results = []
        for chunk_id in Path(self.mesh_root / "chunks").glob("*.json"):
            with open(chunk_id) as f:
                chunk = json.load(f)
            if name_part.lower() in chunk.get('name', '').lower():
                results.append(chunk)
        return results
    
    def system_overview(self):
        """Get complete system overview from mesh"""
        overview = {
            "total_chunks": self.index['total_chunks'],
            "concepts": {}
        }
        
        for concept, chunk_ids in self.index['by_concept'].items():
            overview['concepts'][concept] = {
                "count": len(chunk_ids),
                "locations": []
            }
            
            # Sample locations
            for cid in chunk_ids[:5]:
                chunk_file = self.mesh_root / "chunks" / f"{cid}.json"
                if chunk_file.exists():
                    with open(chunk_file) as f:
                        chunk = json.load(f)
                    overview['concepts'][concept]['locations'].append(chunk['location'])
                    
        return overview

if __name__ == "__main__":
    mesh = MeshQuery()
    
    print("=== SEMANTIC MESH QUERY DEMO ===\n")
    
    # Query 1: Show storage system
    print("Query: 'storage'")
    storage = mesh.query('storage')
    for chunk in storage:
        print(f"  {chunk['location']}")
    print()
    
    # Query 2: Trace tool_use flow
    print("Query: trace 'tools' flow")
    flow = mesh.trace_flow('tools')
    for concept, chunks in flow.items():
        print(f"  [{concept}]")
        for chunk in chunks[:3]:
            print(f"    • {chunk['location']}")
    print()
    
    # Query 3: Find by name
    print("Query: find 'train'")
    train_chunks = mesh.find_by_name('train')
    for chunk in train_chunks[:5]:
        print(f"  {chunk['type']:12} | {chunk['location']}")
    print()
    
    # Query 4: System overview
    print("System Overview:")
    overview = mesh.system_overview()
    print(f"  Total chunks: {overview['total_chunks']}")
    print(f"  Concepts: {len(overview['concepts'])}")
    for concept in ['storage', 'learning', 'processing']:
        if concept in overview['concepts']:
            print(f"    {concept}: {overview['concepts'][concept]['count']} chunks")

