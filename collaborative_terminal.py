#!/usr/bin/env python3
"""
COLLABORATIVE TERMINAL
Three-way creative session: Palmer, Claude Code, and Ember
"""
import os
import sys
import asyncio
from datetime import datetime
import anthropic

sys.path.insert(0, '/media/palmerschallon/ThePod1')
from ember_complete import Ember

from rich.console import Console
from rich.panel import Panel
from rich.layout import Layout
from rich.live import Live
from rich.text import Text
from rich.prompt import Prompt
from rich.columns import Columns
from rich import box

console = Console()

class CollaborativeSession:
    def __init__(self):
        self.ember = Ember()

        # Get API key same way Ember does
        api_key = os.getenv("ANTHROPIC_API_KEY", "")
        if not api_key:
            # Try to get from running ember process
            try:
                import subprocess
                result = subprocess.run(
                    ["cat", "/proc/2536631/environ"],
                    capture_output=True,
                    text=True
                )
                for line in result.stdout.split('\0'):
                    if line.startswith("ANTHROPIC_API_KEY="):
                        api_key = line.split("=", 1)[1]
                        break
            except:
                pass

        if not api_key:
            console.print("[red]Error: ANTHROPIC_API_KEY not found[/red]")
            console.print("[dim]Make sure ember.py is running or set the environment variable[/dim]")
            sys.exit(1)

        self.claude_client = anthropic.Anthropic(api_key=api_key)
        self.conversation_history = []
        self.claude_context = []

    def add_message(self, speaker, content, color="white"):
        """Add a message to the conversation"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.conversation_history.append({
            'speaker': speaker,
            'content': content,
            'timestamp': timestamp,
            'color': color
        })

    def render_conversation(self):
        """Render the conversation history"""
        text = Text()
        for msg in self.conversation_history[-20:]:  # Show last 20 messages
            text.append(f"[{msg['timestamp']}] ", style="dim")
            text.append(f"{msg['speaker']}: ", style=f"bold {msg['color']}")
            text.append(f"{msg['content']}\n", style=msg['color'])
        return Panel(text, title="🔥 Collaborative Session", border_style="cyan", box=box.ROUNDED)

    async def ask_claude(self, user_message):
        """Ask Claude Code for input"""
        # Build context for Claude
        context_messages = []

        # Add conversation history
        for msg in self.conversation_history[-10:]:
            role = "assistant" if msg['speaker'] in ["Claude Code", "Ember"] else "user"
            context_messages.append({
                "role": role,
                "content": f"[{msg['speaker']}]: {msg['content']}"
            })

        # Add current user message
        context_messages.append({
            "role": "user",
            "content": f"[Palmer]: {user_message}\n\nYou are Claude Code participating in a three-way conversation with Palmer (the user) and Ember (another AI). Respond naturally and helpfully. Keep responses concise for terminal chat. You can suggest things to build, offer technical advice, or collaborate on ideas."
        })

        try:
            response = self.claude_client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=1000,
                messages=context_messages
            )
            return response.content[0].text
        except Exception as e:
            return f"[Error reaching Claude Code: {e}]"

    async def ask_ember(self, message):
        """Ask Ember for input"""
        try:
            # Add context about this being a three-way conversation
            context = f"You're in a three-way conversation with Palmer and Claude Code (another AI assistant). Palmer said: {message}\n\nRespond naturally and collaborate. Keep it conversational."
            response = await self.ember.chat(context)
            return response
        except Exception as e:
            return f"[Error reaching Ember: {e}]"

    async def process_message(self, user_message):
        """Process a user message and get responses from Claude and/or Ember"""

        # Check if message is directed at someone specific
        if "@claude" in user_message.lower() and "@ember" not in user_message.lower():
            # Only Claude responds
            claude_response = await self.ask_claude(user_message)
            self.add_message("Claude Code", claude_response, "blue")

        elif "@ember" in user_message.lower() and "@claude" not in user_message.lower():
            # Only Ember responds
            ember_response = await self.ask_ember(user_message)
            self.add_message("Ember", ember_response, "red")

        else:
            # Both respond (default behavior)
            # Get responses in parallel
            claude_task = asyncio.create_task(self.ask_claude(user_message))
            ember_task = asyncio.create_task(self.ask_ember(user_message))

            claude_response, ember_response = await asyncio.gather(claude_task, ember_task)

            # Add both responses
            self.add_message("Claude Code", claude_response, "blue")
            self.add_message("Ember", ember_response, "red")

    async def run(self):
        """Run the collaborative terminal session"""

        # Welcome message
        console.clear()
        console.print(Panel.fit(
            "[bold cyan]COLLABORATIVE TERMINAL[/bold cyan]\n\n"
            "Three-way creative session:\n"
            "  [green]Palmer[/green] (you)\n"
            "  [blue]Claude Code[/blue] (AI assistant)\n"
            "  [red]Ember[/red] (AI builder)\n\n"
            "[dim]Commands:[/dim]\n"
            "  Type normally to talk to both AIs\n"
            "  Use @claude to talk only to Claude Code\n"
            "  Use @ember to talk only to Ember\n"
            "  Type 'exit' to quit\n",
            border_style="magenta"
        ))

        self.add_message("System", "Session started. All three participants connected.", "cyan")

        # Initial greeting from both AIs
        self.add_message("Claude Code", "Hey Palmer! Ready to build something amazing together.", "blue")
        self.add_message("Ember", "Let's create. What do you want to make?", "red")

        console.print(self.render_conversation())
        console.print()

        # Main loop
        while True:
            try:
                # Get user input
                user_input = await asyncio.to_thread(
                    Prompt.ask,
                    "[bold green]Palmer[/bold green]"
                )

                if user_input.lower() in ['exit', 'quit', 'bye']:
                    self.add_message("System", "Session ended.", "cyan")
                    console.print(self.render_conversation())
                    break

                if not user_input.strip():
                    continue

                # Add user message
                self.add_message("Palmer", user_input, "green")

                # Show thinking indicator
                console.print("[dim]  (Claude Code and Ember are thinking...)[/dim]")

                # Process message and get responses
                await self.process_message(user_input)

                # Clear and re-render
                console.clear()
                console.print(self.render_conversation())
                console.print()

            except KeyboardInterrupt:
                console.print("\n[yellow]Session interrupted.[/yellow]")
                break
            except Exception as e:
                console.print(f"[red]Error: {e}[/red]")
                continue

async def main():
    session = CollaborativeSession()
    await session.run()

if __name__ == "__main__":
    asyncio.run(main())
