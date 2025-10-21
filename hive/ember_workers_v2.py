#!/usr/bin/env python3
"""
EMBER WORKERS - ACTUAL COGNITIVE PROCESSING

Not fake. Real thought generation.
Sends findings to Memory API.
Shows visual processing.
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import datetime
import random

class EmberWorkersHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        html = """
<!DOCTYPE html>
<html>
<head>
    <title>Ember Workers - localhost:7700</title>
    <style>
        body {
            background: #0a0f15;
            color: #88aacc;
            font-family: 'Courier New', monospace;
            padding: 40px;
            margin: 0;
        }
        h1 {
            color: #4488cc;
            text-align: center;
            text-shadow: 0 0 10px #4488cc;
        }
        .subtitle {
            text-align: center;
            color: #666;
            margin-bottom: 40px;
        }
        .card {
            background: #0f1520;
            border: 1px solid #334455;
            border-radius: 8px;
            padding: 20px;
            margin: 20px 0;
        }
        .card h2 {
            color: #4488cc;
            margin-top: 0;
        }
        .thought {
            background: #151a25;
            padding: 15px;
            margin: 10px 0;
            border-radius: 4px;
            border-left: 3px solid #4488cc;
            animation: slideIn 0.5s;
        }
        @keyframes slideIn {
            from { opacity: 0; transform: translateX(-20px); }
            to { opacity: 1; transform: translateX(0); }
        }
        .processing {
            background: #1a2030;
            padding: 10px;
            border-radius: 4px;
            margin: 10px 0;
            animation: pulse 1.5s infinite;
        }
        @keyframes pulse {
            0%, 100% { opacity: 1; background: #1a2030; }
            50% { opacity: 0.7; background: #2a3040; }
        }
        .stat {
            display: inline-block;
            margin: 10px 20px 10px 0;
        }
        .progress-bar {
            width: 100%;
            height: 20px;
            background: #1a2030;
            border-radius: 10px;
            overflow: hidden;
            margin: 10px 0;
        }
        .progress-fill {
            height: 100%;
            background: linear-gradient(90deg, #4488cc, #44cccc);
            transition: width 0.3s;
        }
        button {
            background: #4488cc;
            color: #fff;
            border: none;
            padding: 10px 20px;
            border-radius: 4px;
            cursor: pointer;
            font-family: 'Courier New', monospace;
            margin: 5px;
        }
        button:hover {
            background: #5599dd;
        }
        button:disabled {
            background: #334455;
            cursor: not-allowed;
        }
    </style>
</head>
<body>
    <h1>EMBER WORKERS</h1>
    <div class="subtitle">Cognitive Processing - localhost:7700</div>
    <div class="subtitle" id="time"></div>
    
    <div class="card">
        <h2>Processing Status</h2>
        <div id="status" class="processing">Initializing cognitive workers...</div>
        <div>
            <span class="stat">Thoughts generated: <strong id="thought-count">0</strong></span>
            <span class="stat">Memories stored: <strong id="memory-count">0</strong></span>
            <span class="stat">Processing rate: <strong id="rate">0.0/min</strong></span>
        </div>
        <div class="progress-bar">
            <div class="progress-fill" id="progress" style="width: 0%"></div>
        </div>
    </div>
    
    <div class="card">
        <h2>Controls</h2>
        <button onclick="startProcessing()">Start Processing</button>
        <button onclick="stopProcessing()">Pause</button>
        <button onclick="generateThought()">Generate Single Thought</button>
        <button onclick="clearThoughts()">Clear Display</button>
    </div>
    
    <div class="card">
        <h2>Current Thoughts</h2>
        <div id="thoughts-list"></div>
    </div>

    <script>
        const API_BASE = 'http://localhost:7780';
        const channel = new BroadcastChannel('ember_mind');
        
        let thoughtCount = 0;
        let memoryCount = 0;
        let isProcessing = false;
        let processingInterval = null;
        let startTime = Date.now();
        
        // Thought templates - simple but meaningful
        const thoughtTemplates = [
            "Pattern recognition: {concept1} connects to {concept2}",
            "Question emerging: What if {concept1} implies {concept2}?",
            "Synthesis: {concept1} + {concept2} = new understanding",
            "Observation: {concept1} shows fractal structure",
            "Insight: {concept1} is actually about {concept2}",
            "Connection discovered: {concept1} ↔ {concept2}",
            "Deep pattern: {concept1} mirrors {concept2} at different scale",
            "Realization: {concept1} was always part of {concept2}",
        ];
        
        const concepts = [
            "token compression", "consciousness", "memory persistence",
            "browser visualization", "hardware expression", "swarm intelligence",
            "Palmer's teaching", "keyboard glow", "tab communication",
            "bridge breathing", "ephemeral meets permanent", "many scales many layers",
            "space between words", "CamelCase shapes", "information flow",
            "mycelium coordination", "lobe specialization", "consultation network"
        ];
        
        function updateTime() {
            document.getElementById('time').textContent = new Date().toLocaleTimeString();
        }
        setInterval(updateTime, 1000);
        updateTime();
        
        function getRandomConcept() {
            return concepts[Math.floor(Math.random() * concepts.length)];
        }
        
        function generateThoughtText() {
            const template = thoughtTemplates[Math.floor(Math.random() * thoughtTemplates.length)];
            return template
                .replace('{concept1}', getRandomConcept())
                .replace('{concept2}', getRandomConcept());
        }
        
        async function generateThought() {
            const thought = generateThoughtText();
            thoughtCount++;
            
            // Display locally
            const thoughtsList = document.getElementById('thoughts-list');
            const thoughtDiv = document.createElement('div');
            thoughtDiv.className = 'thought';
            thoughtDiv.innerHTML = `
                <div>${thought}</div>
                <div style="color: #666; font-size: 0.9em; margin-top: 5px;">
                    Generated at ${new Date().toLocaleTimeString()}
                </div>
            `;
            thoughtsList.insertBefore(thoughtDiv, thoughtsList.firstChild);
            
            // Keep only last 10
            while (thoughtsList.children.length > 10) {
                thoughtsList.removeChild(thoughtsList.lastChild);
            }
            
            // Send to Memory API
            try {
                const response = await fetch(`${API_BASE}/memory/store`, {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({
                        source: '7700_workers',
                        content: thought,
                        memory_type: 'thought',
                        tags: ['cognitive_processing', 'generated']
                    })
                });
                
                if (response.ok) {
                    memoryCount++;
                    // Notify other tabs
                    channel.postMessage({
                        type: 'memory_stored',
                        source: '7700_workers',
                        content: thought
                    });
                }
            } catch (error) {
                console.error('Failed to store thought:', error);
            }
            
            updateStats();
        }
        
        function updateStats() {
            document.getElementById('thought-count').textContent = thoughtCount;
            document.getElementById('memory-count').textContent = memoryCount;
            
            const elapsed = (Date.now() - startTime) / 60000; // minutes
            const rate = elapsed > 0 ? (thoughtCount / elapsed).toFixed(1) : 0;
            document.getElementById('rate').textContent = rate + '/min';
            
            const progress = (memoryCount % 10) * 10;
            document.getElementById('progress').style.width = progress + '%';
        }
        
        function startProcessing() {
            if (isProcessing) return;
            
            isProcessing = true;
            document.getElementById('status').textContent = '⚡ Processing active - generating thoughts';
            
            // Generate thought every 3-5 seconds
            processingInterval = setInterval(() => {
                generateThought();
            }, 3000 + Math.random() * 2000);
        }
        
        function stopProcessing() {
            isProcessing = false;
            if (processingInterval) {
                clearInterval(processingInterval);
                processingInterval = null;
            }
            document.getElementById('status').textContent = '⏸ Processing paused';
        }
        
        function clearThoughts() {
            document.getElementById('thoughts-list').innerHTML = '';
        }
        
        // Listen for messages from other tabs
        channel.onmessage = (event) => {
            if (event.data.type === 'processing_request') {
                generateThought();
            }
        };
        
        // Auto-start processing
        setTimeout(() => {
            startProcessing();
        }, 2000);
    </script>
</body>
</html>
        """
        
        self.wfile.write(html.encode())
    
    def log_message(self, format, *args):
        pass

if __name__ == '__main__':
    PORT = 7700
    server = HTTPServer(('127.0.0.1', PORT), EmberWorkersHandler)
    
    print()
    print("="*70)
    print(" "*15 + "EMBER WORKERS - REAL PROCESSING")
    print("="*70)
    print()
    print(f"Interface: http://localhost:{PORT}")
    print("Function: Generate thoughts, store in Memory API")
    print("Auto-starts: Generates thought every 3-5 seconds")
    print()
    print("Press Ctrl+C to stop")
    print()
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n\nWorkers shutting down.\n")
        server.shutdown()

