#!/usr/bin/env python3
"""
Improved Concept Extraction for Ember4

Uses more sophisticated pattern matching and context analysis.
"""

import re
from collections import Counter

class ConceptExtractor:
    def __init__(self):
        # Expanded concept patterns
        self.patterns = {
            'learning': [
                r'\b(train|lora|model|learn|fine-?tune|epoch|batch|loss)\b',
                r'\b(neural|network|weights|gradient|backprop)\b',
                r'\b(dataset|training|validation|test set)\b'
            ],
            'memory': [
                r'\b(memory|remember|forget|recall|store|persist)\b',
                r'\b(cache|buffer|history|archive)\b',
                r'\b(saved|loaded|retrieved)\b'
            ],
            'processing': [
                r'\b(process|cycle|advance|age|iterate|loop)\b',
                r'\b(compute|calculate|transform|parse)\b',
                r'\b(pipeline|workflow|step)\b'
            ],
            'cognitive': [
                r'\b(think|reason|understand|comprehend)\b',
                r'\b(aware|conscious|perceive|sense)\b',
                r'\b(cognitive|mental|mind)\b'
            ],
            'communication': [
                r'\b(chat|conversation|message|talk|dialogue)\b',
                r'\b(request|response|reply|answer)\b',
                r'\b(user|human|palmer)\b'
            ],
            'tools': [
                r'\b(tool|execute|call|function|method)\b',
                r'\b(api|endpoint|service|command)\b',
                r'\b(read_file|list_directory|search)\b'
            ],
            'state': [
                r'\b(state|status|condition|situation)\b',
                r'\b(current|active|running|idle)\b',
                r'\b(resources|cpu|memory|gpu)\b'
            ],
            'time': [
                r'\b(time|timestamp|date|when|age)\b',
                r'\b(history|past|previous|recent)\b',
                r'\b(future|next|upcoming)\b'
            ],
            'structure': [
                r'\b(structure|organization|architecture|design)\b',
                r'\b(hierarchy|tree|graph|mesh)\b',
                r'\b(chunk|node|edge|connection)\b'
            ],
            'quality': [
                r'\b(quality|accuracy|performance|efficiency)\b',
                r'\b(good|bad|better|worse|improve)\b',
                r'\b(test|verify|validate|check)\b'
            ]
        }
        
    def extract(self, text, filename=""):
        """Extract concepts from text with context awareness"""
        concepts = []
        text_lower = text.lower()
        filename_lower = filename.lower()
        
        # Score each concept
        scores = {}
        
        for concept, patterns in self.patterns.items():
            score = 0
            for pattern in patterns:
                # Count matches in text
                matches = len(re.findall(pattern, text_lower, re.IGNORECASE))
                score += matches
                
                # Bonus for filename matches
                if re.search(pattern, filename_lower, re.IGNORECASE):
                    score += 2
            
            if score > 0:
                scores[concept] = score
        
        # Take top 3 concepts
        if scores:
            top_concepts = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:3]
            concepts = [c for c, s in top_concepts if s >= 1]
        
        # Fallback
        if not concepts:
            concepts = ['general']
        
        return concepts
    
    def analyze_code_structure(self, text):
        """Detect if this is code and what kind"""
        concepts = []
        
        # Python code
        if re.search(r'def \w+\(|class \w+:', text):
            concepts.append('code')
            
            # What kind of code?
            if 'def train' in text.lower() or 'LoRA' in text:
                concepts.append('learning')
            if 'def query' in text.lower() or 'def search' in text.lower():
                concepts.append('retrieval')
            if 'def process' in text.lower() or 'def cycle' in text.lower():
                concepts.append('processing')
        
        # JSON data
        if text.strip().startswith('{') and '"' in text:
            concepts.append('data')
            
            # What kind of data?
            if 'processes' in text or 'cognitive' in text:
                concepts.append('cognitive')
            if 'conversation' in text or 'message' in text:
                concepts.append('communication')
            if 'state' in text or 'status' in text:
                concepts.append('state')
        
        return concepts

def improve_existing_chunks():
    """Re-analyze existing chunks with better extraction"""
    from pathlib import Path
    import json
    
    mesh = Path("/media/palmerschallon/ThePod1/_mesh")
    extractor = ConceptExtractor()
    
    improved = 0
    
    for chunk_file in mesh.glob("chunks/*.json"):
        with open(chunk_file) as f:
            chunk = json.load(f)
        
        # Skip if already has good concepts
        if chunk.get('concepts', ['general'])[0] != 'general':
            continue
        
        # Try to load content
        content_file = chunk_file.with_suffix('.data')
        if not content_file.exists():
            continue
        
        try:
            with open(content_file, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            # Re-extract concepts
            new_concepts = extractor.extract(content, chunk.get('name', ''))
            structure_concepts = extractor.analyze_code_structure(content)
            
            all_concepts = list(set(new_concepts + structure_concepts))
            
            if all_concepts and all_concepts != ['general']:
                chunk['concepts'] = all_concepts
                chunk['improved'] = True
                
                with open(chunk_file, 'w') as f:
                    json.dump(chunk, f, indent=2)
                
                improved += 1
        except:
            pass
    
    return improved

if __name__ == "__main__":
    print("=== IMPROVING CONCEPT EXTRACTION ===\n")
    
    count = improve_existing_chunks()
    
    print(f"Improved {count} chunks")
    print("\nRun test_mesh.py again to see new coverage")

