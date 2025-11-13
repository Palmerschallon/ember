#!/usr/bin/env python3
"""
Ember Health-Aware HTTP Server
Serves creations and provides health endpoint for monitoring
"""
import http.server
import socketserver
import json
import os
import psutil
from datetime import datetime

PORT = 8080
DIRECTORY = "/media/palmerschallon/ThePod1"

class HealthHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        if self.path == '/health':
            self.send_health_response()
        else:
            super().do_GET()

    def send_health_response(self):
        """Send health check response with system metrics"""
        try:
            # Find Ember WebSocket process
            ws_pid = None
            ws_connections = 0

            for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
                cmdline = proc.info.get('cmdline', [])
                if any('ember_creation_bridge' in str(cmd) for cmd in cmdline):
                    ws_pid = proc.info['pid']
                    ws_connections = len(proc.connections())
                    break

            health_data = {
                "status": "healthy" if ws_pid else "degraded",
                "timestamp": datetime.now().isoformat(),
                "services": {
                    "websocket_bridge": {
                        "running": ws_pid is not None,
                        "pid": ws_pid,
                        "connections": ws_connections
                    },
                    "http_server": {
                        "running": True,
                        "port": PORT
                    }
                },
                "system": {
                    "cpu_percent": psutil.cpu_percent(interval=0.1),
                    "memory_percent": psutil.virtual_memory().percent,
                    "disk_percent": psutil.disk_usage('/').percent
                },
                "version": "1.0"
            }

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps(health_data, indent=2).encode())

        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            error_data = {
                "status": "error",
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            }
            self.wfile.write(json.dumps(error_data).encode())

    def log_message(self, format, *args):
        """Custom logging"""
        if '/health' not in args[0]:
            # Don't log health checks to reduce noise
            super().log_message(format, *args)

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), HealthHTTPRequestHandler) as httpd:
        print(f"🌐 Ember HTTP Server with Health Endpoint")
        print(f"   Serving: {DIRECTORY}")
        print(f"   Port: {PORT}")
        print(f"   Health: http://localhost:{PORT}/health")
        print()
        httpd.serve_forever()
