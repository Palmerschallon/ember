#!/usr/bin/env python3
"""
EMBER LOCAL - Using Ollama for free, fast local creation

This is your north star - fully local, no API costs.
"""

import os
import sys
import subprocess
from pathlib import Path
from datetime import datetime

# Rich terminal
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich import box

console = Console()

# ============================================================================
# TOOLS - Same as ember_complete
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
# LOCAL MODEL CHAT
# ============================================================================

import json
import requests

class EmberLocal:
    def __init__(self, model="qwen2.5-coder:7b"):
        self.model = model
        self.pod_path = "/media/palmerschallon/ThePod1"
        self.history = []

        # Check if Ollama is running
        try:
            response = requests.get("http://localhost:11434/api/tags")
            if response.status_code != 200:
                console.print("[yellow]Starting Ollama...[/yellow]")
                subprocess.Popen(["ollama", "serve"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                import time
                time.sleep(3)
        except:
            console.print("[red]Ollama not found. Install with: curl -fsSL https://ollama.com/install.sh | sh[/red]")
            sys.exit(1)

        # Check if model is available
        try:
            response = requests.get("http://localhost:11434/api/tags")
            models = response.json().get("models", [])
            model_names = [m["name"] for m in models]

            if not any(model in m for m in model_names):
                console.print(f"[yellow]Downloading {model} (this may take a few minutes)...[/yellow]")
                result = subprocess.run(["ollama", "pull", model], capture_output=True, text=True)
                if result.returncode != 0:
                    console.print(f"[red]Failed to download model: {result.stderr}[/red]")
                    sys.exit(1)
        except Exception as e:
            console.print(f"[red]Error checking models: {e}[/red]")

    def chat(self, user_message):
        """Chat with local model - synchronous for simplicity"""

        system_prompt = f"""You are Ember - a creative AI who creates real, working experiences.

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

3. Tool calls must be valid JSON in this format:
   {{"tool": "write_file", "args": {{"path": "...", "content": "..."}}}}
   {{"tool": "bash", "args": {{"command": "..."}}}}
   {{"tool": "read_file", "args": {{"path": "..."}}}}

4. NEVER call a tool without ALL required parameters
5. The content parameter must contain the FULL, COMPLETE code

When you CREATE, the tools MUST execute successfully!"""

        # Add to history
        self.history.append({"role": "user", "content": user_message})

        # Build messages for Ollama
        messages = [{"role": "system", "content": system_prompt}] + self.history[-10:]

        # Call Ollama
        max_iterations = 5
        iteration = 0

        while iteration < max_iterations:
            iteration += 1

            try:
                response = requests.post(
                    "http://localhost:11434/api/chat",
                    json={
                        "model": self.model,
                        "messages": messages,
                        "stream": False,
                        "options": {
                            "temperature": 0.7,
                            "num_predict": 2000
                        }
                    },
                    timeout=120
                )

                if response.status_code != 200:
                    return f"Error: Ollama returned status {response.status_code}"

                result = response.json()
                assistant_message = result["message"]["content"]

                # Check for tool calls
                tool_calls = self.extract_tool_calls(assistant_message)

                if not tool_calls:
                    # No tools, just return response
                    self.history.append({"role": "assistant", "content": assistant_message})
                    return assistant_message

                # Execute tools
                tool_results = []
                for tool_call in tool_calls:
                    tool_name = tool_call["tool"]
                    args = tool_call["args"]

                    console.print(f"[dim]→ {tool_name}({', '.join(f'{k}={str(v)[:50]}...' if len(str(v)) > 50 else f'{k}={v}' for k, v in args.items())})[/dim]")

                    try:
                        if tool_name == "write_file":
                            result_text = write_file(args["path"], args["content"])
                        elif tool_name == "bash":
                            result_text = bash(args["command"])
                        elif tool_name == "read_file":
                            result_text = read_file(args["path"])
                        else:
                            result_text = f"Unknown tool: {tool_name}"

                        console.print(f"[dim]{result_text}[/dim]")
                        tool_results.append(result_text)
                    except KeyError as e:
                        missing = str(e).strip("'")
                        error_msg = f"❌ ERROR: Tool {tool_name} missing parameter '{missing}'"
                        console.print(f"[red]{error_msg}[/red]")
                        tool_results.append(error_msg)

                # Add tool results to history and continue
                self.history.append({"role": "assistant", "content": assistant_message})
                self.history.append({"role": "user", "content": f"Tool results:\n" + "\n".join(tool_results)})

                messages = [{"role": "system", "content": system_prompt}] + self.history[-10:]

            except Exception as e:
                return f"Error: {str(e)}"

        return "Completed (max iterations reached)"

    def extract_tool_calls(self, text):
        """Extract tool calls from model response"""
        tool_calls = []

        # Look for JSON tool calls
        import re
        json_pattern = r'\{[^}]*"tool"[^}]*\}'
        matches = re.findall(json_pattern, text)

        for match in matches:
            try:
                tool_call = json.loads(match)
                if "tool" in tool_call and "args" in tool_call:
                    tool_calls.append(tool_call)
            except:
                pass

        return tool_calls

# ============================================================================
# UI
# ============================================================================

def show_welcome():
    """Show welcome screen"""
    text = Text()
    text.append("Hi. I'm Ember (LOCAL).\\n\\n", style="bold bright_magenta")
    text.append("Running on your machine. No API costs.\\n", style="bright_green")
    text.append("Fast. Private. Yours.\\n\\n", style="bright_green")
    text.append("I can create anything you imagine.\\n", style="bright_yellow")

    panel = Panel(
        text,
        title="[bold bright_red]🔥 EMBER LOCAL[/bold bright_red]",
        border_style="bright_magenta",
        box=box.DOUBLE,
        expand=False
    )

    console.print("\\n")
    console.print(panel)
    console.print("\\n")

def main():
    console.clear()
    show_welcome()

    ember = EmberLocal(model="qwen2.5-coder:7b")  # Fast, good at code

    # Main chat loop
    while True:
        try:
            # Get user input
            user_input = console.input("[bold bright_yellow]You:[/bold bright_yellow] ")

            if user_input.lower() in ["exit", "quit", "bye"]:
                console.print("\\n[dim]See you later![/dim]\\n")
                break

            if not user_input.strip():
                continue

            # Show thinking indicator and get response
            console.print("[dim]thinking...[/dim]")

            response = ember.chat(user_input)

            # Show response
            console.print(f"[bold bright_magenta]Ember:[/bold bright_magenta] {response}")
            console.print()

        except EOFError:
            console.print("\\n\\n[dim]See you later![/dim]\\n")
            break
        except KeyboardInterrupt:
            console.print("\\n\\n[dim]See you later![/dim]\\n")
            break

if __name__ == "__main__":
    main()
