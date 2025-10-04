"""
Ember Flask Backend
Main application with all API endpoints
"""
import os
import json
import time
from flask import Flask, render_template, request, jsonify, Response, stream_with_context
from werkzeug.utils import secure_filename
from dotenv import load_dotenv
from pathlib import Path

from backend.adapters.llm_adapter import get_llm_adapter
from backend.universe_factory import UniverseFactory
from backend.memory_logger import MemoryLogger

# Load environment variables
load_dotenv()

app = Flask(__name__, 
            template_folder='frontend',
            static_folder='frontend/static')

# Configuration
BASE_PATH = os.getenv('BASE_PATH', '/tmp/ember_data')
UPLOADS_PATH = os.path.join(BASE_PATH, 'uploads')
Path(UPLOADS_PATH).mkdir(parents=True, exist_ok=True)

# Initialize components
llm_adapter = get_llm_adapter()
memory_logger = MemoryLogger(BASE_PATH)

# Store active SSE clients
sse_clients = []


@app.route('/')
def index():
    """Serve the main viewer interface"""
    return render_template('index.html')


@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': time.time(),
        'base_path': BASE_PATH
    })


@app.route('/api/chat', methods=['POST'])
def chat():
    """
    Chat endpoint with LLM integration
    Logs conversations to memory
    """
    data = request.json
    user_message = data.get('message', '')
    
    if not user_message:
        return jsonify({'error': 'No message provided'}), 400
    
    # Get chat history if provided
    history = data.get('history', [])
    
    # Build messages for LLM
    messages = []
    for msg in history[-10:]:  # Last 10 messages for context
        messages.append({
            'role': msg.get('role', 'user'),
            'content': msg.get('content', '')
        })
    
    messages.append({
        'role': 'user',
        'content': user_message
    })
    
    # Get response from LLM
    response_text = llm_adapter.chat(messages)
    
    # Log the interaction
    memory_logger.log_chat(user_message, response_text)
    
    # Emit event
    emit_event('chat', {
        'user_message': user_message,
        'assistant_message': response_text
    })
    
    return jsonify({
        'response': response_text,
        'timestamp': time.time()
    })


@app.route('/api/upload', methods=['POST'])
def upload():
    """
    File upload endpoint
    Saves files to configured upload path
    """
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'Empty filename'}), 400
    
    filename = secure_filename(file.filename)
    filepath = os.path.join(UPLOADS_PATH, filename)
    file.save(filepath)
    
    # Log upload event
    memory_logger.log_event('upload', {
        'filename': filename,
        'size': os.path.getsize(filepath)
    })
    
    # Emit event
    emit_event('upload', {
        'filename': filename,
        'path': filepath
    })
    
    return jsonify({
        'success': True,
        'filename': filename,
        'path': filepath
    })


@app.route('/api/events')
def events():
    """
    Server-Sent Events endpoint
    Streams events to connected clients
    """
    def event_stream():
        # Send initial connection event
        yield f"data: {json.dumps({'type': 'connected', 'timestamp': time.time()})}\n\n"
        
        # Keep connection alive and send events
        while True:
            # In a real implementation, you'd use a queue or pub/sub
            # For now, send heartbeat every 30 seconds
            time.sleep(30)
            yield f"data: {json.dumps({'type': 'heartbeat', 'timestamp': time.time()})}\n\n"
    
    return Response(
        stream_with_context(event_stream()),
        mimetype='text/event-stream',
        headers={
            'Cache-Control': 'no-cache',
            'X-Accel-Buffering': 'no'
        }
    )


@app.route('/api/universe', methods=['GET'])
def get_universe():
    """
    Generate and return a universe
    Uses deterministic generation from seed
    """
    seed = request.args.get('seed', type=int, default=42)
    num_entities = request.args.get('entities', type=int, default=100)
    
    # Generate universe
    universe = UniverseFactory.from_seed(seed, num_entities)
    
    # Log event
    memory_logger.log_event('universe_generated', {
        'seed': seed,
        'num_entities': num_entities
    })
    
    # Emit event
    emit_event('universe_generated', {
        'seed': seed,
        'entities': len(universe['entities'])
    })
    
    return jsonify(universe)


def emit_event(event_type: str, data: dict):
    """Emit event to SSE clients and log it"""
    event_data = {
        'type': event_type,
        'data': data,
        'timestamp': time.time()
    }
    
    # Log to memory
    memory_logger.log_event(event_type, data)
    
    # In a real implementation, broadcast to SSE clients
    # For now, just log
    app.logger.info(f"Event: {event_type} - {data}")


if __name__ == '__main__':
    port = int(os.getenv('FLASK_PORT', 5000))
    host = os.getenv('FLASK_HOST', '0.0.0.0')
    debug = os.getenv('FLASK_ENV', 'production') == 'development'
    
    app.run(host=host, port=port, debug=debug)
