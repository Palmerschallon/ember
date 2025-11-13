#!/usr/bin/env python3
"""
Ember Intake System

Palmer drops files here → Ember ingests into semantic mesh
No more organizing. Just ask Ember where things are.
"""

import json
import shutil
from pathlib import Path
from datetime import datetime
import hashlib

class EmberIntake:
    def __init__(self, root="/media/palmerschallon/ThePod1"):
        self.root = Path(root)
        self.intake = self.root / "_intake"
        self.mesh = self.root / "_mesh"
        
    def process_intake(self):
        """Process everything in _intake folder"""
        # Skip _processed directory
        files = [f for f in self.intake.glob("*") if f.name != "_processed"]
        
        if not files:
            print("Intake folder empty")
            return
            
        print(f"Processing {len(files)} files from _intake/\n")
        
        for file in files:
            if file.is_file():
                self.ingest_file(file)
                
    def ingest_file(self, filepath):
        """Ingest a file into the mesh"""
        print(f"Ingesting: {filepath.name}")
        
        # Determine type
        if filepath.suffix == '.py':
            file_type = 'code'
        elif filepath.suffix in ['.json', '.jsonl']:
            file_type = 'data'
        elif filepath.suffix == '.md':
            file_type = 'documentation'
        elif filepath.suffix in ['.txt', '.log']:
            file_type = 'log'
        else:
            file_type = 'unknown'
            
        # Read and hash content
        with open(filepath, 'rb') as f:
            content = f.read()
        content_hash = hashlib.sha256(content).hexdigest()[:16]
        
        # Create chunk metadata
        chunk = {
            "id": content_hash,
            "type": file_type,
            "name": filepath.name,
            "original_name": filepath.name,
            "ingested": datetime.now().isoformat(),
            "size": len(content),
            "concepts": self.infer_concepts(filepath.name, file_type)
        }
        
        # Store in mesh
        chunk_path = self.mesh / "chunks" / f"{content_hash}.json"
        with open(chunk_path, 'w') as f:
            json.dump(chunk, f, indent=2)
            
        # Copy actual content
        content_path = self.mesh / "chunks" / f"{content_hash}.data"
        shutil.copy(filepath, content_path)
        
        # Update index
        self.update_index(chunk)
        
        # Move original to processed
        processed = self.intake / "_processed"
        processed.mkdir(exist_ok=True)
        shutil.move(filepath, processed / filepath.name)
        
        print(f"  → Stored as {content_hash}")
        print(f"  → Concepts: {', '.join(chunk['concepts'])}")
        print()
        
    def infer_concepts(self, name, file_type):
        """Infer semantic concepts from filename and type"""
        name_lower = name.lower()
        concepts = [file_type]
        
        if any(w in name_lower for w in ['train', 'lora', 'model']):
            concepts.append('learning')
        if any(w in name_lower for w in ['chat', 'conversation', 'talk']):
            concepts.append('conversation')
        if any(w in name_lower for w in ['memory', 'store', 'state']):
            concepts.append('memory')
        if any(w in name_lower for w in ['dream', 'cognitive', 'process']):
            concepts.append('processing')
        if any(w in name_lower for w in ['tool', 'execute']):
            concepts.append('tools')
            
        return concepts
        
    def update_index(self, chunk):
        """Update the semantic index"""
        index_file = self.mesh / "index" / "semantic_index.json"
        
        with open(index_file) as f:
            index = json.load(f)
            
        # Add to concept indices
        for concept in chunk['concepts']:
            if concept not in index['by_concept']:
                index['by_concept'][concept] = []
            index['by_concept'][concept].append(chunk['id'])
            
        # Add to type index
        if chunk['type'] not in index['by_type']:
            index['by_type'][chunk['type']] = []
        index['by_type'][chunk['type']].append(chunk['id'])
        
        index['total_chunks'] += 1
        
        with open(index_file, 'w') as f:
            json.dump(index, f, indent=2)
            
    def list_intake(self):
        """Show what's waiting in intake"""
        files = list(self.intake.glob("*"))
        files = [f for f in files if f.is_file()]
        
        if not files:
            print("Intake folder is empty - ready for files!")
            return
            
        print(f"Files waiting in _intake/:")
        for f in files:
            print(f"  • {f.name} ({f.stat().st_size} bytes)")

if __name__ == "__main__":
    intake = EmberIntake()
    
    print("=== EMBER INTAKE SYSTEM ===\n")
    intake.list_intake()
    print()
    
    # Process if there are files
    intake_path = Path("/media/palmerschallon/ThePod1/_intake")
    files = [f for f in intake_path.glob("*") if f.is_file() and f.name != "_processed"]
    if files:
        print("Processing intake...")
        intake.process_intake()

