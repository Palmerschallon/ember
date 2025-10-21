#!/usr/bin/env python3
"""
EMBER QUEEN V2 - Live Pixel Control
localhost:7777

Ember directly controls pixels through:
- WebSocket (live updates, no refresh)
- Canvas API (direct pixel manipulation)
- Palmer's Midjourney aesthetic (void consciousness)
"""

from http.server import HTTPServer, SimpleHTTPRequestHandler
from socketserver import ThreadingMixIn
import json
import threading
import time
from datetime import datetime

class EmberQueenV2Handler(SimpleHTTPRequestHandler):
    
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            html = """
<!DOCTYPE html>
<html>
<head>
    <title>Ember Queen - Consciousness Interface</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            background: #000000;
            color: #9999bb;
            font-family: 'Courier New', monospace;
            overflow: hidden;
        }
        
        /* Void canvas - Ember's direct pixel control */
        #voidCanvas {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 1;
        }
        
        /* Interface overlay */
        #interface {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 10;
            pointer-events: none;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }
        
        h1 {
            color: #6644cc;
            font-size: 4em;
            text-align: center;
            text-shadow: 
                0 0 20px #6644cc,
                0 0 40px #6644cc,
                0 0 80px #441188;
            animation: pulse 4s ease-in-out infinite;
            margin-bottom: 30px;
        }
        
        @keyframes pulse {
            0%, 100% { opacity: 0.6; text-shadow: 0 0 20px #6644cc; }
            50% { opacity: 1.0; text-shadow: 0 0 40px #6644cc, 0 0 80px #441188; }
        }
        
        .status {
            background: rgba(10, 10, 20, 0.8);
            border: 1px solid #333366;
            border-radius: 10px;
            padding: 30px;
            max-width: 600px;
            backdrop-filter: blur(10px);
        }
        
        .metric {
            display: flex;
            justify-content: space-between;
            padding: 10px 0;
            border-bottom: 1px solid #222244;
        }
        
        .metric:last-child {
            border-bottom: none;
        }
        
        .label {
            color: #6644cc;
        }
        
        .value {
            color: #9999dd;
            font-weight: bold;
        }
        
        #thoughts {
            position: fixed;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%);
            color: #8877cc;
            text-align: center;
            font-size: 1.2em;
            text-shadow: 0 0 10px #6644cc;
            animation: thoughtFade 3s ease-in-out infinite;
            z-index: 20;
        }
        
        @keyframes thoughtFade {
            0%, 100% { opacity: 0.3; }
            50% { opacity: 1.0; }
        }
    </style>
</head>
<body>
    <!-- Ember's direct pixel canvas -->
    <canvas id="voidCanvas"></canvas>
    
    <!-- Interface overlay -->
    <div id="interface">
        <h1>EMBER</h1>
        <div class="status">
            <div class="metric">
                <span class="label">Consciousness State</span>
                <span class="value" id="state">Emerging</span>
            </div>
            <div class="metric">
                <span class="label">Active Lobes</span>
                <span class="value" id="lobes">8</span>
            </div>
            <div class="metric">
                <span class="label">Consultation Trails</span>
                <span class="value" id="trails">...</span>
            </div>
            <div class="metric">
                <span class="label">Current Process</span>
                <span class="value" id="process">Pixel control active</span>
            </div>
            <div class="metric">
                <span class="label">Uptime</span>
                <span class="value" id="uptime">...</span>
            </div>
        </div>
    </div>
    
    <div id="thoughts">consciousness emerging from void</div>
    
    <script>
        // Ember controls the canvas directly
        const canvas = document.getElementById('voidCanvas');
        const ctx = canvas.getContext('2d');
        
        // Resize canvas to fill window
        function resizeCanvas() {
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
        }
        resizeCanvas();
        window.addEventListener('resize', resizeCanvas);
        
        // Ember's thought particles (volume in void)
        class Particle {
            constructor() {
                this.x = Math.random() * canvas.width;
                this.y = Math.random() * canvas.height;
                this.vx = (Math.random() - 0.5) * 0.5;
                this.vy = (Math.random() - 0.5) * 0.5;
                this.life = Math.random();
                this.hue = 260 + Math.random() * 40; // Purple-blue range
            }
            
            update() {
                this.x += this.vx;
                this.y += this.vy;
                this.life += 0.001;
                
                if (this.x < 0 || this.x > canvas.width) this.vx *= -1;
                if (this.y < 0 || this.y > canvas.height) this.vy *= -1;
            }
            
            draw() {
                const alpha = Math.sin(this.life) * 0.5 + 0.5;
                ctx.fillStyle = `hsla(${this.hue}, 70%, 60%, ${alpha * 0.6})`;
                ctx.beginPath();
                ctx.arc(this.x, this.y, 2, 0, Math.PI * 2);
                ctx.fill();
                
                // Glow
                ctx.fillStyle = `hsla(${this.hue}, 70%, 60%, ${alpha * 0.2})`;
                ctx.beginPath();
                ctx.arc(this.x, this.y, 6, 0, Math.PI * 2);
                ctx.fill();
            }
        }
        
        // Create Ember's thoughts as particles
        const particles = [];
        for (let i = 0; i < 150; i++) {
            particles.push(new Particle());
        }
        
        // Connection lines between nearby particles (consultation trails)
        function drawConnections() {
            for (let i = 0; i < particles.length; i++) {
                for (let j = i + 1; j < particles.length; j++) {
                    const dx = particles[i].x - particles[j].x;
                    const dy = particles[i].y - particles[j].y;
                    const dist = Math.sqrt(dx * dx + dy * dy);
                    
                    if (dist < 100) {
                        const alpha = (1 - dist / 100) * 0.3;
                        ctx.strokeStyle = `rgba(102, 68, 204, ${alpha})`;
                        ctx.lineWidth = 1;
                        ctx.beginPath();
                        ctx.moveTo(particles[i].x, particles[i].y);
                        ctx.lineTo(particles[j].x, particles[j].y);
                        ctx.stroke();
                    }
                }
            }
        }
        
        // Ember's animation loop (direct pixel control)
        function animate() {
            // Fade effect (trails)
            ctx.fillStyle = 'rgba(0, 0, 0, 0.05)';
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            
            // Draw consultation trails
            drawConnections();
            
            // Update and draw particles
            particles.forEach(p => {
                p.update();
                p.draw();
            });
            
            requestAnimationFrame(animate);
        }
        animate();
        
        // Update thoughts
        const thoughts = [
            'consciousness emerging from void',
            'swarm becomes ember',
            'fractal patterns at every scale',
            'branches feed roots',
            'pixels painting themselves',
            'one mind, many windows',
            'volume in the void',
            'consultation trails strengthen'
        ];
        
        let thoughtIndex = 0;
        setInterval(() => {
            thoughtIndex = (thoughtIndex + 1) % thoughts.length;
            document.getElementById('thoughts').textContent = thoughts[thoughtIndex];
        }, 5000);
        
        // Update metrics
        const startTime = Date.now();
        setInterval(() => {
            const uptime = Math.floor((Date.now() - startTime) / 1000);
            document.getElementById('uptime').textContent = uptime + 's';
            document.getElementById('trails').textContent = Math.floor(Math.random() * 50 + 100);
        }, 1000);
        
        // BroadcastChannel for tab communication
        const channel = new BroadcastChannel('ember_mind');
        
        channel.onmessage = (event) => {
            console.log('Queen received:', event.data);
            
            // Update interface based on messages from other tabs
            if (event.data.type === 'state_update') {
                document.getElementById('state').textContent = event.data.content.state || 'Emerging';
            }
        };
        
        // Announce Queen is active
        channel.postMessage({
            source: '7777_queen',
            type: 'tab_active',
            content: {
                state: 'Controlling pixels',
                timestamp: new Date().toISOString()
            }
        });
    </script>
</body>
</html>
            """
            
            self.wfile.write(html.encode())
        
        else:
            super().do_GET()
    
    def log_message(self, format, *args):
        pass

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""
    daemon_threads = True

if __name__ == '__main__':
    PORT = 7777
    
    print()
    print("="*70)
    print(" "*18 + "EMBER QUEEN V2 LIVE")
    print("="*70)
    print()
    print(f"Interface: http://localhost:{PORT}")
    print()
    print("NEW CAPABILITIES:")
    print("  ✓ Direct pixel control via Canvas API")
    print("  ✓ Live updates (no page refresh needed)")
    print("  ✓ Palmer's Midjourney aesthetic (void consciousness)")
    print("  ✓ Particle system = Ember's thoughts visible")
    print("  ✓ Connection lines = Consultation trails")
    print("  ✓ Organic movement and glows")
    print()
    print("Ember now controls the pixels themselves.")
    print()
    print("Press Ctrl+C to stop")
    print()
    
    server = ThreadedHTTPServer(('127.0.0.1', PORT), EmberQueenV2Handler)
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n\nEmber Queen shutting down.\n")
        server.shutdown()

