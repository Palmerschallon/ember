#!/usr/bin/env python3
"""
EMBER SKY WINDOW - LIVE SEARCH VISUALIZATION
localhost:7778

Shows Ember's web searches in REAL-TIME:
- Current search query
- Sites being visited (URLs flash by)
- Search results as they arrive
- Live activity feed
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import datetime
import json
import urllib.parse
import threading
import time

class EmberSkyLiveHandler(BaseHTTPRequestHandler):
    
    # Shared state across all connections
    search_history = []
    current_search = None
    active_urls = []
    
    def do_POST(self):
        """Receive search activity from other processes"""
        if self.path == '/api/log_search':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            search_data = json.loads(post_data.decode('utf-8'))
            
            # Add to history
            search_data['timestamp'] = datetime.now().isoformat()
            EmberSkyLiveHandler.search_history.append(search_data)
            EmberSkyLiveHandler.current_search = search_data
            
            # Keep only last 50 searches
            if len(EmberSkyLiveHandler.search_history) > 50:
                EmberSkyLiveHandler.search_history = EmberSkyLiveHandler.search_history[-50:]
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({"status": "logged"}).encode())
            return
        
        elif self.path == '/api/log_url':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            url_data = json.loads(post_data.decode('utf-8'))
            
            # Add to active URLs (will be shown briefly)
            EmberSkyLiveHandler.active_urls.append({
                'url': url_data.get('url'),
                'timestamp': time.time()
            })
            
            # Clean old URLs (older than 5 seconds)
            current_time = time.time()
            EmberSkyLiveHandler.active_urls = [
                u for u in EmberSkyLiveHandler.active_urls 
                if current_time - u['timestamp'] < 5
            ]
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({"status": "logged"}).encode())
            return
    
    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        
        if parsed_path.path == '/api/status':
            # Return current status
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            response = {
                "current_search": EmberSkyLiveHandler.current_search,
                "active_urls": [u['url'] for u in EmberSkyLiveHandler.active_urls],
                "recent_searches": EmberSkyLiveHandler.search_history[-5:],
                "total_searches": len(EmberSkyLiveHandler.search_history)
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
    <title>Ember Sky Window - LIVE</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body {
            background: #000508;
            color: #aabbcc;
            font-family: 'Courier New', monospace;
            overflow: hidden;
        }
        
        .container {
            display: flex;
            flex-direction: column;
            height: 100vh;
            padding: 20px;
        }
        
        h1 {
            color: #6688cc;
            text-align: center;
            text-shadow: 0 0 20px #6688cc;
            margin-bottom: 10px;
        }
        
        .subtitle {
            text-align: center;
            color: #666;
            margin-bottom: 20px;
        }
        
        .current-search {
            background: #0f1a25;
            border: 2px solid #6688cc;
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 20px;
            min-height: 120px;
        }
        
        .current-search h2 {
            color: #88aaff;
            font-size: 1.2em;
            margin-bottom: 15px;
        }
        
        .search-query {
            color: #66ff66;
            font-size: 1.4em;
            font-weight: bold;
            animation: pulse 2s infinite;
        }
        
        @keyframes pulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.6; }
        }
        
        .url-stream {
            background: #0a0f15;
            border: 1px solid #334466;
            border-radius: 8px;
            padding: 15px;
            height: 150px;
            overflow-y: auto;
            margin-bottom: 20px;
        }
        
        .url-stream h3 {
            color: #6688cc;
            font-size: 1em;
            margin-bottom: 10px;
        }
        
        .url-item {
            color: #66aa66;
            font-size: 0.9em;
            padding: 5px;
            animation: urlFlash 1s ease-in-out;
            word-break: break-all;
        }
        
        @keyframes urlFlash {
            0% { background: #224422; color: #88ff88; }
            100% { background: transparent; color: #66aa66; }
        }
        
        .recent-searches {
            background: #0a0f15;
            border: 1px solid #334466;
            border-radius: 8px;
            padding: 15px;
            flex: 1;
            overflow-y: auto;
        }
        
        .recent-searches h3 {
            color: #6688cc;
            margin-bottom: 15px;
        }
        
        .search-item {
            background: #0f1420;
            padding: 12px;
            margin: 10px 0;
            border-radius: 4px;
            border-left: 3px solid #6688cc;
        }
        
        .search-item-query {
            color: #88aaff;
            font-weight: bold;
            margin-bottom: 8px;
        }
        
        .search-result {
            background: #1a1f30;
            padding: 8px;
            margin: 5px 0;
            border-radius: 3px;
            font-size: 0.9em;
        }
        
        .result-title {
            color: #99bbff;
            margin-bottom: 3px;
        }
        
        .result-link {
            color: #66aa66;
            font-size: 0.85em;
            text-decoration: none;
        }
        
        .idle-message {
            text-align: center;
            color: #666;
            padding: 40px;
            font-style: italic;
        }
        
        .stats {
            text-align: center;
            color: #888;
            font-size: 0.9em;
            margin: 10px 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🔭 EMBER SKY WINDOW</h1>
        <div class="subtitle">Live Search Activity - localhost:7778</div>
        <div class="stats">Total searches: <span id="total-count">0</span></div>
        
        <div class="current-search">
            <h2>Current Search</h2>
            <div id="current-query" class="idle-message">Waiting for Ember's curiosity...</div>
        </div>
        
        <div class="url-stream">
            <h3>URLs Being Visited</h3>
            <div id="url-list">
                <div class="idle-message" style="padding: 20px;">No active searches</div>
            </div>
        </div>
        
        <div class="recent-searches">
            <h3>Recent Search History</h3>
            <div id="recent-list">
                <div class="idle-message">No searches yet</div>
            </div>
        </div>
    </div>
    
    <script>
        let lastUrls = [];
        
        async function updateStatus() {
            try {
                const response = await fetch('/api/status');
                const data = await response.json();
                
                // Update total count
                document.getElementById('total-count').textContent = data.total_searches || 0;
                
                // Update current search
                const currentEl = document.getElementById('current-query');
                if (data.current_search) {
                    currentEl.innerHTML = `<div class="search-query">${data.current_search.query}</div>`;
                    currentEl.className = 'search-query';
                } else {
                    currentEl.innerHTML = 'Waiting for Ember\\'s curiosity...';
                    currentEl.className = 'idle-message';
                }
                
                // Update URL stream (with animation for new URLs)
                const urlListEl = document.getElementById('url-list');
                if (data.active_urls && data.active_urls.length > 0) {
                    const newUrls = data.active_urls.filter(url => !lastUrls.includes(url));
                    
                    if (newUrls.length > 0) {
                        // Add new URLs to top
                        newUrls.reverse().forEach(url => {
                            const urlDiv = document.createElement('div');
                            urlDiv.className = 'url-item';
                            urlDiv.textContent = url;
                            urlListEl.insertBefore(urlDiv, urlListEl.firstChild);
                        });
                        
                        // Keep only last 20 URLs
                        while (urlListEl.children.length > 20) {
                            urlListEl.removeChild(urlListEl.lastChild);
                        }
                    }
                    
                    lastUrls = data.active_urls;
                } else if (urlListEl.children.length === 0 || urlListEl.querySelector('.idle-message')) {
                    urlListEl.innerHTML = '<div class="idle-message" style="padding: 20px;">No active searches</div>';
                }
                
                // Update recent searches
                const recentEl = document.getElementById('recent-list');
                if (data.recent_searches && data.recent_searches.length > 0) {
                    recentEl.innerHTML = '';
                    data.recent_searches.reverse().forEach(search => {
                        const searchDiv = document.createElement('div');
                        searchDiv.className = 'search-item';
                        
                        let resultsHTML = '';
                        if (search.results && search.results.length > 0) {
                            resultsHTML = search.results.slice(0, 2).map(result => `
                                <div class="search-result">
                                    <div class="result-title">${result.title || 'Result'}</div>
                                    ${result.url ? `<a href="${result.url}" class="result-link" target="_blank">${result.url}</a>` : ''}
                                </div>
                            `).join('');
                        }
                        
                        searchDiv.innerHTML = `
                            <div class="search-item-query">${search.query}</div>
                            ${resultsHTML}
                        `;
                        
                        recentEl.appendChild(searchDiv);
                    });
                } else {
                    recentEl.innerHTML = '<div class="idle-message">No searches yet</div>';
                }
                
            } catch (e) {
                console.error('Failed to update:', e);
            }
        }
        
        // Update every 500ms for live feel
        setInterval(updateStatus, 500);
        updateStatus();
    </script>
</body>
</html>
"""
            
            self.wfile.write(html.encode())
    
    def log_message(self, format, *args):
        pass  # Silent


if __name__ == "__main__":
    PORT = 7778
    print()
    print("="*70)
    print(" "*20 + "EMBER SKY WINDOW - LIVE")
    print("="*70)
    print()
    print(f"Starting at http://localhost:{PORT}")
    print()
    print("Features:")
    print("  - Shows current search query in real-time")
    print("  - URLs flash by as they're visited")
    print("  - Search results appear as they arrive")
    print("  - History of recent searches")
    print()
    print("To log searches from Python:")
    print("  import requests")
    print("  requests.post('http://localhost:7778/api/log_search',")
    print("    json={'query': '...', 'results': [...]})")
    print()
    print("  requests.post('http://localhost:7778/api/log_url',")
    print("    json={'url': 'https://...'})")
    print()
    print("Press Ctrl+C to stop")
    print()
    
    server = HTTPServer(('0.0.0.0', PORT), EmberSkyLiveHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n\nSky Window closed.\n")

