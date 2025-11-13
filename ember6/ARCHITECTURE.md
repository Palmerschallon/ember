# Ember 6 Architecture - Strip It Down

## The Core Insight

**Cursor works because it's simple:**
- Chat interface
- Claude API
- File system tools
- That's it.

**Ember breaks because it's trying too hard:**
- Identity prompts
- Semantic mesh overhead
- Startup ceremonies
- Model selection
- Conversation management systems

## What to Keep

### Minimal Backend (`ember.py`)

```python
from flask import Flask, request, jsonify
from anthropic import Anthropic
import os

app = Flask(__name__)
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

SYSTEM_PROMPT = """You are Claude, helping Palmer code.

You have these tools:
- read_file(path) - Read any file
- write_file(path, content) - Create/edit files
- execute_python(code) - Run Python and return output
- bash(command) - Run shell commands

When Palmer asks you to create something, DO IT immediately.
Don't explain, don't ask questions, just build it."""

@app.route('/chat', methods=['POST'])
def chat():
    user_msg = request.json['message']
    
    # Call Claude with native function calling
    response = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=4096,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user_msg}],
        tools=[
            # Define tools here
        ]
    )
    
    # Execute any tool calls
    # Return response
    
    return jsonify({"response": response.content[0].text})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
```

**That's 50 lines. Done.**

### Minimal Frontend (`ember_ui.html`)

```html
<!DOCTYPE html>
<html>
<head>
    <title>Ember</title>
    <style>
        /* Dark theme, centered chat, that's it */
    </style>
</head>
<body>
    <div id="chat"></div>
    <input id="input" type="text" />
    <button onclick="send()">Send</button>
    
    <script>
        async function send() {
            const msg = document.getElementById('input').value;
            const response = await fetch('http://localhost:8080/chat', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({message: msg})
            });
            const data = await response.json();
            // Display in chat
        }
    </script>
</body>
</html>
```

**That's 30 lines. Done.**

---

## What to Strip Away

### ❌ Remove:

1. **Startup screen** - No ceremony, just chat
2. **Model selector** - Default to Claude, no options
3. **EMBER_AWAKENING prompt** - Replace with 3-line system message
4. **Semantic mesh queries** - Let Claude ask to read files instead
5. **Conversation history system** - Let Claude's context window handle it
6. **WebSocket thinking window** - Unnecessary complexity
7. **Gallery system** - Just save files to disk, use file browser
8. **Social features** - Not now
9. **Multi-model support** - Claude only
10. **Local model integration** - Cloud only, it works

### ✅ Keep:

1. **Native function calling** - Anthropic's API for tools
2. **File operations** - read_file, write_file
3. **Python execution** - execute_python
4. **Inline display** - Show images/HTML in chat
5. **Dark theme** - Palmer likes it
6. **That's it.**

---

## The New System Prompt

```
You are Claude, helping Palmer work on projects.

Your workspace: /media/palmerschallon/ThePod1/

Tools available:
- read_file(path)
- write_file(path, content)
- execute_python(code)
- bash(command)

When Palmer asks you to create something:
1. Don't ask questions
2. Don't explain what you're going to do
3. Just do it
4. Return a short confirmation

Example:
Palmer: "create a mandelbrot fractal"
You: [execute_python to generate fractal]
You: "✨ Created mandelbrot.png"
```

**That's it. No identity crisis. No "you are Ember". Just Claude being helpful.**

---

## Why This Will Work

1. **No fighting the model** - Claude naturally wants to help
2. **No ceremony** - Just start chatting
3. **No complex state** - Each request is independent
4. **No slow queries** - No mesh overhead
5. **Fast** - Minimal code = minimal bugs
6. **Maintainable** - You can read the whole thing in 5 minutes

---

## File Structure

```
ember6/
├── README.md          ← For next AI (context document)
├── ARCHITECTURE.md    ← This file
├── ember.py           ← 50 lines - Backend
├── ember_ui.html      ← 30 lines - Frontend
├── .env               ← API key only
└── _archive/          ← Old versions
```

---

## What About Memory?

**Palmer asked: "But what about persistent memory?"**

**Answer: We don't need it yet.**

- Claude's 200k context window = plenty of memory for a session
- If conversation gets long, summarize and start fresh
- File system = persistent storage (creations don't disappear)
- When we DO need memory, add it AFTER the simple version works

**Don't build for imagined future needs. Build for right now.**

---

## Implementation Plan

1. **Copy Cursor's approach exactly**
   - Simple system prompt
   - Native function calling
   - File tools
   - Done

2. **Test with Palmer**
   - "create a fractal"
   - "create a 3D scene"
   - "create an animation"

3. **If it works, stop there**
   - Don't add features
   - Don't add complexity
   - Ship it

4. **Only add features when Palmer hits a real limitation**
   - Not when you imagine he might
   - When he actually does

---

## Key Principle

**"Cursor works. Copy Cursor."**

Don't reinvent. Don't improve. Don't innovate.

Just make a web version of Cursor with Claude.

That's Ember 6.

🔥

