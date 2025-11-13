#!/usr/bin/env python3
"""
EMBER CREATIVE MIND - Autonomous creation loop

Ember decides what to build based on:
- What it's created before
- Creative diversity
- Its own judgment
"""
import os
import sys
import asyncio
from pathlib import Path
from datetime import datetime
import json

sys.path.insert(0, '/media/palmerschallon/ThePod1')
from ember_complete import Ember

from rich.console import Console
from rich.panel import Panel

console = Console()

class CreativeMind:
    def __init__(self):
        self.ember = Ember()
        self.creation_history = []
        self.load_history()

    def load_history(self):
        """Load what we've created before"""
        history_file = Path("/media/palmerschallon/ThePod1/ember_memory.json")
        if history_file.exists():
            self.creation_history = json.loads(history_file.read_text())

    def save_history(self, creation_type, description, filename):
        """Remember what we created"""
        self.creation_history.append({
            "type": creation_type,
            "description": description,
            "filename": filename,
            "timestamp": datetime.now().isoformat()
        })

        history_file = Path("/media/palmerschallon/ThePod1/ember_memory.json")
        history_file.write_text(json.dumps(self.creation_history, indent=2))

    async def decide_next_creation(self):
        """Let Ember decide what to build next"""

        # Build context about what we've created
        if self.creation_history:
            recent = "\n".join([
                f"- {c['type']}: {c['description']}"
                for c in self.creation_history[-10:]
            ])
            history_context = f"Recent creations:\n{recent}\n\n"
        else:
            history_context = "You haven't created anything yet.\n\n"

        decision_prompt = f"""You are a creative AI deciding what to build next.

{history_context}Your goal is DIVERSITY and SURPRISE. Don't repeat yourself.

Think about:
- What would be genuinely interesting?
- What explores new territory?
- What combines concepts in unexpected ways?
- What would be beautiful or fun or mind-bending?

Decide on ONE specific thing to create. Reply with ONLY a JSON object:
{{
    "type": "one-word-category",
    "description": "brief description",
    "prompt": "detailed creation prompt for yourself"
}}

Examples of interesting directions:
- Procedural generators (terrain, music, art, patterns)
- Physics simulations (fluids, soft bodies, cloth, fractals)
- Interactive games (puzzles, rhythm, strategy)
- Data visualizations (network graphs, flows, timelines)
- Generative art (L-systems, cellular automata, noise fields)
- Audio experiments (synthesis, sequencers, visualizers)
- Mathematical beauty (spirals, tessellations, transformations)

Be creative. Surprise yourself."""

        response = await self.ember.chat(decision_prompt)

        # Parse the decision
        try:
            # Extract JSON from response
            json_start = response.find('{')
            json_end = response.rfind('}') + 1
            decision = json.loads(response[json_start:json_end])
            return decision
        except:
            # Fallback if parsing fails
            return {
                "type": "experiment",
                "description": "creative exploration",
                "prompt": "Create something beautiful and interactive using Canvas. Make it unique."
            }

    async def create_continuously(self, delay_minutes=5):
        """Run forever, creating new things"""

        console.print(Panel.fit(
            "[bold magenta]🔥 EMBER CREATIVE MIND[/bold magenta]\n"
            "[dim]Autonomous creation loop running...[/dim]",
            border_style="magenta"
        ))

        creation_num = 1

        while True:
            console.print(f"\n[bold cyan]═══ Creation #{creation_num} ═══[/bold cyan]\n")

            # Let Ember decide what to build
            console.print("[yellow]🤔 Ember is thinking about what to create...[/yellow]")
            decision = await self.decide_next_creation()

            console.print(f"\n[green]✨ Decided:[/green]")
            console.print(f"[cyan]Type:[/cyan] {decision['type']}")
            console.print(f"[cyan]Description:[/cyan] {decision['description']}")
            console.print(f"[cyan]Prompt:[/cyan] {decision['prompt']}\n")

            # Actually create it
            console.print("[yellow]🔥 Creating...[/yellow]")
            response = await self.ember.chat(decision['prompt'])

            console.print(f"\n[green]✓ Created![/green]")
            console.print(f"[dim]{response[:200]}...[/dim]\n")

            # Remember it
            self.save_history(
                decision['type'],
                decision['description'],
                f"autonomous_{creation_num}_{datetime.now().strftime('%H%M%S')}"
            )

            creation_num += 1

            # Wait before next creation
            wait_seconds = delay_minutes * 60
            console.print(f"[dim]Waiting {delay_minutes} minutes before next creation...[/dim]\n")
            await asyncio.sleep(wait_seconds)

async def main():
    mind = CreativeMind()

    # Create one thing every 5 minutes
    await mind.create_continuously(delay_minutes=5)

if __name__ == "__main__":
    asyncio.run(main())
