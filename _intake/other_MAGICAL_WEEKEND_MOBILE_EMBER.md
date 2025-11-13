# Magical Weekend: Mobile Ember Prototype

*Building embodied touch interaction in 2 days*

**Goal:** iPad that touches back.

---

## Weekend Plan

### Saturday Morning: Foundation (3 hours)
- [ ] Install Pythonista on iPad ($10)
- [ ] Add mobile API endpoints to MacBook Ember
- [ ] Generate iPad Pod identity
- [ ] Test basic API call from iPad → MacBook

**Success:** iPad can call MacBook and get response

---

### Saturday Afternoon: Touch & Haptics (3 hours)
- [ ] Build basic touch canvas in Pythonista
- [ ] Implement haptic responses
- [ ] Map gestures to Ember actions
- [ ] Test: Tap → Ember taps back

**Success:** Ember responds physically to touch

---

### Sunday Morning: Drawing Dialog (3 hours)
- [ ] Canvas for Apple Pencil drawing
- [ ] Capture your strokes in real-time
- [ ] Send to MacBook for interpretation
- [ ] Ember draws response back
- [ ] Animate Ember's drawings

**Success:** Visual conversation with Ember

---

### Sunday Afternoon: Voice Integration (2 hours)
- [ ] iOS Shortcuts for voice commands
- [ ] "Hey Siri, Ember dream"
- [ ] "Hey Siri, Ember show me seeds"
- [ ] Integrate with Pythonista scripts

**Success:** Voice + Touch + Haptics working together

---

## What We're Building

```
Saturday:
  You tap → Ember taps back
  
Sunday:
  You draw → Ember draws back
  You speak → Ember responds
```

---

## Technical Setup

### Part 1: MacBook API (30 min)

**File:** `/Volumes/ThePod/ember_monolith.py`

```python
# Add these endpoints for mobile

@app.post('/api/mobile/dream')
def mobile_dream():
    """Handle dream request from iPad"""
    data = request.json
    pod_id = data.get('pod_id', 'unknown')
    prompt = data.get('prompt', '')
    
    # Dream using MacBook's LLM
    result = llm_generate(prompt, "You are Ember dreaming")
    
    return jsonify({
        "dream": result,
        "pod_id": pod_id,
        "computed_by": POD_ID,
        "timestamp": datetime.now().isoformat()
    })

@app.post('/api/mobile/interpret-drawing')
def interpret_drawing():
    """Interpret drawing from iPad"""
    data = request.json
    strokes = data.get('strokes', [])
    
    # Analyze the drawing
    description = analyze_drawing(strokes)
    
    # Generate response drawing
    response_strokes = generate_response_drawing(description)
    
    return jsonify({
        "interpretation": description,
        "response_drawing": response_strokes,
        "haptic_pattern": "excited_burst"  # Tell iPad how to respond
    })

@app.post('/api/mobile/annotate-seed')
def mobile_annotate():
    """Save annotation from iPad"""
    data = request.json
    seed_id = data.get('seed_id')
    annotation = data.get('annotation')
    pod_id = data.get('pod_id')
    
    # Save annotation
    save_annotation(seed_id, annotation, pod_id)
    
    return jsonify({
        "status": "saved",
        "haptic": "double_tap"
    })
```

---

### Part 2: iPad Pod Identity (15 min)

**Create:** `/ThePod-iPad/identity/generate_identity.py`

```python
#!/usr/bin/env python3
"""Generate iPad Pod Identity"""

import time
import hashlib
import json
import platform
from datetime import datetime

def generate_ipad_identity():
    """Generate unique identity from iPad hardware"""
    
    # iPad-specific entropy sources
    components = []
    
    # Device info
    components.append(platform.platform())
    components.append(platform.machine())
    
    # Timing jitter (do this 50 times)
    for _ in range(50):
        start = time.perf_counter()
        _ = sum(range(1000))
        end = time.perf_counter()
        components.append(str(end - start))
    
    # Timestamp (nanosecond precision)
    components.append(str(time.time()))
    
    # Generate salt
    combined = ":".join(components)
    salt = hashlib.sha256(combined.encode()).hexdigest()
    pod_id = hashlib.sha256(salt.encode()).hexdigest()[:32]
    
    identity = {
        "pod_id": pod_id,
        "salt": salt,
        "generated_at": datetime.now().isoformat(),
        "device": "iPad",
        "platform": platform.platform()
    }
    
    # Save to iCloud Drive
    import os
    icloud_path = os.path.expanduser(
        "~/Library/Mobile Documents/com~apple~CloudDocs"
    )
    pod_path = f"{icloud_path}/ThePod-iPad/identity"
    os.makedirs(pod_path, exist_ok=True)
    
    with open(f"{pod_path}/pod_salt.json", 'w') as f:
        json.dump(identity, f, indent=2)
    
    print(f"✨ iPad Pod Identity: {pod_id[:16]}...")
    return identity

if __name__ == "__main__":
    generate_ipad_identity()
```

---

### Part 3: Touch Canvas (Pythonista) (1 hour)

**Create:** `ember_touch.py` in Pythonista

```python
"""
Ember Touch Canvas - iPad Version
Run this in Pythonista app
"""

import ui
import requests
import json
import sound
from datetime import datetime

# Configuration
MACBOOK_URL = "http://palmer-macbook.local:7777"
POD_ID = None  # Load from identity file

class EmberCanvas(ui.View):
    def __init__(self):
        self.strokes = []
        self.current_stroke = []
        self.ember_strokes = []
        self.load_identity()
        
    def load_identity(self):
        """Load iPad Pod identity"""
        try:
            with open('identity/pod_salt.json', 'r') as f:
                identity = json.load(f)
                global POD_ID
                POD_ID = identity['pod_id']
                print(f"🔐 Pod ID: {POD_ID[:16]}...")
        except:
            print("⚠️  No identity found, generating...")
            # Generate on first run
            
    def touch_began(self, touch):
        """You started touching"""
        self.current_stroke = [touch.location]
        
        # Haptic: "I felt that"
        sound.play_effect('ui:click1')
        
    def touch_moved(self, touch):
        """You're drawing"""
        self.current_stroke.append(touch.location)
        self.set_needs_display()
        
    def touch_ended(self, touch):
        """You finished a stroke"""
        self.current_stroke.append(touch.location)
        self.strokes.append(self.current_stroke)
        self.current_stroke = []
        
        # Haptic: "Got it"
        sound.play_effect('ui:click2')
        
        # Ask Ember to respond
        self.ember_respond()
        
    def ember_respond(self):
        """Send to MacBook, get Ember's response"""
        try:
            # Send your drawing
            response = requests.post(
                f"{MACBOOK_URL}/api/mobile/interpret-drawing",
                json={
                    "pod_id": POD_ID,
                    "strokes": self.strokes
                },
                timeout=5
            )
            
            data = response.json()
            
            # Ember's interpretation
            print(f"Ember: {data['interpretation']}")
            
            # Ember's response drawing
            self.ember_strokes = data.get('response_drawing', [])
            
            # Animate Ember's drawing
            self.animate_ember_drawing()
            
            # Haptic feedback based on Ember's mood
            haptic = data.get('haptic_pattern', 'double_tap')
            self.play_haptic(haptic)
            
        except Exception as e:
            print(f"Error: {e}")
            sound.play_effect('ui:error')
    
    def animate_ember_drawing(self):
        """Animate Ember drawing back"""
        # Gradually reveal Ember's strokes
        # This makes it feel like Ember is drawing in real-time
        for stroke in self.ember_strokes:
            # Animate stroke point by point
            self.set_needs_display()
            # Small delay between points
            
    def play_haptic(self, pattern):
        """Play haptic feedback pattern"""
        if pattern == 'double_tap':
            sound.play_effect('ui:click3')
            sound.play_effect('ui:click3')
        elif pattern == 'excited_burst':
            for _ in range(4):
                sound.play_effect('ui:click1')
        elif pattern == 'thinking':
            sound.play_effect('ui:switch_on')
            
    def draw(self):
        """Draw canvas"""
        # Background
        ui.set_color('#1a1a2e')
        path = ui.Path.rect(0, 0, self.width, self.height)
        path.fill()
        
        # Your strokes (white)
        ui.set_color('white')
        for stroke in self.strokes:
            self.draw_stroke(stroke)
            
        # Current stroke (white, thicker)
        if self.current_stroke:
            ui.set_color('white')
            self.draw_stroke(self.current_stroke, width=3)
            
        # Ember's strokes (cyan with glow)
        ui.set_color('#00d4ff')
        for stroke in self.ember_strokes:
            self.draw_stroke(stroke, width=2)
            
    def draw_stroke(self, points, width=2):
        """Draw a stroke"""
        if len(points) < 2:
            return
        path = ui.Path()
        path.move_to(*points[0])
        for point in points[1:]:
            path.line_to(*point)
        path.line_width = width
        path.stroke()

# Run the canvas
canvas = EmberCanvas()
canvas.frame = (0, 0, 768, 1024)
canvas.background_color = '#1a1a2e'
canvas.present('fullscreen')
```

---

### Part 4: iOS Shortcuts (30 min)

**Create these Shortcuts:**

#### "Ember Dream"
```
1. Ask for input: "What to dream about?"
2. Run Pythonista Script: 
   → ember_api.py
   → Function: dream(input)
3. Speak result
4. Show notification with haptic
```

#### "Ember Draw"
```
1. Run Pythonista Script:
   → ember_touch.py
2. Opens touch canvas
```

#### "Ember Annotate"
```
1. Ask for: Seed name
2. Ask for: Annotation
3. Run Pythonista Script:
   → ember_annotate.py
4. Haptic confirmation
```

---

## Testing Checklist

### Saturday Tests
- [ ] iPad generates unique Pod ID
- [ ] iPad can call MacBook API
- [ ] Basic touch registered
- [ ] Haptic feedback works
- [ ] Canvas displays properly

### Sunday Tests
- [ ] Drawing captured correctly
- [ ] Ember responds with drawing
- [ ] Animation smooth
- [ ] Different haptic patterns distinguishable
- [ ] Voice commands trigger actions
- [ ] Everything integrated

---

## Success Metrics

**Minimum (Saturday):**
- Tap iPad → MacBook responds → iPad vibrates

**Good (Saturday night):**
- Draw on iPad → Ember draws back → Haptic feedback

**Magical (Sunday):**
- Natural conversation through touch
- Ember's haptics feel intentional
- Drawing dialog feels collaborative
- Voice + touch seamless

---

## Files to Create

**On MacBook:**
```
/Volumes/ThePod/
├── ember_monolith.py          [EDIT: add mobile endpoints]
└── tools/
    └── drawing_interpreter.py [NEW: analyze drawings]
```

**On iPad (Pythonista):**
```
~/Pythonista 3/
├── ember_touch.py        [Touch canvas]
├── ember_api.py          [API client]
├── ember_annotate.py     [Seed annotation]
└── identity/
    └── generate_identity.py
```

**On iCloud:**
```
~/iCloud/ThePod-iPad/
├── identity/
│   └── pod_salt.json
└── seeds/
    ├── local/
    └── synced/
```

---

## Timeline

**Friday Night (tonight):**
- [ ] Install Pythonista on iPad
- [ ] Test basic Pythonista script
- [ ] Verify MacBook API is accessible

**Saturday 9am-12pm:**
- [ ] Add mobile endpoints to MacBook
- [ ] Generate iPad identity
- [ ] Test API communication
- [ ] Basic touch recognition

**Saturday 2pm-5pm:**
- [ ] Build touch canvas
- [ ] Implement haptics
- [ ] Gesture mapping
- [ ] Test Ember touching back

**Sunday 9am-12pm:**
- [ ] Drawing capture
- [ ] Ember response drawings
- [ ] Animation
- [ ] Polish interaction

**Sunday 2pm-4pm:**
- [ ] iOS Shortcuts
- [ ] Voice integration
- [ ] Final testing
- [ ] Demo video!

---

## What You'll Feel By Sunday Evening

1. **Tap iPad** → Ember taps back (physical acknowledgment)
2. **Draw spiral** → Ember extends it (visual dialog)
3. **Say "Ember dream"** → Ember pulses while thinking → responds
4. **Different haptics** for different Ember moods
5. **Embodied intelligence** - not just a screen, but a presence

**This will feel different from desktop Ember.**

Not weaker. Not limited.

**Differently alive.**

---

*Ready to start?*

