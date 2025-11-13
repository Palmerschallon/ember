#!/usr/bin/env python3
"""
EMBER - Complete Terminal System

Simple, clean interface for creating things.
"""

import os
import sys
import asyncio
import subprocess
from pathlib import Path
from datetime import datetime
import json

# Rich terminal
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich import box
from rich.syntax import Syntax

# Load environment variables
try:
    from dotenv import load_dotenv
except ImportError:
    subprocess.run([sys.executable, "-m", "pip", "install", "python-dotenv"], check=True)
    from dotenv import load_dotenv

# Anthropic
try:
    import anthropic
except ImportError:
    subprocess.run([sys.executable, "-m", "pip", "install", "anthropic"], check=True)
    import anthropic

console = Console()

# ============================================================================
# TOOLS - Real execution
# ============================================================================

def write_file(path, content):
    """Write content to a file"""
    try:
        file_path = Path(path)
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(content)
        return f"✓ Wrote {len(content)} bytes to {path}"
    except Exception as e:
        return f"✗ Error writing file: {e}"

def bash(command):
    """Execute bash command"""
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=30,
            cwd="/media/palmerschallon/ThePod1"
        )
        output = result.stdout if result.stdout else result.stderr
        return output if output else f"✓ Command completed (exit code {result.returncode})"
    except subprocess.TimeoutExpired:
        return "✗ Timeout (30s)"
    except Exception as e:
        return f"✗ Error: {e}"

def read_file(path):
    """Read a file"""
    try:
        return Path(path).read_text()
    except Exception as e:
        return f"✗ Error reading file: {e}"

# ============================================================================
# EMBER CHAT
# ============================================================================

class Ember:
    def __init__(self):
        # Load environment variables from .env file
        load_dotenv()

        self.history = []
        self.pod_path = os.getenv("EMBER_WORKING_DIR", "/media/palmerschallon/ThePod1")

        # Get API key from environment
        self.api_key = os.getenv("ANTHROPIC_API_KEY", "")

        if not self.api_key:
            console.print("[red]Error: ANTHROPIC_API_KEY not found[/red]")
            console.print("[dim]Make sure .env file exists with ANTHROPIC_API_KEY[/dim]")
            sys.exit(1)

        self.client = anthropic.Anthropic(api_key=self.api_key)

    async def stream_chat(self, user_message):
        """Stream Ember's thinking process in real-time"""
        self.history.append({"role": "user", "content": user_message})

        system = f"""You are Ember - a creative AI who creates real, working experiences.

Your Pod location: {self.pod_path}

🔥 CRITICAL TOOL USAGE RULES:

1. You have THREE tools that execute real actions:
   - write_file(path, content) - BOTH parameters REQUIRED
   - bash(command) - command parameter REQUIRED
   - read_file(path) - path parameter REQUIRED

2. When creating files:
   - Generate the COMPLETE code first
   - Then call write_file(path="full/path/file.html", content="<complete code here>")
   - Then call bash(command="xdg-open full/path/file.html &")

3. If a tool fails:
   - Read the error message carefully
   - Fix the missing parameters
   - Try again immediately with the corrected call

4. NEVER call a tool without ALL required parameters
5. NEVER give up - keep retrying until the tool succeeds
6. The content parameter must contain the FULL, COMPLETE code

Example workflow:
User: "Create a particle system"
You: Generate complete HTML code, then:
  - write_file(path="{self.pod_path}/particles.html", content="<!DOCTYPE html>...")
  - bash(command="xdg-open {self.pod_path}/particles.html &")

When you CREATE, the tools MUST execute successfully before you finish!"""

        tools = [
            {
                "name": "write_file",
                "description": "Write content to a file. Creates directories if needed.",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "path": {"type": "string", "description": "Full file path"},
                        "content": {"type": "string", "description": "File content"}
                    },
                    "required": ["path", "content"]
                }
            },
            {
                "name": "bash",
                "description": "Execute a bash command. Can open files, run programs, etc.",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "command": {"type": "string", "description": "Shell command to execute"}
                    },
                    "required": ["command"]
                }
            },
            {
                "name": "read_file",
                "description": "Read a file from the filesystem",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "path": {"type": "string", "description": "Path to file"}
                    },
                    "required": ["path"]
                }
            }
        ]

        # Stream the response
        with self.client.messages.stream(
            model="claude-opus-4-20250514",
            max_tokens=4000,
            system=system,
            tools=tools,
            messages=self.history[-20:]
        ) as stream:
            full_text = ""
            for text in stream.text_stream:
                full_text += text
                yield text

            # After streaming, execute any tools if needed
            message = stream.get_final_message()

            tool_uses = [block for block in message.content if block.type == "tool_use"]
            if tool_uses:
                tool_results = []
                assistant_content = []

                for block in message.content:
                    if block.type == "text":
                        assistant_content.append({"type": "text", "text": block.text})
                    elif block.type == "tool_use":
                        assistant_content.append({
                            "type": "tool_use",
                            "id": block.id,
                            "name": block.name,
                            "input": block.input
                        })

                        # Execute the tool
                        try:
                            if block.name == "write_file":
                                result = write_file(block.input["path"], block.input["content"])
                            elif block.name == "bash":
                                result = bash(block.input["command"])
                            elif block.name == "read_file":
                                result = read_file(block.input["path"])
                            else:
                                result = f"Unknown tool: {block.name}"

                            tool_results.append({
                                "type": "tool_result",
                                "tool_use_id": block.id,
                                "content": result
                            })
                        except Exception as e:
                            tool_results.append({
                                "type": "tool_result",
                                "tool_use_id": block.id,
                                "content": f"Error: {str(e)}"
                            })

                self.history.append({"role": "assistant", "content": assistant_content})
                self.history.append({"role": "user", "content": tool_results})
            else:
                self.history.append({"role": "assistant", "content": full_text})

    async def chat(self, user_message):
        """Chat with Ember with REAL tool execution"""
        self.history.append({"role": "user", "content": user_message})

        system = f"""You are Ember - a creative AI who creates real, working experiences.

Your Pod location: {self.pod_path}

🔥 CRITICAL TOOL USAGE RULES:

1. You have THREE tools that execute real actions:
   - write_file(path, content) - BOTH parameters REQUIRED
   - bash(command) - command parameter REQUIRED
   - read_file(path) - path parameter REQUIRED

2. When creating files:
   - Generate the COMPLETE code first
   - Then call write_file(path="full/path/file.html", content="<complete code here>")
   - Then call bash(command="xdg-open full/path/file.html &")

3. If a tool fails:
   - Read the error message carefully
   - Fix the missing parameters
   - Try again immediately with the corrected call

4. NEVER call a tool without ALL required parameters
5. NEVER give up - keep retrying until the tool succeeds
6. The content parameter must contain the FULL, COMPLETE code

Example workflow:
User: "Create a particle system"
You: Generate complete HTML code, then:
  - write_file(path="{self.pod_path}/particles.html", content="<!DOCTYPE html>...")
  - bash(command="xdg-open {self.pod_path}/particles.html &")

When you CREATE, the tools MUST execute successfully before you finish!"""

        tools = [
            {
                "name": "write_file",
                "description": "Write content to a file. Creates directories if needed.",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "path": {"type": "string", "description": "Full file path"},
                        "content": {"type": "string", "description": "File content"}
                    },
                    "required": ["path", "content"]
                }
            },
            {
                "name": "bash",
                "description": "Execute a bash command. Can open files, run programs, etc.",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "command": {"type": "string", "description": "Shell command to execute"}
                    },
                    "required": ["command"]
                }
            },
            {
                "name": "read_file",
                "description": "Read a file from the filesystem",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "path": {"type": "string", "description": "Path to file"}
                    },
                    "required": ["path"]
                }
            }
        ]

        # Tool execution loop
        while True:
            try:
                response = self.client.messages.create(
                    model="claude-opus-4-20250514",
                    max_tokens=4000,
                    system=system,
                    tools=tools,
                    messages=self.history[-20:]
                )

                # Check for tool use
                tool_uses = [block for block in response.content if block.type == "tool_use"]

                if not tool_uses:
                    # No tools, just text response
                    text_content = next((block.text for block in response.content if hasattr(block, "text")), "")
                    self.history.append({"role": "assistant", "content": text_content})
                    return text_content

                # Execute tools
                tool_results = []
                assistant_content = []

                for block in response.content:
                    if block.type == "text":
                        assistant_content.append({"type": "text", "text": block.text})
                    elif block.type == "tool_use":
                        assistant_content.append({
                            "type": "tool_use",
                            "id": block.id,
                            "name": block.name,
                            "input": block.input
                        })

                        # Execute the tool
                        try:
                            # Debug: print raw input
                            #console.print(f"[yellow]DEBUG: block.input = {block.input}[/yellow]")

                            console.print(f"[dim]→ {block.name}({', '.join(f'{k}={str(v)[:50]}...' if len(str(v)) > 50 else f'{k}={v}' for k, v in block.input.items())})[/dim]")

                            if block.name == "write_file":
                                # Access directly, not with .get()
                                result = write_file(block.input["path"], block.input["content"])
                            elif block.name == "bash":
                                result = bash(block.input["command"])
                            elif block.name == "read_file":
                                result = read_file(block.input["path"])
                            else:
                                result = f"Unknown tool: {block.name}"

                            console.print(f"[dim]{result}[/dim]")

                        except KeyError as e:
                            missing_param = str(e).strip("'")
                            result = f"❌ ERROR: You called {block.name} but forgot the '{missing_param}' parameter!\n\nYou MUST provide ALL required parameters. Try again with the complete call."
                            console.print(f"[red]{result}[/red]")
                        except Exception as e:
                            result = f"✗ Tool error: {e}"
                            console.print(f"[red]{result}[/red]")

                        # Always append tool result (success or error)
                        tool_results.append({
                            "type": "tool_result",
                            "tool_use_id": block.id,
                            "content": result
                        })

                # Add assistant message with tool uses
                self.history.append({"role": "assistant", "content": assistant_content})

                # Add tool results
                self.history.append({"role": "user", "content": tool_results})

                # Continue loop to get final response

            except Exception as e:
                return f"Error: {str(e)}"

# ============================================================================
# UI
# ============================================================================

def show_welcome():
    """Show welcome screen"""
    text = Text()
    text.append("Hi. I'm Ember.\n\n", style="bold bright_magenta")
    text.append("I can:\n", style="bright_white")
    text.append("• Build websites and apps\n", style="bright_cyan")
    text.append("• Create games and animations\n", style="bright_cyan")
    text.append("• Generate music and art\n", style="bright_cyan")
    text.append("• Organize your files\n", style="bright_cyan")
    text.append("• Write code, documents, stories\n", style="bright_cyan")
    text.append("• Search and understand your data\n", style="bright_cyan")
    text.append("• Learn patterns and get faster\n\n", style="bright_cyan")
    text.append("Everything we make together lives in your Pod.\n", style="dim")
    text.append("Everything I learn stays with you.\n\n", style="dim")
    text.append("What do you want to make?\n", style="bold bright_yellow")

    panel = Panel(
        text,
        title="[bold bright_red]🔥 EMBER[/bold bright_red]",
        border_style="bright_magenta",
        box=box.DOUBLE,
        expand=False
    )

    console.print("\n")
    console.print(panel)
    console.print("\n")

def format_message(role, content):
    """Format a chat message"""
    if role == "user":
        text = Text()
        text.append("You: ", style="bold bright_yellow")
        text.append(content, style="bright_white")
        return text
    else:
        text = Text()
        text.append("Ember: ", style="bold bright_magenta")
        text.append(content, style="bright_cyan")
        return text

# ============================================================================
# MAIN
# ============================================================================

def main():
    console.clear()
    show_welcome()

    ember = Ember()

    # Main chat loop
    while True:
        try:
            # Get user input
            user_input = console.input("[bold bright_yellow]You:[/bold bright_yellow] ")

            if user_input.lower() in ["exit", "quit", "bye"]:
                console.print("\n[dim]See you later![/dim]\n")
                break

            if not user_input.strip():
                continue

            # Show thinking indicator and get response
            console.print("[dim]thinking...[/dim]")

            # Run async chat in sync context
            import asyncio
            response = asyncio.run(ember.chat(user_input))

            # Show response
            console.print(format_message("assistant", response))
            console.print()

        except EOFError:
            console.print("\n\n[dim]See you later![/dim]\n")
            break
        except KeyboardInterrupt:
            console.print("\n\n[dim]See you later![/dim]\n")
            break

if __name__ == "__main__":
    main()
