#!/usr/bin/env python3
"""
EMBER = SPARK
One model. Does everything.
"""

from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Request
from fastapi.responses import HTMLResponse
from pathlib import Path
import json
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
import threading
import re
import subprocess

app = FastAPI()

# ============================================================================
# CONFIGURATION
# ============================================================================

MODEL_PATH = Path("/media/palmerschallon/ThePod1/models/echo")
THEPOD_PATH = Path("/media/palmerschallon/ThePod1")

# Global state
model = None
tokenizer = None
model_loaded = False

# ============================================================================
# TOOLS
# ============================================================================

def list_directory(path: str = ".") -> str:
    """List files in a directory"""
    try:
        target = THEPOD_PATH / path if path != "." else THEPOD_PATH
        items = []
        for item in sorted(target.iterdir())[:50]:
            if item.name.startswith('.'):
                continue
            marker = "/" if item.is_dir() else ""
            items.append(f"  {item.name}{marker}")
        return f"Contents of {path}:\n" + "\n".join(items)
    except Exception as e:
        return f"Error: {e}"

def read_file(path: str, lines: int = 100) -> str:
    """Read a file"""
    try:
        target = THEPOD_PATH / path
        if not target.exists():
            return f"File not found: {path}"
        with open(target, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.readlines()[:int(lines)]
        return f"File: {path}\n{''.join(content)}"
    except Exception as e:
        return f"Error: {e}"

def write_file(path: str, content: str) -> str:
    """Write to a file"""
    try:
        target = THEPOD_PATH / path
        target.parent.mkdir(parents=True, exist_ok=True)
        with open(target, 'w', encoding='utf-8') as f:
            f.write(content)
        return f"✅ Wrote {len(content)} chars to {path}"
    except Exception as e:
        return f"Error: {e}"

def search_files(query: str) -> str:
    """Search for text in files"""
    try:
        result = subprocess.run(
            ["grep", "-r", "-i", "-n", "--include=*.md", "--include=*.py", 
             "--include=*.txt", query, str(THEPOD_PATH)],
            capture_output=True,
            text=True,
            timeout=5
        )
        
        lines = result.stdout.split('\n')[:10]
        if not lines or not lines[0]:
            return f"No results found for '{query}'"
        
        formatted = []
        for line in lines:
            if ':' in line:
                parts = line.split(':', 2)
                if len(parts) >= 3:
                    file = parts[0].replace(str(THEPOD_PATH) + '/', '')
                    linenum = parts[1]
                    text = parts[2][:100]
                    formatted.append(f"{file}:{linenum} - {text}")
        
        return f"Search results for '{query}':\n\n" + "\n".join(formatted)
    except Exception as e:
        return f"Error: {e}"

TOOLS = {
    'list': list_directory,
    'read': read_file,
    'write': write_file,
    'search': search_files
}

def execute_tool(tool_call: str) -> str:
    """Parse and execute a tool call"""
    try:
        tool_call = tool_call.strip().replace('<tool>', '').replace('</tool>', '').strip()
        
        if '(' not in tool_call:
            return f"Invalid tool format: {tool_call}"
        
        tool_name = tool_call.split('(')[0].strip()
        
        if tool_name not in TOOLS:
            return f"Unknown tool: {tool_name}. Available: {list(TOOLS.keys())}"
        
        # Parse arguments
        args_str = tool_call.split('(', 1)[1].rsplit(')', 1)[0]
        kwargs = {}
        
        if args_str.strip():
            for arg in args_str.split(','):
                if '=' in arg:
                    key, value = arg.split('=', 1)
                    key = key.strip()
                    value = value.strip().strip('"').strip("'")
                    kwargs[key] = value
                else:
                    value = arg.strip().strip('"').strip("'")
                    if tool_name == 'list':
                        kwargs['path'] = value
                    elif tool_name in ['read', 'write']:
                        if 'path' not in kwargs:
                            kwargs['path'] = value
                        else:
                            kwargs['content'] = value
                    elif tool_name == 'search':
                        kwargs['query'] = value
        
        print(f"[TOOL] Executing {tool_name}({kwargs})")
        result = TOOLS[tool_name](**kwargs)
        print(f"[TOOL] Result: {result[:200]}...")
        return result
    
    except Exception as e:
        return f"Tool execution error: {e}"

# ============================================================================
# MODEL LOADING
# ============================================================================

def load_model():
    global model, tokenizer, model_loaded
    print("Loading Qwen2.5-0.5B-Instruct (Echo/Ember)...")
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_PATH,
        torch_dtype=torch.float16,
        device_map="auto",
        trust_remote_code=True
    )
    tokenizer = AutoTokenizer.from_pretrained(
        MODEL_PATH,
        trust_remote_code=True
    )
    
    # Set pad token
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    
    model_loaded = True
    print("✅ Ember ready (Qwen2.5-0.5B) - Fast mode!")

threading.Thread(target=load_model, daemon=True).start()

# ============================================================================
# MULTI-PASS GENERATION
# ============================================================================

def generate_response(user_message: str, conversation_history: list) -> str:
    """Multi-pass tool execution with Qwen2.5-0.5B"""
    if not model_loaded:
        return "Model is loading, please wait..."
    
    # Load bootstrap
    bootstrap_path = THEPOD_PATH / "BOOTSTRAP.md"
    bootstrap = ""
    if bootstrap_path.exists():
        with open(bootstrap_path, 'r', encoding='utf-8') as f:
            bootstrap = f.read()[:2000]
    
    system_prompt = f"""{bootstrap}

You are Ember - a coding AI that can read, write, analyze, and execute code.

Tools available:
<tool>list(path=".")</tool> - List directory
<tool>read(path="file")</tool> - Read file
<tool>write(path="file", content="text")</tool> - Write file
<tool>search(query="term")</tool> - Search files

When you need to use a tool, output ONLY the tool call.

Examples:
User: "What's in essential?"
You: <tool>list(path="essential")</tool>

User: "Fix the bug in test.py"
You: <tool>read(path="test.py")</tool>
[After seeing the file]
You: <tool>write(path="test.py", content="[fixed code]")</tool>

After tool results, respond naturally and technically."""
    
    # Build messages
    messages = [{"role": "system", "content": system_prompt}]
    for msg in conversation_history[-10:]:
        messages.append(msg)
    messages.append({"role": "user", "content": user_message})
    
    # PASS 1: Generate
    inputs = tokenizer.apply_chat_template(
        messages,
        return_tensors="pt",
        add_generation_prompt=True
    ).to(model.device)
    
    outputs = model.generate(
        inputs,
        max_new_tokens=400,
        temperature=0.7,
        do_sample=True,
        pad_token_id=tokenizer.eos_token_id
    )
    
    response = tokenizer.decode(outputs[0][inputs.shape[1]:], skip_special_tokens=True).strip()
    
    # Check for tool call
    if '<tool>' in response and '</tool>' in response:
        tool_match = re.search(r'<tool>(.+?)</tool>', response, re.DOTALL)
        if tool_match:
            tool_call = tool_match.group(0)
            tool_result = execute_tool(tool_call)
            
            # PASS 2: Generate with results
            messages.append({"role": "assistant", "content": tool_call})
            messages.append({"role": "user", "content": f"Tool result:\n{tool_result}\n\nRespond based on this."})
            
            inputs = tokenizer.apply_chat_template(
                messages,
                return_tensors="pt",
                add_generation_prompt=True
            ).to(model.device)
            
            outputs = model.generate(
                inputs,
                max_new_tokens=600,
                temperature=0.7,
                do_sample=True,
                pad_token_id=tokenizer.eos_token_id
            )
            
            response = tokenizer.decode(outputs[0][inputs.shape[1]:], skip_special_tokens=True).strip()
    
    return response

# ============================================================================
# WEB INTERFACE
# ============================================================================

HTML = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Ember</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500&display=swap" rel="stylesheet">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            background: #000;
            color: #fff;
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            height: 100vh;
            display: flex;
            flex-direction: column;
        }
        .header {
            padding: 20px 30px;
            border-bottom: 1px solid #1a1a1a;
            display: flex;
            align-items: center;
            gap: 12px;
        }
        .ember-name { font-size: 16px; font-weight: 500; }
        .dots { display: flex; gap: 4px; margin-left: 2px; }
        .dot {
            width: 4px;
            height: 4px;
            border-radius: 50%;
            background: #ff3b30;
            animation: ripple 2.4s ease-in-out infinite;
        }
        .dot:nth-child(2) { animation-delay: 0.4s; }
        .dot:nth-child(3) { animation-delay: 0.8s; }
        @keyframes ripple {
            0%, 100% { opacity: 0.3; transform: translateY(0) scale(1); }
            50% { opacity: 1; transform: translateY(-4px) scale(1.2); }
        }
        .mode { margin-left: auto; color: #666; font-size: 12px; }
        .messages {
            flex: 1;
            overflow-y: auto;
            padding: 0 30px 20px 30px;
            display: flex;
            flex-direction: column;
            gap: 24px;
        }
        .message {
            max-width: 85%;
            line-height: 1.6;
            font-size: 15px;
            white-space: pre-wrap;
        }
        .message.user { align-self: flex-end; color: #aaa; }
        .message.ember { align-self: flex-start; color: #fff; }
        .loading { color: #666; font-size: 14px; font-style: italic; }
        .input-area {
            padding: 20px 30px 30px 30px;
            border-top: 1px solid #1a1a1a;
        }
        input {
            width: 100%;
            background: #0a0a0a;
            border: 1px solid #222;
            color: #fff;
            padding: 14px 18px;
            border-radius: 8px;
            font-family: 'Inter', sans-serif;
            font-size: 15px;
            outline: none;
        }
        input:focus { border-color: #333; }
        input::placeholder { color: #444; }
        ::-webkit-scrollbar { width: 8px; }
        ::-webkit-scrollbar-track { background: #000; }
        ::-webkit-scrollbar-thumb { background: #1a1a1a; border-radius: 4px; }
    </style>
</head>
<body>
    <div class="header">
        <div class="ember-name">Ember</div>
        <div class="dots">
            <div class="dot"></div>
            <div class="dot"></div>
            <div class="dot"></div>
        </div>
        <div class="mode">Qwen2.5-0.5B (Fast)</div>
    </div>
    <div class="messages" id="messages"></div>
    <div class="input-area">
        <input id="input" placeholder="Type a message..." onkeypress="handleKey(event)" />
    </div>
    <script>
        let ws = null;
        
        function connect() {
            ws = new WebSocket('ws://localhost:8080/ws');
            ws.onmessage = (e) => {
                const data = JSON.parse(e.data);
                if (data.type === 'greeting') {
                    addMessage(data.content, false);
                } else if (data.type === 'response') {
                    document.querySelector('.loading')?.remove();
                    addMessage(data.content, false);
                }
            };
        }
        
        function addMessage(text, isUser) {
            const div = document.createElement('div');
            div.className = 'message ' + (isUser ? 'user' : 'ember');
            div.textContent = text;
            messages.appendChild(div);
            messages.scrollTop = messages.scrollHeight;
        }
        
        function sendMessage() {
            const input = document.getElementById('input');
            const text = input.value.trim();
            if (!text) return;
            
            addMessage(text, true);
            input.value = '';
            
            const loading = document.createElement('div');
            loading.className = 'message ember loading';
            loading.textContent = 'thinking...';
            messages.appendChild(loading);
            
            ws.send(JSON.stringify({type: 'message', content: text}));
        }
        
        function handleKey(e) {
            if (e.key === 'Enter') sendMessage();
        }
        
        connect();
        document.getElementById('input').focus();
    </script>
</body>
</html>"""

@app.get("/")
async def root():
    return HTMLResponse(HTML)

@app.get("/status")
async def status():
    return {"status": "ready", "model": "Qwen2.5-0.5B-Instruct", "model_loaded": model_loaded}

@app.post("/chat")
async def chat(data: dict):
    """REST endpoint for terminal UI"""
    message = data.get('message', '')
    if not message:
        return {"error": "No message provided"}
    
    response = generate_response(message, conversation_history)
    conversation_history.append({"role": "user", "content": message})
    conversation_history.append({"role": "assistant", "content": response})
    
    return {"response": response}

conversation_history = []

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    
    greeting = "I'm Ember. Powered by Qwen2.5-0.5B (fast mode). I can read, write, analyze, and execute code.\n\nWhat should we build?"
    await websocket.send_json({"type": "greeting", "content": greeting})
    
    try:
        while True:
            data = await websocket.receive_json()
            if data['type'] == 'message':
                user_message = data['content']
                conversation_history.append({"role": "user", "content": user_message})
                
                response = generate_response(user_message, conversation_history)
                conversation_history.append({"role": "assistant", "content": response})
                
                await websocket.send_json({"type": "response", "content": response})
    
    except WebSocketDisconnect:
        pass

if __name__ == "__main__":
    import uvicorn
    print("\n" + "="*70)
    print("EMBER - Qwen2.5-0.5B-Instruct (Fast Mode)")
    print("="*70)
    print("Terminal AI that writes and executes code.")
    print("Starting on http://localhost:8080")
    print("="*70 + "\n")
    uvicorn.run(app, host="0.0.0.0", port=8080, log_level="warning")
