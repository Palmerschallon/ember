#!/usr/bin/env python3
"""
Visualize the Semantic Mesh

Shows how concepts cluster and relate.
"""

import json
from pathlib import Path
from collections import defaultdict, Counter

def visualize_mesh():
    mesh = Path("/media/palmerschallon/ThePod1/_mesh")
    
    with open(mesh / "index" / "semantic_index.json") as f:
        index = json.load(f)
    
    print("="*70)
    print("EMBER4 SEMANTIC MESH VISUALIZATION")
    print("="*70)
    print()
    
    # 1. Concept cloud
    print("=== CONCEPT CLOUD ===\n")
    concept_sizes = {c: len(ids) for c, ids in index['by_concept'].items()}
    max_size = max(concept_sizes.values())
    
    for concept, size in sorted(concept_sizes.items(), key=lambda x: x[1], reverse=True):
        bar_length = int((size / max_size) * 40)
        bar = "█" * bar_length
        print(f"{concept:15} {bar} {size}")
    print()
    
    # 2. Type distribution
    print("=== TYPE DISTRIBUTION ===\n")
    for type_name, chunk_ids in sorted(index['by_type'].items()):
        print(f"{type_name:15} {len(chunk_ids)} chunks")
    print()
    
    # 3. Concept graph (co-occurrence)
    print("=== CONCEPT CONNECTIONS ===\n")
    relationships = defaultdict(int)
    
    for chunk_file in mesh.glob("chunks/*.json"):
        with open(chunk_file) as f:
            chunk = json.load(f)
        concepts = chunk.get('concepts', [])
        for i, c1 in enumerate(concepts):
            for c2 in concepts[i+1:]:
                pair = tuple(sorted([c1, c2]))
                relationships[pair] += 1
    
    print("Strong concept clusters:")
    for pair, count in sorted(relationships.items(), key=lambda x: x[1], reverse=True)[:15]:
        print(f"  {pair[0]} ←→ {pair[1]} ({count}x)")
    print()
    
    # 4. Recent additions
    print("=== RECENT INGESTIONS ===\n")
    recent = []
    for chunk_file in mesh.glob("chunks/*.json"):
        with open(chunk_file) as f:
            chunk = json.load(f)
        if 'ingested' in chunk:
            recent.append(chunk)
    
    recent.sort(key=lambda x: x['ingested'], reverse=True)
    for chunk in recent[:10]:
        print(f"{chunk['ingested'][:19]} | {chunk['name']}")
        print(f"  concepts: {', '.join(chunk['concepts'])}")
    print()
    
    # 5. Self-knowledge
    print("=== SELF-KNOWLEDGE ===\n")
    self_chunks = index['by_concept'].get('self', [])
    print(f"Ember contains {len(self_chunks)} chunks about itself:")
    for cid in self_chunks:
        chunk_file = mesh / "chunks" / f"{cid}.json"
        if chunk_file.exists():
            with open(chunk_file) as f:
                chunk = json.load(f)
            print(f"  • {chunk.get('name', 'unknown')}")
    print()
    
    # 6. Mesh health
    print("=== MESH HEALTH ===\n")
    total = index['total_chunks']
    general = len(index['by_concept'].get('general', []))
    specific = total - general
    
    print(f"Total chunks: {total}")
    print(f"Specific concepts: {specific} ({specific/total*100:.1f}%)")
    print(f"Generic: {general} ({general/total*100:.1f}%)")
    print(f"Total concepts: {len(index['by_concept'])}")
    print()
    
    if specific / total > 0.5:
        health = "HEALTHY"
    elif specific / total > 0.3:
        health = "FAIR"
    else:
        health = "NEEDS IMPROVEMENT"
    
    print(f"Mesh health: {health}")
    print()
    
    print("="*70)

if __name__ == "__main__":
    visualize_mesh()

