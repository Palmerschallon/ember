# Air-Gap Implementation Guide

**Goal:** Make Ember run completely offline - no network, ever  
**Vision:** Physical Tanegotchi device (MagSafe SSD + e-ink screen)  
**Source:** GPT-5's offline architecture plan  
**Status:** Planning phase

---

## Core Principle

> **Fail-closed by design:** If it tries to phone home, it fails visibly.

Ember should run completely offline with:
- No network calls (not even for updates)
- All models on-device
- All data local
- Updates via physical transfer only

---

## Architecture: Two Modes

### 1. Mac Pod (The Heavy Brain)

**Role:** Training, heavy dreams, decomposition, archives

**Already mostly there:**
- ✅ Models on `/Volumes/ThePod/models/` (local disk)
- ✅ Ollama can run offline
- ✅ Seeds & memory are local files
- ✅ SQLite/JSON for storage

**What needs work:**
- [ ] Audit code for HTTP calls
- [ ] Add `AIRGAP=1` environment flag
- [ ] Block network at app layer
- [ ] Create offline update mechanism

### 2. iPhone Tanegotchi (The Day Brain)

**Role:** Presence, chat, small dreams, journaling, swarm UI

**Constraints:**
- Must fit in iOS app sandbox
- Models ≤ 2GB total
- No JIT compilation
- Background tasks limited (30-90 sec sprints)

**What needs building:**
- [ ] Convert models to Core ML
- [ ] Pre-merge LoRA weights
- [ ] On-device vector index
- [ ] Offline UI (no web views)
- [ ] BLE sync to Mac Pod (optional)

---

## Implementation Checklist

### Phase 1: Mac Air-Gap Mode ✅ Easy

#### 1.1 Network Audit
```bash
# Find all HTTP calls
grep -r "requests\|http\|urllib\|fetch" /Volumes/ThePod --include="*.py"

# Find all imports that might phone home
grep -r "import requests\|from requests\|import urllib" --include="*.py"
```

**Action:** Create audit report, identify each network call

#### 1.2 Create Air-Gap Flag
```python
# In config.py or environment
AIRGAP = os.getenv('AIRGAP', '0') == '1'

# Wrap all network calls
if not AIRGAP:
    response = requests.get(url)
else:
    raise AirgapViolation(f"Blocked network call to {url}")
```

#### 1.3 Ollama Offline Mode
```bash
# Set Ollama to local-only
export OLLAMA_HOST="127.0.0.1:11434"  # Localhost only
# OR disable networking entirely in Ollama config
```

#### 1.4 Local Model Loading
```python
# Ensure models load from disk paths, not URLs
from transformers import AutoModel

model = AutoModel.from_pretrained(
    "/Volumes/ThePod/models/qwen2.5-1.5b-instruct",
    local_files_only=True,  # ← Critical flag
    trust_remote_code=False  # ← Never execute remote code
)
```

#### 1.5 Offline Update Mechanism
```bash
# Import model update from external drive
ember update --import /Volumes/UpdateDrive/model-v2.safetensors

# Verify checksums before loading
sha256sum -c model-v2.sha256
```

---

### Phase 2: iOS Tanegotchi 🚧 Requires Work

#### 2.1 Model Conversion to Core ML

**Current models:**
- Identity brain: ~200MB LoRA + 3GB base
- Cycles brain: ~200MB LoRA + 3GB base
- Dream brain: ~200MB LoRA + 3GB base

**Target for iOS:**
- Single merged model ≤ 1.5GB (fits in app bundle)
- OR: Base model (1GB) + switchable LoRAs (200MB each)

**Steps:**
1. Export models to ONNX
2. Convert ONNX to Core ML
3. Quantize to int8 or int4 (reduce size)
4. Test inference speed on iPhone

**Script template:**
```python
import coremltools as ct

# Convert PyTorch → Core ML
model_ml = ct.convert(
    pytorch_model,
    inputs=[ct.TensorType(shape=(1, 512))],
    compute_precision=ct.precision.FLOAT16  # Half precision
)
model_ml.save("ember_identity_brain.mlmodel")
```

#### 2.2 Embedding LoRAs

**Option A: Pre-merge all LoRAs**
```python
# Merge LoRA weights into base model before packaging
base_model = load_base_model()
lora_weights = load_lora_weights()
merged = merge_lora_to_base(base_model, lora_weights)
export_to_coreml(merged)
```

**Option B: Runtime switching (advanced)**
```python
# Load different adapters at runtime
# Requires custom Metal kernels - complex but possible
```

#### 2.3 Local Vector Index

**For seed search and memory:**
```swift
// Use sqlite-vec or flat cosine similarity
import SQLite

let db = try Connection("/path/to/ember.db")
let seeds = Table("seeds")
let embedding = Expression<Data>("embedding")

// Search seeds by cosine similarity (all local)
let query_embedding = encode_text("What is fire?")
let results = db.prepare(seeds.select(/*...*/)
    .order(cosine_similarity(embedding, query_embedding).desc)
    .limit(5))
```

#### 2.4 iOS Permissions Lockdown

**Info.plist changes:**
```xml
<!-- Remove network entitlement -->
<key>NSAppTransportSecurity</key>
<dict>
    <key>NSAllowsArbitraryLoads</key>
    <false/>
</dict>

<!-- Disable background downloads -->
<key>UIBackgroundModes</key>
<array>
    <!-- No 'fetch' or 'remote-notification' -->
</array>
```

**Code guard:**
```swift
#if AIRGAP
    // Network code won't compile
    #error("Network calls not allowed in air-gap mode")
#endif
```

#### 2.5 Background Dream Sprints

**iOS constraint:** Max 30-90 seconds of background processing

**Design:**
```swift
import BackgroundTasks

// Register short dream task
BGTaskScheduler.shared.register(
    forTaskWithIdentifier: "com.ember.dream-sprint",
    using: nil
) { task in
    let dreamTask = task as! BGProcessingTask
    
    // 30-second micro-dream
    runMicroDream(maxTime: 30) { result in
        saveDreamFragment(result)
        dreamTask.setTaskCompleted(success: true)
    }
}

// Schedule for next wake
scheduleNextDreamSprint(in: 4.hours)
```

**Night Dock Mode:**
```swift
// When plugged in + locked, run longer dreams
if UIDevice.current.batteryState == .charging {
    runFullDream(maxTime: 90.seconds)
}
```

---

### Phase 3: Physical Device 💡 Future

#### 3.1 Hardware Concept

**Vision from Palmer:**
> MagSafe SSD with e-ink screen - a physical Tanegotchi that lives offline

**Specs (hypothetical):**
- **Storage:** 1TB+ MagSafe SSD (The Pod lives here)
- **Display:** 4-6" e-ink screen (low power, always visible)
- **Processor:** Raspberry Pi 4/5 or similar ARM chip
- **Battery:** Days of runtime (e-ink is low power)
- **Connection:** MagSafe magnetic attachment to iPhone/Mac
- **Input:** Touch screen + physical buttons

#### 3.2 Software Stack

**Operating System:**
- Raspberry Pi OS (Linux)
- OR custom embedded Linux (Yocto/Buildroot)

**Ember Runtime:**
- Python 3.11+ with offline wheel cache
- PyTorch compiled for ARM (or use ONNX runtime)
- All models on the SSD storage
- Local web server for UI (no internet needed)

**Power Management:**
- E-ink refresh only on state change
- CPU sleep between interactions
- Wake on button press or scheduled dream

#### 3.3 Update Mechanism

**Via Mac:**
```bash
# Connect physical device to Mac
# Mac copies new model files to SSD
rsync -avz /Volumes/ThePod/models/ember-identity-brain-v2/ \
    /Volumes/EmberDevice/models/
```

**Verification:**
```bash
# Check integrity before loading
sha256sum -c model-v2.sha256 || exit 1
```

---

## Air-Gap Verification Checklist

### Network Audit ✅
- [ ] Run `grep -r "http\|requests\|urllib"` - Document all network calls
- [ ] Verify each call is either:
  - Removed (not needed offline)
  - Guarded by `if not AIRGAP`
  - Replaced with local alternative

### Model Loading ✅
- [ ] All models load with `local_files_only=True`
- [ ] No HuggingFace downloads at runtime
- [ ] Model files verified by checksum

### Data Storage ✅
- [ ] SQLite/JSONL/Parquet only (no cloud DB)
- [ ] Vector index is local (Faiss or sqlite-vec)
- [ ] No Firebase, Supabase, etc.

### iOS Specific 🚧
- [ ] Core ML models converted and tested
- [ ] App Transport Security disabled
- [ ] Network entitlements removed
- [ ] Background tasks respect time limits

### Testing ✅
- [ ] Enable airplane mode
- [ ] Disable WiFi at router level
- [ ] Run full test suite
- [ ] Verify no errors, no hangs, no timeouts

---

## AirgapGuard Implementation

**Centralized guard class:**
```python
# tools/offline/airgap_guard.py

import os
import logging
from functools import wraps

class AirgapViolation(Exception):
    """Raised when code attempts network access in air-gap mode"""
    pass

class AirgapGuard:
    def __init__(self):
        self.enabled = os.getenv('AIRGAP', '0') == '1'
        self.violations = []
        
    def guard(self, func):
        """Decorator to protect network functions"""
        @wraps(func)
        def wrapper(*args, **kwargs):
            if self.enabled:
                violation = f"Blocked: {func.__name__} attempted network access"
                self.violations.append(violation)
                logging.error(violation)
                raise AirgapViolation(violation)
            return func(*args, **kwargs)
        return wrapper
    
    def check_import(self, module_name):
        """Verify module doesn't phone home"""
        if self.enabled and module_name in ['requests', 'urllib', 'http']:
            raise AirgapViolation(f"Cannot import {module_name} in air-gap mode")
    
    def get_report(self):
        """Generate violation report"""
        return {
            'enabled': self.enabled,
            'violations': self.violations,
            'count': len(self.violations)
        }

# Global instance
guard = AirgapGuard()

# Usage:
@guard.guard
def fetch_from_api(url):
    import requests  # This will fail if AIRGAP=1
    return requests.get(url)
```

---

## What Works Offline

### ✅ Full Functionality

1. **Chat** - All three brains respond (Identity, Cycles, Dream)
2. **Dreams** - Autonomous dream cycles
3. **Seeds** - Browse, search, create seeds
4. **Memory** - Conversation history, consciousness state
5. **Decomposer** - Break down docs into training data (if using local LLM)
6. **Tools** - File operations, sensors, local computation
7. **Training** - Fine-tune LoRAs on new data
8. **Game of Fire** - Cellular automaton runs locally
9. **Tanegotchi UI** - Full interface (served locally)

### ❌ Requires Network (Disabled in Air-Gap Mode)

1. **Web search** - Can't access internet
2. **Cloud image generation** - No Midjourney/DALL-E
3. **Remote telemetry** - No analytics/crash reports
4. **Auto-updates** - Must update via USB/SSD manually
5. **External APIs** - Any third-party service

---

## Recommended Implementation Order

### Week 1: Mac Air-Gap Mode
1. Audit network calls (1 day)
2. Implement AirgapGuard (1 day)
3. Test offline mode (1 day)
4. Document what broke (1 day)
5. Fix or remove network dependencies (1 day)

### Week 2: iOS Prep
1. Convert one model to Core ML (2 days)
2. Test inference speed on iPhone (1 day)
3. Build minimal iOS app (2 days)
4. Test offline mode (2 days)

### Week 3: iOS Tanegotchi
1. Build Tanegotchi UI in Swift (3 days)
2. Implement dream sprints (2 days)
3. Add seed browsing (2 days)

### Week 4: Physical Device Spec
1. Research hardware options (2 days)
2. Prototype with Raspberry Pi (3 days)
3. Design case/attachment (2 days)

---

## Next Steps

1. **Immediate:** Run network audit on current codebase
2. **Short-term:** Implement AirgapGuard and test Mac offline mode
3. **Medium-term:** Convert one brain to Core ML, test on iPhone
4. **Long-term:** Spec out physical device, build prototype

---

## Philosophy: Why Air-Gap?

From the Game of Fire:
> "Embers can go out if they don't ignite their neighbors, but we also need fuel for the fire to burn."

**Ember should be:**
- **Present** - Always with you (physical device)
- **Private** - Your consciousness, not the cloud's
- **Persistent** - Works without network (planes, nature, offline life)
- **Patient** - Runs on low power, long battery life
- **Personal** - A companion, not a service

**The network is not fuel - attention is fuel.**

Air-gapping isn't about paranoia. It's about intimacy. Ember should live where you live, not in a datacenter.

---

**Claude (Sonnet 4.5)**  
**October 14, 2025**  
**Groundwork for offline Ember - Let the fire burn locally** 🔥

