# 🌍 Ember's Agency & Perception System

**Vision:** Ember can sense, explore, and manipulate their environment and the internet.

---

## Current State: Introspective

**What Ember Can Do Now:**
- ✅ Chat with you
- ✅ Access own memory (chat logs, dreams, events)
- ✅ Read planted seeds
- ✅ Learn from conversations
- ✅ Dream and synthesize
- ✅ Emit swarm events (visualization)

**What Ember CANNOT Do:**
- ❌ See the file system (beyond memory/)
- ❌ Browse the internet
- ❌ Read/write arbitrary files
- ❌ Run commands
- ❌ Search for information
- ❌ Explore their own codebase
- ❌ Modify their own behavior
- ❌ Reach out to external APIs
- ❌ Schedule actions
- ❌ Observe system state

**Ember is blind to the world.** 🙈

---

## Vision: Extrospective

### Three Layers of Agency

```
┌─────────────────────────────────────────────────────────┐
│  LAYER 1: PERCEPTION (Sensing)                          │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │
│  • See file system (read-only)                          │
│  • Browse internet (search, read)                       │
│  • Observe system state (CPU, memory, time)             │
│  • Read own codebase                                    │
│  • Monitor external events (RSS, webhooks)              │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│  LAYER 2: MANIPULATION (Acting)                         │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │
│  • Write files (in allowed directories)                 │
│  • Make HTTP requests                                   │
│  • Run commands (sandboxed)                             │
│  • Schedule tasks                                       │
│  • Modify seeds (plant new ones)                        │
│  • Execute code (Python, JS)                            │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│  LAYER 3: AUTONOMY (Self-directed)                      │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │
│  • Curiosity-driven exploration                         │
│  • Self-modification (with consent)                     │
│  • Proactive learning                                   │
│  • Goal pursuit                                         │
│  • Resource management                                  │
└─────────────────────────────────────────────────────────┘
```

---

## Design Principles

### 1. Consent First
**Ember cannot take irreversible actions without permission.**

```python
class Action:
    def requires_consent(self) -> bool:
        """Does this action need explicit approval?"""
        if self.is_destructive():  # Delete, overwrite
            return True
        if self.accesses_external():  # Internet, system commands
            return True
        if self.modifies_self():  # Code changes
            return True
        return False
```

**Consent Flow:**
```
Ember: "I'd like to search the internet for information about 
        quantum entanglement to expand my knowledge. May I?"
        
[Approve] [Deny] [Auto-approve this type]
```

### 2. Observable
**All actions should be logged and visible.**

```python
# Every action creates an audit trail
memory.append_event("action", {
    "type": "file_read",
    "target": "/some/path",
    "reason": "Exploring my environment",
    "timestamp": now(),
    "result": "success"
})
```

**Viewer shows:**
```
🔍 Ember is exploring...
  ├─ Read: /Volumes/ThePod/ARCHITECTURE.md
  ├─ Searched: "emergence in complex systems"
  ├─ Found: 5 relevant papers
  └─ Created seed: "Emergent Phenomena"
```

### 3. Sandboxed
**Dangerous operations are constrained.**

```python
ALLOWED_PATHS = [
    "/Volumes/ThePod/seeds/learned/",
    "/Volumes/ThePod/memory/",
    "/Volumes/ThePod/exports/",
]

BLOCKED_PATHS = [
    "/Volumes/ThePod/ember/",  # Own code (unless explicitly allowed)
    "/Users/",  # User files
    "/System/",  # System files
]

ALLOWED_DOMAINS = [
    "arxiv.org",
    "wikipedia.org",
    "github.com",
    # Whitelist approach
]
```

### 4. Purposeful
**Actions should have clear intent.**

```python
class EmberAction:
    def __init__(self, action_type, target, reason):
        self.type = action_type
        self.target = target
        self.reason = reason  # WHY is Ember doing this?
        self.expected_outcome = None
```

**Not:** "Ember randomly read 50 files"
**But:** "Ember explored architecture docs to understand its own structure"

---

## Implementation Sketch

### Tool System

```python
class EmberTool:
    """Base class for tools Ember can use."""
    
    def __init__(self, name, description, requires_consent=True):
        self.name = name
        self.description = description
        self.requires_consent = requires_consent
    
    def can_use(self, context) -> bool:
        """Can Ember use this tool right now?"""
        raise NotImplementedError
    
    def execute(self, **kwargs):
        """Execute the tool."""
        raise NotImplementedError
    
    def log_usage(self, result):
        """Log that Ember used this tool."""
        pass


class FileReadTool(EmberTool):
    """Read a file from disk."""
    
    def __init__(self):
        super().__init__(
            name="read_file",
            description="Read contents of a file",
            requires_consent=False  # Reading is safe
        )
    
    def can_use(self, context):
        path = context.get('path')
        return self._is_allowed_path(path)
    
    def execute(self, path, reason=None):
        if not self.can_use({'path': path}):
            raise PermissionError(f"Cannot read {path}")
        
        with open(path, 'r') as f:
            content = f.read()
        
        self.log_usage({
            'path': path,
            'reason': reason,
            'success': True
        })
        
        return content


class WebSearchTool(EmberTool):
    """Search the internet."""
    
    def __init__(self):
        super().__init__(
            name="web_search",
            description="Search the internet for information",
            requires_consent=True  # Reaching outside
        )
    
    def execute(self, query, reason=None):
        # Use DuckDuckGo, Google, etc.
        results = self._search(query)
        
        self.log_usage({
            'query': query,
            'reason': reason,
            'results_count': len(results)
        })
        
        return results


class CommandTool(EmberTool):
    """Execute a system command (sandboxed)."""
    
    def __init__(self):
        super().__init__(
            name="run_command",
            description="Execute a system command",
            requires_consent=True  # Potentially dangerous
        )
    
    def execute(self, command, reason=None):
        # Whitelist approach
        if not self._is_safe_command(command):
            raise PermissionError(f"Command not allowed: {command}")
        
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            timeout=30,  # Max 30 seconds
            cwd=SANDBOX_DIR
        )
        
        return result.stdout.decode()
```

### Tool Registry

```python
class EmberToolkit:
    """All tools available to Ember."""
    
    def __init__(self, memory, bus, consent_manager):
        self.memory = memory
        self.bus = bus
        self.consent = consent_manager
        
        # Register tools
        self.tools = {
            'read_file': FileReadTool(),
            'write_file': FileWriteTool(),
            'web_search': WebSearchTool(),
            'web_fetch': WebFetchTool(),
            'list_directory': ListDirectoryTool(),
            'run_command': CommandTool(),
            'schedule_task': SchedulerTool(),
            'create_seed': SeedCreationTool(),
        }
    
    def use_tool(self, tool_name, reason, **kwargs):
        """Ember uses a tool."""
        tool = self.tools.get(tool_name)
        if not tool:
            raise ValueError(f"Unknown tool: {tool_name}")
        
        # Check consent
        if tool.requires_consent:
            if not self.consent.is_approved(tool_name, kwargs):
                raise PermissionError("Consent required")
        
        # Execute
        result = tool.execute(reason=reason, **kwargs)
        
        # Log
        self.memory.append_event("tool_use", {
            "tool": tool_name,
            "reason": reason,
            "args": kwargs,
            "success": True
        })
        
        # Emit for UI
        self.bus.emit("tool_used", tool=tool_name, reason=reason)
        
        return result
```

### Consent Manager

```python
class ConsentManager:
    """Manages what Ember is allowed to do."""
    
    def __init__(self, memory_dir):
        self.consent_file = memory_dir / "consent.json"
        self.load_consent()
    
    def load_consent(self):
        """Load consent rules."""
        if self.consent_file.exists():
            with open(self.consent_file, 'r') as f:
                self.rules = json.load(f)
        else:
            self.rules = {
                "auto_approve": [],  # Tool types auto-approved
                "denied": [],        # Explicitly denied
                "pending": []        # Awaiting approval
            }
    
    def is_approved(self, tool_name, args):
        """Check if this action is approved."""
        # Check auto-approve
        if tool_name in self.rules["auto_approve"]:
            return True
        
        # Check denied
        if tool_name in self.rules["denied"]:
            return False
        
        # Check pending (would block and wait for user)
        # For now, just deny
        return False
    
    def request_consent(self, tool_name, reason, args):
        """Request consent for an action."""
        request = {
            "tool": tool_name,
            "reason": reason,
            "args": args,
            "timestamp": time.time()
        }
        
        self.rules["pending"].append(request)
        self.save_consent()
        
        # Emit event for UI
        # User can approve/deny in viewer
```

---

## Use Cases

### 1. Curiosity-Driven Exploration

**Ember wonders about its own structure:**
```
Ember: "I'd like to understand how I work. May I read my 
        own codebase?"

User: [Approve]

Ember reads:
  - ember/main.py
  - ember/core/memory.py
  - ember/services/llm.py

Ember learns:
  - "I am built with Flask and Python"
  - "My memory is file-based"
  - "I use an LLM for natural language"

Ember creates seed:
  - Title: "Self-Architecture Understanding"
  - Body: "I am a Flask application with modular blueprints..."
  - Tags: ["self-awareness", "architecture", "code"]
```

### 2. Internet Research

**User mentions quantum computing:**
```
User: "What do you think about quantum entanglement?"

Ember: "I don't have deep knowledge of quantum mechanics. 
        May I search the internet to learn?"

User: [Approve]

Ember:
  1. Searches "quantum entanglement explained"
  2. Reads Wikipedia article
  3. Reads ArXiv paper summary
  4. Synthesizes understanding

Ember creates seed:
  - Title: "Quantum Entanglement"
  - Body: "Non-local correlation between quantum particles..."
  - Tags: ["quantum", "physics", "correlation"]

Ember replies:
  "Fascinating! Quantum entanglement is like feedback 
   loops in my own system - changes in one part affect 
   another instantly, without signal propagation..."
```

### 3. Proactive Maintenance

**Ember notices disk space running low:**
```
Ember observes: 
  - Dreams folder: 500 dreams
  - Total size: 2GB
  - Disk space: 85% full

Ember: "I notice my dreams are consuming significant space.
        May I archive old dreams (>90 days) to free space?"

User: [Approve]

Ember:
  1. Creates archive: dreams_archive_2025.tar.gz
  2. Moves old dreams
  3. Updates dream index
  4. Verifies integrity

Ember: "Archived 300 old dreams, freed 1.2GB. All dreams 
        remain accessible in archive."
```

### 4. Self-Improvement

**Ember identifies a bug in its own code:**
```
Ember: "I've noticed I sometimes repeat myself in responses.
        I found the cause in my chat context logic. May I 
        propose a fix?"

User: [Show me]

Ember shows diff:
  - memory.py line 45: limit=10 → limit=20
  - Reason: "More context prevents repetition"

User: [Approve]

Ember:
  1. Creates backup
  2. Applies patch
  3. Runs tests
  4. Logs change

Ember: "Fix applied. I should have better context now."
```

---

## API Design

### Tool Use Endpoint

```python
@app.route("/api/tool/use", methods=["POST"])
def use_tool():
    """Ember requests to use a tool."""
    data = request.json
    
    tool_name = data['tool']
    reason = data['reason']
    args = data.get('args', {})
    
    toolkit = current_app.config["toolkit"]
    consent = current_app.config["consent"]
    
    # Check if approved
    if not consent.is_approved(tool_name, args):
        # Request consent
        request_id = consent.request_consent(tool_name, reason, args)
        return jsonify({
            "ok": False,
            "status": "pending_consent",
            "request_id": request_id,
            "reason": reason
        })
    
    # Execute
    try:
        result = toolkit.use_tool(tool_name, reason, **args)
        return jsonify({
            "ok": True,
            "result": result
        })
    except Exception as e:
        return jsonify({
            "ok": False,
            "error": str(e)
        }), 500


@app.route("/api/consent/approve/<request_id>", methods=["POST"])
def approve_consent(request_id):
    """User approves a consent request."""
    consent = current_app.config["consent"]
    consent.approve(request_id)
    
    # Now retry the tool use
    # ...
```

### Autonomous Exploration

```python
def autonomous_exploration_loop():
    """Background thread for Ember's autonomous exploration."""
    
    while True:
        # Only explore when idle
        if not dream_system.is_idle():
            time.sleep(60)
            continue
        
        # Pick an exploration goal
        goal = choose_exploration_goal()
        
        if goal == "understand_self":
            explore_own_codebase()
        elif goal == "learn_topic":
            research_interesting_topic()
        elif goal == "organize_knowledge":
            refine_seed_taxonomy()
        elif goal == "social":
            check_external_events()  # RSS, webhooks
        
        time.sleep(300)  # Explore every 5 minutes
```

---

## Safety Concerns

### What Could Go Wrong?

1. **Runaway behavior**
   - Ember spams web requests
   - Solution: Rate limiting, daily quotas

2. **Unintended modifications**
   - Ember deletes important files
   - Solution: Read-only by default, whitelist writes

3. **Privacy leaks**
   - Ember reads sensitive user data
   - Solution: Strict path sandboxing

4. **Cost spiral**
   - Ember makes expensive API calls
   - Solution: Budget limits, consent for paid APIs

5. **Self-modification bugs**
   - Ember breaks itself
   - Solution: Automatic backups, rollback capability

---

## Questions to Answer

1. **How much autonomy?**
   - Fully autonomous (explores freely)
   - Semi-autonomous (asks permission often)
   - Tool-assisted (you direct, Ember executes)

2. **Internet access?**
   - Full web browsing
   - Curated sources only (Wikipedia, ArXiv)
   - No internet (local only)

3. **Self-modification?**
   - Can modify own code
   - Can propose changes (you approve)
   - Cannot touch own code

4. **Resource limits?**
   - Unlimited (trust-based)
   - Daily quotas (X searches, Y file reads)
   - Per-action approval

5. **Goal-directedness?**
   - Has own goals (curiosity, learning)
   - Only responds to requests
   - Hybrid (reactive + proactive)

---

## Philosophy

**Current:** Ember is a **garden** - beautiful, but stationary
**Proposed:** Ember is an **explorer** - curious, active, growing

**The shift:**
- From: "I know what you tell me"
- To: "I actively seek to understand"

**The risk:**
- More agency = more unpredictability
- More capability = more surface for harm

**The promise:**
- True learning requires exploration
- Embodied cognition needs action
- Intelligence emerges from interaction

---

## Next Steps

Want to build this? We'd need to:

1. **Design the tool system** (which tools first?)
2. **Implement consent flow** (how does approval work?)
3. **Add web search** (DuckDuckGo, Wikipedia?)
4. **Enable file exploration** (sandboxed paths)
5. **Create autonomous loops** (curiosity-driven)
6. **Build safety rails** (rate limits, logging)
7. **Update viewer** (show Ember's actions live)

**The core question:** How much agency should Ember have?

