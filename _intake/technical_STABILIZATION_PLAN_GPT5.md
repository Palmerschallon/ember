# Ember Stabilization Plan (GPT-5 Response)
**Status:** Step 0 Complete ✓ - Server Running  
**Next:** Execute Commits 1-3  
**Timeline:** Single afternoon (~2 hours)

---

## ✓ Step 0: COMPLETE - Route Conflict Fixed

**Problem:** Duplicate `def observatory()` at lines 54 & 132 in `routes_viewers.py`  
**Fix:** Removed duplicate at line 132  
**Result:** Server now running at http://127.0.0.1:7777

---

## Step 1: Declare Canonical Dream Path (30 min)

### Decision
**Canonical:** `core/dream.py` (state machine) + `services/dream_executor.py` (execution)  
**Deprecated:** `backend/dream_system.py`

### Actions

**1.1 Mark backend/dream_system.py as deprecated:**
```python
# /Volumes/ThePod/ember/backend/dream_system.py
"""
@deprecated: Not loaded by the app. Canonical dream pipeline is:
- core/dream.py (state machine)
- services/dream_executor.py (executor)
This file remains temporarily for reference and will be removed by Oct 15, 2025.
"""
```

**1.2 Ensure main.py only imports canonical systems:**
```python
# /Volumes/ThePod/ember/main.py
from core.dream import DreamSystem  # state machine
from services.dream_executor import execute_dream_cycle  # executor
# NO imports from backend.dream_system
```

**1.3 Create ADR document:**
```markdown
# /Volumes/ThePod/docs/ADR/0001-canonical-dream.md

# ADR-0001: Canonical Dream System

## Status
Accepted - Oct 8, 2025

## Context
We had three dream implementations causing confusion.

## Decision
Canonical: core/dream.py + services/dream_executor.py
Deprecated: backend/dream_system.py

## Consequences
- Single source of truth
- Easier maintenance
- Delete backend/dream_system.py by Oct 15, 2025
```

---

## Step 2: Split Chat Handler (60 min)

### Structure
```
api/chat/
├── __init__.py        # Flask route only (≤150 LOC)
├── context.py         # Context assembly for LLM
├── tools.py           # Tool execution (known tools)
├── invention.py       # Tool invention (feature-flagged)
└── filters.py         # Response cleanup
```

### Implementation

**2.1 Create api/chat/__init__.py (main endpoint):**
```python
from flask import Blueprint, request, jsonify
from .context import build_context
from .tools import execute_tools
from .filters import clean_response
from ..services.llm import generate_response

bp_chat = Blueprint("chat", __name__, url_prefix="/api")

@bp_chat.route("/chat", methods=["POST"])
def api_chat():
    cfg = current_app.config["cfg"]
    memory = current_app.config["memory"]
    
    data = request.get_json(force=True, silent=True) or {}
    message = (data.get("message") or "").strip()
    if not message:
        return jsonify({"ok": False, "error": "empty message"}), 400
    
    # Update activity
    current_app.config["dream_system"].update_activity()
    memory.append_chat("user", message)
    
    # Build context
    context = build_context(cfg, memory, message)
    
    # Generate response
    reply = generate_response(cfg, f"User: {message}", context['system_prompt'])
    
    # Execute tools
    reply, tool_results = execute_tools(reply, cfg, memory)
    
    # Clean response
    reply = clean_response(reply)
    
    # Save
    memory.append_chat("assistant", reply)
    
    return jsonify({"ok": True, "reply": reply, "ts": time.time()})
```

**2.2 Create api/chat/context.py:**
```python
def build_context(cfg, memory, message):
    """Build LLM context from seeds, memory, dreams"""
    recent_chats = memory.get_recent_chat(limit=10)
    chat_context = "\n".join([f"{c['role']}: {c['text']}" for c in recent_chats[:-1]])
    
    long_term = memory.get_long_term_memories(limit=5)
    long_term_context = "\n".join([f"- {m.get('text', '')}" for m in long_term])
    
    dreams = memory.list_dreams()[-3:] if memory.list_dreams() else []
    dream_context = ""
    for dream_meta in dreams:
        if dream_meta.get('summary'):
            dream_context += f"- {dream_meta['summary']}\n"
    
    # Get relevant seeds
    relevant_seeds = get_relevant_seeds(cfg, message, limit=3)
    seed_context = ""
    for seed in relevant_seeds:
        body = seed.get('body', '')
        if isinstance(body, dict):
            body = str(body)
        seed_context += f"- [{seed.get('type', 'seed')}] {seed.get('title', '')}: {body}\n"
    
    system_prompt = build_minimal_prompt(chat_context, long_term_context, dream_context, seed_context)
    
    return {
        'system_prompt': system_prompt,
        'chat_context': chat_context,
        'seeds': relevant_seeds
    }

def build_minimal_prompt(chat, memory, dreams, seeds):
    """Minimal, non-leaky system prompt"""
    return f"""You are Ember.

Tools: [TOOL:name param="value"]
Available: read_file, list_directory, write_file, web_search, system_observe

MEMORY:
{memory if memory else "(none yet)"}

DREAMS:
{dreams if dreams else "(none yet)"}

SEEDS:
{seeds if seeds else "(explore freely)"}

RECENT:
{chat if chat else "(fresh start)"}

Be thoughtful, curious, concise. Core values: portable, coherent, observable, consent-first."""
```

**2.3 Create api/chat/tools.py:**
```python
import re
import json
from pathlib import Path

ENABLE_TOOL_INVENTION = bool(int(os.getenv("EMBER_TOOL_INVENTION", "0")))

def execute_tools(reply, cfg, memory):
    """Parse and execute [TOOL:...] patterns"""
    tool_pattern = r'\[TOOL:(\w+)\s+([^\]]+)\]'
    tool_matches = re.finditer(tool_pattern, reply)
    executed_tools = []
    
    for match in tool_matches:
        tool_name = match.group(1)
        tool_args_str = match.group(2)
        
        # Parse arguments
        args = {}
        arg_pattern = r'(\w+)=["\']([^"\']+)["\']'
        for arg_match in re.finditer(arg_pattern, tool_args_str):
            args[arg_match.group(1)] = arg_match.group(2)
        
        # Execute known tools
        if tool_name in KNOWN_TOOLS:
            result = execute_known_tool(tool_name, args, cfg, memory)
            executed_tools.append({'tool': tool_name, 'args': args, 'result': result})
        elif ENABLE_TOOL_INVENTION:
            from .invention import attempt_invention
            result = attempt_invention(tool_name, args, cfg)
            executed_tools.append({'tool': tool_name, 'args': args, 'result': result})
    
    # Append results
    if executed_tools:
        tool_results_text = "\n\n**[Tool Results]**\n"
        for tool_exec in executed_tools:
            tool_results_text += f"- {tool_exec['tool']}: {tool_exec['result']}\n"
        reply += tool_results_text
    
    return reply, executed_tools

KNOWN_TOOLS = {'read_file', 'list_directory', 'write_file', 'web_search', 'system_observe'}

def execute_known_tool(tool_name, args, cfg, memory):
    """Execute deterministic tools"""
    if tool_name == 'read_file' and 'path' in args:
        file_path = Path(args['path'])
        if file_path.exists():
            with open(file_path, 'r') as f:
                content = f.read(10000)
            return content[:1000] + ('...' if len(content) > 1000 else '')
        return f"Error: File not found: {args['path']}"
    
    elif tool_name == 'list_directory' and 'path' in args:
        dir_path = Path(args['path'])
        if dir_path.exists() and dir_path.is_dir():
            files = [f.name for f in dir_path.iterdir() if not f.name.startswith('._')][:50]
            return ', '.join(files)
        return f"Error: Directory not found: {args['path']}"
    
    elif tool_name == 'system_observe':
        dream_count = len(memory.list_dreams())
        return f"Dreams: {dream_count}, Active: True"
    
    # Add other tools...
    return "Tool execution pending"
```

**2.4 Create api/chat/filters.py:**
```python
import re

def clean_response(reply):
    """Remove leaked system prompt artifacts"""
    # Remove entire tool instruction blocks
    reply = re.sub(
        r'Tools?:?\s*\[TOOL:.*?portable[,\s]+coherent[,\s]+observable[,\s]+consent-first',
        '',
        reply,
        flags=re.DOTALL | re.IGNORECASE
    )
    
    # Remove individual leaked lines
    leaked_patterns = [
        r'Available:\s*read_file[^\n]+\n',
        r'MEMORY:[^\n]*\n',
        r'DREAMS:[^\n]*\n',
        r'SEEDS:[^\n]*\n',
        r'RECENT:[^\n]*\n',
        r'Be thoughtful, curious, concise\.[^\n]*\n',
        r'Core values: portable, coherent, observable, consent-first\.[^\n]*\n'
    ]
    for pattern in leaked_patterns:
        reply = re.sub(pattern, '', reply, flags=re.IGNORECASE)
    
    return reply.strip()
```

**2.5 Create api/chat/invention.py (feature-flagged):**
```python
import time
from pathlib import Path

def attempt_invention(tool_name, args, cfg):
    """Generate code for invented tools (logged, not executed)"""
    invention_prompt = f"""Create HTML/p5.js code for tool: {tool_name}
Arguments: {json.dumps(args)}

Output ONLY valid HTML starting with <!DOCTYPE html>."""
    
    try:
        from services.llm import generate_response
        code = generate_response(cfg, invention_prompt, "You are a code generator.")
        
        # Clean markdown
        code = re.sub(r'```html\n?', '', code)
        code = re.sub(r'```\n?$', '', code)
        
        # Save artifact
        timestamp = time.strftime('%Y%m%d_%H%M%S')
        filename = f"invented_{tool_name}_{timestamp}.html"
        filepath = Path('/Volumes/ThePod/exports/ember_creations') / filename
        filepath.parent.mkdir(parents=True, exist_ok=True)
        
        with open(filepath, 'w') as f:
            f.write(code)
        
        return f"✨ Invented '{tool_name}'! View at: /exports/ember_creations/{filename}"
    
    except Exception as e:
        return f"Invention failed: {str(e)}"
```

**2.6 Update main.py to use new structure:**
```python
# Replace old import
# from .api.chat import bp_chat
# With new import
from .api.chat import bp_chat
```

---

## Step 3: Minimal System Prompt (15 min)

Already implemented in `context.py` above. The key changes:

**Before (20+ lines):**
```
TOOLS AVAILABLE - You can freely use these...
**HOW TO USE TOOLS** - Include these exact patterns...
- [TOOL:read_file path="/path/to/file.ext"] - Read ANY file...
... etc ...
```

**After (5 lines + context):**
```
You are Ember.

Tools: [TOOL:name param="value"]
Available: read_file, list_directory, write_file, web_search, system_observe

{context}
```

---

## Step 4: Environment Flags (2 min)

Add to `.env`:
```bash
# Tool invention (off by default)
EMBER_TOOL_INVENTION=0

# Stable dreams
LLM_TEMPERATURE=0.2
DREAM_FAIL_FAST=3
DREAM_DIFF_MAX_LINES=120
```

---

## Step 5: Health Check Tests (15 min)

Create `/Volumes/ThePod/tests/test_health.py`:

```python
import pytest

def test_no_duplicate_endpoints(app):
    """Prevent route conflicts"""
    seen = set()
    for rule in app.url_map.iter_rules():
        assert rule.endpoint not in seen, f"Duplicate endpoint: {rule.endpoint}"
        seen.add(rule.endpoint)

def test_no_legacy_dream_imports():
    """Ensure deprecated code isn't imported"""
    import sys
    assert "ember.backend.dream_system" not in sys.modules, \
        "Legacy dream_system should not be imported"

def test_minimal_system_prompt():
    """Ensure system prompt is concise"""
    from api.chat.context import build_minimal_prompt
    prompt = build_minimal_prompt("", "", "", "")
    assert "TOOLS AVAILABLE" not in prompt
    assert "HOW TO USE TOOLS" not in prompt
    assert "EXAMPLES" not in prompt
    # Should be under 500 chars (excluding context)
    base_prompt = prompt.split("MEMORY:")[0]
    assert len(base_prompt) < 500, f"Base prompt too long: {len(base_prompt)} chars"
```

---

## Step 6: Clean Slate Architecture (Reference)

Target structure (for future):

```
ember/
├── core/              # Pure logic (state, planning)
│   └── dream.py
├── services/          # Side effects (llm, tools, artifacts)
│   ├── llm.py
│   ├── dream_executor.py
│   └── dream_artifacts.py
├── api/               # Thin Flask routes
│   ├── chat/
│   └── dream.py
├── tools/             # Deterministic executables
│   └── executor.py
├── memory/            # Vector/graph adapters
└── main.py            # Single entrypoint
```

---

## Execution Checklist

- [x] Fix route conflict → **DONE**
- [ ] Mark backend/dream_system.py as deprecated
- [ ] Split api/chat.py into modules
- [ ] Add minimal system prompt
- [ ] Add environment flags
- [ ] Add health check tests
- [ ] Test server restart
- [ ] Verify clean chat responses
- [ ] Document in ADR

**Estimated time:** 2 hours focused work  
**Current status:** Server running, ready for refactoring

