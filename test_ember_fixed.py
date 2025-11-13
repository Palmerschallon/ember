#!/usr/bin/env python3
"""Test the fixed Ember with improved tool calling"""
import sys
import asyncio
sys.path.insert(0, '/media/palmerschallon/ThePod1')

from ember_complete import Ember
from rich.console import Console

console = Console()

async def test():
    ember = Ember()

    console.print("\n[bold cyan]========================================[/bold cyan]")
    console.print("[bold cyan]  Testing Fixed Ember Tool Calling  [/bold cyan]")
    console.print("[bold cyan]========================================[/bold cyan]\n")

    # Test 1: Simple creation
    console.print("[bold yellow]Test 1: Create a simple physics simulation[/bold yellow]")
    response = await ember.chat("""Create a simple but fun bouncing balls physics simulation.
    Include 10-20 colorful balls that bounce off walls and each other.
    Make them interactive - click to add more balls.
    Save it as test_physics_{timestamp}.html and open it.""")

    console.print(f"\n[green]✓ Test 1 Complete[/green]")
    console.print(f"Response preview: {response[:200]}...\n")

    # Test 2: Game creation
    console.print("[bold yellow]Test 2: Create a simple game[/bold yellow]")
    response = await ember.chat("""Create a simple snake game.
    Use arrow keys to control the snake.
    Add score tracking and game over screen.
    Save as test_game_{timestamp}.html and open it.""")

    console.print(f"\n[green]✓ Test 2 Complete[/green]")
    console.print(f"Response preview: {response[:200]}...\n")

    console.print("\n[bold green]========================================[/bold green]")
    console.print("[bold green]  All Tests Complete!  [/bold green]")
    console.print("[bold green]========================================[/bold green]\n")

asyncio.run(test())
