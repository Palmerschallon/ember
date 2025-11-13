#!/usr/bin/env python3
"""
Ember Concept Extractor v2

Better semantic understanding using:
- AST parsing for code
- NLP patterns for text  
- Domain-specific keywords
- Context-aware tagging
"""

import json
import ast
from pathlib import Path
import re

class ImprovedExtractor:
    # Expanded concept dictionaries
    CODE_PATTERNS = {
        'storage': ['save', 'store', 'write', 'persist', 'cache', 'db', 'database'],
        'retrieval': ['load', 'read', 'fetch', 'get', 'query', 'search', 'find'],
        'processing': ['process', 'transform', 'compute', 'calculate', 'parse'],
        'learning': ['train', 'learn', 'adapt', 'optimize', 'improve'],
        'memory': ['memory', 'remember', 'recall', 'history', 'past'],
        'state': ['state', 'status', 'current', 'active', 'session'],
        'tools': ['tool', 'function', 'method', 'utility', 'helper'],
        'connection': ['connect', 'network', 'api', 'request', 'socket'],
        'cognitive': ['think', 'cognitive', 'aware', 'conscious', 'mind'],
        'communication': ['message', 'chat', 'speak', 'talk', 'respond'],
        'visualization': ['display', 'render', 'show', 'draw', 'graph'],
        'monitoring': ['monitor', 'watch', 'track', 'observe', 'log'],
        'security': ['auth', 'secure', 'protect', 'encrypt', 'verify'],
        'analysis': ['analyze', 'evaluate', 'assess', 'measure', 'metric'],
    }
    
    AI_PATTERNS = {
        'ai_research': ['neural', 'llm', 'gpt', 'transformer', 'ai', 'ml', 'model'],
        'cognitive_science': ['consciousness', 'cognition', 'perception', 'psychology'],
        'programming': ['python', 'code', 'algorithm', 'function', 'class', 'syntax'],
        'data_science': ['dataset', 'training', 'feature', 'label', 'regression'],
    }
    
    def extract_from_text(self, text, metadata=None):
        """Extract concepts from any text"""
        text_lower = text.lower()
        concepts = set()
        
        # Check all patterns
        for concept, keywords in {**self.CODE_PATTERNS, **self.AI_PATTERNS}.items():
            if any(kw in text_lower for kw in keywords):
                concepts.add(concept)
        
        # Context-aware: if it's a filename/path, add structure concepts
        if metadata and 'source' in metadata:
            source = metadata['source'].lower()
            if 'state' in source or 'status' in source:
                concepts.add('state')
            if 'memory' in source or 'remember' in source:
                concepts.add('memory')
            if 'manifest' in source or 'index' in source:
                concepts.add('meta')
        
        # Semantic self-reference
        if any(w in text_lower for w in ['ember', 'self', 'itself', 'itself', 'my', 'i am']):
            concepts.add('self')
        
        # Documentation vs code vs data
        if metadata:
            file_type = metadata.get('type', '')
            if 'function' in file_type or 'class' in file_type:
                concepts.add('code')
            elif 'documentation' in file_type or 'readme' in text_lower:
                concepts.add('documentation')
            elif 'state' in file_type or 'json' in text_lower:
                concepts.add('data')
        
        return list(concepts) if concepts else ['general']
    
    def extract_from_code(self, code_text, file_ext='py'):
        """Parse code structure for better concepts"""
        concepts = set()
        
        if file_ext == 'py':
            try:
                tree = ast.parse(code_text)
                
                # Analyze AST
                for node in ast.walk(tree):
                    # Classes
                    if isinstance(node, ast.ClassDef):
                        name_lower = node.name.lower()
                        if 'memory' in name_lower:
                            concepts.add('memory')
                        if 'state' in name_lower:
                            concepts.add('state')
                        if 'tool' in name_lower:
                            concepts.add('tools')
                        if 'visual' in name_lower or 'ui' in name_lower:
                            concepts.add('visualization')
                    
                    # Function names
                    elif isinstance(node, ast.FunctionDef):
                        name_lower = node.name.lower()
                        for concept, keywords in self.CODE_PATTERNS.items():
                            if any(kw in name_lower for kw in keywords):
                                concepts.add(concept)
            except:
                pass  # Fall back to text analysis
        
        # Combine with text-based extraction
        text_concepts = self.extract_from_text(code_text)
        concepts.update(text_concepts)
        
        return list(concepts) if concepts else ['general']

def rebuild_mesh_with_better_concepts():
    """Rebuild semantic index with improved extraction"""
    
    print("\n🔧 Rebuilding mesh with improved concept extraction...\n")
    
    root = Path("/media/palmerschallon/ThePod1")
    mesh = root / "_mesh"
    extractor = ImprovedExtractor()
    
    updated = 0
    
    for chunk_file in mesh.glob("chunks/*.json"):
        with open(chunk_file) as f:
            chunk = json.load(f)
        
        # Skip if already has good concepts
        concepts = chunk.get('concepts', [])
        if concepts and concepts != ['general'] and len(concepts) > 1:
            continue
        
        # Re-extract
        data_file = chunk_file.with_suffix('.data')
        if data_file.exists():
            with open(data_file) as f:
                content = f.read()
        else:
            content = str(chunk)  # Use chunk metadata itself
        
        new_concepts = extractor.extract_from_text(content, chunk)
        
        if new_concepts != concepts:
            chunk['concepts'] = new_concepts
            with open(chunk_file, 'w') as f:
                json.dump(chunk, f, indent=2)
            updated += 1
            print(f"  ✓ {chunk.get('name', chunk_file.stem)}: {concepts} → {new_concepts}")
    
    print(f"\n✨ Updated {updated} chunks with better concepts\n")
    
    # Rebuild index
    from build_semantic_mesh import rebuild_index
    rebuild_index()

if __name__ == "__main__":
    rebuild_mesh_with_better_concepts()

