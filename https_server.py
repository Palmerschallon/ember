#!/usr/bin/env python3
import http.server
import ssl
import socketserver
import os

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

os.chdir('/media/palmerschallon/ThePod1')

# Create an SSL context
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain('cert.pem', 'key.pem')

# Create the HTTPS server
with socketserver.TCPServer(("0.0.0.0", 8088), MyHTTPRequestHandler) as httpd:
    httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
    print(f"🔥 Ember HTTPS Server running on https://0.0.0.0:8088")
    print("Ready for Quest 3 connections!")
    httpd.serve_forever()