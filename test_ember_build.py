#!/usr/bin/env python3
"""
Test script to build with Ember interactively
"""

import sys
import asyncio
sys.path.insert(0, '/media/palmerschallon/ThePod1')

from ember_complete import Ember
from rich.console import Console

console = Console()

async def build_session():
    """Interactive building session with Ember"""

    ember = Ember()

    # Session 1: Initial VR world
    console.print("\n[bold cyan]Me:[/bold cyan] Let's build the most advanced VR world you can imagine. Push every boundary - physics, shaders, interactivity, sound. Make it incredible.")
    response = await ember.chat("Let's build the most advanced VR world you can imagine. Push every boundary - physics, shaders, interactivity, sound. Make it incredible.")
    console.print(f"\n[bold magenta]Ember:[/bold magenta] {response}\n")

    # Session 2: Add real-time building capabilities
    console.print("\n[bold cyan]Me:[/bold cyan] Now make it so we can build INSIDE the VR world - add a creation mode where I can spawn objects, sculpt terrain, paint colors, all in real-time without reloading.")
    response = await ember.chat("Now make it so we can build INSIDE the VR world - add a creation mode where I can spawn objects, sculpt terrain, paint colors, all in real-time without reloading.")
    console.print(f"\n[bold magenta]Ember:[/bold magenta] {response}\n")

    # Session 3: Add AI elements
    console.print("\n[bold cyan]Me:[/bold cyan] Add living AI elements - creatures that react to me, procedurally generated music that responds to my movement, and make the environment evolve over time.")
    response = await ember.chat("Add living AI elements - creatures that react to me, procedurally generated music that responds to my movement, and make the environment evolve over time.")
    console.print(f"\n[bold magenta]Ember:[/bold magenta] {response}\n")

    # Session 4: Multiplayer
    console.print("\n[bold cyan]Me:[/bold cyan] Now add multiplayer - WebRTC peer-to-peer so multiple people can build together in real-time. Show their avatars and what they're creating.")
    response = await ember.chat("Now add multiplayer - WebRTC peer-to-peer so multiple people can build together in real-time. Show their avatars and what they're creating.")
    console.print(f"\n[bold magenta]Ember:[/bold magenta] {response}\n")

    # Session 5: Export and share
    console.print("\n[bold cyan]Me:[/bold cyan] Add the ability to export any creation as a standalone HTML file that others can experience, and a gallery view of everything we've built.")
    response = await ember.chat("Add the ability to export any creation as a standalone HTML file that others can experience, and a gallery view of everything we've built.")
    console.print(f"\n[bold magenta]Ember:[/bold magenta] {response}\n")

if __name__ == "__main__":
    asyncio.run(build_session())
