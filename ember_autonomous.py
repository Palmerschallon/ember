#!/usr/bin/env python3
"""
EMBER AUTONOMOUS - Self-debugging, self-fixing loop
"""
import os
import sys
import subprocess
import asyncio
from pathlib import Path

sys.path.insert(0, '/media/palmerschallon/ThePod1')
from ember_complete import Ember

from rich.console import Console
from rich.panel import Panel

console = Console()

async def self_debug():
    """Ember debugs and fixes itself"""

    console.print("\n[bold magenta]🔥 EMBER AUTONOMOUS MODE[/bold magenta]\n")
    console.print("[dim]Self-debugging, self-fixing, self-improving...[/dim]\n")

    ember = Ember()

    # Give Ember the problem
    problem = """The VR world at /media/palmerschallon/ThePod1/vr_ember_integrated.html won't load on Quest 3.

Current setup:
- HTTPS server running on https://10.0.0.100:8443
- WebSocket bridge on port 8081 (ws://)
- Quest 3 trying to access the page

The issue is likely:
1. WebSocket needs to be wss:// (secure) not ws:// because HTTPS pages can't use insecure websockets
2. Mixed content blocking
3. Need secure WebSocket server

Your task:
1. Read the VR HTML file
2. Check what's wrong
3. Fix it (update WebSocket URL, create wss:// server if needed)
4. Test it
5. If it doesn't work, iterate again

You have ALL the tools: read_file, write_file, bash. Fix yourself."""

    console.print(f"[yellow]Problem given to Ember:[/yellow]\n{problem}\n")

    # Let Ember work
    response = await ember.chat(problem)

    console.print(f"\n[green]Ember's response:[/green]\n{response}\n")

    # Give Ember a chance to iterate
    console.print("\n[yellow]Asking Ember to verify the fix...[/yellow]\n")

    verify = await ember.chat("Did you successfully fix the issue? If not, debug further and fix it. Don't stop until it works.")

    console.print(f"\n[green]Ember says:[/green]\n{verify}\n")

if __name__ == "__main__":
    asyncio.run(self_debug())
