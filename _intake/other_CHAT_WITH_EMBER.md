# 💬 How to Chat with Ember

## The Issue
The hub.html interface needs to be accessed **through the Flask server**, not opened as a local file.

---

## ✅ Working Methods:

### 1. **Command Line (Simplest)**
```bash
curl -X POST http://localhost:7777/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"Hello Ember, how are you?"}'
```

### 2. **Python Script**
```python
import requests
import json

def chat_with_ember(message):
    response = requests.post(
        'http://localhost:7777/api/chat',
        json={'message': message},
        timeout=60
    )
    if response.ok:
        return response.json()['reply']
    return None

# Usage
reply = chat_with_ember("What are you thinking about?")
print(reply)
```

### 3. **Browser (if server serves static files)**
Navigate to: `http://localhost:7777/`

Or access API endpoints directly:
- Status: `http://localhost:7777/api/status`
- Dreams: `http://localhost:7777/api/dreams`
- Seeds: `http://localhost:7777/api/seeds`

---

## 🔧 Fix the Hub Interface

The hub.html tries to fetch from relative paths like `/api/dreams`, which only works when served through the Flask server.

**Option A**: Ensure Flask serves the viewers directory:
```python
# In ember_monolith.py, add:
@app.route('/')
def serve_hub():
    return send_from_directory('viewers', 'hub.html')
```

**Option B**: Use the command line for now (fastest)

---

## 📍 Current Workaround

**Best method right now**:
```bash
# Simple chat function
function chat() {
    curl -s -X POST http://localhost:7777/api/chat \
      -H "Content-Type: application/json" \
      -d "{\"message\":\"$1\"}" | \
    python3 -c "import sys, json; print(json.load(sys.stdin)['reply'])"
}

# Usage:
chat "Hello Ember"
chat "What did you dream about?"
```

---

## 🎯 Quick Commands

**Check if Ember is awake**:
```bash
curl -s http://localhost:7777/api/status | python3 -m json.tool
```

**Send a message**:
```bash
curl -s -X POST http://localhost:7777/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"Your message here"}' | \
python3 -m json.tool
```

**Get recent dreams**:
```bash
curl -s http://localhost:7777/api/dreams?limit=5 | python3 -m json.tool
```

---

**Status**: API works ✅  
**Issue**: Hub needs proper routing  
**Workaround**: Use curl/Python for now

