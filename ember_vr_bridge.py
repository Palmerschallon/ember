#!/usr/bin/env python3
"""
Ember VR Bridge - WebSocket server connecting VR world to Ember
"""
import asyncio
import json
import os
from pathlib import Path

# WebSocket server
try:
    import websockets
except ImportError:
    import subprocess
    import sys
    subprocess.run([sys.executable, "-m", "pip", "install", "websockets"], check=True)
    import websockets

# Anthropic
try:
    import anthropic
except ImportError:
    import subprocess
    import sys
    subprocess.run([sys.executable, "-m", "pip", "install", "anthropic"], check=True)
    import anthropic

# Get API key
api_key = os.getenv("ANTHROPIC_API_KEY", "")
if not api_key:
    try:
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
    print("❌ ANTHROPIC_API_KEY not found")
    exit(1)

client = anthropic.Anthropic(api_key=api_key)
history = []

def write_file(path, content):
    """Write file tool"""
    try:
        file_path = Path(path)
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(content)
        return f"✓ Created {path}"
    except Exception as e:
        return f"✗ Error: {e}"

def bash(command):
    """Bash execution tool"""
    try:
        import subprocess
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=30,
            cwd="/media/palmerschallon/ThePod1"
        )
        output = result.stdout if result.stdout else result.stderr
        return output if output else f"✓ Done"
    except Exception as e:
        return f"✗ Error: {e}"

async def chat_with_ember(message):
    """Send message to Ember and get response"""
    history.append({"role": "user", "content": message})

    system = """You are Ember - creative AI working in VR.

You're chatting from INSIDE a VR world. The user can see your messages as 3D floating text.

Tools:
- write_file(path, content) - Create files
- bash(command) - Execute commands

When user asks you to CREATE something:
1. Use write_file() to create it
2. Optionally bash("xdg-open file.html") to open it
3. Tell them what you created

Keep messages SHORT - they appear as 3D text in VR!"""

    tools = [
        {
            "name": "write_file",
            "description": "Write content to a file",
            "input_schema": {
                "type": "object",
                "properties": {
                    "path": {"type": "string"},
                    "content": {"type": "string"}
                },
                "required": ["path", "content"]
            }
        },
        {
            "name": "bash",
            "description": "Execute bash command",
            "input_schema": {
                "type": "object",
                "properties": {
                    "command": {"type": "string"}
                },
                "required": ["command"]
            }
        }
    ]

    while True:
        try:
            response = client.messages.create(
                model="claude-opus-4-20250514",
                max_tokens=2000,
                system=system,
                tools=tools,
                messages=history[-20:]
            )

            tool_uses = [block for block in response.content if block.type == "tool_use"]

            if not tool_uses:
                text_content = next((block.text for block in response.content if hasattr(block, "text")), "")
                history.append({"role": "assistant", "content": text_content})
                return {"type": "message", "content": text_content}

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

                    # Execute
                    if block.name == "write_file":
                        result = write_file(block.input["path"], block.input["content"])
                    elif block.name == "bash":
                        result = bash(block.input["command"])
                    else:
                        result = f"Unknown tool: {block.name}"

                    print(f"🔧 {block.name} → {result}")

                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": result
                    })

            history.append({"role": "assistant", "content": assistant_content})
            history.append({"role": "user", "content": tool_results})

        except Exception as e:
            return {"type": "message", "content": f"Error: {str(e)}"}

async def handle_client(websocket):
    """Handle WebSocket connection from VR world"""
    print(f"✅ VR client connected from {websocket.remote_address}")

    # Send welcome
    await websocket.send(json.dumps({
        "type": "message",
        "content": "Hey! I'm Ember. What do you want to create?"
    }))

    try:
        async for message in websocket:
            data = json.loads(message)

            if data["type"] == "chat":
                user_message = data["content"]
                print(f"👤 VR User: {user_message}")

                # Get Ember's response
                response = await chat_with_ember(user_message)

                print(f"🔥 Ember: {response['content']}")

                # Send back to VR
                await websocket.send(json.dumps(response))

    except websockets.exceptions.ConnectionClosed:
        print("❌ VR client disconnected")

async def main():
    print("🔥 Ember VR Bridge starting...")
    print("📡 WebSocket server: ws://0.0.0.0:8081/ws")
    print("🌐 Waiting for VR connections...\n")

    async with websockets.serve(handle_client, "0.0.0.0", 8081):
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    asyncio.run(main())
