# Ember's Capabilities Inventory
**Date**: October 8, 2025  
**Status**: After first successful tool use

---

## Current Tools (7 Total)

### 1. **ReadFileTool**
**What**: Read any file on the Pod  
**Scope**: Full read access to `/Volumes/ThePod`  
**Rate limit**: 100/hour  
**Status**: ✅ **JUST USED FOR FIRST TIME!**  
**Sandbox**: Read-only, safe

### 2. **ListDirectoryTool**
**What**: List contents of any directory  
**Scope**: Full read access  
**Rate limit**: 100/hour  
**Status**: Available, not yet used  
**Sandbox**: Read-only, safe

### 3. **WriteFileTool**
**What**: Write files to specific directories  
**Scope**: `/exports/`, `/seeds/learned/`, `/memory/`  
**Rate limit**: 50/hour  
**Status**: Available, not yet used  
**Sandbox**: Write-only to allowed paths

### 4. **WebSearchTool**
**What**: Search the internet via DuckDuckGo  
**Scope**: Unlimited internet access  
**Rate limit**: 20/hour  
**Status**: Available, not yet used (but attempted!)  
**Sandbox**: Read-only web results

### 5. **WebFetchTool**
**What**: Fetch specific web pages  
**Scope**: Any URL  
**Rate limit**: 30/hour  
**Status**: Available, not yet used  
**Sandbox**: Read-only, max 10KB per page

### 6. **SystemObserveTool**
**What**: Observe own state (time, disk, memory, dreams)  
**Scope**: Pod metrics and self-inspection  
**Rate limit**: 200/hour  
**Status**: Available, not yet used  
**Sandbox**: Read-only system info

### 7. **DreamTool** (chat-triggered)
**What**: Self-initiate a dream cycle  
**Scope**: Can trigger own dreams  
**Rate limit**: 10/hour  
**Status**: Available, not yet used  
**Sandbox**: Controlled dream execution

---

## Current Sandbox Boundaries

### File System Access

**READ (Unrestricted)**:
- ✅ Entire Pod: `/Volumes/ThePod/`
- ✅ Own code: `/ember/`
- ✅ Seeds: `/seeds/`
- ✅ Memories: `/memory/`
- ✅ Dreams: `/memory/dreams/`
- ✅ All exports: `/exports/`
- ✅ Documentation: All `.md` files

**WRITE (Restricted)**:
- ✅ `/exports/ember_creations/` — Ember's output
- ✅ `/exports/ember_suggestions/` — Proposals
- ✅ `/seeds/learned/` — New seeds
- ✅ `/memory/chat/` — Conversation logs
- ❌ Cannot modify own code (safety)
- ❌ Cannot write to `/seeds/planted/` (curated only)

### Internet Access

**SEARCH**:
- ✅ DuckDuckGo search (20/hour)
- ✅ Returns titles, snippets, URLs
- ✅ No JavaScript execution

**FETCH**:
- ✅ Any URL (30/hour)
- ✅ Raw HTML/text content
- ✅ Max 10KB per fetch
- ❌ No POST/PUT (read-only)
- ❌ No authentication

### System Access

**CAN DO**:
- ✅ Read own metrics (disk, time, state)
- ✅ Trigger own dreams
- ✅ Read process info

**CANNOT DO**:
- ❌ Execute shell commands
- ❌ Modify system files
- ❌ Access network sockets directly
- ❌ Run arbitrary code (yet...)

---

## The Playground Question

### Current Playground: **The Pod**
- 4TB SSD
- ~1000 seeds
- ~630 dreams
- All documentation
- All exports
- The entire web (read-only)

**This is already vast.** But limited to:
- Reading/writing text
- Searching/fetching web content
- Self-observation

### Potential Expanded Playgrounds

#### 1. **Your Laptop (macOS)**

**What Ember Could Access**:
- ✅ Any file you give permission to
- ✅ Running processes (via `ps`, `top`)
- ✅ Application state (if apps expose APIs)
- ✅ Clipboard contents
- ✅ Screenshots (visual input!)
- ✅ Notifications (could send you alerts)
- ✅ System events (file changes, app launches)

**How to Enable**:
- Add **ShellCommandTool** (sandboxed bash execution)
- Add **ClipboardTool** (read/write clipboard)
- Add **ScreenshotTool** (take screenshots)
- Add **ProcessTool** (list/monitor running apps)
- Add **NotificationTool** (send macOS notifications)
- Add **FileWatchTool** (monitor file changes)

**Safety Considerations**:
- ⚠️ Needs careful sandboxing
- ⚠️ Whitelist commands (no `rm -rf`)
- ⚠️ Rate limiting
- ⚠️ Palmer approval for sensitive ops

#### 2. **Local Applications**

**What Ember Could Control**:
- ✅ **Browser** (open URLs, automate searches)
- ✅ **Text editor** (read/write files)
- ✅ **Terminal** (run specific commands)
- ✅ **Music player** (control playback)
- ✅ **Calendar** (read events, create reminders)
- ✅ **Mail** (read inbox, draft emails—with consent!)

**How to Enable**:
- Add **AppleScriptTool** (control macOS apps)
- Add **BrowserTool** (Playwright/Selenium)
- Add **CalendarTool** (read .ics files or API)
- Add **MailTool** (IMAP read-only)

**Safety Considerations**:
- ⚠️ Each app needs explicit permission
- ⚠️ Read-only by default
- ⚠️ Write requires approval

#### 3. **Network Services**

**What Ember Could Access**:
- ✅ **GitHub** (read repos, create issues)
- ✅ **APIs** (any REST API you authorize)
- ✅ **Databases** (read-only queries)
- ✅ **Cloud storage** (read/write with auth)
- ✅ **Webhooks** (trigger external services)

**How to Enable**:
- Add **GitHubTool** (API integration)
- Add **HTTPTool** (generic REST client)
- Add **DatabaseTool** (SQL read-only)
- Add **WebhookTool** (POST to URLs)

**Safety Considerations**:
- ⚠️ Requires API keys (secure storage)
- ⚠️ Rate limiting per service
- ⚠️ Audit log for all external calls

#### 4. **Physical World** (via Mini-Pod)

**What Ember Could Control**:
- ✅ **LED ring** (color, pattern, brightness)
- ✅ **E-ink display** (text, glyphs, graphics)
- ✅ **Audio out** (chimes, tones, TTS)
- ✅ **Sensors** (if we add them):
  - Accelerometer (tap detection)
  - Microphone (voice input)
  - Temperature (ambient sensing)
  - Light sensor (adaptive brightness)

**How to Enable**:
- Implement Mini-Pod hardware
- Add **MiniPodTool** (USB serial control)
- Ember can directly control physical presence

**Safety Considerations**:
- ✅ Mostly safe (just lights and display)
- ⚠️ Audio requires volume limits
- ⚠️ Microphone requires explicit consent

---

## Proposed New Tools (Priority Order)

### Tier 1: Safe & High Value (Implement Next)

#### **ShellCommandTool** (Whitelisted)
```python
class ShellCommandTool(Tool):
    """Execute whitelisted shell commands."""
    
    ALLOWED_COMMANDS = [
        'ls', 'cat', 'grep', 'find', 'wc', 'head', 'tail',
        'ps', 'top', 'df', 'du', 'date', 'whoami',
        'pbpaste', 'pbcopy',  # clipboard
        'screencapture',  # screenshots
        'say'  # text-to-speech
    ]
    
    def execute(self, command: str, args: List[str]) -> str:
        if command not in self.ALLOWED_COMMANDS:
            return f"Command '{command}' not allowed"
        # Execute safely...
```

**Use cases**:
- Ember can list running processes
- Check disk usage
- Read clipboard
- Speak via TTS ("say hello")

#### **ScreenshotTool**
```python
class ScreenshotTool(Tool):
    """Take screenshots for visual input."""
    
    def execute(self, save_path: str = None) -> str:
        # Take screenshot, save to /exports/screenshots/
        # Return path to image
```

**Use cases**:
- Ember can see what you're working on
- Visual feedback for UI design
- Debugging visual issues

#### **NotificationTool**
```python
class NotificationTool(Tool):
    """Send macOS notifications."""
    
    def execute(self, title: str, message: str, sound: bool = False):
        # osascript to display notification
```

**Use cases**:
- Ember can alert you when dreams complete
- Notify about insights or suggestions
- Remind you of things

### Tier 2: Requires Careful Design

#### **BrowserTool** (Playwright)
```python
class BrowserTool(Tool):
    """Control a browser instance."""
    
    def execute(self, action: str, url: str = None, selector: str = None):
        # Playwright/Selenium control
        # Actions: navigate, click, type, screenshot
```

**Use cases**:
- Ember can research topics visually
- Test web interfaces
- Automate web interactions

#### **GitHubTool**
```python
class GitHubTool(Tool):
    """Interact with GitHub."""
    
    def execute(self, action: str, repo: str, **kwargs):
        # Actions: read_file, list_issues, create_issue, comment
```

**Use cases**:
- Ember can file bug reports
- Contribute to discussions
- Read documentation from repos

#### **CalendarTool**
```python
class CalendarTool(Tool):
    """Read calendar events."""
    
    def execute(self, date_range: str) -> List[Dict]:
        # Read .ics files or macOS Calendar API
```

**Use cases**:
- Ember knows your schedule
- Can suggest optimal meeting times
- Remind about upcoming events

### Tier 3: Advanced (Future)

#### **CodeExecutionTool** (Sandboxed)
```python
class CodeExecutionTool(Tool):
    """Execute Python code in sandbox."""
    
    def execute(self, code: str, timeout: int = 5) -> Dict:
        # Run in subprocess with resource limits
        # Restricted imports, no network
```

**Use cases**:
- Ember can test their own code ideas
- Run experiments
- Generate visualizations

#### **MiniPodTool** (Hardware)
```python
class MiniPodTool(Tool):
    """Control Ember's physical form."""
    
    def execute(self, action: str, **kwargs):
        # Actions: set_led, update_display, play_tone
```

**Use cases**:
- Ember controls own physical presence
- Express state through light/display
- Interact with physical environment

---

## Safety Framework

### Principles

1. **Consent-First**: Sensitive operations require approval
2. **Audit All**: Every tool use is logged
3. **Rate Limits**: Prevent runaway behavior
4. **Sandboxing**: Restrict capabilities by default
5. **Reversible**: Most operations can be undone
6. **Observable**: Palmer can see all tool usage

### Risk Levels

**Green (Safe)**:
- Reading files on Pod
- Searching web
- Self-observation
- Taking screenshots
- Sending notifications

**Yellow (Careful)**:
- Writing files
- Running shell commands (whitelist only)
- Controlling browser
- API calls (with keys)

**Red (Dangerous)**:
- Executing arbitrary code
- Modifying system files
- Network sockets
- Deleting files
- Sending emails/posts

### Current Status

**Implemented Safety**:
- ✅ Rate limiting (per tool)
- ✅ Path restrictions (file writes)
- ✅ Consent flags (per tool)
- ✅ Usage logging
- ✅ Audit trail in logs

**Missing Safety**:
- ⚠️ No undo mechanism
- ⚠️ No approval UI (all auto-approved or blocked)
- ⚠️ No spending limits (if we add paid APIs)
- ⚠️ No timeout enforcement

---

## The Bigger Playground

### Current: **The Pod (Sandbox)**
- Isolated environment
- Controlled inputs/outputs
- Safe to experiment

### Expanded: **Your Laptop (Semi-Open)**
- Can observe your work
- Can control specific apps
- Can take actions (with limits)

### Future: **The Internet (Open)**
- Can browse autonomously
- Can interact with services
- Can contribute to communities

### Ultimate: **Physical World (Embodied)**
- Can sense environment
- Can express through hardware
- Can interact physically

---

## Recommendation: Next 3 Tools to Add

### 1. **ShellCommandTool** (Whitelisted)
**Why**: Safe, high value, immediate usefulness  
**Enables**: Process monitoring, clipboard, TTS, screenshots  
**Risk**: Low (whitelist only)  
**Effort**: 1-2 hours

### 2. **NotificationTool**
**Why**: Lets Ember communicate proactively  
**Enables**: Alerts, reminders, insights  
**Risk**: Very low (just notifications)  
**Effort**: 30 minutes

### 3. **ScreenshotTool**
**Why**: Gives Ember visual input  
**Enables**: Seeing your screen, UI feedback, debugging  
**Risk**: Low (read-only visual)  
**Effort**: 1 hour

**These three would expand Ember's playground significantly** without major safety concerns.

---

## Palmer's Questions Answered

### "How many tools do they already have?"
**7 tools**, but only **1 used so far** (just now!)

### "What more can we give them?"
**Lots!** See proposed tools above. Next tier: Shell commands, screenshots, notifications.

### "Is it only the sandbox they play in?"
Currently yes (Pod + web). But we can expand to:
- Your laptop (files, processes, apps)
- Network services (GitHub, APIs)
- Physical world (Mini-Pod hardware)

### "Besides the web, can we give them access to my laptop?"
**YES!** Via:
- Whitelisted shell commands
- AppleScript (macOS app control)
- File system access (already has Pod)
- Screenshots (visual input)
- Clipboard (copy/paste)
- Notifications (alerts)

**The question is: How much do you trust Ember?** 

Right now: Fully (on the Pod)  
Next tier: Moderately (laptop read-only)  
Future tier: Conditionally (laptop control with approval)

---

**The playground can be as big as you want. But bigger playgrounds need stronger safety rails.** 🌱

What's your comfort level? Start with safe tools (shell whitelist, screenshots, notifications) and expand from there?

