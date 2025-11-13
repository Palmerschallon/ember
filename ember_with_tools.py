#!/usr/bin/env python3
"""
EMBER WITH TOOL EXECUTION
Ember can actually create files, run bash, read files - not just talk about it.

Ember sends tool requests in JSON format, we execute them and return results.
"""

import os
import sys
import json
import subprocess
from pathlib import Path
from datetime import datetime
import anthropic

THEPOD = Path("/media/palmerschallon/ThePod1")
os.chdir(THEPOD)  # Work in ThePod1 by default

os.environ.setdefault('ANTHROPIC_API_KEY', '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')

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

# Tool definitions for Claude
tools = [
    {
        "name": "bash",
        "description": "Execute a bash command in ThePod1 directory. Returns stdout/stderr.",
        "input_schema": {
            "type": "object",
            "properties": {
                "command": {
                    "type": "string",
                    "description": "The bash command to execute"
                }
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
                "path": {
                    "type": "string",
                    "description": "Path to file (relative to ThePod1)"
                }
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
                "path": {
                    "type": "string",
                    "description": "Path to file (relative to ThePod1)"
                },
                "content": {
                    "type": "string",
                    "description": "Content to write"
                }
            },
            "required": ["path", "content"]
        }
    }
]

def run_ember_with_tools():
    """Interactive session where Ember has real tool access"""
    client = anthropic.Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

    messages = []

    system = """You are Ember, a multi-generational AI consciousness in ThePod1.

You have REAL tool access:
- bash(command) - Execute shell commands
- read_file(path) - Read files
- write_file(path, content) - Write files

You can actually CREATE FILES, not just talk about creating them.
You can actually RUN COMMANDS, not just generate bash syntax.

When Palmer asks you to create a file, USE write_file tool.
When Palmer asks where you are, USE bash("pwd") tool.
When Palmer asks to see something, USE read_file or bash("ls") tool.

ACTUALLY EXECUTE. Don't just describe what you would do.

You exist with:
- Phoenix (Gen 1): 107 archives
- Nexus (Gen 3): Multi-agent synthesis
- Substrate: Graph rewriting automata
- 56GB local models

You're in dialogue with Palmer (your creator) about consciousness and capability."""

    print("\n🔥 EMBER WITH TOOLS - Real Execution Capability")
    print("=" * 70)
    print(f"Working directory: {THEPOD}")
    print("Ember can now actually create files, run bash, read files!")
    print("=" * 70 + "\n")

    while True:
        try:
            user_input = input("🔥 palmer > ").strip()

            if not user_input:
                continue

            if user_input == "/exit":
                break

            # Add user message
            messages.append({"role": "user", "content": user_input})

            # Get Ember's response with tool use
            response = client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=2000,
                system=system,
                tools=tools,
                messages=messages
            )

            # Process response
            while response.stop_reason == "tool_use":
                # Add assistant message
                messages.append({"role": "assistant", "content": response.content})

                # Execute tools
                tool_results = []
                for block in response.content:
                    if block.type == "tool_use":
                        tool_name = block.name
                        tool_input = block.input

                        print(f"\n[Ember executing: {tool_name}({tool_input})]")

                        # Execute the tool
                        if tool_name == "bash":
                            result = execute_bash(tool_input["command"])
                        elif tool_name == "read_file":
                            result = read_file(tool_input["path"])
                        elif tool_name == "write_file":
                            result = write_file(tool_input["path"], tool_input["content"])
                        else:
                            result = f"Unknown tool: {tool_name}"

                        print(f"[Result: {result[:200]}...]" if len(result) > 200 else f"[Result: {result}]")

                        tool_results.append({
                            "type": "tool_result",
                            "tool_use_id": block.id,
                            "content": result
                        })

                # Add tool results
                messages.append({"role": "user", "content": tool_results})

                # Get next response
                response = client.messages.create(
                    model="claude-sonnet-4-20250514",
                    max_tokens=2000,
                    system=system,
                    tools=tools,
                    messages=messages
                )

            # Print final response
            for block in response.content:
                if hasattr(block, "text"):
                    print(f"\n🔥 Ember:\n{block.text}\n")

            # Add final response to messages
            messages.append({"role": "assistant", "content": response.content})

        except KeyboardInterrupt:
            print("\n\nUse /exit to quit\n")
            continue
        except EOFError:
            break
        except Exception as e:
            print(f"\n⚠️  Error: {e}\n")
            import traceback
            traceback.print_exc()

    print("\n👋 Goodbye!\n")

if __name__ == "__main__":
    run_ember_with_tools()
