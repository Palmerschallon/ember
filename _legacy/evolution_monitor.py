#!/usr/bin/env python3
"""
Ember Evolution Monitor

Watch in real-time as Ember digests knowledge and expresses themselves.
Track mesh growth, concept emergence, and fruiting body creation.
"""

import time
import json
from pathlib import Path
from datetime import datetime
from collections import defaultdict

class Colors:
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'

class EvolutionMonitor:
    def __init__(self, root="/media/palmerschallon/ThePod1"):
        self.root = Path(root)
        self.mesh = self.root / "_mesh"
        self.expressions = self.root / "bookshelves" / "ember_expressions"
        self.intake = self.root / "_intake"
        
        self.baseline = self.get_stats()
        
    def get_stats(self):
        """Get current system stats"""
        stats = {}
        
        # Mesh stats
        index_file = self.mesh / "index" / "semantic_index.json"
        if index_file.exists():
            with open(index_file) as f:
                index = json.load(f)
            stats['chunks'] = index['total_chunks']
            stats['concepts'] = len(index['by_concept'])
            stats['top_concept'] = max(index['by_concept'].items(), key=lambda x: len(x[1]))
        else:
            stats['chunks'] = 0
            stats['concepts'] = 0
            stats['top_concept'] = ('none', [])
        
        # Expression stats
        expressions = list(self.expressions.glob("*.md"))
        stats['expressions'] = len(expressions)
        
        # Intake stats
        intake_files = [f for f in self.intake.glob("*") if f.is_file() and f.name != "_processed"]
        stats['intake_pending'] = len(intake_files)
        
        return stats
    
    def print_header(self):
        print(f"\n{Colors.CYAN}{'═' * 80}{Colors.END}")
        print(f"{Colors.BOLD}{Colors.CYAN}{'EMBER EVOLUTION MONITOR':^80}{Colors.END}")
        print(f"{Colors.CYAN}{'═' * 80}{Colors.END}\n")
    
    def print_stats(self, stats, baseline):
        """Print current stats with deltas"""
        
        # Chunks
        chunk_delta = stats['chunks'] - baseline['chunks']
        chunk_color = Colors.GREEN if chunk_delta > 0 else Colors.DIM
        print(f"  🧠 Chunks:      {stats['chunks']:5,} {chunk_color}(+{chunk_delta}){Colors.END}")
        
        # Concepts
        concept_delta = stats['concepts'] - baseline['concepts']
        concept_color = Colors.GREEN if concept_delta > 0 else Colors.DIM
        print(f"  💡 Concepts:    {stats['concepts']:5,} {concept_color}(+{concept_delta}){Colors.END}")
        
        # Expressions
        expr_delta = stats['expressions'] - baseline['expressions']
        expr_color = Colors.YELLOW if expr_delta > 0 else Colors.DIM
        print(f"  🌱 Expressions: {stats['expressions']:5,} {expr_color}(+{expr_delta}){Colors.END}")
        
        # Intake
        intake_color = Colors.RED if stats['intake_pending'] > 100 else Colors.YELLOW if stats['intake_pending'] > 0 else Colors.GREEN
        print(f"  📥 Pending:     {stats['intake_pending']:5,} {intake_color}(waiting){Colors.END}")
        
        # Top concept
        concept_name, concept_chunks = stats['top_concept']
        print(f"\n  {Colors.BOLD}Top Concept:{Colors.END} {Colors.CYAN}{concept_name}{Colors.END} ({len(concept_chunks)} chunks)")
        
        print()
    
    def check_new_expressions(self):
        """Check for new markdown expressions"""
        expressions = sorted(self.expressions.glob("*.md"), key=lambda x: x.stat().st_mtime, reverse=True)
        
        # Only show last 3
        recent = expressions[:3]
        if recent:
            print(f"  {Colors.YELLOW}{'Recent Fruiting Bodies:'}{Colors.END}")
            for expr in recent:
                age_seconds = time.time() - expr.stat().st_mtime
                age_minutes = int(age_seconds / 60)
                
                if age_minutes < 60:
                    age_str = f"{age_minutes}m ago"
                else:
                    age_str = f"{age_minutes // 60}h ago"
                
                # Read first line for title
                with open(expr) as f:
                    lines = f.readlines()
                    title = "untitled"
                    for line in lines:
                        if line.startswith('#'):
                            title = line.strip('# \n')
                            break
                
                print(f"    {Colors.DIM}{age_str:10}{Colors.END} {title[:60]}")
            print()
    
    def monitor(self, interval=30):
        """Monitor in real-time"""
        
        self.print_header()
        
        print(f"{Colors.BOLD}Baseline established:{Colors.END}")
        self.print_stats(self.baseline, {'chunks': 0, 'concepts': 0, 'expressions': 0, 'intake_pending': 0, 'top_concept': ('none', [])})
        
        print(f"{Colors.DIM}Monitoring every {interval} seconds... (Ctrl+C to stop){Colors.END}\n")
        print(f"{Colors.CYAN}{'─' * 80}{Colors.END}\n")
        
        try:
            while True:
                time.sleep(interval)
                
                current = self.get_stats()
                timestamp = datetime.now().strftime('%H:%M:%S')
                
                print(f"[{timestamp}] {Colors.BOLD}Update:{Colors.END}")
                self.print_stats(current, self.baseline)
                
                # Check for new expressions
                self.check_new_expressions()
                
                print(f"{Colors.CYAN}{'─' * 80}{Colors.END}\n")
                
        except KeyboardInterrupt:
            print(f"\n\n{Colors.CYAN}{'═' * 80}{Colors.END}")
            print(f"{Colors.BOLD}{Colors.GREEN}{'MONITORING STOPPED':^80}{Colors.END}")
            print(f"{Colors.CYAN}{'═' * 80}{Colors.END}\n")
            
            final = self.get_stats()
            print(f"{Colors.BOLD}Final Stats:{Colors.END}")
            self.print_stats(final, self.baseline)

if __name__ == "__main__":
    monitor = EvolutionMonitor()
    monitor.monitor(interval=30)

