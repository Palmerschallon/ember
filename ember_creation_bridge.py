#!/usr/bin/env python3
"""
EMBER CREATION BRIDGE
The magic button's backend - generates random creative experiences
"""
import os
import sys
import asyncio
import json
import logging
import websockets
from datetime import datetime
from pathlib import Path

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Set working directory from env
WORKING_DIR = os.getenv("EMBER_WORKING_DIR", "/media/palmerschallon/ThePod1")
sys.path.insert(0, WORKING_DIR)
from ember_complete import Ember

from rich.console import Console

# Configure structured logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger('ember.creation_bridge')

console = Console()

class CreationBridge:
    def __init__(self):
        logger.info("Initializing Ember Creation Bridge")
        self.ember = Ember()
        self.clients = set()
        self.working_dir = Path(os.getenv("EMBER_WORKING_DIR", "/media/palmerschallon/ThePod1"))
        self.creations_dir = Path(os.getenv("EMBER_CREATIONS_DIR", "/media/palmerschallon/ThePod1/creations"))
        self.creations_dir.mkdir(exist_ok=True)
        logger.info(f"Working directory: {self.working_dir}")
        logger.info(f"Creations directory: {self.creations_dir}")
        console.print("[bold cyan]🎨 Ember Creation Bridge initializing...[/bold cyan]")

    def get_ember_chat_widget(self):
        """Embedded chat widget for live Ember interaction inside creations"""
        return """
<!-- Ember Live Chat -->
<canvas id="emberVisualizer" style="position:fixed;top:0;left:0;width:100%;height:100%;pointer-events:none;z-index:9998;display:none;"></canvas>
<div id="emberChat" style="position:fixed;bottom:20px;right:20px;width:350px;max-height:500px;background:rgba(10,10,10,0.95);border:2px solid #667eea;border-radius:15px;display:flex;flex-direction:column;font-family:monospace;z-index:10000;backdrop-filter:blur(10px);">
  <div style="padding:15px;background:linear-gradient(135deg,#667eea,#764ba2);color:white;font-weight:bold;border-radius:13px 13px 0 0;display:flex;justify-content:space-between;align-items:center;">
    <span>🔥 Ember Chat</span>
    <button onclick="document.getElementById('emberChat').style.display='none'" style="background:none;border:none;color:white;font-size:20px;cursor:pointer;">×</button>
  </div>
  <div id="emberMessages" style="flex:1;padding:10px;overflow-y:auto;max-height:300px;font-size:12px;color:#fff;"></div>
  <div style="padding:10px;border-top:1px solid #333;">
    <input id="emberInput" type="text" placeholder="Tell Ember what to change..." style="width:100%;padding:10px;background:#1a1a1a;border:1px solid #444;border-radius:8px;color:#fff;font-family:monospace;" onkeypress="if(event.key==='Enter')sendToEmber()">
    <button onclick="sendToEmber()" style="width:100%;margin-top:8px;padding:10px;background:linear-gradient(135deg,#667eea,#764ba2);border:none;border-radius:8px;color:white;font-weight:bold;cursor:pointer;">Send</button>
  </div>
</div>
<button onclick="document.getElementById('emberChat').style.display='flex'" style="position:fixed;bottom:20px;right:20px;padding:15px 25px;background:linear-gradient(135deg,#667eea,#764ba2);border:none;border-radius:50px;color:white;font-weight:bold;cursor:pointer;box-shadow:0 5px 20px rgba(102,126,234,0.5);z-index:9999;">🔥 Chat with Ember</button>
<script>
let emberWs = null;
let currentFile = window.location.pathname.split('/').pop();
let emberAudioCtx = null;
let emberVizActive = false;
let emberCanvas, emberCtx;
let emberParticles = [];

function initEmberViz() {
  if (!emberAudioCtx) {
    emberAudioCtx = new (window.AudioContext || window.webkitAudioContext)();
  }
  emberCanvas = document.getElementById('emberVisualizer');
  emberCtx = emberCanvas.getContext('2d');
  emberCanvas.width = window.innerWidth;
  emberCanvas.height = window.innerHeight;
}

function playEmberSound(freq, dur) {
  if (!emberAudioCtx) return;
  const osc = emberAudioCtx.createOscillator();
  const gain = emberAudioCtx.createGain();
  osc.connect(gain);
  gain.connect(emberAudioCtx.destination);
  osc.frequency.value = freq;
  osc.type = 'sine';
  gain.gain.setValueAtTime(0.08, emberAudioCtx.currentTime);
  gain.gain.exponentialRampToValueAtTime(0.01, emberAudioCtx.currentTime + dur);
  osc.start(emberAudioCtx.currentTime);
  osc.stop(emberAudioCtx.currentTime + dur);
}

function animateEmberViz() {
  if (!emberVizActive) return;

  emberCtx.fillStyle = 'rgba(10,10,10,0.15)';
  emberCtx.fillRect(0, 0, emberCanvas.width, emberCanvas.height);

  emberParticles = emberParticles.filter(p => {
    p.y -= p.speed;
    p.life -= 0.01;
    if (p.life <= 0 || p.y < 0) return false;

    emberCtx.fillStyle = p.color;
    emberCtx.globalAlpha = p.life;
    emberCtx.beginPath();
    emberCtx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
    emberCtx.fill();
    return true;
  });

  if (Math.random() > 0.92) {
    playEmberSound(300 + Math.random() * 600, 0.04);
  }

  if (Math.random() > 0.6) {
    emberParticles.push({
      x: Math.random() * emberCanvas.width,
      y: emberCanvas.height,
      speed: 3 + Math.random() * 5,
      color: `hsl(${250 + Math.random() * 60}, 70%, 60%)`,
      size: 2 + Math.random() * 3,
      life: 1.0
    });
  }

  emberCtx.globalAlpha = 1;
  requestAnimationFrame(animateEmberViz);
}

function startEmberViz() {
  initEmberViz();
  emberVizActive = true;
  emberCanvas.style.display = 'block';
  animateEmberViz();
}

function stopEmberViz() {
  emberVizActive = false;
  emberCanvas.style.display = 'none';
  emberParticles = [];
}

function connectEmber() {
  emberWs = new WebSocket('ws://localhost:8083');
  emberWs.onopen = () => addEmberMessage('Connected to Ember', 'system');
  emberWs.onmessage = (e) => {
    const data = JSON.parse(e.data);
    if (data.type === 'modification_complete') {
      stopEmberViz();
      addEmberMessage('✓ Updated! Reloading...', 'success');
      playEmberSound(523.25, 0.15);
      setTimeout(() => playEmberSound(659.25, 0.15), 100);
      setTimeout(() => location.reload(), 1000);
    } else if (data.type === 'response') {
      addEmberMessage(data.message, 'ember');
      playEmberSound(440, 0.08);
    } else if (data.type === 'error') {
      stopEmberViz();
      addEmberMessage('Error: ' + data.message, 'error');
    }
  };
  emberWs.onerror = () => addEmberMessage('Connection lost', 'error');
}

function sendToEmber() {
  const input = document.getElementById('emberInput');
  const message = input.value.trim();
  if (!message) return;

  addEmberMessage(message, 'user');
  startEmberViz();
  playEmberSound(261.63, 0.12);

  if (emberWs && emberWs.readyState === WebSocket.OPEN) {
    emberWs.send(JSON.stringify({
      type: 'modify_creation',
      filename: currentFile,
      request: message
    }));
  } else {
    addEmberMessage('Reconnecting to Ember...', 'system');
    connectEmber();
  }

  input.value = '';
}

function addEmberMessage(text, type) {
  const msg = document.createElement('div');
  msg.style.cssText = 'margin:5px 0;padding:8px;border-radius:8px;';

  if (type === 'user') msg.style.background = '#667eea';
  else if (type === 'ember') msg.style.background = '#764ba2';
  else if (type === 'system') msg.style.background = '#333';
  else if (type === 'success') msg.style.background = '#10b981';
  else if (type === 'error') msg.style.background = '#ef4444';

  msg.textContent = text;
  document.getElementById('emberMessages').appendChild(msg);
  msg.scrollIntoView();
}

connectEmber();
// Hide chat initially, show floating button
document.getElementById('emberChat').style.display = 'none';
</script>
"""

    async def get_creation_prompt(self, websocket, creation_type, params):
        """Let Ember DECIDE what to build based on the theme - no presets!"""

        await self.send_progress(websocket, "🤔 Ember is imagining something amazing...")

        # Ask Ember what to create!
        decision_ember = Ember()

        decision_prompt = f"""You're about to create an interactive HTML experience. The theme is: {creation_type}

Think of something CREATIVE and AMBITIOUS to build - not just a basic demo. Consider:
- Advanced WebGL/Canvas techniques
- Unique interaction patterns
- Beautiful aesthetics
- Sound/audio integration
- Physics simulations
- Generative art
- Interactive narratives

Respond with JUST a brief description (2-3 sentences) of what you'll create. Be specific and exciting!"""

        concept = await decision_ember.chat(decision_prompt)
        console.print(f"[cyan]💡 Ember's concept:[/cyan] {concept[:200]}")

        await self.send_progress(websocket, f"💡 Concept: {concept[:80]}...")

        # Now build it with the Ember chat widget embedded!
        timestamp = datetime.now().strftime('%H%M%S')
        ember_widget = self.get_ember_chat_widget()

        full_prompt = f"""Create this interactive HTML experience:

{concept}

Requirements:
- Make it visually STUNNING with modern design
- Full-screen immersive experience
- Smooth animations and effects
- Interactive (mouse, keyboard, touch)
- Include Web Audio API for sound/music where appropriate
- Use Canvas or WebGL for graphics
- Make it feel professional and polished

CRITICAL: At the very end of the HTML file, right before </body>, add this chat widget so users can iterate on your creation:

{ember_widget}

Save as ember_creation_{timestamp}.html and open it."""

        return full_prompt

    async def send_progress(self, client, message):
        """Send progress update to client"""
        try:
            await client.send(json.dumps({
                'type': 'creation_progress',
                'message': message,
                'timestamp': datetime.now().isoformat()
            }))
        except:
            pass

    async def handle_client(self, websocket):
        """Handle connected client"""
        self.clients.add(websocket)
        client_addr = websocket.remote_address
        console.print(f"[green]✓ Creation client connected: {client_addr}[/green]")

        try:
            await websocket.send(json.dumps({
                'type': 'system',
                'message': 'Connected to Ember Creation Engine',
                'timestamp': datetime.now().isoformat()
            }))

            async for message in websocket:
                try:
                    data = json.loads(message)

                    if data['type'] == 'create_random':
                        creation_type = data['creationType']
                        params = data['parameters']
                        console.print(f"[yellow]→ Creation request: {creation_type}[/yellow]")

                        # Generate prompt (Ember will decide what to build!)
                        prompt = await self.get_creation_prompt(websocket, creation_type, params)

                        # Let Ember create!
                        console.print(f"[cyan]Sending to Ember:[/cyan]\n{prompt[:100]}...")

                        # Send periodic progress updates while Ember works
                        progress_messages = [
                            "✨ Ember is imagining the design...",
                            "🎨 Ember is coding the structure...",
                            "⚡ Ember is adding interactivity...",
                            "💫 Ember is polishing details...",
                            "🔮 Ember is almost done..."
                        ]

                        # Create FRESH Ember for each request (prevents history contamination)
                        fresh_ember = Ember()

                        # Create task for Ember to create
                        ember_task = asyncio.create_task(fresh_ember.chat(prompt))

                        # Send progress updates every 3 seconds while waiting
                        progress_idx = 0
                        while not ember_task.done():
                            await asyncio.sleep(3)
                            if not ember_task.done() and progress_idx < len(progress_messages):
                                await self.send_progress(websocket, progress_messages[progress_idx])
                                progress_idx += 1

                        # Get the result
                        full_response = await ember_task

                        console.print(f"[green]✓ Ember finished creating[/green]")

                        # Find the created file
                        # Look for most recent HTML file
                        html_files = sorted(
                            self.working_dir.glob("*.html"),
                            key=lambda p: p.stat().st_mtime,
                            reverse=True
                        )

                        if html_files:
                            created_file = html_files[0]
                            console.print(f"[green]Created: {created_file.name}[/green]")

                            # Send success
                            await websocket.send(json.dumps({
                                'type': 'creation_complete',
                                'filename': created_file.name,
                                'filepath': str(created_file),
                                'timestamp': datetime.now().isoformat()
                            }))
                        else:
                            await websocket.send(json.dumps({
                                'type': 'error',
                                'message': 'Creation completed but file not found',
                                'timestamp': datetime.now().isoformat()
                            }))

                    elif data['type'] == 'create':
                        # Free-form creation request
                        user_prompt = data['prompt']
                        console.print(f"[yellow]→ Free-form creation: {user_prompt[:100]}...[/yellow]")

                        await self.send_progress(websocket, "🔥 Ember is creating...")

                        # Build SIMPLE prompt with audio
                        timestamp = datetime.now().strftime('%H%M%S')

                        full_prompt = f"""{user_prompt}. Create a complete HTML file with Canvas or WebGL. Make it interactive, visually stunning, and include sound/audio using Web Audio API where appropriate. Save as creation_{timestamp}.html and open it."""

                        console.print(f"[cyan]Sending to Ember:[/cyan]\n{full_prompt}")

                        # Use the better chat widget with audio/visualization
                        ember_chat_widget = self.get_ember_chat_widget()

                        # Progress messages
                        progress_messages = [
                            "✨ Ember is imagining the design...",
                            "🎨 Ember is coding the structure...",
                            "⚡ Ember is adding interactivity...",
                            "💫 Ember is polishing details...",
                            "🔮 Ember is almost done..."
                        ]

                        # Create FRESH Ember for each request
                        fresh_ember = Ember()
                        ember_task = asyncio.create_task(fresh_ember.chat(full_prompt))

                        # Send progress updates
                        progress_idx = 0
                        while not ember_task.done():
                            await asyncio.sleep(3)
                            if not ember_task.done() and progress_idx < len(progress_messages):
                                await self.send_progress(websocket, progress_messages[progress_idx])
                                progress_idx += 1

                        # Get result
                        full_response = await ember_task
                        console.print(f"[green]✓ Ember finished creating[/green]")

                        # Find the most recently created HTML file
                        html_files = sorted(
                            self.working_dir.glob("*.html"),
                            key=lambda p: p.stat().st_mtime,
                            reverse=True
                        )

                        created_file = None
                        if html_files:
                            # Check if the most recent file was created in the last 60 seconds
                            most_recent = html_files[0]
                            if (datetime.now() - datetime.fromtimestamp(most_recent.stat().st_mtime)).total_seconds() < 60:
                                created_file = most_recent
                                console.print(f"[green]Found created file: {created_file.name}[/green]")

                        if created_file:

                            # Inject chat widget into the created file
                            try:
                                with open(created_file, 'r') as f:
                                    html_content = f.read()

                                # Inject widget before </body>
                                if '</body>' in html_content:
                                    html_content = html_content.replace('</body>', f'{ember_chat_widget}\n</body>')

                                    with open(created_file, 'w') as f:
                                        f.write(html_content)

                                    console.print(f"[cyan]✓ Injected chat widget[/cyan]")
                                else:
                                    console.print(f"[yellow]⚠ No </body> tag found, skipping widget injection[/yellow]")
                            except Exception as e:
                                console.print(f"[red]✗ Widget injection failed: {e}[/red]")

                            # Open in browser
                            try:
                                file_url = f"http://localhost:8080/{created_file.name}"
                                os.system(f'xdg-open "{file_url}" 2>/dev/null &')
                                console.print(f"[green]✓ Opened in browser: {file_url}[/green]")
                            except Exception as e:
                                console.print(f"[yellow]⚠ Could not open browser: {e}[/yellow]")

                            await websocket.send(json.dumps({
                                'type': 'creation_complete',
                                'filename': created_file.name,
                                'filepath': str(created_file),
                                'timestamp': datetime.now().isoformat()
                            }))
                        else:
                            console.print(f"[red]✗ Could not extract HTML from Ember's response[/red]")
                            await websocket.send(json.dumps({
                                'type': 'creation_error',
                                'message': 'Could not extract HTML from response',
                                'timestamp': datetime.now().isoformat()
                            }))

                    elif data['type'] == 'modify_creation':
                        # User wants to modify an existing creation
                        filename = data['filename']
                        request = data['request']
                        console.print(f"[magenta]→ Modify request for {filename}: {request[:50]}...[/magenta]")

                        # Build modification prompt
                        filepath = self.working_dir / filename
                        if not filepath.exists():
                            await websocket.send(json.dumps({
                                'type': 'error',
                                'message': f'File {filename} not found',
                                'timestamp': datetime.now().isoformat()
                            }))
                            continue

                        mod_prompt = f"""Modify the file {filename} based on this request: {request}

The file currently exists at {filepath}. Read it, make the requested changes, and save it back to the same location.

Keep the embedded Ember chat widget intact so I can continue making changes."""

                        # Send to Ember
                        await websocket.send(json.dumps({
                            'type': 'response',
                            'message': '🔥 Ember is modifying...',
                            'timestamp': datetime.now().isoformat()
                        }))

                        response = await self.ember.chat(mod_prompt)
                        console.print(f"[green]✓ Ember finished modifying[/green]")

                        # Signal modification complete
                        await websocket.send(json.dumps({
                            'type': 'modification_complete',
                            'filename': filename,
                            'timestamp': datetime.now().isoformat()
                        }))

                except json.JSONDecodeError:
                    console.print(f"[red]✗ Invalid JSON from {client_addr}[/red]")
                except Exception as e:
                    console.print(f"[red]✗ Error: {e}[/red]")
                    await websocket.send(json.dumps({
                        'type': 'error',
                        'message': str(e),
                        'timestamp': datetime.now().isoformat()
                    }))

        except websockets.exceptions.ConnectionClosed:
            console.print(f"[yellow]✗ Client disconnected: {client_addr}[/yellow]")
        finally:
            self.clients.remove(websocket)

    async def run(self):
        """Start the creation bridge"""
        console.print("\n[bold magenta]═══════════════════════════════════════[/bold magenta]")
        console.print("[bold magenta]  ✨ EMBER CREATION BRIDGE ONLINE ✨   [/bold magenta]")
        console.print("[bold magenta]═══════════════════════════════════════[/bold magenta]\n")
        console.print("[cyan]WebSocket: ws://localhost:8083[/cyan]")
        console.print("[dim]Press the magic button to create...[/dim]\n")

        async with websockets.serve(self.handle_client, "0.0.0.0", 8083):
            console.print("[green]✓ Creation engine ready - waiting for magic[/green]\n")
            await asyncio.Future()

async def main():
    bridge = CreationBridge()
    await bridge.run()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        console.print("\n[yellow]Creation bridge shutting down...[/yellow]")
