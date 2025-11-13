#!/usr/bin/env python3
"""
Ember Mesh Janitor - Automatic Cleanup

Detect and remove:
- True duplicates (same content hash)
- Over-generic chunks (no real concepts)
- Orphaned files
- Stale data

With beautiful progress indicators.
"""

import json
import hashlib
from pathlib import Path
from collections import defaultdict

class UI:
    RED = '\033[91m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    CYAN = '\033[96m'
    DIM = '\033[2m'
    BOLD = '\033[1m'
    END = '\033[0m'
    
    TRASH = "🗑"
    WARN = "⚠"
    CLEAN = "✨"
    CHECK = "✓"

class MeshJanitor:
    def __init__(self, root="/media/palmerschallon/ThePod1", dry_run=True):
        self.root = Path(root)
        self.mesh = self.root / "_mesh"
        self.dry_run = dry_run
        self.issues = []
    
    def scan(self):
        print(f"\n{UI.CYAN}{'═' * 70}{UI.END}")
        print(f"{UI.BOLD}EMBER MESH JANITOR{UI.END}")
        print(f"{UI.CYAN}{'═' * 70}{UI.END}\n")
        
        if self.dry_run:
            print(f"{UI.YELLOW}{UI.WARN} DRY RUN - no files will be deleted{UI.END}\n")
        
        self.check_duplicates()
        self.check_overgeneric()
        self.check_orphans()
        self.check_empty()
        
        self.report()
    
    def check_duplicates(self):
        """Find chunks with identical content"""
        print(f"{UI.BOLD}Checking for duplicates...{UI.END}")
        
        content_hashes = defaultdict(list)
        
        for chunk_file in self.mesh.glob("chunks/*.json"):
            with open(chunk_file) as f:
                chunk = json.load(f)
            
            # Hash the actual content
            data_file = chunk_file.with_suffix('.data')
            if data_file.exists():
                with open(data_file, 'rb') as f:
                    content_hash = hashlib.sha256(f.read()).hexdigest()
                content_hashes[content_hash].append(chunk_file)
        
        duplicates = {h: files for h, files in content_hashes.items() if len(files) > 1}
        
        if duplicates:
            for content_hash, files in duplicates.items():
                self.issues.append({
                    'type': 'duplicate',
                    'severity': 'medium',
                    'files': files[1:],  # Keep first, remove rest
                    'message': f"Duplicate content: {len(files)} copies"
                })
                print(f"  {UI.YELLOW}{UI.WARN} {len(files)} copies of same content{UI.END}")
        else:
            print(f"  {UI.GREEN}{UI.CHECK} No duplicates found{UI.END}")
        print()
    
    def check_overgeneric(self):
        """Find chunks that are too generic to be useful"""
        print(f"{UI.BOLD}Checking for over-generic chunks...{UI.END}")
        
        generic_count = 0
        
        for chunk_file in self.mesh.glob("chunks/*.json"):
            with open(chunk_file) as f:
                chunk = json.load(f)
            
            concepts = chunk.get('concepts', [])
            
            # Flag if ONLY "general" concept or no concepts
            if concepts == ['general'] or not concepts:
                generic_count += 1
                self.issues.append({
                    'type': 'overgeneric',
                    'severity': 'low',
                    'files': [chunk_file],
                    'message': f"{chunk.get('name', 'unknown')}: no useful concepts"
                })
        
        if generic_count > 0:
            print(f"  {UI.YELLOW}{UI.WARN} {generic_count} over-generic chunks{UI.END}")
            print(f"    {UI.DIM}(These could be improved with better concept extraction){UI.END}")
        else:
            print(f"  {UI.GREEN}{UI.CHECK} All chunks have specific concepts{UI.END}")
        print()
    
    def check_orphans(self):
        """Find .data files without .json or vice versa"""
        print(f"{UI.BOLD}Checking for orphaned files...{UI.END}")
        
        json_files = {f.stem for f in self.mesh.glob("chunks/*.json")}
        data_files = {f.stem for f in self.mesh.glob("chunks/*.data")}
        
        orphan_data = data_files - json_files
        orphan_json = json_files - data_files
        
        for orphan in orphan_data:
            self.issues.append({
                'type': 'orphan',
                'severity': 'high',
                'files': [self.mesh / "chunks" / f"{orphan}.data"],
                'message': f"Data file without metadata: {orphan}"
            })
        
        for orphan in orphan_json:
            self.issues.append({
                'type': 'orphan',
                'severity': 'medium',
                'files': [self.mesh / "chunks" / f"{orphan}.json"],
                'message': f"Metadata without data: {orphan}"
            })
        
        total_orphans = len(orphan_data) + len(orphan_json)
        if total_orphans > 0:
            print(f"  {UI.RED}{UI.WARN} {total_orphans} orphaned files{UI.END}")
        else:
            print(f"  {UI.GREEN}{UI.CHECK} All files properly paired{UI.END}")
        print()
    
    def check_empty(self):
        """Find empty or near-empty chunks"""
        print(f"{UI.BOLD}Checking for empty chunks...{UI.END}")
        
        empty_count = 0
        
        for data_file in self.mesh.glob("chunks/*.data"):
            size = data_file.stat().st_size
            if size < 10:  # Less than 10 bytes
                empty_count += 1
                self.issues.append({
                    'type': 'empty',
                    'severity': 'medium',
                    'files': [data_file, data_file.with_suffix('.json')],
                    'message': f"Near-empty file: {size} bytes"
                })
        
        if empty_count > 0:
            print(f"  {UI.YELLOW}{UI.WARN} {empty_count} near-empty chunks{UI.END}")
        else:
            print(f"  {UI.GREEN}{UI.CHECK} All chunks have content{UI.END}")
        print()
    
    def report(self):
        print(f"{UI.CYAN}{'═' * 70}{UI.END}")
        print(f"{UI.BOLD}SCAN RESULTS{UI.END}")
        print(f"{UI.CYAN}{'═' * 70}{UI.END}\n")
        
        if not self.issues:
            print(f"{UI.GREEN}{UI.CLEAN} MESH IS CLEAN! No issues found.{UI.END}\n")
            return
        
        by_severity = defaultdict(list)
        for issue in self.issues:
            by_severity[issue['severity']].append(issue)
        
        print(f"  {UI.RED}High:{UI.END}   {len(by_severity['high'])} issues")
        print(f"  {UI.YELLOW}Medium:{UI.END} {len(by_severity['medium'])} issues")
        print(f"  {UI.DIM}Low:{UI.END}    {len(by_severity['low'])} issues")
        print()
        
        if self.dry_run:
            print(f"{UI.YELLOW}To actually clean, run with --clean flag{UI.END}")
        else:
            self.clean()
    
    def clean(self):
        """Actually remove problematic files"""
        print(f"\n{UI.BOLD}Cleaning...{UI.END}\n")
        
        removed = 0
        for issue in self.issues:
            if issue['severity'] == 'low':
                continue  # Don't auto-remove over-generic chunks
            
            for file in issue['files']:
                if file.exists():
                    file.unlink()
                    removed += 1
                    print(f"  {UI.RED}{UI.TRASH} Removed: {file.name}{UI.END}")
        
        print(f"\n{UI.GREEN}{UI.CHECK} Cleaned {removed} files{UI.END}\n")

def main():
    import sys
    dry_run = '--clean' not in sys.argv
    
    janitor = MeshJanitor(dry_run=dry_run)
    janitor.scan()

if __name__ == "__main__":
    main()

