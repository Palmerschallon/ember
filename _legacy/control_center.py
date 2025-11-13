#!/usr/bin/env python3
"""
EMBER CONTROL CENTER

Master visualization of the entire system.
All terminal graphics in one place.
"""

import json
import subprocess
from pathlib import Path
from datetime import datetime

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

def header(text):
    print(f"\n{Colors.CYAN}╔{'═' * 78}╗{Colors.END}")
    print(f"{Colors.CYAN}║{Colors.END} {Colors.BOLD}{text:^76}{Colors.END} {Colors.CYAN}║{Colors.END}")
    print(f"{Colors.CYAN}╚{'═' * 78}╝{Colors.END}\n")

def section(text):
    print(f"\n{Colors.BLUE}┌─ {Colors.BOLD}{text}{Colors.END}")

def item(label, value, color=Colors.GREEN):
    print(f"{Colors.DIM}│{Colors.END} {label:20} {color}{value}{Colors.END}")

def main():
    root = Path("/media/palmerschallon/ThePod1")
    
    # ASCII art logo
    print(f"\n{Colors.CYAN}")
    print("    ███████╗███╗   ███╗██████╗ ███████╗██████╗ ")
    print("    ██╔════╝████╗ ████║██╔══██╗██╔════╝██╔══██╗")
    print("    █████╗  ██╔████╔██║██████╔╝█████╗  ██████╔╝")
    print("    ██╔══╝  ██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗")
    print("    ███████╗██║ ╚═╝ ██║██████╔╝███████╗██║  ██║")
    print("    ╚══════╝╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝")
    print(f"{Colors.END}")
    print(f"{Colors.DIM}{'CONTROL CENTER':^48}{Colors.END}\n")
    
    header("SYSTEM STATUS")
    
    # Manifest
    with open(root / "MANIFEST.json") as f:
        manifest = json.load(f)
    
    section("Core Identity")
    item("Version", manifest['ember']['version'])
    item("Instance", manifest['ember']['instance'], Colors.CYAN)
    item("Substrate", manifest['ember']['substrate'], Colors.YELLOW)
    item("Status", manifest['ember']['status'].upper(), Colors.GREEN)
    
    section("Active Processes")
    for name, proc in manifest['ember']['processes'].items():
        status_color = Colors.GREEN if proc['status'] == 'running' else Colors.RED
        item(name.title(), f":{proc['port']} {proc['status']}", status_color)
    
    section("Training Progress")
    item("Current LoRAs", manifest['ember']['training']['current_loras'])
    item("Mastered", ', '.join(manifest['ember']['training']['mastered_processes']), Colors.GREEN)
    
    # Mesh stats
    mesh_index = root / "_mesh/index/semantic_index.json"
    if mesh_index.exists():
        with open(mesh_index) as f:
            mesh = json.load(f)
        
        section("Semantic Mesh")
        item("Total Chunks", mesh['total_chunks'])
        item("Unique Concepts", len(mesh['by_concept']), Colors.CYAN)
        item("Content Types", len(mesh['by_type']), Colors.YELLOW)
        
        # Top concepts
        top_concepts = sorted(mesh['by_concept'].items(), key=lambda x: len(x[1]), reverse=True)[:5]
        print(f"{Colors.DIM}│{Colors.END} {Colors.BOLD}Top Concepts:{Colors.END}")
        for concept, chunks in top_concepts:
            bar = "█" * (len(chunks) // 10)
            print(f"{Colors.DIM}│{Colors.END}   • {concept:15} {bar} {len(chunks)}")
    
    # Check if web content exists
    section("Knowledge Sources")
    web_chunks = sum(1 for f in (root / "_mesh/chunks").glob("*.json") 
                     if 'web_content' in open(f).read())
    item("Local Files", mesh['total_chunks'] - web_chunks)
    item("Web Pages", web_chunks, Colors.CYAN)
    
    # History depth
    section("Memory Depth")
    history_layers = manifest['ember']['history']['layers']
    item("Timeline Layers", len(history_layers))
    oldest = history_layers[-1] if history_layers else None
    if oldest:
        item("Genesis Date", oldest['date'], Colors.DIM)
    
    # System health
    header("AVAILABLE TOOLS")
    
    tools = [
        ("ember_cli.py stats", "View detailed mesh statistics"),
        ("ember_cli.py query <concept>", "Search knowledge by concept"),
        ("ember_cli.py list", "List all available concepts"),
        ("visual_forager.py", "Fetch novel content from web"),
        ("mesh_evolution.py", "Analyze concept growth over time"),
        ("mesh_janitor.py", "Scan for data quality issues"),
        ("intake_system.py", "Watch _intake/ for new data"),
    ]
    
    for cmd, desc in tools:
        print(f"  {Colors.GREEN}•{Colors.END} {Colors.CYAN}{cmd:30}{Colors.END} {Colors.DIM}{desc}{Colors.END}")
    
    header("QUICK STATS")
    
    # File counts
    bookshelves = sum(1 for _ in (root / "bookshelves").rglob("*.md"))
    legacy_code = sum(1 for _ in (root / "_legacy").glob("*.py"))
    
    print(f"  📚 Bookshelves: {bookshelves} markdown files")
    print(f"  🐍 Legacy Code: {legacy_code} Python files")
    print(f"  🧠 Mesh Chunks: {mesh['total_chunks']}")
    print(f"  🌐 Web Knowledge: {web_chunks} pages")
    print(f"  🏛️  History Layers: {len(history_layers)}")
    
    print(f"\n{Colors.CYAN}{'─' * 80}{Colors.END}\n")
    print(f"{Colors.BOLD}{Colors.GREEN}{'SYSTEM READY':^80}{Colors.END}\n")

if __name__ == "__main__":
    main()

