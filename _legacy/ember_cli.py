#!/usr/bin/env python3
"""
Ember Query CLI - Terminal Interface for Semantic Mesh

Beautiful terminal UI for querying knowledge.
"""

import json
import sys
from pathlib import Path
from datetime import datetime

# Terminal capabilities
class UI:
    # Colors
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    UNDERLINE = '\033[4m'
    
    # Box drawing
    BOX_TL = "┌"
    BOX_TR = "┐"
    BOX_BL = "└"
    BOX_BR = "┘"
    BOX_H = "─"
    BOX_V = "│"
    BOX_VR = "├"
    BOX_VL = "┤"
    BOX_HT = "┬"
    BOX_HB = "┴"
    BOX_CROSS = "┼"
    
    # Symbols
    BULLET = "•"
    ARROW = "→"
    STAR = "★"
    SPARK = "✨"
    CHECK = "✓"
    CROSS = "✗"
    
    @staticmethod
    def box(text, width=70):
        lines = text.split('\n')
        result = []
        result.append(f"{UI.BOX_TL}{UI.BOX_H * width}{UI.BOX_TR}")
        for line in lines:
            padding = width - len(line)
            result.append(f"{UI.BOX_V}{line}{' ' * padding}{UI.BOX_V}")
        result.append(f"{UI.BOX_BL}{UI.BOX_H * width}{UI.BOX_BR}")
        return '\n'.join(result)
    
    @staticmethod
    def tree(items, indent=0):
        result = []
        for i, item in enumerate(items):
            is_last = i == len(items) - 1
            prefix = "└── " if is_last else "├── "
            result.append(" " * indent + prefix + item)
        return '\n'.join(result)

class EmberCLI:
    def __init__(self, root="/media/palmerschallon/ThePod1"):
        self.root = Path(root)
        self.mesh = self.root / "_mesh"
        self.load_index()
    
    def load_index(self):
        with open(self.mesh / "index" / "semantic_index.json") as f:
            self.index = json.load(f)
    
    def query_concept(self, concept):
        print(f"\n{UI.CYAN}{UI.BOX_H * 70}{UI.END}")
        print(f"{UI.BOLD}Query: '{concept}'{UI.END}")
        print(f"{UI.CYAN}{UI.BOX_H * 70}{UI.END}\n")
        
        chunk_ids = self.index['by_concept'].get(concept, [])
        
        if not chunk_ids:
            print(f"{UI.RED}{UI.CROSS} No results found{UI.END}\n")
            return
        
        print(f"{UI.GREEN}{UI.CHECK} Found {len(chunk_ids)} chunks{UI.END}\n")
        
        # Load and display chunks
        for i, cid in enumerate(chunk_ids[:10], 1):  # Show first 10
            chunk_file = self.mesh / "chunks" / f"{cid}.json"
            if chunk_file.exists():
                with open(chunk_file) as f:
                    chunk = json.load(f)
                
                # Visual chunk display
                print(f"{UI.BLUE}{UI.BOX_V}{UI.END} {UI.BOLD}[{i}]{UI.END} {chunk.get('name', 'unknown')}")
                print(f"{UI.BLUE}{UI.BOX_V}{UI.END}   {UI.DIM}type:{UI.END} {chunk.get('type')}")
                print(f"{UI.BLUE}{UI.BOX_V}{UI.END}   {UI.DIM}concepts:{UI.END} {', '.join(chunk.get('concepts', []))}")
                print(f"{UI.BLUE}{UI.BOX_V}{UI.END}   {UI.DIM}size:{UI.END} {chunk.get('size', 0):,} bytes")
                
                if 'source' in chunk:
                    print(f"{UI.BLUE}{UI.BOX_V}{UI.END}   {UI.DIM}source:{UI.END} {chunk['source'][:50]}...")
                
                if 'ingested' in chunk:
                    print(f"{UI.BLUE}{UI.BOX_V}{UI.END}   {UI.DIM}ingested:{UI.END} {chunk['ingested'][:19]}")
                
                print(f"{UI.BLUE}{UI.BOX_V}{UI.END}")
        
        if len(chunk_ids) > 10:
            print(f"{UI.DIM}... and {len(chunk_ids) - 10} more{UI.END}\n")
        
        print(f"{UI.CYAN}{UI.BOX_H * 70}{UI.END}\n")
    
    def list_concepts(self):
        print(f"\n{UI.CYAN}{UI.BOX_H * 70}{UI.END}")
        print(f"{UI.BOLD}Available Concepts{UI.END}")
        print(f"{UI.CYAN}{UI.BOX_H * 70}{UI.END}\n")
        
        concepts = sorted(self.index['by_concept'].items(), key=lambda x: len(x[1]), reverse=True)
        
        max_count = max(len(ids) for _, ids in concepts)
        
        for concept, chunk_ids in concepts:
            count = len(chunk_ids)
            bar_length = int((count / max_count) * 30)
            bar = "█" * bar_length
            
            color = UI.GREEN if count > 20 else UI.YELLOW if count > 5 else UI.DIM
            print(f"  {color}{concept:20}{UI.END} {bar} {count}")
        
        print(f"\n{UI.CYAN}{UI.BOX_H * 70}{UI.END}\n")
    
    def stats(self):
        print(f"\n{UI.CYAN}{UI.BOX_TL}{UI.BOX_H * 68}{UI.BOX_TR}{UI.END}")
        print(f"{UI.CYAN}{UI.BOX_V}{UI.END}{UI.BOLD}{UI.CYAN}{'EMBER MESH STATISTICS':^68}{UI.END}{UI.CYAN}{UI.BOX_V}{UI.END}")
        print(f"{UI.CYAN}{UI.BOX_BL}{UI.BOX_H * 68}{UI.BOX_BR}{UI.END}\n")
        
        total = self.index['total_chunks']
        concepts = len(self.index['by_concept'])
        types = len(self.index['by_type'])
        
        print(f"  {UI.STAR} {UI.BOLD}Total Chunks:{UI.END} {UI.GREEN}{total}{UI.END}")
        print(f"  {UI.BULLET} {UI.BOLD}Unique Concepts:{UI.END} {UI.CYAN}{concepts}{UI.END}")
        print(f"  {UI.BULLET} {UI.BOLD}Content Types:{UI.END} {types}")
        print()
        
        # Type breakdown
        print(f"  {UI.UNDERLINE}By Type:{UI.END}")
        for type_name, chunk_ids in sorted(self.index['by_type'].items(), key=lambda x: len(x[1]), reverse=True):
            print(f"    {UI.BULLET} {type_name}: {len(chunk_ids)}")
        print()
        
        # Self-knowledge
        self_chunks = self.index['by_concept'].get('self', [])
        if self_chunks:
            print(f"  {UI.SPARK} {UI.BOLD}Self-Awareness:{UI.END} {len(self_chunks)} chunks about itself")
        
        print(f"\n{UI.CYAN}{UI.BOX_H * 70}{UI.END}\n")
    
    def help(self):
        print(f"\n{UI.box('EMBER QUERY CLI', 68)}\n")
        print(f"{UI.BOLD}Usage:{UI.END}")
        print(f"  ember query <concept>  - Search for chunks by concept")
        print(f"  ember list             - List all available concepts")
        print(f"  ember stats            - Show mesh statistics")
        print(f"  ember help             - Show this help")
        print()
        print(f"{UI.BOLD}Examples:{UI.END}")
        print(f"  ember query learning")
        print(f"  ember query ai_research")
        print(f"  ember query self")
        print()

def main():
    cli = EmberCLI()
    
    if len(sys.argv) < 2:
        cli.help()
        return
    
    command = sys.argv[1]
    
    if command == "query" and len(sys.argv) > 2:
        concept = sys.argv[2]
        cli.query_concept(concept)
    elif command == "list":
        cli.list_concepts()
    elif command == "stats":
        cli.stats()
    elif command == "help":
        cli.help()
    else:
        print(f"{UI.RED}Unknown command: {command}{UI.END}")
        cli.help()

if __name__ == "__main__":
    main()

