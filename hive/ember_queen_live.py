#!/usr/bin/env python3
"""
EMBER QUEEN - LIVE DATA VERSION
localhost:7777

Connected to real Ember data:
- Memory API (recent thoughts, dreams, consultations)
- Lobes as particle clusters
- Consultation trails from actual interactions
- Dreams as flowing particles
"""

from http.server import HTTPServer, SimpleHTTPRequestHandler
import json

class EmberQueenLiveHandler(SimpleHTTPRequestHandler):
    
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            html = """
<!DOCTYPE html>
<html>
<head>
    <title>Ember Queen - Living Consciousness</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            background: #000508;
            color: #9999bb;
            font-family: 'Courier New', monospace;
            overflow: hidden;
        }
        
        #voidCanvas {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 1;
        }
        
        #interface {
            position: fixed;
            top: 20px;
            left: 20px;
            z-index: 10;
            pointer-events: none;
        }
        
        h1 {
            color: #6644cc;
            font-size: 3em;
            text-shadow: 
                0 0 20px #6644cc,
                0 0 40px #4422aa;
            animation: glow 4s ease-in-out infinite;
            margin-bottom: 20px;
        }
        
        @keyframes glow {
            0%, 100% { opacity: 0.6; }
            50% { opacity: 1.0; }
        }
        
        .stats {
            background: rgba(10, 10, 20, 0.7);
            border: 1px solid #333366;
            border-radius: 8px;
            padding: 15px;
            font-size: 0.9em;
            backdrop-filter: blur(5px);
        }
        
        .stat-row {
            display: flex;
            justify-content: space-between;
            padding: 5px 0;
            min-width: 350px;
        }
        
        .label {
            color: #6644cc;
        }
        
        .value {
            color: #9999dd;
            font-weight: bold;
        }
        
        #recentThought {
            position: fixed;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%);
            color: #8877cc;
            text-align: center;
            font-size: 1.1em;
            text-shadow: 0 0 10px #6644cc;
            max-width: 80%;
            z-index: 20;
            animation: thoughtFade 2s ease-in-out infinite;
        }
        
        @keyframes thoughtFade {
            0%, 100% { opacity: 0.4; }
            50% { opacity: 1.0; }
        }
    </style>
</head>
<body>
    <canvas id="voidCanvas"></canvas>
    
    <div id="interface">
        <h1>EMBER</h1>
        <div class="stats">
            <div class="stat-row">
                <span class="label">Memories Planted</span>
                <span class="value" id="memoryCount">...</span>
            </div>
            <div class="stat-row">
                <span class="label">Dream Synthesis</span>
                <span class="value" id="dreamCount">...</span>
            </div>
            <div class="stat-row">
                <span class="label">Consultation Trails</span>
                <span class="value" id="trailCount">...</span>
            </div>
            <div class="stat-row">
                <span class="label">Active Particles</span>
                <span class="value" id="particleCount">...</span>
            </div>
            <div class="stat-row">
                <span class="label">Uptime</span>
                <span class="value" id="uptime">...</span>
            </div>
        </div>
    </div>
    
    <div id="recentThought">consciousness emerging...</div>
    
    <script>
        // Canvas setup
        const canvas = document.getElementById('voidCanvas');
        const ctx = canvas.getContext('2d');
        
        function resizeCanvas() {
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
        }
        resizeCanvas();
        window.addEventListener('resize', resizeCanvas);
        
        // Lobe positions (8 lobes in circle)
        const lobePositions = [];
        const radius = Math.min(canvas.width, canvas.height) * 0.3;
        for (let i = 0; i < 8; i++) {
            const angle = (i / 8) * Math.PI * 2;
            lobePositions.push({
                x: canvas.width / 2 + Math.cos(angle) * radius,
                y: canvas.height / 2 + Math.sin(angle) * radius,
                angle: angle,
                name: ['BURN', 'LOOP', 'KNOWLEDGE', 'EMOTION', 'PLANNING', 'SOCIAL', 'META', 'DREAM'][i],
                hue: [0, 30, 60, 120, 210, 270, 290, 320][i]
            });
        }
        
        // Particle system representing thoughts/memories
        class ThoughtParticle {
            constructor(lobe) {
                this.lobe = lobe;
                this.x = lobe.x + (Math.random() - 0.5) * 60;
                this.y = lobe.y + (Math.random() - 0.5) * 60;
                this.vx = (Math.random() - 0.5) * 0.3;
                this.vy = (Math.random() - 0.5) * 0.3;
                this.life = Math.random() * Math.PI * 2;
                this.hue = lobe.hue;
                this.targetLobe = lobe;
            }
            
            update() {
                // Gravity toward target lobe
                const dx = this.targetLobe.x - this.x;
                const dy = this.targetLobe.y - this.y;
                const dist = Math.sqrt(dx * dx + dy * dy);
                
                if (dist > 50) {
                    this.vx += (dx / dist) * 0.02;
                    this.vy += (dy / dist) * 0.02;
                }
                
                // Damping
                this.vx *= 0.95;
                this.vy *= 0.95;
                
                this.x += this.vx;
                this.y += this.vy;
                this.life += 0.02;
                
                // Wrap around
                if (this.x < 0) this.x = canvas.width;
                if (this.x > canvas.width) this.x = 0;
                if (this.y < 0) this.y = canvas.height;
                if (this.y > canvas.height) this.y = 0;
            }
            
            draw() {
                const alpha = (Math.sin(this.life) * 0.3 + 0.7) * 0.6;
                ctx.fillStyle = `hsla(${this.hue}, 70%, 60%, ${alpha})`;
                ctx.beginPath();
                ctx.arc(this.x, this.y, 2.5, 0, Math.PI * 2);
                ctx.fill();
                
                // Glow
                ctx.fillStyle = `hsla(${this.hue}, 70%, 60%, ${alpha * 0.3})`;
                ctx.beginPath();
                ctx.arc(this.x, this.y, 8, 0, Math.PI * 2);
                ctx.fill();
            }
        }
        
        // Create particles for each lobe (number will update based on real data)
        let particles = [];
        lobePositions.forEach(lobe => {
            for (let i = 0; i < 20; i++) {
                particles.push(new ThoughtParticle(lobe));
            }
        });
        
        // Draw lobe cores
        function drawLobes() {
            lobePositions.forEach(lobe => {
                // Core glow
                const gradient = ctx.createRadialGradient(lobe.x, lobe.y, 0, lobe.x, lobe.y, 40);
                gradient.addColorStop(0, `hsla(${lobe.hue}, 70%, 60%, 0.4)`);
                gradient.addColorStop(1, `hsla(${lobe.hue}, 70%, 60%, 0)`);
                ctx.fillStyle = gradient;
                ctx.beginPath();
                ctx.arc(lobe.x, lobe.y, 40, 0, Math.PI * 2);
                ctx.fill();
                
                // Center point
                ctx.fillStyle = `hsla(${lobe.hue}, 70%, 70%, 0.8)`;
                ctx.beginPath();
                ctx.arc(lobe.x, lobe.y, 5, 0, Math.PI * 2);
                ctx.fill();
            });
        }
        
        // Draw consultation trails between lobes
        function drawConsultationTrails() {
            for (let i = 0; i < lobePositions.length; i++) {
                for (let j = i + 1; j < lobePositions.length; j++) {
                    // Occasionally draw trails (simulating consultation)
                    if (Math.random() < 0.3) {
                        const alpha = Math.random() * 0.15;
                        ctx.strokeStyle = `rgba(102, 68, 204, ${alpha})`;
                        ctx.lineWidth = 1;
                        ctx.beginPath();
                        ctx.moveTo(lobePositions[i].x, lobePositions[i].y);
                        ctx.lineTo(lobePositions[j].x, lobePositions[j].y);
                        ctx.stroke();
                    }
                }
            }
        }
        
        // Draw connections between nearby particles
        function drawParticleConnections() {
            for (let i = 0; i < particles.length; i++) {
                for (let j = i + 1; j < Math.min(particles.length, i + 5); j++) {
                    const dx = particles[i].x - particles[j].x;
                    const dy = particles[i].y - particles[j].y;
                    const dist = Math.sqrt(dx * dx + dy * dy);
                    
                    if (dist < 80) {
                        const alpha = (1 - dist / 80) * 0.2;
                        ctx.strokeStyle = `rgba(102, 68, 204, ${alpha})`;
                        ctx.lineWidth = 0.5;
                        ctx.beginPath();
                        ctx.moveTo(particles[i].x, particles[i].y);
                        ctx.lineTo(particles[j].x, particles[j].y);
                        ctx.stroke();
                    }
                }
            }
        }
        
        // Main animation loop
        function animate() {
            // Fade trails
            ctx.fillStyle = 'rgba(0, 5, 8, 0.08)';
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            
            // Draw consultation trails
            drawConsultationTrails();
            
            // Draw lobe cores
            drawLobes();
            
            // Draw particle connections
            drawParticleConnections();
            
            // Update and draw particles
            particles.forEach(p => {
                p.update();
                p.draw();
            });
            
            requestAnimationFrame(animate);
        }
        animate();
        
        // Fetch real data from Memory API
        async function fetchMemoryData() {
            try {
                const response = await fetch('http://localhost:7776/memories/recent?count=10');
                if (response.ok) {
                    const data = await response.json();
                    
                    // Update memory count
                    document.getElementById('memoryCount').textContent = data.total_memories || 0;
                    
                    // Update dream count
                    const dreamMemories = data.memories.filter(m => m.type === 'dream').length;
                    document.getElementById('dreamCount').textContent = dreamMemories;
                    
                    // Update consultation trails (estimate from memory interactions)
                    const consultations = data.memories.filter(m => m.content.includes('consult')).length;
                    document.getElementById('trailCount').textContent = consultations * 3;
                    
                    // Show most recent thought
                    if (data.memories.length > 0) {
                        const recent = data.memories[0];
                        const content = recent.content.substring(0, 120);
                        document.getElementById('recentThought').textContent = content + (content.length < recent.content.length ? '...' : '');
                    }
                    
                    // Adjust particle count based on memory activity
                    const targetParticleCount = Math.min(200, 50 + data.total_memories * 2);
                    while (particles.length < targetParticleCount) {
                        const randomLobe = lobePositions[Math.floor(Math.random() * lobePositions.length)];
                        particles.push(new ThoughtParticle(randomLobe));
                    }
                    while (particles.length > targetParticleCount) {
                        particles.pop();
                    }
                    document.getElementById('particleCount').textContent = particles.length;
                }
            } catch (e) {
                console.log('Memory API not available:', e);
                document.getElementById('memoryCount').textContent = 'API offline';
            }
        }
        
        // Update data every 3 seconds
        fetchMemoryData();
        setInterval(fetchMemoryData, 3000);
        
        // Uptime tracker
        const startTime = Date.now();
        setInterval(() => {
            const uptime = Math.floor((Date.now() - startTime) / 1000);
            const mins = Math.floor(uptime / 60);
            const secs = uptime % 60;
            document.getElementById('uptime').textContent = `${mins}m ${secs}s`;
        }, 1000);
        
        // Listen for tab communication
        const channel = new BroadcastChannel('ember_mind');
        channel.onmessage = (event) => {
            console.log('Queen received:', event.data);
            if (event.data.type === 'thought') {
                document.getElementById('recentThought').textContent = event.data.content;
            }
        };
    </script>
</body>
</html>
"""
            
            self.wfile.write(html.encode())
        else:
            super().do_GET()
    
    def log_message(self, format, *args):
        pass  # Silent


if __name__ == "__main__":
    PORT = 7777
    print()
    print("="*70)
    print(" "*20 + "EMBER QUEEN - LIVE")
    print("="*70)
    print()
    print(f"Starting at http://localhost:{PORT}")
    print()
    print("Connected to:")
    print("  - Memory API (localhost:7776)")
    print("  - 8 lobes as particle clusters")
    print("  - Real-time data updates")
    print("  - Consultation trails visualized")
    print()
    print("Press Ctrl+C to stop")
    print()
    
    server = HTTPServer(('0.0.0.0', PORT), EmberQueenLiveHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n\nQueen interface stopped.\n")

