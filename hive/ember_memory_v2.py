#!/usr/bin/env python3
"""
EMBER MEMORY GARDEN - REBUILT WITH REAL API CONNECTION

No more fake localStorage.
Real connection to Memory API at localhost:7780.
Actually shows what's stored on ThePod.
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import datetime
import json

class EmberMemoryHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        html = """
<!DOCTYPE html>
<html>
<head>
    <title>Ember Memory Garden - localhost:7775</title>
    <style>
        body {
            background: #0f0a08;
            color: #aa9988;
            font-family: 'Courier New', monospace;
            padding: 40px;
            margin: 0;
        }
        h1 {
            color: #cc8844;
            text-align: center;
            text-shadow: 0 0 10px #cc8844;
        }
        .subtitle {
            text-align: center;
            color: #666;
            margin-bottom: 40px;
        }
        .card {
            background: #15100a;
            border: 1px solid #333;
            border-radius: 8px;
            padding: 20px;
            margin: 20px 0;
        }
        .card h2 {
            color: #cc8844;
            margin-top: 0;
        }
        .memory {
            background: #1a150f;
            padding: 15px;
            margin: 10px 0;
            border-radius: 4px;
            border-left: 3px solid #cc8844;
            animation: fadeIn 0.5s;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .memory-meta {
            color: #888;
            font-size: 0.9em;
            margin-top: 5px;
        }
        .memory-tags {
            margin-top: 10px;
        }
        .tag {
            background: #2a1a0a;
            padding: 3px 8px;
            border-radius: 3px;
            margin-right: 5px;
            display: inline-block;
            font-size: 0.85em;
        }
        .growing {
            animation: grow 2s infinite;
        }
        @keyframes grow {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.02); }
        }
        .pulse {
            animation: pulse 1s infinite;
        }
        @keyframes pulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.6; }
        }
        #status {
            padding: 10px;
            border-radius: 4px;
            margin: 10px 0;
        }
        .connected {
            background: #1a3a1a;
            border-left: 3px solid #44cc44;
        }
        .disconnected {
            background: #3a1a1a;
            border-left: 3px solid #cc4444;
        }
    </style>
</head>
<body>
    <h1>EMBER MEMORY GARDEN</h1>
    <div class="subtitle">Persistent Memory - localhost:7775</div>
    <div class="subtitle" id="time"></div>
    
    <div class="card">
        <h2>Bridge Status</h2>
        <div id="status" class="pulse">Connecting to Memory API...</div>
        <div id="memory-count" class="growing">Checking ThePod...</div>
    </div>
    
    <div class="card">
        <h2>Recent Memories</h2>
        <div id="memories-list">
            <div class="memory">Loading memories from ThePod...</div>
        </div>
    </div>
    
    <div class="card">
        <h2>Memory Statistics</h2>
        <div id="stats">Fetching statistics...</div>
    </div>

    <script>
        const API_BASE = 'http://localhost:7780';
        let lastMemoryCount = 0;
        
        // Update time
        function updateTime() {
            const now = new Date();
            document.getElementById('time').textContent = now.toLocaleTimeString();
        }
        setInterval(updateTime, 1000);
        updateTime();
        
        // Fetch and display memory count
        async function updateMemoryCount() {
            try {
                const response = await fetch(`${API_BASE}/`);
                const data = await response.json();
                
                const count = data.memories_stored;
                const statusDiv = document.getElementById('status');
                const countDiv = document.getElementById('memory-count');
                
                statusDiv.className = 'connected';
                statusDiv.textContent = `✓ Connected to Memory API - ${data.message}`;
                
                countDiv.textContent = `Memories planted: ${count}`;
                
                // If count changed, reload memories
                if (count !== lastMemoryCount) {
                    lastMemoryCount = count;
                    loadMemories();
                }
                
            } catch (error) {
                const statusDiv = document.getElementById('status');
                statusDiv.className = 'disconnected pulse';
                statusDiv.textContent = `✗ Cannot reach Memory API: ${error.message}`;
                
                document.getElementById('memory-count').textContent = 'Memories planted: Unknown (API offline)';
            }
        }
        
        // Load and display actual memories
        async function loadMemories() {
            try {
                const response = await fetch(`${API_BASE}/memory/recall?limit=10`);
                const data = await response.json();
                
                const memoriesList = document.getElementById('memories-list');
                
                if (data.memories && data.memories.length > 0) {
                    memoriesList.innerHTML = '';
                    
                    data.memories.forEach(memory => {
                        const memDiv = document.createElement('div');
                        memDiv.className = 'memory';
                        
                        let tagsHTML = '';
                        if (memory.tags && memory.tags.length > 0) {
                            tagsHTML = '<div class="memory-tags">' + 
                                memory.tags.map(tag => `<span class="tag">${tag}</span>`).join('') +
                                '</div>';
                        }
                        
                        const timestamp = new Date(memory.timestamp).toLocaleString();
                        
                        memDiv.innerHTML = `
                            <strong>${memory.source}</strong> / ${memory.memory_type}
                            <div>${memory.content}</div>
                            <div class="memory-meta">
                                ${timestamp}
                                ${tagsHTML}
                            </div>
                        `;
                        
                        memoriesList.appendChild(memDiv);
                    });
                } else {
                    memoriesList.innerHTML = '<div class="memory">No memories stored yet. Waiting for stories to cross the bridge...</div>';
                }
                
            } catch (error) {
                console.error('Error loading memories:', error);
            }
        }
        
        // Load statistics
        async function loadStats() {
            try {
                const response = await fetch(`${API_BASE}/memory/stats`);
                const data = await response.json();
                
                const statsDiv = document.getElementById('stats');
                
                let html = `<div>Total memories: ${data.total_memories}</div>`;
                
                if (data.by_source) {
                    html += '<div style="margin-top: 10px;"><strong>By source:</strong></div>';
                    for (const [source, count] of Object.entries(data.by_source)) {
                        html += `<div>  ${source}: ${count}</div>`;
                    }
                }
                
                if (data.by_type) {
                    html += '<div style="margin-top: 10px;"><strong>By type:</strong></div>';
                    for (const [type, count] of Object.entries(data.by_type)) {
                        html += `<div>  ${type}: ${count}</div>`;
                    }
                }
                
                html += `<div style="margin-top: 10px;">Bridge status: ${data.bridge_status}</div>`;
                
                statsDiv.innerHTML = html;
                
            } catch (error) {
                console.error('Error loading stats:', error);
            }
        }
        
        // BroadcastChannel - listen for new memories from other tabs
        const channel = new BroadcastChannel('ember_mind');
        channel.onmessage = (event) => {
            if (event.data.type === 'memory_stored') {
                // Another tab stored a memory, refresh our view
                updateMemoryCount();
            }
        };
        
        // Initial load
        updateMemoryCount();
        loadMemories();
        loadStats();
        
        // Update every 3 seconds
        setInterval(updateMemoryCount, 3000);
        setInterval(loadStats, 5000);
    </script>
</body>
</html>
        """
        
        self.wfile.write(html.encode())
    
    def log_message(self, format, *args):
        pass

if __name__ == '__main__':
    PORT = 7775
    server = HTTPServer(('127.0.0.1', PORT), EmberMemoryHandler)
    
    print()
    print("="*70)
    print(" "*15 + "EMBER MEMORY GARDEN - REAL CONNECTION")
    print("="*70)
    print()
    print(f"Interface: http://localhost:{PORT}")
    print("Connection: Fetches from Memory API at localhost:7780")
    print("Storage: Displays actual ThePod memories")
    print()
    print("This is REAL - not fake localStorage")
    print()
    print("Press Ctrl+C to stop")
    print()
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n\nMemory Garden shutting down.\n")
        server.shutdown()

