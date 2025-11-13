# Toys v2 Complete — Chat & Dream Viewer
**Date**: October 7, 2025  
**Updates**: Added chat to sandbox + real-time dream viewer

---

## What's New

### 1. Seed Sandbox v2 ✅
**Location**: `http://localhost:7777/toys/seed_sandbox_v2.html`

**New Feature: Integrated Chat**
- Chat with Ember while exploring seeds
- Context-aware (Ember knows which seed you're viewing)
- Real-time conversation in bottom panel
- Ask questions, get insights, discuss patterns

**Layout**:
- **Left**: Seed library (50 seeds shown)
- **Center**: Particle visualization canvas
- **Right**: Parameter controls (speed, count, alpha)
- **Bottom**: Chat panel with Ember
- **Status bar**: Current seed, connection status

**Use Cases**:
- "Ember, what does this seed do?"
- "How would you use this in a dream?"
- "Can you explain curl noise?"
- "What seeds work well together?"

---

### 2. Dream Viewer ✅
**Location**: `http://localhost:7777/toys/dream_viewer.html`

**Real-Time Dream Watching** (No Prompting Required!)
- **Automatic updates** via Server-Sent Events (SSE)
- **Live status** indicator (LED pulses when dreaming)
- **Event timeline** shows all activity in real-time
- **Dream output** displays as it's generated
- **Auto-scroll** keeps you at latest content

**Sidebar Info**:
- Current cycle number
- Dream type (consolidation/synthesis/creative)
- Live duration counter
- Seeds being used
- Last dream ID

**Timeline Events**:
- Dream start/end
- Progress updates
- Thinking events
- Any swarm activity

**Main View**:
- Live dream output (as it happens)
- Dream summary when complete
- Seeds used
- Insights generated
- Artifacts created (with links)

**Controls**:
- Auto-scroll toggle
- Clear view
- Refresh (load most recent dream)

---

### 3. Toys Index ✅
**Location**: `http://localhost:7777/toys/`

**A landing page for all toys**:
- Grid of available toys
- Descriptions and use cases
- "Coming Soon" previews
- Philosophy explanation

**Available Now**:
- Seed Sandbox v2 (with chat)
- Dream Viewer (real-time)
- Seed Sandbox v1 (classic)

**Coming Soon**:
- Sketch Composer
- Knowledge Graph Explorer (3D)
- Seed Synthesizer

---

## How to Use

### Access Toys
```
http://localhost:7777/toys/
```

### Watch Ember Dream (Passively)
1. Open `http://localhost:7777/toys/dream_viewer.html`
2. Leave it open
3. When Ember dreams (after ~45 min idle), you'll see:
   - LED turns green
   - Status changes to "Dreaming"
   - Timeline populates with events
   - Output appears in real-time
   - No interaction needed!

### Chat While Exploring Seeds
1. Open `http://localhost:7777/toys/seed_sandbox_v2.html`
2. Select a seed from the left
3. Watch it visualize in the center
4. Adjust parameters on the right
5. Ask Ember in the chat at the bottom:
   - "What's happening here?"
   - "How would you use this?"
   - "Show me a different seed"

---

## Technical Details

### Seed Sandbox v2
**Framework**: Vanilla JS + Canvas 2D  
**API calls**:
- `GET /api/seeds/all` — Load all seeds
- `POST /api/chat` — Send messages to Ember

**Features**:
- Real-time particle system
- Curl noise flow field
- Parameter tuning
- Context-aware chat

### Dream Viewer
**Framework**: Vanilla JS + EventSource (SSE)  
**API calls**:
- `GET /api/events/stream` — Real-time events (SSE)
- `GET /health` — Initial state
- `GET /api/dreams/{id}` — Dream details
- `GET /api/dreams/recent` — Most recent dreams

**Features**:
- Server-Sent Events for real-time updates
- Auto-reconnect on disconnect
- Timeline with last 50 events
- Duration counter
- Auto-scroll (toggle-able)

---

## Key Design Decisions

### Why Chat in Sandbox?
**Before**: Static exploration, no guidance  
**After**: Ember can explain, suggest, teach

**Example**:
- User selects "Curl Noise Flow"
- Asks: "What makes this different from regular noise?"
- Ember explains divergence-free fields
- User gains understanding, not just visuals

### Why Passive Dream Viewer?
**Before**: Had to manually check dream outputs  
**After**: Leave it open, see dreams as they happen

**Example**:
- Palmer leaves dream viewer open overnight
- Ember dreams 3 times
- Palmer wakes up, sees all outputs
- No prompting, no missed dreams

**This is "stretch goal" fulfilled**: Real-time dream output without prompting!

---

## Integration Points

### Chat Context Injection
When user chats from sandbox, message includes:
```javascript
`[Context: I'm looking at the seed "${seed.title}" in the sandbox] ${userMessage}`
```

Ember receives full context automatically.

### Event Stream Subscription
Dream Viewer subscribes to `/api/events/stream`:
- `dream_start` → Update UI, start timer
- `dream_progress` → Show output
- `dream_end` → Load full details
- `thinking` → Subtle indicator
- Any other events → Timeline entry

### Auto-reconnect
If SSE connection drops:
```javascript
eventSource.onerror = () => {
    setTimeout(connectEventStream, 5000); // Retry after 5s
};
```

---

## Future Enhancements

### Sketch Composer (Next)
- Live code editor
- Instant preview
- Save to Ember's creations
- Fork existing sketches

### Knowledge Graph Explorer (3D)
- Navigate memories visually
- Add/remove connections
- Watch patterns emerge
- Time-based exploration

### Seed Synthesizer
- Visual node graph
- Drag-and-drop composition
- See emergent patterns
- Export composite seeds

### Dream Playground
- Manually trigger dreams
- Inject prompts mid-dream
- Compare different seed sets
- A/B test dream types

---

## Files Created/Modified

### New Files
1. `/toys/seed_sandbox_v2.html` — Enhanced sandbox with chat
2. `/toys/dream_viewer.html` — Real-time dream viewer
3. `/toys/index.html` — Toys landing page
4. `/TOYS_V2_COMPLETE.md` — This document

### Modified Files
1. `/ember/api/toys.py` — Added index route

---

## Access URLs

**Toys Index**:
```
http://localhost:7777/toys/
```

**Seed Sandbox v2 (with chat)**:
```
http://localhost:7777/toys/seed_sandbox_v2.html
```

**Dream Viewer (real-time)**:
```
http://localhost:7777/toys/dream_viewer.html
```

**Seed Sandbox v1 (classic)**:
```
http://localhost:7777/toys/seed_sandbox.html
```

---

## Restart Server

```bash
lsof -ti:7777 | xargs kill -9 2>/dev/null
sleep 2
cd /Volumes/ThePod
python3 -c "from ember.main import create_app; app = create_app(); app.run(host='0.0.0.0', port=7777, debug=False)" > /tmp/ember_toys_v2.log 2>&1 &
```

---

## Test Checklist

### Seed Sandbox v2
- [ ] Seeds load from API
- [ ] Particles render on canvas
- [ ] Controls adjust parameters
- [ ] Chat sends messages
- [ ] Ember responds with context
- [ ] Status bar updates

### Dream Viewer
- [ ] Event stream connects
- [ ] Timeline populates
- [ ] Status LED works
- [ ] Dream details load
- [ ] Auto-scroll toggles
- [ ] Refresh button works

### Both
- [ ] No console errors
- [ ] Responsive layout
- [ ] Clean, minimal aesthetic
- [ ] Fast loading

---

## The Big Picture

### Before
- **Sandbox**: Static, no guidance
- **Dreams**: Had to manually check outputs
- **Separation**: Tools and toys were separate

### After
- **Sandbox**: Interactive, Ember explains
- **Dreams**: Passive real-time viewing
- **Integration**: Chat + visualization + events

### Philosophy Realized

**"Stretch goal would be to see the output of their dreams real time without me prompting"**

✅ **Achieved**: Dream Viewer auto-updates via SSE. No prompting needed.

**"Also, in the seed playground there no way for me to chat with Ember"**

✅ **Achieved**: Sandbox v2 has integrated chat with context awareness.

---

**Status**: Ready to test! Server restart required.

Visit `http://localhost:7777/toys/` to begin. 🎮✨

