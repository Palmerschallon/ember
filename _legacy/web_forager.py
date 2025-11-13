#!/usr/bin/env python3
"""
Ember Web Forager - Digestive System Meets Internet

Crawls web → extracts novel information → discards duplicates
Only keeps what's NEW to Ember's understanding.
"""

import hashlib
import json
from pathlib import Path
from datetime import datetime
import urllib.request
import urllib.parse
from html.parser import HTMLParser

class HTMLTextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []
        
    def handle_data(self, data):
        self.text.append(data.strip())
        
    def get_text(self):
        return ' '.join([t for t in self.text if t])

class WebForager:
    def __init__(self, root="/media/palmerschallon/ThePod1"):
        self.root = Path(root)
        self.mesh = self.root / "_mesh"
        self.cache = self.root / "_web_cache"
        self.cache.mkdir(exist_ok=True)
        
        # Load existing knowledge
        with open(self.mesh / "index" / "semantic_index.json") as f:
            self.index = json.load(f)
        
        # Track what we already know
        self.known_hashes = set()
        for chunk_file in self.mesh.glob("chunks/*.json"):
            with open(chunk_file) as f:
                chunk = json.load(f)
                self.known_hashes.add(chunk['id'])
    
    def is_novel(self, content):
        """Check if content is new to Ember"""
        content_hash = hashlib.sha256(content.encode()).hexdigest()[:16]
        return content_hash not in self.known_hashes
    
    def fetch_url(self, url):
        """Fetch and extract text from URL"""
        try:
            with urllib.request.urlopen(url, timeout=5) as response:
                html = response.read().decode('utf-8', errors='ignore')
                
            # Extract text from HTML
            parser = HTMLTextExtractor()
            parser.feed(html)
            text = parser.get_text()
            
            return text
        except Exception as e:
            return None
    
    def extract_concepts(self, text):
        """Extract concepts from web content"""
        text_lower = text.lower()
        concepts = []
        
        # AI/ML concepts
        if any(w in text_lower for w in ['neural network', 'machine learning', 'deep learning', 'ai', 'llm', 'transformer']):
            concepts.append('ai_research')
        
        # Programming concepts
        if any(w in text_lower for w in ['python', 'javascript', 'code', 'function', 'algorithm']):
            concepts.append('programming')
            
        # Cognitive science
        if any(w in text_lower for w in ['consciousness', 'cognition', 'mind', 'brain', 'neural']):
            concepts.append('cognitive_science')
            
        # Data/systems
        if any(w in text_lower for w in ['database', 'architecture', 'system design', 'infrastructure']):
            concepts.append('systems')
        
        return concepts if concepts else ['web_content']
    
    def digest_url(self, url):
        """Fetch, analyze, decide if novel, ingest if yes"""
        print(f"\nForaging: {url}")
        
        text = self.fetch_url(url)
        if not text:
            print("  ✗ Failed to fetch")
            return False
        
        print(f"  → Fetched {len(text)} bytes")
        
        # Check novelty
        if not self.is_novel(text):
            print("  ⊗ Duplicate - already known")
            return False
        
        print("  ✓ NOVEL - digesting...")
        
        # Extract concepts
        concepts = self.extract_concepts(text)
        print(f"  → Concepts: {', '.join(concepts)}")
        
        # Create chunk
        content_hash = hashlib.sha256(text.encode()).hexdigest()[:16]
        chunk = {
            "id": content_hash,
            "type": "web_content",
            "name": url.split('//')[-1][:50],
            "source": url,
            "ingested": datetime.now().isoformat(),
            "size": len(text),
            "concepts": concepts,
            "origin": "web_forage"
        }
        
        # Save
        chunk_path = self.mesh / "chunks" / f"{content_hash}.json"
        with open(chunk_path, 'w') as f:
            json.dump(chunk, f, indent=2)
        
        content_path = self.mesh / "chunks" / f"{content_hash}.data"
        with open(content_path, 'w') as f:
            f.write(text[:10000])  # Store first 10KB
        
        self.known_hashes.add(content_hash)
        print(f"  ✓ Stored as {content_hash}")
        
        return True
    
    def forage_targets(self, urls):
        """Forage a list of URLs"""
        print("="*70)
        print("EMBER WEB FORAGER")
        print("="*70)
        print(f"\nKnown chunks: {len(self.known_hashes)}")
        print(f"Targets: {len(urls)}")
        
        novel_count = 0
        duplicate_count = 0
        failed_count = 0
        
        for url in urls:
            result = self.digest_url(url)
            if result is True:
                novel_count += 1
            elif result is False:
                duplicate_count += 1
            else:
                failed_count += 1
        
        print("\n" + "="*70)
        print("FORAGE COMPLETE")
        print("="*70)
        print(f"Novel ingested: {novel_count}")
        print(f"Duplicates rejected: {duplicate_count}")
        print(f"Failed: {failed_count}")
        print(f"\nEfficiency: {(duplicate_count/(novel_count+duplicate_count)*100) if (novel_count+duplicate_count) > 0 else 0:.1f}% filtered")

if __name__ == "__main__":
    # Example: Forage AI/ML research pages
    test_urls = [
        "https://en.wikipedia.org/wiki/Artificial_intelligence",
        "https://en.wikipedia.org/wiki/Machine_learning",
        "https://en.wikipedia.org/wiki/Neural_network",
        # These would be duplicates if run twice
    ]
    
    print("="*70)
    print("WEB FORAGER - PROTOTYPE")
    print("="*70)
    print()
    print("This demonstrates:")
    print("  • Fetch content from web")
    print("  • Check if novel (content-addressed)")
    print("  • Extract concepts automatically")
    print("  • Only store what's new")
    print("  • Build knowledge graph from internet")
    print()
    print("What would happen at scale:")
    print("  • Crawl thousands of pages")
    print("  • 99% rejected as duplicate/known")
    print("  • 1% novel information added")
    print("  • Queryable: 'show me all AI research'")
    print("  • No storage waste")
    print()
    print("THE INTERNET → DIGESTIVE FILTER → KNOWLEDGE MESH")
    print()
    print("="*70)
    print()
    print("Ready to forage? (requires internet connection)")
    print("Uncomment below to actually crawl:")
    print()
    
    # UNCOMMENT TO ACTUALLY CRAWL:
    # forager = WebForager()
    # forager.forage_targets(test_urls)
    
    print("(Not running to avoid network activity during demo)")

