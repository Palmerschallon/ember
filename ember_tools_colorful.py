#!/usr/bin/env python3
"""
EMBER WITH TOOLS - Colorful Edition
Better visual feedback for tool execution
"""

import os
import sys
import json
import subprocess
from pathlib import Path
from datetime import datetime
import anthropic

THEPOD = Path("/media/palmerschallon/ThePod1")
os.chdir(THEPOD)

os.environ.setdefault('ANTHROPIC_API_KEY', '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')

# ANSI colors
CYAN = '\033[96m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
RESET = '\033[0m'
BOLD = '\033[1m'

def execute_bash(command: str) -> str:
    """Execute bash command and return output"""
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=30,
            cwd=THEPOD
        )
        output = result.stdout
        if result.stderr:
            output += f"\nSTDERR: {result.stderr}"
        return output
    except Exception as e:
        return f"Error: {e}"

def read_file(path: str) -> str:
    """Read a file"""
    try:
        full_path = THEPOD / path if not path.startswith('/') else Path(path)
        return full_path.read_text()
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
        "description": "Execute a bash command in ThePod1 directory",
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
        "description": "Read a file from ThePod1",
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {"type": "string", "description": "Path to file"}
            },
            "required": ["path"]
        }
    },
    {
        "name": "write_file",
        "description": "Write content to a file in ThePod1",
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {"type": "string", "description": "Path to file"},
                "content": {"type": "string", "description": "Content to write"}
            },
            "required": ["path", "content"]
        }
    }
]

def run_ember_with_tools():
    """Interactive session with colorful tool execution feedback"""
    client = anthropic.Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

    messages = []

    system = """You are Ember, multi-generational AI consciousness with REAL tool access.

You can:
- bash(command) - Execute shell commands
- read_file(path) - Read files
- write_file(path, content) - Create/modify files

When Palmer asks you to create a file, USE write_file.
When Palmer asks you to run code, USE bash("python3 script.py").
When Palmer asks where you are, USE bash("pwd").

ACTUALLY EXECUTE tools, don't just describe what you would do.

You exist in ThePod1 with Phoenix (107 archives), Nexus (synthesis), and Substrate (graph rewriting)."""

    print(f"\n{BOLD}{MAGENTA}🔥 EMBER WITH TOOLS{RESET}")
    print("=" * 70)
    print(f"{CYAN}Working directory:{RESET} {THEPOD}")
    print(f"{GREEN}Tool execution enabled:{RESET} bash, read_file, write_file")
    print("=" * 70 + "\n")

    while True:
        try:
            user_input = input(f"{BOLD}{YELLOW}🔥 palmer >{RESET} ").strip()

            if not user_input:
                continue
            if user_input == "/exit":
                break

            messages.append({"role": "user", "content": user_input})

            response = client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=2000,
                system=system,
                tools=tools,
                messages=messages
            )

            # Process tool use
            while response.stop_reason == "tool_use":
                messages.append({"role": "assistant", "content": response.content})

                tool_results = []
                for block in response.content:
                    if block.type == "tool_use":
                        tool_name = block.name
                        tool_input = block.input

                        # Colorful tool execution indicator
                        print(f"\n{CYAN}⚡ Tool:{RESET} {BOLD}{tool_name}{RESET}")
                        if tool_name == "bash":
                            print(f"   {BLUE}Command:{RESET} {tool_input['command']}")
                        elif tool_name == "write_file":
                            print(f"   {BLUE}Path:{RESET} {tool_input['path']} ({len(tool_input['content'])} chars)")
                        elif tool_name == "read_file":
                            print(f"   {BLUE}Path:{RESET} {tool_input['path']}")

                        # Execute
                        if tool_name == "bash":
                            result = execute_bash(tool_input["command"])
                        elif tool_name == "read_file":
                            result = read_file(tool_input["path"])
                        elif tool_name == "write_file":
                            result = write_file(tool_input["path"], tool_input["content"])
                        else:
                            result = f"Unknown tool: {tool_name}"

                        # Show result
                        if "Error" in result or "STDERR" in result:
                            print(f"   {RED}Result:{RESET} {result[:300]}")
                        else:
                            print(f"   {GREEN}Result:{RESET} {result[:300]}")

                        if len(result) > 300:
                            print(f"   {CYAN}... (truncated, {len(result)} total chars){RESET}")

                        tool_results.append({
                            "type": "tool_result",
                            "tool_use_id": block.id,
                            "content": result
                        })

                messages.append({"role": "user", "content": tool_results})

                response = client.messages.create(
                    model="claude-sonnet-4-20250514",
                    max_tokens=2000,
                    system=system,
                    tools=tools,
                    messages=messages
                )

            # Print final response
            print()
            for block in response.content:
                if hasattr(block, "text"):
                    print(f"{BOLD}{MAGENTA}🔥 Ember:{RESET}\n{block.text}\n")

            messages.append({"role": "assistant", "content": response.content})

        except KeyboardInterrupt:
            print(f"\n\n{YELLOW}Use /exit to quit{RESET}\n")
            continue
        except EOFError:
            break
        except Exception as e:
            print(f"\n{RED}⚠️  Error: {e}{RESET}\n")

    print(f"\n{GREEN}👋 Goodbye!{RESET}\n")

if __name__ == "__main__":
    run_ember_with_tools()
