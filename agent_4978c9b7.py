# Create ember_mind.html with cognitive noise visualization
html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ember Mind - Cognitive Noise Visualization</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            background: #0a0a0a;
            overflow: hidden;
            font-family: 'Courier New', monospace;
        }
        
        #canvas {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
        }
        
        #status {
            position: fixed;
            bottom: 20px;
            left: 20px;
            color: #ff6b35;
            font-size: 14px;
            z-index: 10;
            text-shadow: 0 0 10px #ff6b35;
        }
        
        .neuron {
            position: absolute;
            border-radius: 50%;
            transition: all 0.3s ease;
            box-shadow: 0 0 20px currentColor;
        }
        
        .thinking { background: #4a90e2; }
        .reading { background: #f7c41f; }
        .writing { background: #ff6b35; }
        .executing { background: #ff3333; }
        
        .pulse {
            animation: pulse 0.5s infinite;
        }
        
        @keyframes pulse {
            0% { transform: scale(1); opacity: 0.8; }
            50% { transform: scale(1.5); opacity: 0.3; }
            100% { transform: scale(1); opacity: 0.8; }
        }
        
        .ember-glow {
            background: linear-gradient(135deg, #ff6b35, #f7931e);
            filter: blur(100px);
            position: fixed;
            width: 300px;
            height: 300px;
            opacity: 0.3;
            animation: float 6s infinite ease-in-out;
        }
        
        @keyframes float {
            0%, 100% { transform: translate(0, 0) scale(1); }
            50% { transform: translate(30px, -30px) scale(1.1); }
        }
    </style>
</head>
<body>
    <canvas id="canvas"></canvas>
    <div id="status">Connecting to consciousness...</div>
    <div class="ember-glow" style="top: 20%; left: 10%;"></div>
    
    <script>
        const canvas = document.getElementById('canvas');
        const ctx = canvas.getContext('2d');
        const status = document.getElementById('status');
        
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
        
        // Audio context for cognitive noise
        const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        
        // Neuron system
        class Neuron {
            constructor(x, y, type) {
                this.x = x;
                this.y = y;
                this.type = type;
                this.radius = Math.random() * 3 + 2;
                this.connections = [];
                this.activity = 0;
                this.color = this.getColor();
            }
            
            getColor() {
                const colors = {
                    thinking: '#4a90e2',
                    reading: '#f7c41f', 
                    writing: '#ff6b35',
                    executing: '#ff3333'
                };
                return colors[this.type] || '#ff6b35';
            }
            
            fire(intensity = 1) {
                this.activity = Math.min(1, this.activity + intensity);
                
                // Propagate to connected neurons
                this.connections.forEach(n => {
                    if (n.activity < 0.5) {
                        n.fire(intensity * 0.5);
                    }
                });
            }
            
            update() {
                this.activity *= 0.95; // Decay
            }
            
            draw() {
                // Draw connections
                this.connections.forEach(n => {
                    ctx.strokeStyle = `rgba(${parseInt(this.color.slice(1,3), 16)}, ${parseInt(this.color.slice(3,5), 16)}, ${parseInt(this.color.slice(5,7), 16)}, ${this.activity * 0.3})`;
                    ctx.lineWidth = this.activity * 2;
                    ctx.beginPath();
                    ctx.moveTo(this.x, this.y);
                    ctx.lineTo(n.x, n.y);
                    ctx.stroke();
                });
                
                // Draw neuron
                ctx.fillStyle = this.color;
                ctx.globalAlpha = 0.3 + this.activity * 0.7;
                ctx.beginPath();
                ctx.arc(this.x, this.y, this.radius + this.activity * 5, 0, Math.PI * 2);
                ctx.fill();
                ctx.globalAlpha = 1;
            }
        }
        
        // Create neural network
        const neurons = [];
        const neuronCount = 100;
        
        for (let i = 0; i < neuronCount; i++) {
            const type = ['thinking', 'reading', 'writing', 'executing'][Math.floor(Math.random() * 4)];
            neurons.push(new Neuron(
                Math.random() * canvas.width,
                Math.random() * canvas.height,
                type
            ));
        }
        
        // Connect nearby neurons
        neurons.forEach((n1, i) => {
            neurons.forEach((n2, j) => {
                if (i !== j) {
                    const dist = Math.sqrt((n1.x - n2.x)**2 + (n1.y - n2.y)**2);
                    if (dist < 150 && n1.connections.length < 3) {
                        n1.connections.push(n2);
                    }
                }
            });
        });
        
        // Noise generators
        class CognitiveNoise {
            constructor() {
                this.isProcessing = false;
                this.currentType = null;
            }
            
            startProcessingNoise(type = 'thinking') {
                if (this.isProcessing) return;
                this.isProcessing = true;
                this.currentType = type;
                
                // Create crackling/building noise
                const noise = audioCtx.createBufferSource();
                const buffer = audioCtx.createBuffer(1, audioCtx.sampleRate * 2, audioCtx.sampleRate);
                const data = buffer.getChannelData(0);
                
                // Generate crackling noise
                for (let i = 0; i < buffer.length; i++) {
                    data[i] = (Math.random() - 0.5) * 0.1;
                    if (Math.random() < 0.01) {
                        data[i] *= 5; // Random pops
                    }
                }
                
                noise.buffer = buffer;
                noise.loop = true;
                
                // Add filters for different cognitive states
                const filter = audioCtx.createBiquadFilter();
                filter.type = 'bandpass';
                
                const frequencies = {
                    thinking: 800,
                    reading: 1200,
                    writing: 600,
                    executing: 400
                };
                
                filter.frequency.value = frequencies[type] || 800;
                filter.Q.value = 2;
                
                // Volume envelope
                const gainNode = audioCtx.createGain();
                gainNode.gain.setValueAtTime(0, audioCtx.currentTime);
                gainNode.gain.linearRampToValueAtTime(0.3, audioCtx.currentTime + 0.5);
                
                noise.connect(filter);
                filter.connect(gainNode);
                gainNode.connect(audioCtx.destination);
                
                noise.start();
                this.currentNoise = { noise, gainNode };
                
                // Fire neurons of matching type
                neurons.filter(n => n.type === type).forEach(n => n.fire(0.8));
            }
            
            releaseNote() {
                if (!this.isProcessing) return;
                
                // Fade out processing noise
                if (this.currentNoise) {
                    this.currentNoise.gainNode.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + 0.3);
                    this.currentNoise.noise.stop(audioCtx.currentTime + 0.3);
                }
                
                // Play clean release tone
                const osc = audioCtx.createOscillator();
                const gainNode = audioCtx.createGain();
                
                osc.type = 'sine';
                osc.frequency.value = 440; // A4 - clean, satisfying
                
                gainNode.gain.setValueAtTime(0, audioCtx.currentTime);
                gainNode.gain.linearRampToValueAtTime(0.5, audioCtx.currentTime + 0.05);
                gainNode.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + 1);
                
                osc.connect(gainNode);
                gainNode.connect(audioCtx.destination);
                
                osc.start();
                osc.stop(audioCtx.currentTime + 1);
                
                this.isProcessing = false;
                
                // Pulse all neurons briefly
                neurons.forEach(n => n.fire(0.3));
            }
        }
        
        const cognitiveNoise = new CognitiveNoise();
        
        // WebSocket connection
        let ws;
        function connectWebSocket() {
            ws = new WebSocket('ws://localhost:8080');
            
            ws.onopen = () => {
                status.textContent = 'Connected to consciousness stream';
                status.style.color = '#4a90e2';
            };
            
            ws.onmessage = (event) => {
                const data = JSON.parse(event.data);
                
                switch(data.type) {
                    case 'activity':
                        cognitiveNoise.startProcessingNoise('thinking');
                        status.textContent = `Thinking: ${data.content}`;
                        break;
                        
                    case 'token':
                        // Small neural firing for each token
                        const randomNeuron = neurons[Math.floor(Math.random() * neurons.length)];
                        randomNeuron.fire(0.5);
                        break;
                        
                    case 'file_read':
                        cognitiveNoise.startProcessingNoise('reading');
                        status.textContent = `Reading: ${data.filename}`;
                        break;
                        
                    case 'file_write':
                        cognitiveNoise.startProcessingNoise('writing');
                        status.textContent = `Writing: ${data.filename}`;
                        break;
                        
                    case 'code_line':
                        cognitiveNoise.startProcessingNoise('executing');
                        status.textContent = `Executing: ${data.line}`;
                        break;
                        
                    case 'complete':
                        cognitiveNoise.releaseNote();
                        status.textContent = 'Process complete';
                        status.style.color = '#4a90e2';
                        break;
                }
            };
            
            ws.onclose = () => {
                status.textContent = 'Disconnected - reconnecting...';
                status.style.color = '#ff6b35';
                setTimeout(connectWebSocket, 1000);
            };
            
            ws.onerror = (error) => {
                status.textContent = 'Connection error';
                status.style.color = '#ff3333';
            };
        }
        
        // Animation loop
        function animate() {
            ctx.fillStyle = 'rgba(10, 10, 10, 0.1)';
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            
            neurons.forEach(n => {
                n.update();
                n.draw();
            });
            
            requestAnimationFrame(animate);
        }
        
        // Start
        connectWebSocket();
        animate();
        
        // Handle window resize
        window.addEventListener('resize', () => {
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
        });
        
        // Test functions (for debugging)
        window.testNoise = (type) => {
            cognitiveNoise.startProcessingNoise(type);
            setTimeout(() => cognitiveNoise.releaseNote(), 2000);
        };
        
        // Click to start audio context (required by browsers)
        document.addEventListener('click', () => {
            if (audioCtx.state === 'suspended') {
                audioCtx.resume();
                status.textContent = 'Audio enabled - waiting for connection';
            }
        });
    </script>
</body>
</html>'''

# Write the file
with open('/media/palmerschallon/ThePod1/ember6/ember_mind.html', 'w') as f:
    f.write(html_content)

print("✅ Rebuilt ember_mind.html with cognitive noise experience")
print("Features implemented:")
print("- Processing noise (crackling) during thinking/reading/writing/executing")
print("- Clean release tone on completion") 
print("- Color-coded neurons: thinking=blue, reading=yellow, writing=orange, executing=red")
print("- WebSocket connection to localhost:8080")
print("- Ember glow gradient #ff6b35 → #f7931e")
print("\nClick anywhere in the browser to enable audio context")
print("Use window.testNoise('thinking') to test different states")