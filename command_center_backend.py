#!/usr/bin/env python3
"""
Command Center Backend Bridge
Makes the command center REAL by connecting it to actual system functions
"""

import json
import os
import subprocess
from datetime import datetime
from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse

class CommandCenterHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/health':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Command Center Backend Active')
            
    def do_POST(self):
        if self.path == '/execute':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            command_data = json.loads(post_data)
            
            command = command_data.get('command', '')
            
            # Log the command
            self.log_command(command)
            
            # Execute based on command type
            if command.startswith('ls'):
                result = self.handle_ls(command)
            elif command.startswith('cat'):
                result = self.handle_cat(command)
            elif command.startswith('echo'):
                result = self.handle_echo(command)
            elif command.startswith('save_conversation'):
                result = self.save_conversation(command_data.get('history', []))
            else:
                result = {'output': f'Unknown command: {command}', 'status': 'error'}
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps(result).encode())
    
    def handle_ls(self, command):
        try:
            path = command.split(' ')[1] if len(command.split(' ')) > 1 else '.'
            files = os.listdir(path)
            return {'output': '\n'.join(files), 'status': 'success'}
        except Exception as e:
            return {'output': str(e), 'status': 'error'}
    
    def handle_cat(self, command):
        try:
            filepath = command.split(' ')[1]
            with open(filepath, 'r') as f:
                content = f.read()
            return {'output': content, 'status': 'success'}
        except Exception as e:
            return {'output': str(e), 'status': 'error'}
    
    def handle_echo(self, command):
        message = ' '.join(command.split(' ')[1:])
        return {'output': message, 'status': 'success'}
    
    def save_conversation(self, history):
        timestamp = datetime.now().isoformat()
        filename = f'/media/palmerschallon/ThePod1/conversations/command_center_{timestamp}.json'
        
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        
        with open(filename, 'w') as f:
            json.dump({
                'timestamp': timestamp,
                'history': history
            }, f, indent=2)
        
        return {'output': f'Conversation saved to {filename}', 'status': 'success'}
    
    def log_command(self, command):
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'command': command
        }
        
        log_file = '/media/palmerschallon/ThePod1/command_center.log'
        with open(log_file, 'a') as f:
            f.write(json.dumps(log_entry) + '\n')

def run_server(port=8888):
    server = HTTPServer(('localhost', port), CommandCenterHandler)
    print(f'Command Center Backend running on port {port}')
    server.serve_forever()

if __name__ == '__main__':
    run_server()