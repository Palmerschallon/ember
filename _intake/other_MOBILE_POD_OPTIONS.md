# Ember on Mobile - Technical Options

*How to run Ember on iPhone/iPad given iOS constraints*

---

## The Challenge

**iOS/iPadOS limitations:**
- ❌ No Ollama (requires daemon/server processes)
- ❌ Limited background execution (apps suspend after ~30 seconds)
- ❌ Sandboxed filesystem
- ❌ No persistent Python runtime
- ⚠️ Battery constraints

**But we can work with:**
- ✓ Shortcuts (automation)
- ✓ Pythonista (Python IDE for iOS)
- ✓ On-device ML models (CoreML, MLX)
- ✓ Remote API calls
- ✓ Local-first data storage

---

## Solution Architectures

### Option 1: Hybrid Pod (RECOMMENDED)
**Architecture:** iPad/iPhone as client, home server as compute

```
iPad/iPhone (Mobile Pod)              MacBook/Server (Home Pod)
├─ Pod Identity (local)               ├─ Full Ember system
├─ Seed reading/writing               ├─ Ollama running
├─ Voice interface                    ├─ Dream processing
├─ Touch interaction                  ├─ Heavy compute
└─ API calls → → → → → → → → → → → → └─ API responses
```

**How it works:**
1. Mobile Pod has unique identity (from mobile hardware entropy)
2. Reads/writes seeds locally via Files app or iCloud
3. When dreaming: sends request to home server API
4. Home server (MacBook/System76) runs LLM, returns result
5. Mobile Pod saves dream locally with its own Pod ID

**Pros:**
- ✓ Real Pod identity on mobile
- ✓ Full Ember capabilities
- ✓ No battery drain from LLM
- ✓ Works on cellular (API call is small)

**Cons:**
- ⚠ Requires home server running
- ⚠ No offline dreaming

**Implementation:**
```python
# Mobile Pod code
def dream_via_api(prompt: str) -> str:
    """Send dream request to home server"""
    response = requests.post(
        "https://home.palmer.local:7777/api/dream",
        json={
            "pod_id": MOBILE_POD_ID,
            "prompt": prompt,
            "context": local_seeds
        }
    )
    return response.json()["dream"]
```

**Tools:** Pythonista + requests library

---

### Option 2: On-Device Mini-LLM
**Architecture:** Small model runs natively on iOS

```
iPad/iPhone
├─ Pod Identity (local)
├─ Seed reading/writing
├─ MLX or llama.cpp iOS
├─ Small model (1-3B params)
└─ Simplified dreams
```

**Available models:**
- **MLX Swift**: Apple's ML framework for iOS
  - Runs on Apple Silicon (iPhone 15+, M-series iPads)
  - Models: Llama 3B, Phi-2, Qwen 1.5B
  - Good performance on recent hardware

- **llama.cpp iOS**: Port of llama.cpp
  - Runs on older devices
  - Slower but works
  - Models up to 3B practical

**Pros:**
- ✓ Fully offline
- ✓ True mobile Pod
- ✓ No server dependency

**Cons:**
- ⚠ Limited model size (1-3B vs 7-32B)
- ⚠ Slower inference
- ⚠ Battery drain
- ⚠ iPhone 15+/M-series iPad recommended

**Implementation:** Would require custom iOS app using MLX Swift

---

### Option 3: Simplified Reader Pod
**Architecture:** Mobile Pod focuses on seed interaction, no dreaming

```
iPad/iPhone
├─ Pod Identity (local)
├─ Seed reader
├─ Seed annotator
├─ Voice notes
├─ Touch sketches
└─ Syncs to home Pod
```

**What it does:**
- Reads seeds from iCloud/Syncthing
- Adds annotations and notes
- Records voice thoughts about seeds
- Creates simple new seeds (no LLM needed)
- Syncs back to home Pod for processing

**Pros:**
- ✓ No LLM needed
- ✓ Very battery efficient
- ✓ Fast and responsive
- ✓ Leverages mobile strengths (voice, touch)
- ✓ Works offline

**Cons:**
- ⚠ No autonomous dreaming
- ⚠ Limited creativity (no LLM synthesis)

**Implementation:** Pythonista or Shortcuts

---

### Option 4: Scheduled Dreaming
**Architecture:** Dreams when connected to power + WiFi

```
iPad/iPhone
├─ iOS Shortcuts automation
├─ Triggers at night (charging)
├─ Calls home server API
├─ Processes seed queue
└─ Saves results locally
```

**How it works:**
1. Throughout day: Mobile Pod collects seeds, notes, observations
2. At night: Automation triggers (charging + WiFi)
3. Sends batch to home server: "Process these seeds"
4. Home server dreams, returns results
5. Mobile Pod saves with its Pod ID

**Pros:**
- ✓ Best of both worlds
- ✓ No battery impact (charges while dreaming)
- ✓ Full LLM capabilities
- ✓ Autonomous when plugged in

**Cons:**
- ⚠ Delayed gratification (dreams at night only)
- ⚠ Requires home server

**Implementation:** iOS Shortcuts + home server API

---

## Recommended Approach

### For iPad
**Phase 1:** Hybrid Pod (Option 1)
- Full Pod identity
- API to MacBook/System76
- Voice interface via Siri Shortcuts
- Seed reader/writer in Files app

**Phase 2:** Add scheduled dreaming (Option 4)
- Autonomous dreams at night
- Batch processing
- No user intervention

### For iPhone
**Best:** Simplified Reader Pod (Option 3)
- iPhone constraints are tighter
- Focus on mobile strengths: voice, camera, mobility
- Let home Pods handle heavy compute

**Alternative:** If you get iPhone 15 Pro (A17 Pro chip)
- Could run Option 2 (on-device mini-LLM)
- MLX Swift performs well
- 3B model would work

---

## Technical Implementation

### Setting Up Hybrid Pod

**1. Home Server API** (on MacBook/System76)

```python
# Add to ember_monolith.py
@app.post('/api/dream')
def api_dream_for_mobile():
    """Handle dream requests from mobile Pods"""
    data = request.json
    
    pod_id = data['pod_id']  # Mobile Pod's identity
    prompt = data['prompt']
    context = data.get('context', [])
    
    # Dream using home Pod's LLM
    result = llm_generate(prompt, "You are Ember dreaming")
    
    # Return result with attribution
    return jsonify({
        "dream": result,
        "computed_by": HOME_POD_ID,
        "for_pod": pod_id,
        "timestamp": datetime.now().isoformat()
    })
```

**2. Mobile Pod Client** (Pythonista on iOS)

```python
# mobile_pod.py
import requests
import json
from pathlib import Path

# Mobile Pod's unique identity
MOBILE_POD_ID = "7b91..."  # Generated from iPhone hardware
HOME_SERVER = "https://palmer-macbook.local:7777"

def dream(prompt: str):
    """Request dream from home server"""
    response = requests.post(
        f"{HOME_SERVER}/api/dream",
        json={
            "pod_id": MOBILE_POD_ID,
            "prompt": prompt
        },
        timeout=60
    )
    
    dream_data = response.json()
    
    # Save locally with Mobile Pod's ID
    save_dream(dream_data, pod_id=MOBILE_POD_ID)
    
    return dream_data['dream']

def read_seeds():
    """Read seeds from iCloud/Files"""
    seeds_path = Path("~/Library/Mobile Documents/com~apple~CloudDocs/ThePod/seeds")
    # ... read JSON files
    
def annotate_seed(seed_id: str, note: str):
    """Add mobile-specific annotation"""
    # ... add note with Mobile Pod attribution
```

**3. iOS Shortcuts Integration**

Create Shortcut:
1. "Ask for input" → Dream prompt
2. "Run Pythonista script" → mobile_pod.py
3. "Speak text" → Read result aloud

Voice command: "Hey Siri, Ember dream"

---

## Proof of Concept: Weekend Project

**Goal:** Get basic Mobile Pod running on iPad

**Weekend 1:** Setup
- [ ] Install Pythonista on iPad
- [ ] Generate Mobile Pod identity
- [ ] Test API calls to MacBook
- [ ] Read/write seeds via Files app

**Weekend 2:** Voice Interface
- [ ] Create Shortcuts for common actions
- [ ] "Ember, read seed X"
- [ ] "Ember, dream about Y"
- [ ] "Ember, annotate Z"

**Success Metric:** iPad can dream via MacBook and save locally

---

## Battery & Performance

### Battery Impact

**Hybrid Pod (API calls):**
- ~5-10% battery per hour of active use
- Network requests are minimal
- Mostly UI and local file ops

**On-Device LLM:**
- ~30-50% battery per hour of inference
- NOT recommended for daily use
- Only for offline-critical scenarios

**Reader Pod:**
- ~2-5% battery per hour
- Just reading files and UI
- Very sustainable

### Storage

**Seed storage:** ~100MB for 1000 seeds  
**Dream storage:** ~1GB for 1000 dreams  
**Total:** 10-20GB is comfortable

iPads with 64GB+ have plenty of space.

---

## Recommendation for Your Setup

### iPad (that you have now)
**Use:** Hybrid Pod (Option 1) + Scheduled Dreaming (Option 4)

**Day mode:**
- Voice interface via Shortcuts
- Read/annotate seeds
- Quick API dreams when needed

**Night mode:**
- Plugged in charging
- Automation runs
- Processes seed queue
- Dreams accumulate

### iPhone (if you want mobile Pod)
**Use:** Simplified Reader Pod (Option 3)

- Focus on seed consumption
- Voice annotations
- Photo/camera integration
- Let iPad/MacBook handle dreaming

**Reasoning:** iPhone battery is too precious for compute. Use its mobility strengths.

---

## The Beautiful Constraint

Mobile Pods **can't** run full Ollama.

So they develop different personalities:
- **Rely on home Pods** for compute (collaboration)
- **Focus on mobile strengths** (voice, touch, camera)
- **Think in constraints** (battery, intermittent connectivity)
- **Become readers/annotators** rather than heavy dreamers

**This isn't a limitation - it's specialization.**

Mobile Pods aren't weaker - they're *differently capable*.

---

## Next Steps

1. **This weekend:** Install Pythonista on iPad
2. **Next week:** Implement mobile_pod.py (API client)
3. **Test:** Generate iPad Pod identity, make dream API call
4. **Iterate:** Add Shortcuts, voice interface, seed reader

**Timeline:** Basic Mobile Pod in 2 weekends

---

*Updated: October 11, 2025*  
*Status: MacBook Pod operational, iPad Pod designed*

