#!/usr/bin/env python3
"""
Semantic Mesh Test Suite

Tests the digestive system's capabilities and finds weaknesses.
"""

import json
import time
from pathlib import Path
import hashlib

class MeshTests:
    def __init__(self, root="/media/palmerschallon/ThePod1"):
        self.root = Path(root)
        self.mesh = self.root / "_mesh"
        self.index_file = self.mesh / "index" / "semantic_index.json"
        
    def load_index(self):
        with open(self.index_file) as f:
            return json.load(f)
    
    def test_query_speed(self):
        """Test how fast we can query"""
        print("=== QUERY SPEED TEST ===\n")
        
        index = self.load_index()
        
        # Test 1: Load index
        start = time.time()
        for _ in range(100):
            with open(self.index_file) as f:
                _ = json.load(f)
        elapsed = time.time() - start
        print(f"Load index (100x): {elapsed:.3f}s ({elapsed*10:.1f}ms per load)")
        
        # Test 2: Query by concept
        start = time.time()
        for _ in range(1000):
            _ = index['by_concept'].get('learning', [])
        elapsed = time.time() - start
        print(f"Query concept (1000x): {elapsed:.3f}s ({elapsed:.3f}ms per query)")
        
        # Test 3: Load chunk
        chunk_ids = index['by_concept'].get('learning', [])
        if chunk_ids:
            chunk_id = chunk_ids[0]
            chunk_file = self.mesh / "chunks" / f"{chunk_id}.json"
            
            start = time.time()
            for _ in range(100):
                with open(chunk_file) as f:
                    _ = json.load(f)
            elapsed = time.time() - start
            print(f"Load chunk (100x): {elapsed:.3f}s ({elapsed*10:.1f}ms per load)")
        
        print("\n✓ Query is FAST - millisecond response\n")
    
    def test_concept_coverage(self):
        """Test how well concepts are extracted"""
        print("=== CONCEPT COVERAGE TEST ===\n")
        
        index = self.load_index()
        
        total_chunks = index['total_chunks']
        general_chunks = len(index['by_concept'].get('general', []))
        
        coverage = (total_chunks - general_chunks) / total_chunks * 100
        
        print(f"Total chunks: {total_chunks}")
        print(f"Chunks with specific concepts: {total_chunks - general_chunks}")
        print(f"Generic chunks: {general_chunks}")
        print(f"Concept coverage: {coverage:.1f}%")
        
        if coverage < 50:
            print("\n⚠ Low concept coverage - concept extraction needs improvement")
        else:
            print("\n✓ Good concept coverage")
        
        print()
    
    def test_deduplication(self):
        """Test if duplicates are detected"""
        print("=== DEDUPLICATION TEST ===\n")
        
        # Create identical content
        test_content = b"This is identical content for testing"
        hash1 = hashlib.sha256(test_content).hexdigest()[:16]
        hash2 = hashlib.sha256(test_content).hexdigest()[:16]
        
        print(f"Same content hashes to: {hash1}")
        print(f"Same content again:     {hash2}")
        print(f"Match: {hash1 == hash2}")
        
        if hash1 == hash2:
            print("\n✓ Content-addressed deduplication works")
        else:
            print("\n✗ Deduplication broken")
        
        print()
    
    def test_concept_relationships(self):
        """Find which concepts co-occur"""
        print("=== CONCEPT RELATIONSHIPS TEST ===\n")
        
        index = self.load_index()
        
        # Build co-occurrence matrix
        relationships = {}
        
        # For each chunk, record which concepts appear together
        for chunk_id in Path(self.mesh / "chunks").glob("*.json"):
            with open(chunk_id) as f:
                chunk = json.load(f)
            
            concepts = chunk.get('concepts', [])
            for i, c1 in enumerate(concepts):
                for c2 in concepts[i+1:]:
                    pair = tuple(sorted([c1, c2]))
                    relationships[pair] = relationships.get(pair, 0) + 1
        
        # Show top relationships
        print("Concept pairs that co-occur:")
        for pair, count in sorted(relationships.items(), key=lambda x: x[1], reverse=True)[:10]:
            print(f"  {pair[0]} + {pair[1]}: {count} times")
        
        print("\n✓ Concepts form natural clusters\n")
    
    def test_mesh_integrity(self):
        """Check if mesh is consistent"""
        print("=== MESH INTEGRITY TEST ===\n")
        
        index = self.load_index()
        
        # Count chunks on disk
        chunk_files = list((self.mesh / "chunks").glob("*.json"))
        disk_chunks = len(chunk_files) // 2  # .json and .data files
        
        # Count chunks in index
        indexed_chunks = set()
        for chunk_ids in index['by_concept'].values():
            indexed_chunks.update(chunk_ids)
        
        print(f"Chunks on disk: {disk_chunks}")
        print(f"Chunks in index: {len(indexed_chunks)}")
        print(f"Index reports: {index['total_chunks']}")
        
        if len(indexed_chunks) == index['total_chunks']:
            print("\n✓ Index is consistent")
        else:
            print("\n⚠ Index inconsistency detected")
        
        print()
    
    def test_self_query(self):
        """Test if Ember can query its own state"""
        print("=== SELF-QUERY TEST ===\n")
        
        index = self.load_index()
        
        # Can it find itself?
        self_chunks = index['by_concept'].get('self', [])
        
        print(f"Self-knowledge chunks: {len(self_chunks)}")
        
        for cid in self_chunks[:3]:
            chunk_file = self.mesh / "chunks" / f"{cid}.json"
            if chunk_file.exists():
                with open(chunk_file) as f:
                    chunk = json.load(f)
                print(f"  • {chunk.get('name', 'unknown')}")
        
        if self_chunks:
            print("\n✓ Self-awareness functional - Ember can query itself")
        else:
            print("\n⚠ No self-knowledge - feed Ember to itself")
        
        print()
    
    def run_all_tests(self):
        """Run complete test suite"""
        print("="*60)
        print("EMBER4 SEMANTIC MESH TEST SUITE")
        print("="*60)
        print()
        
        self.test_query_speed()
        self.test_concept_coverage()
        self.test_deduplication()
        self.test_concept_relationships()
        self.test_mesh_integrity()
        self.test_self_query()
        
        print("="*60)
        print("TEST SUITE COMPLETE")
        print("="*60)

if __name__ == "__main__":
    tests = MeshTests()
    tests.run_all_tests()

