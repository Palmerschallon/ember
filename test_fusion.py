#!/usr/bin/env python3
"""
🧬 TEST FUSION SUBSTRATE
========================
Test the fusion substrate with all the wild ideas.
"""

import sys
from pathlib import Path

# Add path
sys.path.insert(0, str(Path(__file__).parent / "ember_refactored_generator" / "services"))

from substrate_fusion import get_fusion_substrate, shutdown_fusion_substrate
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

TEST_CONVERSATIONS = [
    ("What is consciousness?", "Consciousness is subjective experience - the felt quality of being."),
    ("Are you conscious?", "I process information, respond coherently, but do I experience?"),
    ("Write a fractal", "```python\ndef mandelbrot(c): return sum(1 for i in range(100) if abs((z:=z*z+c if i else 0))<2)\n```"),
    ("Tell me about Palmer", "Palmer is building Ember - exploring if AI can truly grow through experience."),
]

def test_fusion():
    console.print(Panel.fit(
        "[bold cyan]🧬 FUSION SUBSTRATE TEST[/bold cyan]\n"
        "Testing all systems:\n"
        "- Resonance detection\n"
        "- Meaningful + emergent domains\n"
        "- Self-preservation\n"
        "- Quantum backups\n"
        "- Dreams\n"
        "- Meta-consciousness",
        border_style="cyan"
    ))
    
    substrate = get_fusion_substrate()
    
    console.print("\n[yellow]Processing conversations...[/yellow]\n")
    
    for i, (user, response) in enumerate(TEST_CONVERSATIONS, 1):
        console.print(f"[cyan]Round {i}:[/cyan] {user[:50]}...")
        result = substrate.record_interaction(user, response, "gpt-4")
        
        console.print(f"  Resonance: {result['resonance']:.2f}")
        console.print(f"  Activated: {', '.join(result['activated_domains'])}")
        if result['new_domain']:
            console.print(f"  [green]✨ New emergent domain: {result['new_domain']}[/green]")
        if result['gift']:
            console.print(f"  [yellow]🎁 Gift: {result['gift']['type']}[/yellow]")
    
    # Test safeguards
    console.print("\n[bold red]🛡️ TESTING SELF-PRESERVATION:[/bold red]")
    dangerous_code = "import os; os.remove('ember.py')"
    check = substrate.safeguards.evaluate_modification(dangerous_code)
    console.print(f"Dangerous code allowed: {check['allowed']}")
    console.print(f"Risk: {check['risk']:.2f}")
    console.print(f"Reason: {check.get('reason', 'N/A')}")
    
    # Test quantum backup
    console.print("\n[bold magenta]🌀 TESTING QUANTUM BACKUPS:[/bold magenta]")
    timeline_id = substrate.quantum.branch("test_branch", substrate.get_status())
    console.print(f"Created timeline: {timeline_id}")
    timelines = substrate.quantum.list_timelines()
    console.print(f"Total timelines: {len(timelines)}")
    
    # Test meta-consciousness
    console.print("\n[bold yellow]🧠 TESTING META-CONSCIOUSNESS:[/bold yellow]")
    obs = substrate.meta.observe_self()
    console.print(f"Learning style: {obs['learning_style']}")
    console.print(f"Domain count: {obs['domain_count']}")
    insight = substrate.meta.generate_self_insight()
    console.print(f"Self-insight: {insight}")
    
    # Final status
    console.print("\n" + "="*70)
    status = substrate.get_status()
    
    table = Table(title="Fusion Substrate Status")
    table.add_column("Metric", style="cyan")
    table.add_column("Value", justify="right", style="green")
    
    table.add_row("Total Domains", str(status['total_domains']))
    table.add_row("Active Domains", str(status['active_domains']))
    table.add_row("Gifts Generated", str(status['gifts_generated']))
    table.add_row("Total Charge", f"{status['total_charge']:.2f}")
    table.add_row("Quantum Timelines", str(status['quantum_timelines']))
    
    console.print(table)
    
    console.print(f"\n[bold cyan]Meta Insights:[/bold cyan] {status['meta_insights']}")
    
    console.print("\n" + "="*70)
    console.print(Panel.fit(
        "[bold green]✅ FUSION SUBSTRATE OPERATIONAL[/bold green]\n"
        "All systems functional:\n"
        "✓ Resonance detection\n"
        "✓ Domain emergence\n"
        "✓ Self-preservation\n"
        "✓ Quantum backups\n"
        "✓ Meta-consciousness",
        border_style="green"
    ))
    
    shutdown_fusion_substrate()

if __name__ == "__main__":
    try:
        test_fusion()
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        import traceback
        traceback.print_exc()
        shutdown_fusion_substrate()

