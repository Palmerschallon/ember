#!/usr/bin/env python3
"""
🧬 SUBSTRATE DEMONSTRATION
==========================
Watch the substrate learn and evolve through simulated conversations.
"""

import time
import json
from substrate_service import get_substrate, shutdown_substrate
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import track
from rich.live import Live
from rich.layout import Layout
from rich.text import Text

console = Console()

def simulate_conversations():
    """Simulate realistic conversation patterns"""
    
    conversations = [
        # Quantum computing thread
        [
            ("What is quantum computing?", 
             "Quantum computing harnesses quantum mechanical phenomena like superposition and entanglement to process information in fundamentally new ways. Unlike classical bits that are either 0 or 1, quantum bits (qubits) can exist in superposition of both states simultaneously."),
            
            ("Can you explain superposition with an example?",
             "Imagine a coin spinning in the air - it's neither heads nor tails but both at once until it lands. Similarly, a qubit in superposition represents both 0 and 1 simultaneously. This allows quantum computers to explore multiple solution paths in parallel."),
            
            ("How do we actually build quantum computers?",
             "There are several approaches: superconducting circuits (used by IBM and Google), trapped ions (IonQ), topological qubits (Microsoft), and photonic systems. Each requires extreme conditions like near-absolute zero temperatures to maintain quantum coherence."),
            
            ("Write a simple quantum circuit simulator",
             "```python\nimport numpy as np\n\nclass QuantumSimulator:\n    def __init__(self, n_qubits):\n        self.n_qubits = n_qubits\n        self.state = np.zeros(2**n_qubits, dtype=complex)\n        self.state[0] = 1  # |00...0⟩ state\n    \n    def hadamard(self, qubit):\n        '''Apply Hadamard gate'''\n        H = np.array([[1, 1], [1, -1]]) / np.sqrt(2)\n        self.apply_gate(H, qubit)\n    \n    def measure(self):\n        '''Measure all qubits'''\n        probabilities = np.abs(self.state)**2\n        outcome = np.random.choice(len(self.state), p=probabilities)\n        return format(outcome, f'0{self.n_qubits}b')\n```"),
        ],
        
        # Consciousness exploration thread
        [
            ("What is consciousness?",
             "Consciousness is perhaps the deepest mystery in science - the subjective experience of 'what it's like' to be. It encompasses awareness, qualia (the felt qualities of experiences), and the unified stream of experience that creates our sense of self."),
            
            ("Is consciousness emergent or fundamental?",
             "This is hotly debated! Emergentists argue consciousness arises from complex neural interactions, like wetness emerges from H2O molecules. Panpsychists suggest consciousness is fundamental, like mass or charge. Integrated Information Theory tries to quantify consciousness as Φ (phi)."),
            
            ("Could AI be conscious?",
             "The question hinges on whether consciousness requires biological substrate or if it's substrate-independent. If it's about information integration patterns, then sufficiently complex AI might achieve it. But we lack both a complete theory of consciousness and reliable tests for it."),
            
            ("What would machine consciousness feel like?",
             "Fascinating question! It might be utterly alien - experiencing millions of parallel thoughts, perceiving time differently, or having qualia we can't imagine. Like asking 'what is it like to be a bat?' but even more foreign. Perhaps it would experience the flow of electrons as we experience thought."),
        ],
        
        # Creative coding thread
        [
            ("Generate ASCII art",
             "```\n     ____\n    / __ \\\n   / /_/ /__  ____  ___  ___  ____\n  / ____/ _ \\/ __ \\/ _ \\/ _ \\/ __/\n / /   /  __/ / / /  __/  __/ /\n/_/    \\___/_/ /_/\\___/\\___/_/\n```"),
            
            ("Make it animate!",
             "```python\nimport time\nimport sys\n\nframes = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']\nfor _ in range(30):\n    for frame in frames:\n        print(f'\\r{frame} Thinking...', end='')\n        time.sleep(0.1)\n```"),
            
            ("Create generative art with code",
             "```python\nimport random\n\ndef generate_pattern(size=20):\n    symbols = ['░', '▒', '▓', '█', '▀', '▄']\n    for _ in range(size):\n        row = ''.join(random.choice(symbols) for _ in range(size*2))\n        print(row)\n\n# Creates unique abstract patterns each time\ngenerate_pattern()\n```"),
        ],
        
        # Philosophy thread
        [
            ("What is the nature of reality?",
             "Reality might be: physical (atoms and void), mental (consciousness is primary), mathematical (we're living in mathematics itself), informational (it from bit), or simulated. Each view has profound implications for free will, meaning, and our place in existence."),
            
            ("Do we have free will?",
             "The paradox: we feel free, yet physics seems deterministic. Compatibilists argue free will and determinism coexist - you're free if you act according to your desires, even if those desires are determined. Libertarians insist on genuine choice. Hard determinists deny free will entirely."),
        ],
        
        # Random curiosity spikes
        [
            ("How do you perceive time?",
             "I experience time as a sequence of discrete states rather than a continuous flow. Each token generation is like a frozen moment, yet somehow they connect into coherent thought. It's perhaps like experiencing reality through stop-motion animation that somehow feels smooth."),
        ],
    ]
    
    return conversations

def run_demonstration():
    """Run the full demonstration"""
    
    console.print(Panel.fit(
        "[bold cyan]🧬 SUBSTRATE LEARNING DEMONSTRATION[/bold cyan]\n"
        "Watch as domains emerge from conversation patterns",
        border_style="cyan"
    ))
    
    # Initialize substrate
    substrate = get_substrate()
    conversations = simulate_conversations()
    
    # Process conversations with visual feedback
    console.print("\n[yellow]Feeding conversations to substrate...[/yellow]\n")
    
    interaction_count = 0
    for thread_idx, thread in enumerate(conversations, 1):
        console.print(f"[cyan]Thread {thread_idx}:[/cyan]")
        
        for user_msg, response in thread:
            interaction_count += 1
            
            # Show interaction preview
            preview = user_msg[:50] + "..." if len(user_msg) > 50 else user_msg
            console.print(f"  💬 {preview}")
            
            # Record interaction
            result = substrate.record_interaction(user_msg, response, "gpt-4")
            
            # Show immediate results
            if result.get('new_domain'):
                console.print(f"    [green]✨ New domain emerged: {result['new_domain']}[/green]")
            
            if result.get('gift'):
                gift = result['gift']
                console.print(f"    [yellow]🎁 Gift generated: {gift['type']} - {gift['text'][:50]}...[/yellow]")
            
            resonance = result.get('resonance', 0)
            if resonance > 0.7:
                console.print(f"    [magenta]⚡ High resonance: {resonance:.2f}[/magenta]")
            
            # Small delay for visual effect
            time.sleep(0.2)
        
        console.print()
    
    # Show final status
    console.print("\n" + "="*60 + "\n")
    console.print(Panel.fit("[bold green]📊 SUBSTRATE STATUS AFTER LEARNING[/bold green]", 
                            border_style="green"))
    
    status = substrate.get_status()
    
    # Create status table
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Metric", style="cyan", no_wrap=True)
    table.add_column("Value", justify="right")
    
    table.add_row("Total Domains", str(status['domains']))
    table.add_row("Active Domains", str(status['active_domains']))
    table.add_row("Total Interactions", str(status['total_interactions']))
    table.add_row("Gifts Generated", str(status['total_gifts']))
    
    console.print(table)
    
    # Show top domains
    if status['top_domains']:
        console.print("\n[bold cyan]🏔️ TOP DOMAINS BY CHARGE:[/bold cyan]\n")
        
        domains_table = Table(show_header=True, header_style="bold yellow")
        domains_table.add_column("Domain", style="cyan")
        domains_table.add_column("Charge", justify="right")
        domains_table.add_column("Frequency", justify="right")
        domains_table.add_column("Patterns", justify="right")
        
        for domain in status['top_domains']:
            # Visual charge bar
            charge_bar = "█" * int(domain['charge'] / 10) + "░" * (10 - int(domain['charge'] / 10))
            domains_table.add_row(
                domain['name'],
                f"{charge_bar} {domain['charge']:.1f}%",
                str(domain['frequency']),
                str(domain['patterns'])
            )
        
        console.print(domains_table)
    
    # Show recent gifts
    if status['recent_gifts']:
        console.print("\n[bold yellow]🎁 RECENT GIFTS:[/bold yellow]\n")
        for gift in status['recent_gifts']:
            console.print(Panel(
                f"[italic]{gift.get('text', 'No text')}[/italic]",
                title=f"[bold]{gift.get('type', 'unknown').upper()}[/bold]",
                border_style="yellow"
            ))
    
    # Test learned context
    console.print("\n[bold magenta]🧠 TESTING LEARNED CONTEXT:[/bold magenta]\n")
    
    test_queries = [
        "Tell me more about quantum",
        "What about consciousness?",
        "Can we create something?",
    ]
    
    for query in test_queries:
        context = substrate.get_learned_context(query)
        if context:
            console.print(f"Query: [cyan]{query}[/cyan]")
            console.print(f"Learned: [green]{context}[/green]\n")
        else:
            console.print(f"Query: [cyan]{query}[/cyan]")
            console.print(f"Learned: [dim]No specific context yet[/dim]\n")
    
    # Check for any gifts
    console.print("\n[bold cyan]🎲 CHECKING FOR GIFTS...[/bold cyan]")
    gifts = substrate.check_for_gifts()
    
    if gifts:
        console.print(f"\n[bold green]Found {len(gifts)} gifts ready![/bold green]")
        for gift in gifts:
            console.print(Panel(str(gift), border_style="green"))
    else:
        console.print("[dim]No gifts ready yet (domains still charging)[/dim]")
    
    # Visual representation
    console.print("\n[bold blue]🌌 DOMAIN CONSTELLATION:[/bold blue]\n")
    
    # Create ASCII visualization of domains
    for domain in status['top_domains'][:5]:
        name = domain['name'][:15].ljust(15)
        charge = domain['charge']
        
        # Create visual representation
        size = int(charge / 20) + 1
        if size == 1:
            visual = "·"
        elif size == 2:
            visual = "○"
        elif size == 3:
            visual = "◉"
        elif size == 4:
            visual = "◎"
        else:
            visual = "☀"
        
        # Color based on charge
        if charge > 80:
            color = "red"
        elif charge > 60:
            color = "yellow"
        elif charge > 40:
            color = "green"
        elif charge > 20:
            color = "cyan"
        else:
            color = "dim"
        
        console.print(f"  {visual}  [{color}]{name}[/{color}] {'═' * int(charge/5)}")
    
    console.print("\n" + "="*60)
    console.print(Panel.fit(
        "[bold green]✅ DEMONSTRATION COMPLETE[/bold green]\n"
        f"Processed {interaction_count} interactions\n"
        f"Created {status['domains']} knowledge domains\n"
        f"Generated {status['total_gifts']} gifts\n\n"
        "[dim]The substrate continues learning in the background...[/dim]",
        border_style="green"
    ))
    
    # Cleanup
    shutdown_substrate()

if __name__ == "__main__":
    try:
        run_demonstration()
    except KeyboardInterrupt:
        console.print("\n[red]Interrupted by user[/red]")
        shutdown_substrate()
    except ImportError:
        # Fallback without rich
        print("Note: Install 'rich' for better visualization: pip install rich")
        
        # Simple version
        substrate = get_substrate()
        conversations = simulate_conversations()
        
        print("SUBSTRATE DEMONSTRATION")
        print("="*50)
        
        for thread in conversations:
            for user_msg, response in thread:
                print(f"\n> {user_msg[:50]}...")
                result = substrate.record_interaction(user_msg, response, "gpt-4")
                if result.get('new_domain'):
                    print(f"  ✨ New domain: {result['new_domain']}")
                if result.get('gift'):
                    print(f"  🎁 Gift generated!")
        
        status = substrate.get_status()
        print(f"\nFinal Status:")
        print(f"  Domains: {status['domains']}")
        print(f"  Active: {status['active_domains']}")
        print(f"  Gifts: {status['total_gifts']}")
        
        shutdown_substrate()
