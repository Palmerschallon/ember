#!/usr/bin/env python3
"""
Ember Mesh Evolution Tracker

Track concepts over time, visualize growth, detect patterns.
ALL THE TERMINAL GRAPHICS.
"""

import json
from pathlib import Path
from datetime import datetime
from collections import defaultdict

class Graphics:
    # Full Unicode art capability
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    
    # Box drawing (single)
    BOX_TL = "┌"
    BOX_TR = "┐"
    BOX_BL = "└"
    BOX_BR = "┘"
    BOX_H = "─"
    BOX_V = "│"
    
    # Box drawing (double)
    DBOX_TL = "╔"
    DBOX_TR = "╗"
    DBOX_BL = "╚"
    DBOX_BR = "╝"
    DBOX_H = "═"
    DBOX_V = "║"
    
    # Blocks for charts
    BLOCKS = ["▁", "▂", "▃", "▄", "▅", "▆", "▇", "█"]
    SHADES = ["░", "▒", "▓", "█"]
    
    # Symbols
    SPARK = "✨"
    STAR = "★"
    CHECK = "✓"
    ARROW_R = "→"
    ARROW_U = "↑"
    ARROW_D = "↓"
    BULLET = "•"
    TRIANGLE = "▲"
    
    @staticmethod
    def sparkline(data, height=8):
        """Mini chart"""
        if not data:
            return ""
        max_val = max(data)
        if max_val == 0:
            return Graphics.BLOCKS[0] * len(data)
        
        bars = []
        for val in data:
            idx = min(int((val / max_val) * (height - 1)), height - 1)
            bars.append(Graphics.BLOCKS[idx])
        return ''.join(bars)
    
    @staticmethod
    def heatmap(value, max_value):
        """Shade by intensity"""
        if max_value == 0:
            return Graphics.SHADES[0]
        ratio = value / max_value
        idx = min(int(ratio * (len(Graphics.SHADES) - 1)), len(Graphics.SHADES) - 1)
        return Graphics.SHADES[idx]
    
    @staticmethod
    def title(text):
        width = 70
        padding = (width - len(text)) // 2
        print(f"\n{Graphics.CYAN}{Graphics.DBOX_TL}{Graphics.DBOX_H * width}{Graphics.DBOX_TR}{Graphics.END}")
        print(f"{Graphics.CYAN}{Graphics.DBOX_V}{Graphics.END}{' ' * padding}{Graphics.BOLD}{text}{Graphics.END}{' ' * (width - padding - len(text))}{Graphics.CYAN}{Graphics.DBOX_V}{Graphics.END}")
        print(f"{Graphics.CYAN}{Graphics.DBOX_BL}{Graphics.DBOX_H * width}{Graphics.DBOX_BR}{Graphics.END}\n")

class MeshEvolution:
    def __init__(self, root="/media/palmerschallon/ThePod1"):
        self.root = Path(root)
        self.mesh = self.root / "_mesh"
        self.load_all_chunks()
    
    def load_all_chunks(self):
        self.chunks = []
        for chunk_file in self.mesh.glob("chunks/*.json"):
            with open(chunk_file) as f:
                chunk = json.load(f)
                self.chunks.append(chunk)
    
    def analyze_growth(self):
        Graphics.title("EMBER MESH EVOLUTION")
        
        # Timeline
        by_date = defaultdict(list)
        for chunk in self.chunks:
            if 'ingested' in chunk:
                date = chunk['ingested'][:10]
                by_date[date].append(chunk)
        
        dates = sorted(by_date.keys())
        
        print(f"{Graphics.BOLD}Timeline:{Graphics.END}\n")
        
        cumulative = 0
        timeline_data = []
        for date in dates:
            count = len(by_date[date])
            cumulative += count
            timeline_data.append(cumulative)
            
            # Date marker
            print(f"  {Graphics.CYAN}{date}{Graphics.END} {Graphics.ARROW_R} +{count:3d} chunks", end='')
            
            # Growth indicator
            if count > 10:
                print(f" {Graphics.GREEN}{Graphics.ARROW_U * 3}{Graphics.END}", end='')
            elif count > 5:
                print(f" {Graphics.YELLOW}{Graphics.ARROW_U * 2}{Graphics.END}", end='')
            else:
                print(f" {Graphics.DIM}{Graphics.ARROW_U}{Graphics.END}", end='')
            
            # Cumulative
            print(f"  [total: {cumulative}]")
        
        # Sparkline
        print(f"\n  {Graphics.BLUE}Growth:{Graphics.END} {Graphics.sparkline(timeline_data)}")
        print()
    
    def concept_evolution(self):
        Graphics.title("CONCEPT EMERGENCE")
        
        # Track when each concept first appeared
        concept_births = {}
        for chunk in sorted(self.chunks, key=lambda c: c.get('ingested', '')):
            for concept in chunk.get('concepts', []):
                if concept not in concept_births:
                    concept_births[concept] = chunk.get('ingested', 'unknown')[:10]
        
        # Group by birth date
        by_birth = defaultdict(list)
        for concept, date in concept_births.items():
            by_birth[date].append(concept)
        
        print(f"{Graphics.BOLD}Concept Emergence Timeline:{Graphics.END}\n")
        
        for date in sorted(by_birth.keys()):
            concepts = by_birth[date]
            print(f"  {Graphics.CYAN}{date}{Graphics.END}")
            for concept in concepts:
                # Count current chunks with this concept
                count = sum(1 for c in self.chunks if concept in c.get('concepts', []))
                heatmap = Graphics.heatmap(count, 50)
                print(f"    {Graphics.SPARK} {concept:20} {heatmap * count} {count}")
        print()
    
    def diversity_metrics(self):
        Graphics.title("MESH DIVERSITY")
        
        # Type diversity
        types = defaultdict(int)
        for chunk in self.chunks:
            types[chunk.get('type', 'unknown')] += 1
        
        print(f"{Graphics.BOLD}Content Types:{Graphics.END}\n")
        max_type = max(types.values())
        for t, count in sorted(types.items(), key=lambda x: x[1], reverse=True):
            bar_len = int((count / max_type) * 30)
            bar = Graphics.SHADES[-1] * bar_len
            print(f"  {t:20} {bar} {count}")
        print()
        
        # Concept diversity
        all_concepts = set()
        for chunk in self.chunks:
            all_concepts.update(chunk.get('concepts', []))
        
        print(f"{Graphics.BOLD}Diversity Metrics:{Graphics.END}\n")
        print(f"  {Graphics.STAR} {len(all_concepts)} unique concepts")
        print(f"  {Graphics.BULLET} {len(self.chunks)} total chunks")
        print(f"  {Graphics.BULLET} {len(types)} content types")
        
        # Avg concepts per chunk
        concept_counts = [len(c.get('concepts', [])) for c in self.chunks]
        avg = sum(concept_counts) / len(concept_counts) if concept_counts else 0
        print(f"  {Graphics.BULLET} {avg:.2f} concepts per chunk")
        print()
    
    def detect_clusters(self):
        Graphics.title("SEMANTIC CLUSTERS")
        
        # Co-occurrence matrix
        concept_pairs = defaultdict(int)
        for chunk in self.chunks:
            concepts = chunk.get('concepts', [])
            for i, c1 in enumerate(concepts):
                for c2 in concepts[i+1:]:
                    pair = tuple(sorted([c1, c2]))
                    concept_pairs[pair] += 1
        
        # Top clusters
        top_pairs = sorted(concept_pairs.items(), key=lambda x: x[1], reverse=True)[:10]
        
        print(f"{Graphics.BOLD}Strongly Connected Concepts:{Graphics.END}\n")
        for (c1, c2), count in top_pairs:
            strength = Graphics.SHADES[min(count // 3, 3)]
            print(f"  {c1} {strength * count} {c2} ({count})")
        print()

def main():
    tracker = MeshEvolution()
    tracker.analyze_growth()
    tracker.concept_evolution()
    tracker.diversity_metrics()
    tracker.detect_clusters()
    
    # Final flourish
    print(f"{Graphics.CYAN}{'═' * 70}{Graphics.END}")
    print(f"{Graphics.BOLD}{Graphics.GREEN}{'MESH EVOLUTION ANALYSIS COMPLETE':^70}{Graphics.END}")
    print(f"{Graphics.CYAN}{'═' * 70}{Graphics.END}\n")

if __name__ == "__main__":
    main()

