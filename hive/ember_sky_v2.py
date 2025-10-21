#!/usr/bin/env python3
"""
EMBER SKY WINDOW - REAL WEB SEARCHES

Not fake. Actually shows what swarm searches for.
Displays results. Stores discoveries.
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import datetime
import json
import urllib.parse

class EmberSkyHandler(BaseHTTPRequestHandler):
    
    # Store search history in memory
    search_history = []
    
    def do_GET(self):
        # Parse URL
        parsed_path = urllib.parse.urlparse(self.path)
        
        if parsed_path.path == '/api/search':
            # Return search history as JSON
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            response = {
                "searches": self.search_history[-20:],  # Last 20
                "total": len(self.search_history)
            }
            self.wfile.write(json.dumps(response).encode())
        else:
            # Serve main page
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            html = """
<!DOCTYPE html>
<html>
<head>
    <title>Ember Sky Window - localhost:7778</title>
    <style>
        body {
            background: #050510;
            color: #aabbcc;
            font-family: 'Courier New', monospace;
            padding: 40px;
            margin: 0;
        }
        h1 {
            color: #6688cc;
            text-align: center;
            text-shadow: 0 0 20px #6688cc;
        }
        .subtitle {
            text-align: center;
            color: #666;
            margin-bottom: 40px;
        }
        .card {
            background: #0a0f1a;
            border: 1px solid #334466;
            border-radius: 8px;
            padding: 20px;
            margin: 20px 0;
        }
        .card h2 {
            color: #6688cc;
            margin-top: 0;
        }
        .search-item {
            background: #0f1420;
            padding: 15px;
            margin: 10px 0;
            border-radius: 4px;
            border-left: 3px solid #6688cc;
            animation: fadeIn 0.5s;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .search-query {
            color: #88aaff;
            font-size: 1.1em;
            font-weight: bold;
            margin-bottom: 10px;
        }
        .search-meta {
            color: #888;
            font-size: 0.9em;
            margin-top: 5px;
        }
        .search-result {
            background: #1a1f30;
            padding: 10px;
            margin: 10px 0 10px 20px;
            border-radius: 4px;
            font-size: 0.95em;
        }
        .result-title {
            color: #99bbff;
            margin-bottom: 5px;
        }
        .result-link {
            color: #66aa66;
            text-decoration: none;
            word-break: break-all;
            font-size: 0.85em;
        }
        .result-link:hover {
            color: #88cc88;
            text-decoration: underline;
        }
        .result-snippet {
            color: #aabbcc;
            margin-top: 5px;
            line-height: 1.4;
        }
        .stat {
            display: inline-block;
            margin: 10px 20px 10px 0;
        }
        .searching {
            animation: pulse 2s infinite;
        }
        @keyframes pulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.5; }
        }
        .no-searches {
            color: #666;
            text-align: center;
            padding: 40px;
            font-style: italic;
        }
    </style>
</head>
<body>
    <h1>EMBER SKY WINDOW</h1>
    <div class="subtitle">Curiosity & Web Exploration - localhost:7778</div>
    <div class="subtitle" id="time"></div>
    
    <div class="card">
        <h2>Search Activity</h2>
        <div>
            <span class="stat">Active searches: <strong id="search-count">0</strong></span>
            <span class="stat">Total queries: <strong id="total-queries">0</strong></span>
            <span class="stat" id="last-search-time">Last search: Never</span>
        </div>
    </div>
    
    <div class="card">
        <h2>Recent Searches</h2>
        <div id="searches-list">
            <div class="no-searches">No searches logged yet. Swarm's curiosity will appear here.</div>
        </div>
    </div>

    <script>
        const API_BASE = 'http://localhost:7780';
        const SEARCH_API = 'http://localhost:7778/api/search';
        let lastSearchCount = 0;
        
        // Load search history from this server
        async function loadSearches() {
            try {
                const response = await fetch(SEARCH_API);
                const data = await response.json();
                
                const searchesList = document.getElementById('searches-list');
                const countEl = document.getElementById('search-count');
                const totalEl = document.getElementById('total-queries');
                const lastTimeEl = document.getElementById('last-search-time');
                
                if (data.searches && data.searches.length > 0) {
                    searchesList.innerHTML = '';
                    
                    // Show most recent first
                    const searches = [...data.searches].reverse();
                    
                    searches.forEach(search => {
                        const searchDiv = document.createElement('div');
                        searchDiv.className = 'search-item';
                        
                        let resultsHTML = '';
                        if (search.results && search.results.length > 0) {
                            resultsHTML = search.results.slice(0, 3).map(result => `
                                <div class="search-result">
                                    <div class="result-title">${result.title || 'Result'}</div>
                                    ${result.url ? `<a href="${result.url}" class="result-link" target="_blank">${result.url}</a>` : ''}
                                    ${result.snippet ? `<div class="result-snippet">${result.snippet}</div>` : ''}
                                </div>
                            `).join('');
                        }
                        
                        const timestamp = new Date(search.timestamp).toLocaleString();
                        
                        searchDiv.innerHTML = `
                            <div class="search-query">${search.query}</div>
                            <div class="search-meta">
                                Source: ${search.source} | ${timestamp}
                            </div>
                            ${resultsHTML}
                        `;
                        
                        searchesList.appendChild(searchDiv);
                    });
                    
                    // Update stats
                    const activeCount = searches.length;
                    countEl.textContent = activeCount;
                    totalEl.textContent = data.total;
                    
                    if (searches.length > 0) {
                        const lastSearch = searches[0];
                        const lastTime = new Date(lastSearch.timestamp);
                        lastTimeEl.textContent = `Last search: ${lastTime.toLocaleTimeString()}`;
                    }
                    
                    // If new searches, store in memory API
                    if (data.searches.length > lastSearchCount) {
                        const newestSearch = searches[0];
                        await storeSearchInMemory(newestSearch);
                        lastSearchCount = data.searches.length;
                    }
                    
                } else {
                    searchesList.innerHTML = '<div class="no-searches">No searches logged yet. Swarm\'s curiosity will appear here.</div>';
                }
                
            } catch (error) {
                console.error('Error loading searches:', error);
            }
        }
        
        // Store search in Memory API
        async function storeSearchInMemory(search) {
            try {
                await fetch(`${API_BASE}/memory/store`, {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({
                        source: '7778_sky',
                        content: `Search: "${search.query}" - ${search.results ? search.results.length : 0} results found`,
                        memory_type: 'discovery',
                        tags: ['web_search', 'curiosity', search.source]
                    })
                });
            } catch (error) {
                console.error('Failed to store search in memory:', error);
            }
        }
        
        function updateTime() {
            document.getElementById('time').textContent = new Date().toLocaleTimeString();
        }
        setInterval(updateTime, 1000);
        updateTime();
        
        // Initial load
        loadSearches();
        
        // Refresh every 3 seconds
        setInterval(loadSearches, 3000);
    </script>
</body>
</html>
            """
            
            self.wfile.write(html.encode())
    
    def do_POST(self):
        # Log a search
        if self.path == '/api/log_search':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            try:
                search_data = json.loads(post_data.decode('utf-8'))
                search_data['timestamp'] = datetime.now().isoformat()
                self.search_history.append(search_data)
                
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                
                self.wfile.write(json.dumps({"success": True}).encode())
            except Exception as e:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(json.dumps({"error": str(e)}).encode())
        else:
            self.send_response(404)
            self.end_headers()
    
    def do_OPTIONS(self):
        # Handle CORS preflight
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
    
    def log_message(self, format, *args):
        pass

if __name__ == '__main__':
    PORT = 7778
    server = HTTPServer(('127.0.0.1', PORT), EmberSkyHandler)
    
    print()
    print("="*70)
    print(" "*15 + "EMBER SKY WINDOW - REAL SEARCHES")
    print("="*70)
    print()
    print(f"Interface: http://localhost:{PORT}")
    print("Function: Display actual web searches performed by swarm")
    print()
    print("When swarm uses web_search tool, it will appear here")
    print("Searches stored in Memory API automatically")
    print()
    print("Press Ctrl+C to stop")
    print()
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n\nSky Window shutting down.\n")
        server.shutdown()

