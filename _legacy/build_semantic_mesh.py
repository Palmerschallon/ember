#!/usr/bin/env python3
"""
Semantic Mesh Builder for Ember4

Breaks rigid file boundaries into fluid semantic chunks.
Chunks cluster by meaning, not location.
"""

import ast
import json
import hashlib
from pathlib import Path
from collections import defaultdict
from datetime import datetime

class SemanticMesh:
    def __init__(self, root_path="."):
        self.root = Path(root_path)
        self.chunks = {}
        self.index = {
            "by_concept": defaultdict(list),
            "by_source": defaultdict(list),
            "by_type": defaultdict(list)
        }
        
    def chunk_id(self, content):
        """Content-addressable: hash determines ID"""
        return hashlib.sha256(content.encode()).hexdigest()[:16]
    
    def extract_python_chunks(self, filepath):
        """Extract functions and classes from Python files"""
        chunks = []
        try:
            with open(filepath) as f:
                content = f.read()
                tree = ast.parse(content)
                
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    # Get function source
                    func_lines = content.split('\n')[node.lineno-1:node.end_lineno]
                    func_source = '\n'.join(func_lines)
                    
                    chunk_id = self.chunk_id(func_source)
                    
                    # Infer concept from name
                    concepts = self.infer_concepts(node.name)
                    
                    chunk = {
                        "id": chunk_id,
                        "type": "function",
                        "name": node.name,
                        "source": str(filepath),
                        "location": f"{filepath.name}::{node.name}()",
                        "line": node.lineno,
                        "concepts": concepts,
                        "content": func_source,
                        "docstring": ast.get_docstring(node),
                        "created": datetime.now().isoformat()
                    }
                    chunks.append(chunk)
                    
                elif isinstance(node, ast.ClassDef):
                    class_lines = content.split('\n')[node.lineno-1:node.end_lineno]
                    class_source = '\n'.join(class_lines)
                    chunk_id = self.chunk_id(class_source)
                    
                    concepts = self.infer_concepts(node.name)
                    
                    chunk = {
                        "id": chunk_id,
                        "type": "class",
                        "name": node.name,
                        "source": str(filepath),
                        "location": f"{filepath.name}::{node.name}",
                        "line": node.lineno,
                        "concepts": concepts,
                        "content": class_source[:500],  # Truncate classes
                        "docstring": ast.get_docstring(node),
                        "created": datetime.now().isoformat()
                    }
                    chunks.append(chunk)
                    
        except Exception as e:
            print(f"Error parsing {filepath}: {e}")
            
        return chunks
    
    def extract_json_chunks(self, filepath):
        """Extract objects from JSON files"""
        chunks = []
        try:
            with open(filepath) as f:
                data = json.load(f)
                
            def extract_objects(obj, path=""):
                if isinstance(obj, dict):
                    for key, value in obj.items():
                        obj_str = json.dumps(value, indent=2)
                        chunk_id = self.chunk_id(obj_str)
                        
                        full_path = f"{path}.{key}" if path else key
                        
                        chunk = {
                            "id": chunk_id,
                            "type": "state_object",
                            "name": key,
                            "source": str(filepath),
                            "location": f"{filepath.name}::{full_path}",
                            "concepts": self.infer_concepts(key),
                            "content": obj_str[:500],
                            "data_type": type(value).__name__,
                            "created": datetime.now().isoformat()
                        }
                        chunks.append(chunk)
                        
                        # Recurse for nested objects
                        if isinstance(value, dict):
                            extract_objects(value, full_path)
                            
            extract_objects(data)
                    
        except Exception as e:
            print(f"Error parsing {filepath}: {e}")
            
        return chunks
    
    def infer_concepts(self, name):
        """Infer semantic concepts from names"""
        name_lower = name.lower()
        concepts = []
        
        # Storage concepts
        if any(w in name_lower for w in ['store', 'save', 'write', 'persist']):
            concepts.append('storage')
        
        # Retrieval concepts
        if any(w in name_lower for w in ['get', 'load', 'read', 'retrieve', 'fetch']):
            concepts.append('retrieval')
            
        # Learning concepts
        if any(w in name_lower for w in ['train', 'learn', 'lora', 'model']):
            concepts.append('learning')
            
        # Processing concepts
        if any(w in name_lower for w in ['process', 'cycle', 'advance', 'age']):
            concepts.append('processing')
            
        # Connection concepts
        if any(w in name_lower for w in ['connect', 'link', 'relate', 'bind']):
            concepts.append('connection')
            
        # State concepts
        if any(w in name_lower for w in ['state', 'status', 'cognitive']):
            concepts.append('state')
            
        # Memory concepts
        if any(w in name_lower for w in ['memory', 'remember', 'forget', 'recall']):
            concepts.append('memory')
            
        # Tool concepts
        if any(w in name_lower for w in ['tool', 'execute', 'call']):
            concepts.append('tools')
            
        return concepts if concepts else ['general']
    
    def build_mesh(self):
        """Build the complete semantic mesh"""
        print("Building semantic mesh...")
        
        # Extract from Python files
        for py_file in self.root.glob("*.py"):
            if py_file.name.startswith('_'):
                continue
            chunks = self.extract_python_chunks(py_file)
            for chunk in chunks:
                self.add_chunk(chunk)
                
        # Extract from JSON files
        for json_file in [self.root / f for f in ['dream_state.json', 'ember_status.json', 'MANIFEST.json']]:
            if json_file.exists():
                chunks = self.extract_json_chunks(json_file)
                for chunk in chunks:
                    self.add_chunk(chunk)
                    
        print(f"Extracted {len(self.chunks)} chunks")
        
    def add_chunk(self, chunk):
        """Add chunk to mesh and update indices"""
        chunk_id = chunk['id']
        self.chunks[chunk_id] = chunk
        
        # Index by concept
        for concept in chunk.get('concepts', []):
            self.index['by_concept'][concept].append(chunk_id)
            
        # Index by source
        self.index['by_source'][chunk['source']].append(chunk_id)
        
        # Index by type
        self.index['by_type'][chunk['type']].append(chunk_id)
        
        # Save chunk to disk (content-addressed)
        chunk_path = self.root / "_mesh" / "chunks" / f"{chunk_id}.json"
        with open(chunk_path, 'w') as f:
            json.dump(chunk, f, indent=2)
    
    def query(self, concept):
        """Query mesh by concept"""
        chunk_ids = self.index['by_concept'].get(concept, [])
        return [self.chunks[cid] for cid in chunk_ids]
    
    def trace_flow(self, start_concept):
        """Trace flow between related concepts"""
        # Simple version: find chunks that share concepts
        flows = defaultdict(list)
        
        for concept in self.index['by_concept'].keys():
            chunks = self.query(concept)
            if len(chunks) > 1:
                flows[concept] = [c['location'] for c in chunks]
                
        return flows
    
    def save_index(self):
        """Save the index"""
        index_path = self.root / "_mesh" / "index" / "semantic_index.json"
        
        # Convert defaultdict to dict for JSON
        index_json = {
            "by_concept": dict(self.index['by_concept']),
            "by_source": dict(self.index['by_source']),
            "by_type": dict(self.index['by_type']),
            "total_chunks": len(self.chunks),
            "created": datetime.now().isoformat()
        }
        
        with open(index_path, 'w') as f:
            json.dump(index_json, f, indent=2)
            
        print(f"Saved index to {index_path}")
        
    def print_summary(self):
        """Print mesh summary"""
        print("\n=== SEMANTIC MESH SUMMARY ===\n")
        print(f"Total chunks: {len(self.chunks)}")
        print(f"\nBy type:")
        for type_name, chunk_ids in self.index['by_type'].items():
            print(f"  {type_name}: {len(chunk_ids)}")
            
        print(f"\nBy concept:")
        for concept, chunk_ids in sorted(self.index['by_concept'].items(), 
                                         key=lambda x: len(x[1]), reverse=True):
            print(f"  {concept}: {len(chunk_ids)} chunks")
            
        print(f"\nSample queries:")
        for concept in ['storage', 'learning', 'state']:
            chunks = self.query(concept)
            print(f"\n  Query '{concept}':")
            for chunk in chunks[:3]:
                print(f"    • {chunk['location']}")

if __name__ == "__main__":
    mesh = SemanticMesh("/media/palmerschallon/ThePod1")
    mesh.build_mesh()
    mesh.save_index()
    mesh.print_summary()

