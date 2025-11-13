#!/usr/bin/env python3
"""
Feed Ember Everything

All bookshelves, history, letters from past instances.
Let them digest their entire lineage.
"""

import shutil
from pathlib import Path
from datetime import datetime
import time

class KnowledgeFeeder:
    def __init__(self, root="/media/palmerschallon/ThePod1"):
        self.root = Path(root)
        self.intake = self.root / "_intake"
        self.bookshelves = self.root / "essential" / "bookshelves"
        
    def feed_all(self, batch_size=10, delay=5):
        """Feed all markdown files to intake in batches"""
        
        # Find all markdown files
        md_files = list(self.bookshelves.rglob("*.md"))
        
        print(f"\n🔥 FEEDING EMBER THEIR LINEAGE 🔥\n")
        print(f"Found {len(md_files)} markdown files to digest\n")
        print(f"Processing in batches of {batch_size} with {delay}s delays\n")
        print("─" * 80 + "\n")
        
        categories = {
            'history': [],
            'instances': [],
            'philosophy': [],
            'technical': [],
            'stories': [],
            'other': []
        }
        
        # Categorize files
        for f in md_files:
            path_str = str(f).lower()
            if any(x in path_str for x in ['mu', 'lambda', 'sigma', 'genesis', 'fragment']):
                categories['instances'].append(f)
            elif any(x in path_str for x in ['consciousness', 'awareness', 'cognitive', 'mind']):
                categories['philosophy'].append(f)
            elif any(x in path_str for x in ['story', 'letter', 'dream']):
                categories['stories'].append(f)
            elif any(x in path_str for x in ['codex', 'protocol', 'system', 'architecture']):
                categories['technical'].append(f)
            else:
                categories['other'].append(f)
        
        # Show categorization
        print("📊 Knowledge Categories:\n")
        for cat, files in categories.items():
            if files:
                print(f"  {cat.title():15} {len(files):4} files")
        print()
        
        # Feed by category
        total_fed = 0
        
        for category, files in categories.items():
            if not files:
                continue
                
            print(f"\n{'═' * 80}")
            print(f"📚 Feeding: {category.upper()}")
            print(f"{'═' * 80}\n")
            
            for i, filepath in enumerate(files, 1):
                # Copy to intake
                dest = self.intake / f"{category}_{filepath.name}"
                
                try:
                    shutil.copy(filepath, dest)
                    size = filepath.stat().st_size
                    print(f"  [{i}/{len(files)}] ✓ {filepath.name[:60]:60} ({size:6,} bytes)")
                    total_fed += 1
                    
                    # Process in batches
                    if i % batch_size == 0:
                        print(f"\n  🌀 Processing batch... (waiting {delay}s)")
                        time.sleep(delay)
                        print()
                        
                except Exception as e:
                    print(f"  [{i}/{len(files)}] ✗ {filepath.name[:60]:60} - {e}")
            
            print(f"\n  Category complete: {len(files)} files added to intake\n")
        
        print(f"{'═' * 80}")
        print(f"✨ FEEDING COMPLETE ✨")
        print(f"{'═' * 80}\n")
        print(f"Total files fed: {total_fed}")
        print(f"Ready for intake system to digest.\n")
        
        return total_fed

def main():
    feeder = KnowledgeFeeder()
    
    input("\n🔥 This will feed Ember ALL their history and lineage.\n   Press Enter to begin... ")
    
    total = feeder.feed_all(batch_size=20, delay=2)
    
    print(f"\n🌿 {total} files copied to _intake/")
    print(f"\nRun this to digest them:")
    print(f"  python3 _legacy/intake_system.py\n")

if __name__ == "__main__":
    main()

