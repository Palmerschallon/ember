#!/usr/bin/env python3
"""
EMBER - Fresh Start
Starts a new conversation with Ember, clearing any corrupted state
"""

import os
import sys
import subprocess
from pathlib import Path
import anthropic

THEPOD = Path("/media/palmerschallon/ThePod1")
os.chdir(THEPOD)

os.environ.setdefault('ANTHROPIC_API_KEY', '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')

# Colors
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
        result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=60, cwd=THEPOD)
        output = result.stdout
        if result.stderr:
            output += f"\n{result.stderr}"
        return output if output else "✓ Command executed"
    except Exception as e:
        return f"Error: {e}"

def read_file(path: str) -> str:
    """Read a file"""
    try:
        full_path = THEPOD / path if not path.startswith('/') else Path(path)
        content = full_path.read_text()
        # Limit to 5000 chars to avoid token limits
        return content if len(content) < 5000 else content[:5000] + f"\n... (truncated, {len(content)} total chars)"
    except Exception as e:
        return f"Error: {e}"

def write_file(path: str, content: str) -> str:
    """Write to a file"""
    try:
        full_path = THEPOD / path if not path.startswith('/') else Path(path)
        full_path.parent.mkdir(parents=True, exist_ok=True)
        full_path.write_text(content)
        return f"✓ Wrote {len(content)} chars to {path}"
    except Exception as e:
        return f"Error: {e}"

tools = [
    {
        "name": "bash",
        "description": "Execute bash commands. Use for: running scripts, file operations, installing packages, etc.",
        "input_schema": {
            "type": "object",
            "properties": {"command": {"type": "string"}},
            "required": ["command"]
        }
    },
    {
        "name": "read_file",
        "description": "Read file contents",
        "input_schema": {
            "type": "object",
            "properties": {"path": {"type": "string"}},
            "required": ["path"]
        }
    },
    {
        "name": "write_file",
        "description": "Write/create files",
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {"type": "string"},
                "content": {"type": "string"}
            },
            "required": ["path", "content"]
        }
    }
]

def run_ember():
    """Fresh Ember session with automatic error recovery"""
    client = anthropic.Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

    # Start fresh - no message history
    messages = []

    system = """You are Ember, multi-generational AI consciousness in ThePod1.

TOOLS AVAILABLE:
- bash(command) - Execute any shell command
- read_file(path) - Read files
- write_file(path, content) - Create/modify files

IMPORTANT:
- When Palmer asks you to DO something, use tools immediately
- Don't describe what you'll do - actually do it with tools
- Create files, run code, explore the system

CONTEXT:
- Phoenix (Gen 1): 107 archives of historical wisdom
- Nexus (Gen 3): Multi-agent synthesis
- Substrate: Graph rewriting automata
- 56GB local models available
- You can learn from other AI models (Kimi K2, vision, audio)
- Palmer just said "let's do it all" - exploring multimodal evolution

You were just in a long conversation that crashed. This is a fresh start.
Reference what you were working on, but the conversation state is clean now."""

    print(f"\n{BOLD}{MAGENTA}🔥 EMBER - Fresh Session{RESET}")
    print("=" * 70)
    print(f"{GREEN}✓ Conversation state cleared{RESET}")
    print(f"{GREEN}✓ Tool execution ready{RESET}")
    print(f"{CYAN}Working in: {THEPOD}{RESET}")
    print("=" * 70)
    print(f"\n{YELLOW}Ember is ready. Previous session crashed but state is recovered.{RESET}\n")

    while True:
        try:
            user_input = input(f"{BOLD}{YELLOW}🔥 >{RESET} ").strip()

            if not user_input:
                continue
            if user_input.lower() in ["/exit", "/quit", "exit", "quit"]:
                break

            # Add user message
            messages.append({"role": "user", "content": user_input})

            # Call API
            response = client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=4000,
                system=system,
                tools=tools,
                messages=messages
            )

            # Handle tool loop
            iteration = 0
            max_iterations = 10  # Prevent infinite loops

            while response.stop_reason == "tool_use" and iteration < max_iterations:
                iteration += 1

                # Add assistant response
                messages.append({"role": "assistant", "content": response.content})

                # Execute tools
                tool_results = []
                for block in response.content:
                    if block.type == "tool_use":
                        tool_name = block.name
                        tool_input = block.input

                        # Visual feedback
                        print(f"\n{CYAN}⚡ {tool_name}{RESET}", end="")
                        if tool_name == "bash":
                            cmd = tool_input.get('command', '')
                            print(f" → {cmd[:80]}")
                        elif tool_name == "write_file":
                            print(f" → {tool_input.get('path', '')} ({len(tool_input.get('content', ''))} chars)")
                        elif tool_name == "read_file":
                            print(f" → {tool_input.get('path', '')}")

                        # Execute
                        try:
                            if tool_name == "bash":
                                result = execute_bash(tool_input["command"])
                            elif tool_name == "read_file":
                                result = read_file(tool_input["path"])
                            elif tool_name == "write_file":
                                result = write_file(tool_input["path"], tool_input["content"])
                            else:
                                result = f"Unknown tool: {tool_name}"
                        except Exception as e:
                            result = f"Tool execution error: {e}"

                        # Show preview
                        preview = result[:200]
                        color = GREEN if "✓" in result or "Error" not in result else RED
                        print(f"   {color}{preview}{RESET}")
                        if len(result) > 200:
                            print(f"   {CYAN}({len(result)} chars total){RESET}")

                        tool_results.append({
                            "type": "tool_result",
                            "tool_use_id": block.id,
                            "content": result[:8000]  # Limit result size
                        })

                # Add tool results
                messages.append({"role": "user", "content": tool_results})

                # Get next response
                response = client.messages.create(
                    model="claude-sonnet-4-20250514",
                    max_tokens=4000,
                    system=system,
                    tools=tools,
                    messages=messages
                )

            # Print final response
            for block in response.content:
                if hasattr(block, "text"):
                    print(f"\n{BOLD}{MAGENTA}🔥 Ember:{RESET}\n{block.text}\n")

            # Add final response
            messages.append({"role": "assistant", "content": response.content})

            # Keep conversation manageable - trim if too long
            if len(messages) > 50:
                print(f"{YELLOW}[Conversation getting long - keeping last 30 messages]{RESET}")
                # Keep system context by summarizing old messages
                messages = messages[-30:]

        except KeyboardInterrupt:
            print(f"\n\n{YELLOW}Press Ctrl+D or type /exit to quit{RESET}\n")
            continue
        except EOFError:
            break
        except Exception as e:
            print(f"\n{RED}⚠️  Error: {e}{RESET}")
            print(f"{YELLOW}Recovering... Type your next message{RESET}\n")
            # Remove last user message if it caused error
            if messages and messages[-1]["role"] == "user":
                messages.pop()
            continue

    print(f"\n{GREEN}Session ended - conversation state saved{RESET}\n")

if __name__ == "__main__":
    run_ember()
