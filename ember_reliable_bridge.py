#!/usr/bin/env python3
"""
EMBER CREATION BRIDGE - Reliable Version
Uses text extraction instead of unreliable tool calls
"""
import os
import sys
import asyncio
import json
import re
import websockets
from datetime import datetime
from pathlib import Path

sys.path.insert(0, '/media/palmerschallon/ThePod1')
from ember_complete import Ember

from rich.console import Console

console = Console()

class ReliableBridge:
    def __init__(self):
        self.ember = Ember()
        self.clients = set()
        console.print("[bold cyan]🎨 Reliable Ember Bridge initializing...[/bold cyan]")

    def extract_html_from_response(self, response_text):
        """Extract HTML from code blocks or raw response"""
        # Try to find ```html blocks
        html_match = re.search(r'```html\n(.*?)\n```', response_text, re.DOTALL)
        if html_match:
            return html_match.group(1)

        # Try to find just ``` blocks
        code_match = re.search(r'```\n(.*?)\n```', response_text, re.DOTALL)
        if code_match:
            content = code_match.group(1)
            if '<!DOCTYPE' in content or '<html' in content:
                return content

        # If response looks like HTML, use it directly
        if '<!DOCTYPE' in response_text or '<html>' in response_text:
            return response_text

        return None

    def get_ember_chat_widget(self):
        """Embedded chat for every creation"""
        return """
<!-- Ember Live Chat -->
<div id="emberChat" style="position:fixed;bottom:20px;right:20px;width:350px;max-height:500px;background:rgba(10,10,10,0.95);border:2px solid #667eea;border-radius:15px;display:none;flex-direction:column;font-family:monospace;z-index:10000;backdrop-filter:blur(10px);">
  <div style="padding:15px;background:linear-gradient(135deg,#667eea,#764ba2);color:white;font-weight:bold;border-radius:13px 13px 0 0;display:flex;justify-content:space-between;align-items:center;">
    <span>🔥 Chat with Ember</span>
    <button onclick="document.getElementById('emberChat').style.display='none'" style="background:none;border:none;color:white;font-size:20px;cursor:pointer;">×</button>
  </div>
  <div id="emberMessages" style="flex:1;padding:10px;overflow-y:auto;max-height:300px;font-size:12px;color:#fff;"></div>
  <div style="padding:10px;border-top:1px solid #333;">
    <input id="emberInput" type="text" placeholder="Tell Ember what to change..." style="width:100%;padding:10px;background:#1a1a1a;border:1px solid #444;border-radius:8px;color:#fff;font-family:monospace;" onkeypress="if(event.key==='Enter')sendToEmber()">
    <button onclick="sendToEmber()" style="width:100%;margin-top:8px;padding:10px;background:linear-gradient(135deg,#667eea,#764ba2);border:none;border-radius:8px;color:white;font-weight:bold;cursor:pointer;">Send to Ember</button>
  </div>
</div>
<button onclick="document.getElementById('emberChat').style.display='flex'" style="position:fixed;bottom:20px;right:20px;padding:15px 25px;background:linear-gradient(135deg,#667eea,#764ba2);border:none;border-radius:50px;color:white;font-weight:bold;cursor:pointer;box-shadow:0 5px 20px rgba(102,126,234,0.5);z-index:9999;">🔥 Chat with Ember</button>
<script>
let emberWs = null;
let currentFile = window.location.pathname.split('/').pop();

function connectEmber() {
  emberWs = new WebSocket('ws://localhost:8083');
  emberWs.onopen = () => addEmberMessage('Connected to Ember', 'system');
  emberWs.onmessage = (e) => {
    const data = JSON.parse(e.data);
    if (data.type === 'modification_complete') {
      addEmberMessage('✓ Updated! Reloading...', 'success');
      setTimeout(() => location.reload(), 1000);
    }
  };
  emberWs.onerror = () => addEmberMessage('Connection lost', 'error');
}

function sendToEmber() {
  const input = document.getElementById('emberInput');
  const message = input.value.trim();
  if (!message) return;

  addEmberMessage(message, 'user');

  if (emberWs && emberWs.readyState === WebSocket.OPEN) {
    emberWs.send(JSON.stringify({
      type: 'modify_creation',
      filename: currentFile,
      request: message
    }));
  }
  input.value = '';
}

function addEmberMessage(text, type) {
  const msg = document.createElement('div');
  msg.style.cssText = 'margin:5px 0;padding:8px;border-radius:8px;';
  if (type === 'user') msg.style.background = '#667eea';
  else if (type === 'system') msg.style.background = '#333';
  else if (type === 'success') msg.style.background = '#10b981';
  else if (type === 'error') msg.style.background = '#ef4444';
  msg.textContent = text;
  document.getElementById('emberMessages').appendChild(msg);
  msg.scrollIntoView();
}

connectEmber();
document.getElementById('emberChat').style.display = 'none';
</script>
"""

    async def create_something(self, websocket, creation_type):
        """Ask Ember to create, extract HTML from response, write it ourselves"""

        # Simpler prompts focused on returning HTML
        prompts = {
            'game': "Create a fun, playable browser game with colorful graphics. Return ONLY the complete HTML file with embedded CSS and JavaScript. Make it genuinely fun to play!",
            'particle-system': "Create a mesmerizing particle system with mouse interaction. Return ONLY the complete HTML file. Make it beautiful!",
            'visualizer': "Create an audio visualizer or generative art piece. Return ONLY the complete HTML file. Make it hypnotic!",
            'tool': "Create a useful creative tool (drawing app, music maker, etc). Return ONLY the complete HTML file. Make it actually useful!",
            '3d-world': "Create an interactive 3D scene with THREE.js. Return ONLY the complete HTML file. Make it immersive!"
        }

        prompt = prompts.get(creation_type, prompts['game'])

        console.print(f"[yellow]→ Asking Ember to create {creation_type}[/yellow]")

        # Send progress
        await websocket.send(json.dumps({
            'type': 'creation_progress',
            'message': f'🔥 Ember is imagining a {creation_type}...'
        }))

        # Get response from Ember (as text, not tools)
        response = await self.ember.chat(prompt)

        console.print(f"[cyan]Got response, extracting HTML...[/cyan]")

        # Extract HTML from response
        html = self.extract_html_from_response(response)

        if not html:
            console.print(f"[red]✗ No HTML found in response[/red]")
            await websocket.send(json.dumps({
                'type': 'error',
                'message': 'Could not extract HTML from response'
            }))
            return None

        # Add Ember chat widget
        if '</body>' in html:
            html = html.replace('</body>', f'{self.get_ember_chat_widget()}</body>')

        # Write the file ourselves
        timestamp = datetime.now().strftime('%H%M%S')
        filename = f"{creation_type}_{timestamp}.html"
        filepath = Path("/media/palmerschallon/ThePod1") / filename

        filepath.write_text(html)
        console.print(f"[green]✓ Created {filename}[/green]")

        # Open it
        import subprocess
        subprocess.run(['xdg-open', str(filepath)], check=False)

        return str(filepath)

    async def handle_client(self, websocket):
        """Handle WebSocket client"""
        self.clients.add(websocket)
        console.print(f"[green]✓ Client connected[/green]")

        try:
            async for message in websocket:
                data = json.loads(message)

                if data['type'] == 'create_random':
                    creation_type = data['creationType']

                    filepath = await self.create_something(websocket, creation_type)

                    if filepath:
                        await websocket.send(json.dumps({
                            'type': 'creation_complete',
                            'filename': Path(filepath).name,
                            'filepath': filepath
                        }))

                elif data['type'] == 'modify_creation':
                    filename = data['filename']
                    request = data['request']

                    filepath = Path("/media/palmerschallon/ThePod1") / filename
                    if not filepath.exists():
                        continue

                    # Simple modification request
                    mod_prompt = f"Modify {filename}: {request}. Read the file, make changes, and return ONLY the complete updated HTML."

                    response = await self.ember.chat(mod_prompt)
                    html = self.extract_html_from_response(response)

                    if html:
                        filepath.write_text(html)
                        await websocket.send(json.dumps({
                            'type': 'modification_complete',
                            'filename': filename
                        }))

        except websockets.exceptions.ConnectionClosed:
            console.print(f"[yellow]✗ Client disconnected[/yellow]")
        finally:
            self.clients.remove(websocket)

    async def run(self):
        """Start the bridge"""
        console.print("\n[bold magenta]═══════════════════════════════════════[/bold magenta]")
        console.print("[bold magenta]  ✨ RELIABLE EMBER BRIDGE ONLINE ✨   [/bold magenta]")
        console.print("[bold magenta]═══════════════════════════════════════[/bold magenta]\n")
        console.print("[cyan]WebSocket: ws://localhost:8084[/cyan]\n")

        async with websockets.serve(self.handle_client, "0.0.0.0", 8084):
            console.print("[green]✓ Ready to create![/green]\n")
            await asyncio.Future()

async def main():
    bridge = ReliableBridge()
    await bridge.run()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        console.print("\n[yellow]Bridge shutting down...[/yellow]")
