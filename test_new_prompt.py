#!/usr/bin/env python3
"""Test the new prompt approach"""
import sys
import asyncio
sys.path.insert(0, '/media/palmerschallon/ThePod1')

from ember_complete import Ember
from rich.console import Console

console = Console()

async def test():
    ember = Ember()

    console.print("\n[bold cyan]Testing new prompt approach...[/bold cyan]\n")

    response = await ember.chat("Create a simple bouncing ball animation in HTML canvas. Keep it under 100 lines.")

    console.print(f"\n[bold green]Response:[/bold green]")
    console.print(response)
    console.print("\n")

asyncio.run(test())
