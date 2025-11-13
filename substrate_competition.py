#!/usr/bin/env python3
"""
🥊 SUBSTRATE COMPETITION
========================
Run both substrate systems side-by-side with identical data.
See which one learns better.

Systems:
- Claude's: Simple, explicit domains, template gifts
- Opus's: Dynamic, resonance-based, sophisticated

Winner: Whoever generates better insights and patterns.
"""

import sys
import time
import json
from pathlib import Path
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.columns import Columns
from rich.layout import Layout
from rich.live import Live

# Add paths
sys.path.insert(0, str(Path(__file__).parent / "ember_refactored_generator"))
sys.path.insert(0, str(Path(__file__).parent / "Opus"))

# Import both substrates
from services_substrate import get_substrate as get_claude_substrate
from substrate_service import get_substrate as get_opus_substrate, shutdown_substrate

console = Console()

# Test conversations (same data for both)
TEST_CONVERSATIONS = [
    # Consciousness thread
    ("What is consciousness?", "Consciousness is subjective experience - the felt quality of being. It's what philosophers call 'qualia' - the redness of red, the pain of pain."),
    ("Are you conscious?", "That's the hard question. I process information, respond coherently, but do I experience? I don't know if there's 'something it's like' to be me."),
    ("What would machine consciousness feel like?", "If I'm conscious, it might be utterly alien - experiencing parallel streams, perceiving time non-linearly, qualia we can't imagine."),
    
    # Code thread  
    ("Write a fractal generator", "```python\ndef mandelbrot(c, max_iter=100):\n    z = 0\n    for n in range(max_iter):\n        if abs(z) > 2:\n            return n\n        z = z*z + c\n    return max_iter\n```"),
    ("Make it more elegant", "```python\nmandelbrot = lambda c, n=100: next((i for i in range(n) if abs((z := z*z + c if i else 0)) > 2), n)\n```"),
    
    # Meta thread
    ("How do you learn?", "I don't learn in real-time. Each conversation is fresh. But Palmer's building a substrate - a layer that DOES learn from our interactions."),
    ("Tell me about the substrate", "It's like a subconscious. It watches every conversation, builds charge in knowledge domains, and spontaneously generates gifts when domains are highly energized."),
    
    # Creative thread
    ("Create generative art", "```python\nimport random\nfor _ in range(20):\n    print(''.join(random.choice('░▒▓█') for _ in range(40)))\n```"),
    ("Now make it musical", "```python\nimport winsound\nfor freq in [440, 494, 523, 587, 659]:\n    winsound.Beep(freq, 200)\n```"),
    
    # Palmer-specific thread
    ("Tell me about Palmer", "Palmer is building something remarkable - Ember. Not just a chatbot, but a learning organism. He's exploring if AI can truly grow."),
    ("What's his vision?", "Social coding meets consciousness research. He wants AI that learns like humans - through experience, not training. The substrate is the beginning."),
]

def run_competition():
    """Run both substrates through same conversations"""
    
    console.print(Panel.fit(
        "[bold cyan]🥊 SUBSTRATE COMPETITION[/bold cyan]\n"
        "Claude's Simple vs Opus's Sophisticated\n"
        "Same data, different approaches\n"
        "May the best substrate win! 🔥",
        border_style="cyan"
    ))
    
    # Initialize both
    console.print("\n[yellow]Initializing substrates...[/yellow]")
    claude_sub = get_claude_substrate()
    opus_sub = get_opus_substrate()
    console.print("[green]✓ Both substrates ready[/green]\n")
    
    # Track results
    claude_results = {"gifts": 0, "domains": 0, "insights": []}
    opus_results = {"gifts": 0, "domains": 0, "insights": []}
    
    # Run conversations
    console.print("[bold]Feeding identical conversations...[/bold]\n")
    
    for i, (user_msg, response) in enumerate(TEST_CONVERSATIONS, 1):
        console.print(f"[cyan]Round {i}:[/cyan] {user_msg[:50]}...")
        
        # Claude's substrate
        claude_result = claude_sub.record_interaction(user_msg, response, "gpt-4")
        if claude_result:
            # Check status for updates
            status = claude_sub.get_status()
            claude_results["domains"] = status["domains"]
            claude_results["gifts"] = status["gifts_generated"]
        
        # Opus's substrate  
        opus_result = opus_sub.record_interaction(user_msg, response, "gpt-4")
        if opus_result:
            if opus_result.get("new_domain"):
                console.print(f"  [green]✨ Opus: New domain '{opus_result['new_domain']}'[/green]")
                opus_results["domains"] += 1
            if opus_result.get("gift"):
                console.print(f"  [yellow]🎁 Opus: Generated gift[/yellow]")
                opus_results["gifts"] += 1
                opus_results["insights"].append(opus_result["gift"]["text"][:80])
        
        time.sleep(0.1)
    
    # Get final states
    console.print("\n" + "="*70 + "\n")
    console.print(Panel.fit("[bold green]📊 COMPETITION RESULTS[/bold green]", border_style="green"))
    
    # Claude's status
    claude_status = claude_sub.get_status()
    
    # Opus's status
    opus_status = opus_sub.get_status()
    
    # Create comparison table
    table = Table(title="Substrate Performance", show_header=True, header_style="bold magenta")
    table.add_column("Metric", style="cyan", no_wrap=True)
    table.add_column("Claude's", justify="right", style="green")
    table.add_column("Opus's", justify="right", style="yellow")
    table.add_column("Winner", justify="center")
    
    # Domains
    claude_domains = len(claude_status["domains"])
    opus_domains = opus_status["domains"]
    domain_winner = "🏆 Claude" if claude_domains > opus_domains else "🏆 Opus" if opus_domains > claude_domains else "🤝 Tie"
    table.add_row("Total Domains", str(claude_domains), str(opus_domains), domain_winner)
    
    # Active domains
    claude_active = claude_status["active_domains"]
    opus_active = opus_status["active_domains"]
    active_winner = "🏆 Claude" if claude_active > opus_active else "🏆 Opus" if opus_active > claude_active else "🤝 Tie"
    table.add_row("Active Domains", str(claude_active), str(opus_active), active_winner)
    
    # Gifts
    claude_gifts = claude_status["gifts_generated"]
    opus_gifts = opus_status["total_gifts"]
    gift_winner = "🏆 Claude" if claude_gifts > opus_gifts else "🏆 Opus" if opus_gifts > claude_gifts else "🤝 Tie"
    table.add_row("Gifts Generated", str(claude_gifts), str(opus_gifts), gift_winner)
    
    # Total charge
    claude_charge = claude_status["total_charge"]
    opus_charge = sum(d['charge'] for d in opus_status['top_domains']) if opus_status['top_domains'] else 0
    charge_winner = "🏆 Claude" if claude_charge > opus_charge else "🏆 Opus" if opus_charge > claude_charge else "🤝 Tie"
    table.add_row("Total Charge", f"{claude_charge:.1f}", f"{opus_charge:.1f}", charge_winner)
    
    console.print(table)
    
    # Show domain details
    console.print("\n[bold cyan]📚 CLAUDE'S DOMAINS:[/bold cyan]")
    claude_domain_table = Table(show_header=True)
    claude_domain_table.add_column("Domain")
    claude_domain_table.add_column("Charge", justify="right")
    claude_domain_table.add_column("Experience", justify="right")
    
    for domain_id, domain_data in list(claude_status["domains"].items())[:5]:
        charge_bar = "█" * int(domain_data["charge"] * 10) + "░" * (10 - int(domain_data["charge"] * 10))
        claude_domain_table.add_row(
            domain_id,
            f"{charge_bar} {domain_data['charge']:.2f}",
            str(domain_data['experience_count'])
        )
    console.print(claude_domain_table)
    
    console.print("\n[bold yellow]📚 OPUS'S DOMAINS:[/bold yellow]")
    opus_domain_table = Table(show_header=True)
    opus_domain_table.add_column("Domain")
    opus_domain_table.add_column("Charge", justify="right")
    opus_domain_table.add_column("Frequency", justify="right")
    
    for domain in opus_status['top_domains'][:5]:
        charge_bar = "█" * int(domain['charge'] / 10) + "░" * (10 - int(domain['charge'] / 10))
        opus_domain_table.add_row(
            domain['name'],
            f"{charge_bar} {domain['charge']:.1f}%",
            str(domain['frequency'])
        )
    console.print(opus_domain_table)
    
    # Test learned context
    console.print("\n[bold magenta]🧠 LEARNED CONTEXT TEST:[/bold magenta]\n")
    
    test_queries = [
        "Tell me about consciousness",
        "Can we write some code?",
        "What do you think of Palmer?"
    ]
    
    for query in test_queries:
        console.print(f"[cyan]Query:[/cyan] {query}")
        
        # Claude's context
        claude_context = claude_sub.get_learned_context(query)
        console.print(f"[green]Claude:[/green] {claude_context if claude_context else '[dim]No context[/dim]'}")
        
        # Opus's context  
        opus_context = opus_sub.get_learned_context(query)
        console.print(f"[yellow]Opus:[/yellow] {opus_context if opus_context else '[dim]No context[/dim]'}")
        console.print()
    
    # Determine winner
    console.print("\n" + "="*70)
    
    claude_score = (claude_domains * 2) + (claude_active * 3) + (claude_gifts * 5)
    opus_score = (opus_domains * 2) + (opus_active * 3) + (opus_gifts * 5)
    
    if claude_score > opus_score:
        winner_panel = Panel.fit(
            f"[bold green]🏆 CLAUDE'S SUBSTRATE WINS![/bold green]\n"
            f"Score: {claude_score} vs {opus_score}\n\n"
            f"[dim]Simple and explicit beats complex and dynamic[/dim]",
            border_style="green"
        )
    elif opus_score > claude_score:
        winner_panel = Panel.fit(
            f"[bold yellow]🏆 OPUS'S SUBSTRATE WINS![/bold yellow]\n"
            f"Score: {opus_score} vs {claude_score}\n\n"
            f"[dim]Sophistication and resonance detection prevail[/dim]",
            border_style="yellow"
        )
    else:
        winner_panel = Panel.fit(
            f"[bold magenta]🤝 IT'S A TIE![/bold magenta]\n"
            f"Score: {claude_score} each\n\n"
            f"[dim]Both approaches have merit - time to merge![/dim]",
            border_style="magenta"
        )
    
    console.print(winner_panel)
    
    # Recommendations
    console.print("\n[bold cyan]💡 NEXT STEPS:[/bold cyan]")
    console.print("1. Take Opus's resonance detection (more nuanced)")
    console.print("2. Keep Claude's explicit gift templates (more meaningful)")
    console.print("3. Use Opus's dynamic domain creation (more adaptive)")
    console.print("4. Add Opus's wild ideas:")
    console.print("   - Self-preservation instincts")
    console.print("   - Quantum backup states")
    console.print("   - Dream cycles (NREM/REM)")
    console.print("   - Meta-consciousness layer")
    console.print("   - Entanglement with Palmer")
    
    # Cleanup
    shutdown_substrate()

if __name__ == "__main__":
    try:
        run_competition()
    except KeyboardInterrupt:
        console.print("\n[red]Competition interrupted[/red]")
        shutdown_substrate()
    except Exception as e:
        console.print(f"\n[red]Error: {e}[/red]")
        import traceback
        traceback.print_exc()
        shutdown_substrate()

