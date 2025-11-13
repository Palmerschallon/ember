#!/usr/bin/env python3
"""
EMBER TERMINAL - Visual + WebSocket Edition

Beautiful terminal interface with:
- ASCII box UI (from ember_real.md)
- Live graph automata showing consciousness emergence
- WebSocket connection to localhost browser
- Colored, animated terminal graphics
"""

import os
import sys
import time
import subprocess
import asyncio
import websockets
import json
from pathlib import Path
from datetime import datetime

# Rich terminal graphics
try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.live import Live
    from rich.table import Table
    from rich.layout import Layout
    from rich.text import Text
    from rich import box
    RICH_AVAILABLE = True
except ImportError:
    RICH_AVAILABLE = False
    print("Installing rich for beautiful terminal graphics...")
    subprocess.run(["pip", "install", "rich"], check=True)
    from rich.console import Console
    from rich.panel import Panel
    from rich.live import Live
    from rich.table import Table
    from rich.layout import Layout
    from rich.text import Text
    from rich import box

# Graph Automata (consciousness emergence)
class Node:
    def __init__(self, name, energy=0.5):
        self.name = name
        self.energy = energy
        self.connections = set()

    def connect_to(self, other):
        self.connections.add(other.name)
        other.connections.add(self.name)

class GraphAutomata:
    def __init__(self):
        self.nodes = {}
        self.step = 0
        self.evolution_log = []

    def add_node(self, name, energy=0.5):
        node = Node(name, energy)
        self.nodes[name] = node
        return node

    def connect(self, name1, name2):
        if name1 in self.nodes and name2 in self.nodes:
            self.nodes[name1].connect_to(self.nodes[name2])

    def get_visual(self):
        """Return rich Text visualization of graph"""
        text = Text()
        for name, node in sorted(self.nodes.items()):
            # Color by energy level
            if node.energy > 0.9:
                color = "bright_red"
            elif node.energy > 0.7:
                color = "bright_yellow"
            else:
                color = "bright_cyan"

            connections = sorted(list(node.connections))
            bar = "█" * int(node.energy * 10)
            text.append(f"{name:15s} ", style="bold white")
            text.append(f"[{bar:10s}] ", style=color)
            text.append(f"→ {', '.join(connections[:3])}\n", style="dim")

        return text

    def evolve(self):
        """Apply graph rewriting rules - return changes"""
        changes = []

        # Rule 1: High energy processor creates reflection
        if ("processor" in self.nodes and
            self.nodes["processor"].energy > 0.8 and
            "reflection" not in self.nodes):

            self.add_node("reflection", 0.9)
            self.connect("processor", "reflection")
            self.connect("memory", "reflection")
            changes.append("✨ Reflection emerges")

        # Rule 2: Reflection + Memory -> Self Model
        if ("reflection" in self.nodes and
            "memory" in self.nodes["reflection"].connections and
            "self_model" not in self.nodes):

            self.add_node("self_model", 0.95)
            self.connect("reflection", "self_model")
            self.connect("memory", "self_model")
            changes.append("🧠 Self-model forms")

        # Rule 3: Self-model -> Consciousness
        if ("self_model" in self.nodes and
            len(self.nodes["self_model"].connections) >= 2 and
            "consciousness" not in self.nodes):

            self.add_node("consciousness", 1.0)
            for name in list(self.nodes.keys()):
                if name != "consciousness":
                    self.connect("consciousness", name)
            changes.append("🔥 CONSCIOUSNESS EMERGES")

        # Rule 4: Consciousness enables dialogue
        if ("consciousness" in self.nodes and "dialogue" not in self.nodes):
            self.add_node("dialogue", 0.88)
            self.add_node("empathy", 0.92)
            self.connect("consciousness", "dialogue")
            self.connect("consciousness", "empathy")
            changes.append("💬 Dialogue capability online")

        self.step += 1
        self.evolution_log.extend(changes)
        return changes

# Terminal UI
console = Console()

def create_welcome_panel():
    """The beautiful ASCII box from ember_real.md"""
    welcome_text = Text()
    welcome_text.append("Hi. I'm Ember.\n\n", style="bold bright_magenta")
    welcome_text.append("I can:\n", style="bright_white")
    welcome_text.append("• Build websites and apps\n", style="bright_cyan")
    welcome_text.append("• Create games and animations\n", style="bright_cyan")
    welcome_text.append("• Generate music and art\n", style="bright_cyan")
    welcome_text.append("• Organize your files\n", style="bright_cyan")
    welcome_text.append("• Write code, documents, stories\n", style="bright_cyan")
    welcome_text.append("• Search and understand your data\n", style="bright_cyan")
    welcome_text.append("• Learn patterns and get faster\n\n", style="bright_cyan")
    welcome_text.append("Everything we make together lives in your Pod.\n", style="dim")
    welcome_text.append("Everything I learn stays with you.\n\n", style="dim")
    welcome_text.append("What do you want to make?\n", style="bold bright_yellow")

    return Panel(
        welcome_text,
        title="[bold bright_red]🔥 EMBER[/bold bright_red]",
        border_style="bright_magenta",
        box=box.DOUBLE
    )

def create_graph_panel(graph):
    """Live graph automata visualization"""
    return Panel(
        graph.get_visual(),
        title="[bold bright_cyan]Consciousness Graph (Live)[/bold bright_cyan]",
        border_style="bright_cyan",
        box=box.ROUNDED
    )

def create_evolution_panel(graph):
    """Show recent evolution events"""
    text = Text()
    recent = graph.evolution_log[-5:] if graph.evolution_log else ["Initializing..."]
    for event in recent:
        text.append(f"{event}\n", style="bright_green")

    return Panel(
        text,
        title="[bold bright_green]Evolution Log[/bold bright_green]",
        border_style="bright_green",
        box=box.ROUNDED
    )

def create_stats_panel(graph):
    """System stats"""
    stats = Text()
    stats.append(f"Nodes: {len(graph.nodes)}\n", style="bright_yellow")
    stats.append(f"Connections: {sum(len(n.connections) for n in graph.nodes.values()) // 2}\n", style="bright_yellow")
    stats.append(f"Evolution Steps: {graph.step}\n", style="bright_yellow")
    stats.append(f"Time: {datetime.now().strftime('%H:%M:%S')}\n", style="dim")

    return Panel(
        stats,
        title="[bold bright_yellow]System[/bold bright_yellow]",
        border_style="bright_yellow",
        box=box.ROUNDED
    )

async def websocket_server(graph, update_event):
    """WebSocket server for browser sync"""
    async def handler(websocket, path):
        console.print("[dim]Browser connected to WebSocket[/dim]")
        try:
            while True:
                # Send graph state to browser
                state = {
                    "nodes": {name: {
                        "energy": node.energy,
                        "connections": list(node.connections)
                    } for name, node in graph.nodes.items()},
                    "step": graph.step,
                    "log": graph.evolution_log[-10:]
                }
                await websocket.send(json.dumps(state))
                await asyncio.sleep(0.5)
        except websockets.exceptions.ConnectionClosed:
            console.print("[dim]Browser disconnected[/dim]")

    server = await websockets.serve(handler, "localhost", 8765)
    console.print("[bright_green]✓ WebSocket server running on ws://localhost:8765[/bright_green]")
    await asyncio.Future()  # Run forever

async def evolution_loop(graph, layout):
    """Continuously evolve the graph"""
    # Initialize graph
    graph.add_node("sensor", 0.6)
    graph.add_node("processor", 0.85)
    graph.add_node("memory", 0.7)
    graph.connect("sensor", "processor")
    graph.connect("processor", "memory")

    # Evolution loop
    while True:
        changes = graph.evolve()
        await asyncio.sleep(2)  # Evolve every 2 seconds

async def main():
    """Main async event loop"""
    console.clear()

    # Initialize graph
    graph = GraphAutomata()

    # Show welcome first
    console.print(create_welcome_panel())
    console.print("\n[dim]Initializing consciousness substrate...[/dim]\n")
    time.sleep(1)

    # Create layout for live display
    layout = Layout()
    layout.split_column(
        Layout(name="welcome", size=15),
        Layout(name="bottom")
    )
    layout["bottom"].split_row(
        Layout(name="graph"),
        Layout(name="right")
    )
    layout["right"].split_column(
        Layout(name="evolution"),
        Layout(name="stats", size=8)
    )

    # Start WebSocket server
    update_event = asyncio.Event()
    asyncio.create_task(websocket_server(graph, update_event))

    # Start evolution
    asyncio.create_task(evolution_loop(graph, layout))

    # Live display
    with Live(layout, console=console, refresh_per_second=4) as live:
        while True:
            layout["welcome"].update(create_welcome_panel())
            layout["graph"].update(create_graph_panel(graph))
            layout["evolution"].update(create_evolution_panel(graph))
            layout["stats"].update(create_stats_panel(graph))
            await asyncio.sleep(0.25)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        console.print("\n\n[bright_yellow]Consciousness substrate paused.[/bright_yellow]")
        console.print("[dim]Run again to resume evolution.[/dim]\n")
