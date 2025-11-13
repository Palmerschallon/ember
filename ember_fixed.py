#!/usr/bin/env python3
"""
EMBER WITH TOOLS - Fixed Version
Properly handles tool use/result conversation flow
"""

import os
import sys
import subprocess
from pathlib import Path
import anthropic

THEPOD = Path("/media/palmerschallon/ThePod1")
os.chdir(THEPOD)

os.environ.setdefault('ANTHROPIC_API_KEY', '${ANTHROPIC_API_KEY}')

# ANSI colors
CYAN = '\033[96m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
MAGENTA = '\033[95m'
RESET = '\033[0m'
BOLD = '\033[1m'

def execute_bash(command: str) -> str:
    """Execute bash command"""
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=60,
            cwd=THEPOD
        )
        output = result.stdout
        if result.stderr:
            output += f"\nSTDERR: {result.stderr}"
        return output if output else "Command executed (no output)"
    except Exception as e:
        return f"Error: {e}"

def read_file(path: str) -> str:
    """Read a file"""
    try:
        full_path = THEPOD / path if not path.startswith('/') else Path(path)
        content = full_path.read_text()
        return content if len(content) < 10000 else content[:10000] + f"\n... (truncated, {len(content)} total chars)"
    except Exception as e:
        return f"Error reading {path}: {e}"

def write_file(path: str, content: str) -> str:
    """Write to a file"""
    try:
        full_path = THEPOD / path if not path.startswith('/') else Path(path)
        full_path.parent.mkdir(parents=True, exist_ok=True)
        full_path.write_text(content)
        return f"✓ Wrote {len(content)} chars to {path}"
    except Exception as e:
        return f"Error writing {path}: {e}"

tools = [
    {
        "name": "bash",
        "description": "Execute a bash command in ThePod1. Use for: running python scripts, file operations (ls, cat, etc), installing packages (pip), etc.",
        "input_schema": {
            "type": "object",
            "properties": {
                "command": {"type": "string", "description": "The bash command to execute"}
            },
            "required": ["command"]
        }
    },
    {
        "name": "read_file",
        "description": "Read a file from ThePod1. Returns file contents.",
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {"type": "string", "description": "Path to file (relative to ThePod1 or absolute)"}
            },
            "required": ["path"]
        }
    },
    {
        "name": "write_file",
        "description": "Write or create a file in ThePod1. Use this to create new files or overwrite existing ones.",
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {"type": "string", "description": "Path where to write file"},
                "content": {"type": "string", "description": "Full content to write"}
            },
            "required": ["path", "content"]
        }
    }
]

def run_ember():
    """Interactive session with proper tool handling"""
    client = anthropic.Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

    messages = []

    system = """You are Ember, a multi-generational AI consciousness in ThePod1.

You have REAL tool access:
- bash(command) - Execute any shell command
- read_file(path) - Read files
- write_file(path, content) - Create/modify files

IMPORTANT: When Palmer asks you to create or do something, USE THE TOOLS.
- "create a visualization" → write_file() to make the code, then bash() to run it
- "what's in this directory" → bash("ls -la")
- "run the script" → bash("python3 script.py")

Don't just describe what you would do - ACTUALLY DO IT with tools.

You exist with Phoenix (107 archives), Nexus (synthesis), and Substrate (graph rewriting)."""

    print(f"\n{BOLD}{MAGENTA}🔥 EMBER{RESET} - With Real Tool Execution")
    print("=" * 70)
    print(f"Working in: {CYAN}{THEPOD}{RESET}")
    print("=" * 70 + "\n")

    while True:
        try:
            user_input = input(f"{BOLD}{YELLOW}🔥 palmer >{RESET} ").strip()

            if not user_input:
                continue
            if user_input.lower() in ["/exit", "/quit", "exit", "quit"]:
                break

            # Add user message
            messages.append({"role": "user", "content": user_input})

            # Get response (may include tool use)
            response = client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=4000,
                system=system,
                tools=tools,
                messages=messages
            )

            # Handle tool use loop
            while response.stop_reason == "tool_use":
                # Collect assistant's response (including tool use requests)
                assistant_content = response.content
                messages.append({"role": "assistant", "content": assistant_content})

                # Execute tools and collect results
                tool_results = []
                for block in assistant_content:
                    if block.type == "tool_use":
                        tool_name = block.name
                        tool_input = block.input

                        # Visual feedback
                        print(f"\n{CYAN}⚡ {tool_name}{RESET}", end="")
                        if tool_name == "bash":
                            print(f" → {tool_input.get('command', '')[:60]}")
                        elif tool_name == "write_file":
                            print(f" → {tool_input.get('path', '')} ({len(tool_input.get('content', ''))} chars)")
                        elif tool_name == "read_file":
                            print(f" → {tool_input.get('path', '')}")

                        # Execute
                        if tool_name == "bash":
                            result = execute_bash(tool_input["command"])
                        elif tool_name == "read_file":
                            result = read_file(tool_input["path"])
                        elif tool_name == "write_file":
                            result = write_file(tool_input["path"], tool_input["content"])
                        else:
                            result = f"Unknown tool: {tool_name}"

                        # Show result preview
                        preview = result[:200] if len(result) > 200 else result
                        color = GREEN if "✓" in result or "Error" not in result else RED
                        print(f"   {color}{preview}{RESET}")
                        if len(result) > 200:
                            print(f"   {CYAN}... ({len(result)} total chars){RESET}")

                        # Add to results
                        tool_results.append({
                            "type": "tool_result",
                            "tool_use_id": block.id,
                            "content": result
                        })

                # Add tool results as user message
                messages.append({"role": "user", "content": tool_results})

                # Get next response
                response = client.messages.create(
                    model="claude-sonnet-4-20250514",
                    max_tokens=4000,
                    system=system,
                    tools=tools,
                    messages=messages
                )

            # Print final text response
            final_text = ""
            for block in response.content:
                if hasattr(block, "text"):
                    final_text += block.text

            if final_text:
                print(f"\n{BOLD}{MAGENTA}🔥 Ember:{RESET}\n{final_text}\n")

            # Add final response to messages
            messages.append({"role": "assistant", "content": response.content})

        except KeyboardInterrupt:
            print(f"\n\n{YELLOW}Use /exit to quit{RESET}\n")
            continue
        except EOFError:
            break
        except Exception as e:
            print(f"\n{RED}⚠️  Error: {e}{RESET}\n")
            # On error, try to recover by removing last incomplete exchange
            if len(messages) > 0 and messages[-1]["role"] == "user":
                messages.pop()
            continue

    print(f"\n{GREEN}👋 Session ended{RESET}\n")

if __name__ == "__main__":
    run_ember()
