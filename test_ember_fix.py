#!/usr/bin/env python3
"""Test if Ember now provides complete tool parameters"""
import sys
import asyncio
sys.path.insert(0, '/media/palmerschallon/ThePod1')

from ember_complete import Ember
from rich.console import Console

console = Console()

async def test():
    ember = Ember()

    console.print("\n[bold cyan]Testing Ember tool parameter fix...[/bold cyan]\n")

    # Simple test - create a basic HTML page
    console.print("[yellow]Test: Create a simple animated HTML page[/yellow]")
    response = await ember.chat("Create a simple HTML page with a bouncing ball animation using canvas. Save it as test_ball.html and open it.")

    console.print(f"\n[green]✓ Test complete![/green]")
    console.print(f"[dim]Check if test_ball.html was created successfully[/dim]\n")

asyncio.run(test())
