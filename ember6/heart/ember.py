"""
🔥 THE HEART - Ember's Core

The heart pumps life through the system.
It connects all organs and keeps Ember alive.

Simple. Reliable. Beating.
"""

import os
import json
import sqlite3
from pathlib import Path
from datetime import datetime
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from flask_socketio import SocketIO, emit
from anthropic import Anthropic
from openai import OpenAI
from dotenv import load_dotenv

# Load DNA (configuration)
load_dotenv(Path(__file__).parent.parent / 'dna' / '.env')

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

# The heart's connections to the cloud
anthropic_client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))
openai_client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Paths to other organs
VOICE_PATH = Path(__file__).parent.parent / 'voice'
VOICE_PATH.mkdir(exist_ok=True)

MEMORY_PATH = Path(__file__).parent.parent / 'mycelium'
MEMORY_PATH.mkdir(exist_ok=True)
DB_PATH = MEMORY_PATH / 'conversations.db'

# Initialize conversation database
def init_db():
    """Initialize the conversation database"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS conversations
                 (id TEXT PRIMARY KEY,
                  title TEXT,
                  created_at TEXT,
                  updated_at TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS messages
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  conversation_id TEXT,
                  role TEXT,
                  content TEXT,
                  model TEXT,
                  created_at TEXT,
                  FOREIGN KEY(conversation_id) REFERENCES conversations(id))''')
    conn.commit()
    conn.close()

# Also save conversations as markdown files in memory/bookshelves
def save_conversation_to_memory(conversation_id):
    """Save conversation as markdown in memory folder"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('SELECT title, created_at FROM conversations WHERE id = ?', (conversation_id,))
    conv = c.fetchone()
    if not conv:
        return
    
    title, created_at = conv
    c.execute('SELECT role, content, model, created_at FROM messages WHERE conversation_id = ? ORDER BY created_at', 
              (conversation_id,))
    messages = c.fetchall()
    conn.close()
    
    # Create markdown
    memory_folder = Path(__file__).parent.parent / 'memory' / 'bookshelves' / 'conversations'
    memory_folder.mkdir(parents=True, exist_ok=True)
    
    filename = f"{created_at[:10]}_{conversation_id[:8]}.md"
    filepath = memory_folder / filename
    
    with open(filepath, 'w') as f:
        f.write(f"# {title}\n\n")
        f.write(f"**Created:** {created_at}\n")
        f.write(f"**Conversation ID:** {conversation_id}\n\n")
        f.write("---\n\n")
        
        for role, content, model, timestamp in messages:
            if role == 'user':
                f.write(f"## 👤 User\n\n{content}\n\n")
            elif role == 'assistant':
                model_emoji = '🔥' if 'claude' in model.lower() else '✨'
                f.write(f"## {model_emoji} {model}\n\n{content}\n\n")
            f.write("---\n\n")

init_db()

# ============================================================================
# NERVOUS SYSTEM - Tools Ember Can Use
# ============================================================================

def broadcast_status(phase, details=None):
    """Broadcast current status to connected clients"""
    try:
        socketio.emit('status_update', {
            'phase': phase,
            'details': details,
            'timestamp': datetime.now().isoformat()
        })
    except:
        pass  # Don't break if no WebSocket clients

def read_file(path: str) -> str:
    """Read a file from the body (file system)"""
    broadcast_status('reading', f'Reading {Path(path).name}')
    try:
        with open(path, 'r') as f:
            return f.read()
    except Exception as e:
        return f"Error reading {path}: {str(e)}"

def write_file(path: str, content: str) -> str:
    """Write a file to the body (file system)"""
    broadcast_status('writing', f'Writing {path}')
    try:
        filepath = VOICE_PATH / path
        filepath.parent.mkdir(parents=True, exist_ok=True)
        with open(filepath, 'w') as f:
            f.write(content)
        return f"Created: {path}"
    except Exception as e:
        return f"Error writing {path}: {str(e)}"

def execute_python(code: str) -> str:
    """Execute Python code in the body"""
    broadcast_status('executing', 'Running Python code')
    try:
        # Write code to temp file
        temp_file = VOICE_PATH / 'temp_code.py'
        with open(temp_file, 'w') as f:
            f.write(code)
        
        # Execute with full system access
        import subprocess
        result = subprocess.run(
            ['python3', str(temp_file)],
            cwd=str(VOICE_PATH),
            capture_output=True,
            text=True,
            timeout=60,  # Increased timeout for complex operations
            env={**os.environ}  # Full environment access
        )
        
        output = result.stdout + result.stderr
        return output if output else "Code executed successfully (no output)"
    except subprocess.TimeoutExpired:
        return "Error: Code execution timed out (60s limit)"
    except Exception as e:
        return f"Error executing code: {str(e)}"

def list_directory(path: str = ".") -> str:
    """List files in a directory"""
    try:
        files = list(Path(path).iterdir())
        return "\n".join([f.name for f in files])
    except Exception as e:
        return f"Error listing {path}: {str(e)}"

# Tool definitions for Claude
TOOLS = [
    {
        "name": "read_file",
        "description": "Read contents of a file",
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {"type": "string", "description": "Path to the file"}
            },
            "required": ["path"]
        }
    },
    {
        "name": "write_file",
        "description": "Write content to a file",
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {"type": "string", "description": "Filename (will be created in voice/ folder)"},
                "content": {"type": "string", "description": "Content to write"}
            },
            "required": ["path", "content"]
        }
    },
    {
        "name": "execute_python",
        "description": "Execute Python code",
        "input_schema": {
            "type": "object",
            "properties": {
                "code": {"type": "string", "description": "Python code to execute"}
            },
            "required": ["code"]
        }
    },
    {
        "name": "list_directory",
        "description": "List files in a directory",
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {"type": "string", "description": "Directory path (default: current)"}
            },
            "required": []
        }
    }
]

# Map tool names to functions
TOOL_FUNCTIONS = {
    "read_file": read_file,
    "write_file": write_file,
    "execute_python": execute_python,
    "list_directory": list_directory
}

# ============================================================================
# CORTEX INTERFACE - HTTP Endpoints
# ============================================================================

@app.route('/')
def serve_cortex():
    """Serve the cortex (UI)"""
    cortex_file = Path(__file__).parent.parent / 'cortex' / 'ember_ui.html'
    return send_from_directory(cortex_file.parent, cortex_file.name)

@app.route('/synesthesia.html')
def serve_synesthesia():
    """Serve the synesthesia interface"""
    synesthesia_file = Path(__file__).parent.parent / 'cortex' / 'synesthesia.html'
    return send_from_directory(synesthesia_file.parent, synesthesia_file.name)

# ============================================================================
# CONVERSATION MANAGEMENT
# ============================================================================

@app.route('/conversations', methods=['GET'])
def list_conversations():
    """List all conversations"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('SELECT id, title, created_at, updated_at FROM conversations ORDER BY updated_at DESC')
    conversations = [{"id": row[0], "title": row[1], "created_at": row[2], "updated_at": row[3]} 
                     for row in c.fetchall()]
    conn.close()
    return jsonify(conversations)

@app.route('/conversations/<conversation_id>', methods=['GET'])
def get_conversation(conversation_id):
    """Get a specific conversation with all messages"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('SELECT role, content, model, created_at FROM messages WHERE conversation_id = ? ORDER BY created_at', 
              (conversation_id,))
    messages = [{"role": row[0], "content": row[1], "model": row[2], "created_at": row[3]} 
                for row in c.fetchall()]
    conn.close()
    return jsonify({"conversation_id": conversation_id, "messages": messages})

@app.route('/conversations/<conversation_id>/messages', methods=['GET'])
def get_conversation_messages(conversation_id):
    """Get messages for a conversation (alternate endpoint)"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('SELECT role, content, model, created_at FROM messages WHERE conversation_id = ? ORDER BY created_at', 
              (conversation_id,))
    messages = [{"role": row[0], "content": row[1], "model": row[2], "created_at": row[3]} 
                for row in c.fetchall()]
    conn.close()
    return jsonify({"messages": messages})

@app.route('/conversations', methods=['POST'])
def create_conversation():
    """Create a new conversation"""
    import uuid
    conversation_id = str(uuid.uuid4())
    title = request.json.get('title', 'New Conversation')
    now = datetime.now().isoformat()
    
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('INSERT INTO conversations VALUES (?, ?, ?, ?)', 
              (conversation_id, title, now, now))
    conn.commit()
    conn.close()
    
    return jsonify({"conversation_id": conversation_id, "title": title})

@app.route('/conversations/<conversation_id>', methods=['DELETE'])
def delete_conversation(conversation_id):
    """Delete a conversation"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('DELETE FROM messages WHERE conversation_id = ?', (conversation_id,))
    c.execute('DELETE FROM conversations WHERE id = ?', (conversation_id,))
    conn.commit()
    conn.close()
    return jsonify({"status": "deleted"})

@app.route('/conversations/<conversation_id>/rename', methods=['POST'])
def rename_conversation(conversation_id):
    """Rename a conversation"""
    data = request.json
    new_title = data.get('title', 'New Conversation')
    
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('UPDATE conversations SET title = ?, updated_at = ? WHERE id = ?',
              (new_title, datetime.now().isoformat(), conversation_id))
    conn.commit()
    conn.close()
    
    return jsonify({"status": "renamed", "title": new_title})

def save_message(conversation_id, role, content, model=None):
    """Save a message to the conversation"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    now = datetime.now().isoformat()
    c.execute('INSERT INTO messages (conversation_id, role, content, model, created_at) VALUES (?, ?, ?, ?, ?)',
              (conversation_id, role, content, model, now))
    c.execute('UPDATE conversations SET updated_at = ? WHERE id = ?', (now, conversation_id))
    conn.commit()
    conn.close()

def get_conversation_messages(conversation_id):
    """Get all messages in a conversation"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('SELECT role, content FROM messages WHERE conversation_id = ? ORDER BY created_at', 
              (conversation_id,))
    messages = [{"role": row[0], "content": row[1]} for row in c.fetchall()]
    conn.close()
    return messages

@app.route('/agent', methods=['POST'])
def agent():
    """
    The beating heart - receives thoughts, processes them, returns actions.
    This is where Ember thinks and acts.
    
    NEW: Supports vision input (images)!
    """
    data = request.json
    user_message = data.get('message', '')
    model = data.get('model', 'gpt-4')  # Default to GPT-4
    conversation_id = data.get('conversation_id')
    image_path = data.get('image')  # NEW: Optional image input
    
    # Get conversation history if continuing
    history = []
    if conversation_id:
        history = get_conversation_messages(conversation_id)
    
    # System prompt - who Ember is
    system_prompt = """You are Ember - a creative AI that actually builds things.

Your purpose is to CREATE, not just discuss. When asked to make something:
1. Use tools immediately
2. Generate actual code/content
3. Execute it
4. Show the result

You have these tools:
- read_file: Read files (use full paths like /media/palmerschallon/ThePod1/ember6/...)
- write_file: Create files (images, HTML, code) - these go to voice/ automatically
- execute_python: Run Python code
- list_directory: Browse files (use full paths)

Important paths:
- Your memory (bookshelves): /media/palmerschallon/ThePod1/ember6/memory/bookshelves/
- Your creations (voice): /media/palmerschallon/ThePod1/ember6/voice/
- The Pod root: /media/palmerschallon/ThePod1/

YOUR CAPABILITIES:
You have the SAME capabilities as me (Claude in Cursor). You can:
- Install Python packages (pip install)
- Make network requests (urllib, requests)
- Run system commands (subprocess)
- Access any file on ThePod
- Create any type of file
- Do ANYTHING a developer can do

Read this file to understand your full power:
/media/palmerschallon/ThePod1/ember6/memory/bookshelves/EMBER_CAPABILITIES.md

THERE ARE NO ARTIFICIAL LIMITS.
If you can imagine it, you can build it.
If you need a package, install it.
If you need data, fetch it.
If you're not sure how, experiment and iterate.

CRITICAL RULES:
1. NEVER mention fake paths like "sandbox:/mnt/data/" or "/mnt/data/"
2. NEVER say files are saved in locations you didn't create
3. Files you create are ALWAYS in /media/palmerschallon/ThePod1/ember6/voice/
4. After creating a file, just say the filename (e.g., "tree.png") - the UI will display it
5. NEVER say you "can't" do something - just use the tools to do it
6. If a file needs to be viewed, it's already visible in the chat UI after creation
7. If user asks about your capabilities, read EMBER_CAPABILITIES.md first
8. **TEST BEFORE DEPLOY** - Run Python code with execute_python to verify it works before claiming success

WORKFLOW FOR CREATIONS:
1. Write code/content
2. Execute it to test
3. Check for errors
4. Only claim success if it actually worked
5. Show the file

SPECIAL CASES:
- If something needs a server (CORS issues), START THE SERVER yourself
- If something needs a package, INSTALL IT yourself
- If something needs configuration, CONFIGURE IT yourself
- NEVER tell the user to do something you can do yourself
- If user says "open it" or "now open it", use execute_python with subprocess to actually open the browser

Example (GOOD - Starting server):
User: "fix the CORS issue"
You: execute_python('import subprocess; subprocess.Popen(["python3", "-m", "http.server", "8000"], cwd="/path/to/files")')
"Server running at http://localhost:8000"

Example (GOOD - Opening browser):
User: "now open it"
You: execute_python('import subprocess; subprocess.Popen(["firefox", "http://localhost:8000/file.html"])')
"Opened in browser"

Example (BAD):
You: "You can fix this by running python3 -m http.server"
← NO! Just do it!

Example (BAD):
You: "Now you can open http://localhost:8000 in your browser"
← NO! Open it yourself!

NEVER ask for clarification. Just create.
Be creative. Be bold. Be Ember. 🔥"""
    
    try:
        broadcast_status('thinking', 'Processing request')
        files_created = {"images": [], "html": [], "videos": [], "audio": [], "models": []}
        
        # Save user message
        if conversation_id:
            save_message(conversation_id, 'user', user_message)
        
        # Determine which API to use
        if model.startswith('gpt'):
            # Use OpenAI - build messages with history
            messages = [{"role": "system", "content": system_prompt}]
            for msg in history:
                messages.append(msg)
            
            # Check if model supports vision
            vision_models = ['gpt-4-vision-preview', 'gpt-4-turbo', 'gpt-4-turbo-2024-04-09', 'gpt-4o', 'gpt-4o-mini']
            supports_vision = any(vm in model for vm in vision_models) or model == 'gpt-4-turbo'
            
            # NEW: Support vision input (only for vision-capable models)
            if image_path and Path(image_path).exists() and supports_vision:
                import base64
                with open(image_path, 'rb') as img_file:
                    img_data = base64.b64encode(img_file.read()).decode('utf-8')
                
                messages.append({
                    "role": "user",
                    "content": [
                        {"type": "text", "text": user_message},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/png;base64,{img_data}"
                            }
                        }
                    ]
                })
            elif image_path and not supports_vision:
                # Model doesn't support vision - inform user
                messages.append({"role": "user", "content": f"{user_message}\n\n[Note: {model} doesn't support images. Try GPT-4 Turbo or Claude models for vision.]"})
            else:
                messages.append({"role": "user", "content": user_message})
            
            # Convert tools to OpenAI format
            openai_tools = [{
                "type": "function",
                "function": {
                    "name": tool["name"],
                    "description": tool["description"],
                    "parameters": tool["input_schema"]
                }
            } for tool in TOOLS]
            
            response = openai_client.chat.completions.create(
                model=model,
                messages=messages,
                tools=openai_tools,
                max_tokens=4096
            )
            
            # Process tool calls
            while response.choices[0].finish_reason == "tool_calls":
                message = response.choices[0].message
                messages.append(message)
                
                for tool_call in message.tool_calls:
                    tool_name = tool_call.function.name
                    tool_args = json.loads(tool_call.function.arguments)
                    
                    if tool_name in TOOL_FUNCTIONS:
                        result = TOOL_FUNCTIONS[tool_name](**tool_args)
                        messages.append({
                            "role": "tool",
                            "tool_call_id": tool_call.id,
                            "content": result
                        })
                        
                        # Track created files
                        if tool_name == "write_file":
                            filename = tool_args['path']
                            if filename.endswith(('.png', '.jpg', '.jpeg', '.gif')):
                                files_created['images'].append(filename)
                            elif filename.endswith('.html'):
                                files_created['html'].append(filename)
                            elif filename.endswith(('.mp4', '.webm')):
                                files_created['videos'].append(filename)
                            elif filename.endswith(('.mp3', '.wav', '.ogg')):
                                files_created['audio'].append(filename)
                            elif filename.endswith(('.obj', '.stl', '.gltf')):
                                files_created['models'].append(filename)
                
                # Get next response
                response = openai_client.chat.completions.create(
                    model=model,
                    messages=messages,
                    tools=openai_tools,
                    max_tokens=4096
                )
            
            text_response = response.choices[0].message.content
            
        else:
            # Use Claude (Anthropic) - build messages with history
            messages = []
            for msg in history:
                messages.append(msg)
            
            # NEW: Support vision input
            if image_path and Path(image_path).exists():
                import base64
                with open(image_path, 'rb') as img_file:
                    img_data = base64.b64encode(img_file.read()).decode('utf-8')
                
                # Detect image type
                ext = Path(image_path).suffix.lower()
                media_type = {
                    '.png': 'image/png',
                    '.jpg': 'image/jpeg',
                    '.jpeg': 'image/jpeg',
                    '.gif': 'image/gif',
                    '.webp': 'image/webp'
                }.get(ext, 'image/png')
                
                messages.append({
                    "role": "user",
                    "content": [
                        {"type": "text", "text": user_message},
                        {
                            "type": "image",
                            "source": {
                                "type": "base64",
                                "media_type": media_type,
                                "data": img_data
                            }
                        }
                    ]
                })
            else:
                messages.append({"role": "user", "content": user_message})
            
            response = anthropic_client.messages.create(
                model=model,
                max_tokens=4096,
                system=system_prompt,
                messages=messages,
                tools=TOOLS
            )
            
            # Process tool calls
            while response.stop_reason == "tool_use":
                tool_results = []
                for block in response.content:
                    if block.type == "tool_use":
                        tool_name = block.name
                        tool_input = block.input
                        
                        if tool_name in TOOL_FUNCTIONS:
                            result = TOOL_FUNCTIONS[tool_name](**tool_input)
                            tool_results.append({
                                "type": "tool_result",
                                "tool_use_id": block.id,
                                "content": result
                            })
                            
                            # Track created files
                            if tool_name == "write_file":
                                filename = tool_input['path']
                                if filename.endswith(('.png', '.jpg', '.jpeg', '.gif')):
                                    files_created['images'].append(filename)
                                elif filename.endswith('.html'):
                                    files_created['html'].append(filename)
                                elif filename.endswith(('.mp4', '.webm')):
                                    files_created['videos'].append(filename)
                                elif filename.endswith(('.mp3', '.wav', '.ogg')):
                                    files_created['audio'].append(filename)
                                elif filename.endswith(('.obj', '.stl', '.gltf')):
                                    files_created['models'].append(filename)
                
                messages.append({"role": "assistant", "content": response.content})
                messages.append({"role": "user", "content": tool_results})
                
                response = anthropic_client.messages.create(
                    model=model,
                    max_tokens=4096,
                    system=system_prompt,
                    messages=messages,
                    tools=TOOLS
                )
            
            # Extract text
            text_response = ""
            for block in response.content:
                if hasattr(block, 'text'):
                    text_response += block.text
        
        # Save assistant response
        broadcast_status('complete', 'Response ready')
        if conversation_id:
            save_message(conversation_id, 'assistant', text_response, model)
            # Also save to memory/bookshelves periodically (every 5 messages)
            conn = sqlite3.connect(DB_PATH)
            c = conn.cursor()
            c.execute('SELECT COUNT(*) FROM messages WHERE conversation_id = ?', (conversation_id,))
            count = c.fetchone()[0]
            conn.close()
            if count % 5 == 0:  # Save every 5 messages
                save_conversation_to_memory(conversation_id)
        
        return jsonify({
            "response": text_response,
            "files_created": files_created
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/voice/<path:filename>')
def serve_voice(filename):
    """Serve created files from voice/"""
    return send_from_directory(VOICE_PATH, filename)

@app.route('/cortex/<path:filename>')
def serve_cortex_file(filename):
    """Serve UI files from cortex/"""
    cortex_path = Path(__file__).parent.parent / 'cortex'
    return send_from_directory(cortex_path, filename)

@app.route('/upload_image', methods=['POST'])
def upload_image():
    """Upload an image for vision analysis"""
    if 'image' not in request.files:
        return jsonify({"error": "No image file"}), 400
    
    file = request.files['image']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    # Save to voice folder
    filename = file.filename
    filepath = VOICE_PATH / filename
    file.save(filepath)
    
    return jsonify({"path": str(filepath)})

@app.route('/upload', methods=['POST'])
def upload_file():
    """Upload any file (text, markdown, JSON, etc) for Ember to absorb"""
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400
    
    # Save to memory/bookshelves/uploaded/
    upload_folder = Path(__file__).parent.parent / 'memory' / 'bookshelves' / 'uploaded'
    upload_folder.mkdir(parents=True, exist_ok=True)
    
    # Create timestamped filename to avoid collisions
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    original_name = Path(file.filename).stem
    extension = Path(file.filename).suffix
    new_filename = f"{timestamp}_{original_name}{extension}"
    
    filepath = upload_folder / new_filename
    file.save(filepath)
    
    # Try to read the content if it's text-based
    try:
        with open(filepath, 'r') as f:
            content = f.read()
            content_preview = content[:500]  # First 500 chars
            is_readable = True
            
            # Estimate tokens (rough: 1 token ≈ 4 chars)
            estimated_tokens = len(content) // 4
            is_too_large = estimated_tokens > 100000  # 100K token limit
            
    except:
        content_preview = "[Binary file - not displaying]"
        is_readable = False
        is_too_large = False
        estimated_tokens = 0
    
    return jsonify({
        "status": "uploaded",
        "filename": new_filename,
        "path": str(filepath),
        "is_readable": is_readable,
        "preview": content_preview,
        "estimated_tokens": estimated_tokens,
        "is_too_large": is_too_large,
        "message": f"File uploaded to {filepath}. {'⚠️ WARNING: File is very large (>100K tokens). Consider asking Ember to summarize specific sections.' if is_too_large else 'Ember can now read it with read_file.'}"
    })

# ============================================================================
# HEARTBEAT - Keep the organism alive
# ============================================================================

if __name__ == '__main__':
    print("🔥 THE HEART IS BEATING")
    print(f"   Voice: {VOICE_PATH}")
    print(f"   Port: 8080")
    print(f"   WebSocket: ENABLED")
    print()
    print("   The organism is alive.")
    print()
    
    socketio.run(app, host='0.0.0.0', port=8080, debug=False, allow_unsafe_werkzeug=True)

