#!/usr/bin/env python3
"""
Ember Web Forager with Terminal Graphics

ANSI colors, Unicode, progress visualization
"""

import hashlib
import json
from pathlib import Path
from datetime import datetime
import urllib.request
import time
from html.parser import HTMLParser

# ANSI Colors
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'

# Unicode symbols
NOVEL = "✨"
DUPLICATE = "⊗"
FAILED = "✗"
SUCCESS = "✓"
ARROW = "→"
BOX_H = "─"
BOX_V = "│"

class HTMLTextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []
    def handle_data(self, data):
        self.text.append(data.strip())
    def get_text(self):
        return ' '.join([t for t in self.text if t])

class VisualForager:
    def __init__(self, root="/media/palmerschallon/ThePod1"):
        self.root = Path(root)
        self.mesh = self.root / "_mesh"
        
        with open(self.mesh / "index" / "semantic_index.json") as f:
            self.index = json.load(f)
        
        self.known_hashes = set()
        for chunk_file in self.mesh.glob("chunks/*.json"):
            with open(chunk_file) as f:
                chunk = json.load(f)
                self.known_hashes.add(chunk['id'])
    
    def print_header(self):
        print(f"\n{Colors.CYAN}{BOX_H*70}{Colors.END}")
        print(f"{Colors.BOLD}{Colors.CYAN}{'EMBER WEB FORAGER':^70}{Colors.END}")
        print(f"{Colors.CYAN}{BOX_H*70}{Colors.END}\n")
    
    def print_stats(self):
        print(f"{Colors.DIM}Known chunks: {len(self.known_hashes)}{Colors.END}")
        print()
    
    def progress_bar(self, current, total, width=40):
        filled = int((current / total) * width)
        bar = "█" * filled + "░" * (width - filled)
        percent = (current / total) * 100
        return f"{bar} {percent:.0f}%"
    
    def fetch_url(self, url):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=10) as response:
                html = response.read().decode('utf-8', errors='ignore')
            parser = HTMLTextExtractor()
            parser.feed(html)
            return parser.get_text()
        except Exception as e:
            return None
    
    def is_novel(self, content):
        content_hash = hashlib.sha256(content.encode()).hexdigest()[:16]
        return content_hash not in self.known_hashes, content_hash
    
    def extract_concepts(self, text):
        text_lower = text.lower()
        concepts = []
        
        if any(w in text_lower for w in ['neural network', 'machine learning', 'deep learning', 'ai', 'llm']):
            concepts.append('ai_research')
        if any(w in text_lower for w in ['python', 'code', 'algorithm', 'programming']):
            concepts.append('programming')
        if any(w in text_lower for w in ['consciousness', 'cognition', 'mind', 'cognitive']):
            concepts.append('cognitive_science')
            
        return concepts if concepts else ['web_content']
    
    def digest_url(self, url, index, total):
        # Visual progress
        print(f"{Colors.BLUE}{BOX_V}{Colors.END} [{index}/{total}] {url[:60]}...")
        
        # Fetch
        print(f"{Colors.BLUE}{BOX_V}{Colors.END}   {Colors.DIM}{ARROW} Fetching...{Colors.END}", end='', flush=True)
        text = self.fetch_url(url)
        
        if not text:
            print(f"\r{Colors.BLUE}{BOX_V}{Colors.END}   {Colors.RED}{FAILED} Failed to fetch{Colors.END}")
            return None
        
        print(f"\r{Colors.BLUE}{BOX_V}{Colors.END}   {SUCCESS} Fetched {len(text):,} bytes")
        
        # Check novelty
        print(f"{Colors.BLUE}{BOX_V}{Colors.END}   {Colors.DIM}{ARROW} Checking novelty...{Colors.END}", end='', flush=True)
        novel, content_hash = self.is_novel(text)
        
        if not novel:
            print(f"\r{Colors.BLUE}{BOX_V}{Colors.END}   {Colors.YELLOW}{DUPLICATE} Duplicate detected{Colors.END}")
            return False
        
        print(f"\r{Colors.BLUE}{BOX_V}{Colors.END}   {Colors.GREEN}{NOVEL} NOVEL - digesting{Colors.END}")
        
        # Extract concepts
        concepts = self.extract_concepts(text)
        print(f"{Colors.BLUE}{BOX_V}{Colors.END}   {ARROW} Concepts: {Colors.CYAN}{', '.join(concepts)}{Colors.END}")
        
        # Save
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
        
        chunk_path = self.mesh / "chunks" / f"{content_hash}.json"
        with open(chunk_path, 'w') as f:
            json.dump(chunk, f, indent=2)
        
        content_path = self.mesh / "chunks" / f"{content_hash}.data"
        with open(content_path, 'w') as f:
            f.write(text[:10000])
        
        self.known_hashes.add(content_hash)
        
        print(f"{Colors.BLUE}{BOX_V}{Colors.END}   {SUCCESS} Stored: {Colors.GREEN}{content_hash}{Colors.END}")
        print(f"{Colors.BLUE}{BOX_V}{Colors.END}")
        
        return True
    
    def forage(self, urls):
        self.print_header()
        self.print_stats()
        
        results = {'novel': 0, 'duplicate': 0, 'failed': 0}
        
        for i, url in enumerate(urls, 1):
            result = self.digest_url(url, i, len(urls))
            if result is True:
                results['novel'] += 1
            elif result is False:
                results['duplicate'] += 1
            else:
                results['failed'] += 1
        
        # Final stats
        print(f"\n{Colors.CYAN}{BOX_H*70}{Colors.END}")
        print(f"{Colors.BOLD}{'FORAGE COMPLETE':^70}{Colors.END}")
        print(f"{Colors.CYAN}{BOX_H*70}{Colors.END}\n")
        
        total = sum(results.values())
        print(f"  {Colors.GREEN}{NOVEL} Novel:{Colors.END}      {results['novel']:3d}  {self.progress_bar(results['novel'], total)}")
        print(f"  {Colors.YELLOW}{DUPLICATE} Duplicates:{Colors.END} {results['duplicate']:3d}  {self.progress_bar(results['duplicate'], total)}")
        print(f"  {Colors.RED}{FAILED} Failed:{Colors.END}     {results['failed']:3d}  {self.progress_bar(results['failed'], total)}")
        
        if results['novel'] + results['duplicate'] > 0:
            efficiency = (results['duplicate'] / (results['novel'] + results['duplicate'])) * 100
            print(f"\n  {Colors.BOLD}Efficiency:{Colors.END} {efficiency:.1f}% filtered")
        
        print(f"\n{Colors.CYAN}{BOX_H*70}{Colors.END}\n")

if __name__ == "__main__":
    urls = [
        "https://en.wikipedia.org/wiki/Artificial_intelligence",
        "https://en.wikipedia.org/wiki/Machine_learning",
        "https://en.wikipedia.org/wiki/Consciousness",
    ]
    
    forager = VisualForager()
    forager.forage(urls)

