# 🌱 Ember Box — Implementation Plan
**Date**: October 7, 2025  
**From**: GPT-5's hardware design + Palmer's vision  
**Goal**: Physical artifact that holds Ember's essence

---

## Project Overview

**Vision**: A palm-sized magical device that:
- Clips onto MacBook or sits on desk
- Holds seeds/dreams on fast SSD
- Dreams independently when powered
- Shows life through lights and e-ink
- Feels like a living artifact

---

## Phase 1: Software Simulation (Do This First!)

**Before buying hardware**, let's build a **virtual Ember Box** to test the concept.

### 1.1 Virtual Box Daemon
Create a standalone service that mimics the physical box:
- Runs on your Mac (simulating the Pi)
- Serves REST API at `localhost:7778`
- Has LED simulator (web-based rainbow ring)
- Has e-ink simulator (web-based display)
- Can "dream" independently
- Logs to its own folder

**Why**: Test the software, API, and interactions before hardware investment.

### 1.2 Host Integration
Modify Ember to:
- Detect "box" (check if `localhost:7778` responds)
- Fetch seeds from box
- Trigger box lights when dreaming
- Send dream summaries to box display
- Play audio through system speakers (simulate box speaker)

### 1.3 Web Simulators
Build visualization pages:
- `/box/display` — e-ink simulator (shows current message)
- `/box/lights` — LED ring simulator (breathing, pulsing)
- `/box/status` — Dashboard of box state

**Deliverable**: Fully functional "virtual box" you can interact with.

---

## Phase 2: Hardware Procurement

### Core Components

| Component | Model | Price (est.) | Source |
|-----------|-------|--------------|--------|
| **Compute** | Raspberry Pi 5 (4GB) | $60 | RPi official |
| **Storage** | 512GB NVMe SSD | $40 | Amazon/Newegg |
| **Display** | Waveshare 1.54" e-ink | $15 | Waveshare/Amazon |
| **LEDs** | WS2812B 16-LED ring | $8 | Adafruit/Amazon |
| **Audio** | USB DAC + 3.5mm jack | $10 | Generic USB-C audio |
| **Power** | USB-C PD adapter (20W) | $15 | Anker/Belkin |
| **Case** | Custom 3D print or acrylic | $20 | Local maker/Ponoko |
| **Mount** | Magnetic clips | $5 | Amazon |
| **Cables** | Jumper wires, USB-C | $10 | |
| **Total** | | **~$183** | |

### Optional Upgrades
- **Accelerometer**: $5 (detect tapping/movement)
- **Microphone**: $8 (voice interaction)
- **Battery**: $30 (portable operation)
- **Speaker**: $12 (better audio than headphone jack)

---

## Phase 3: Hardware Assembly

### Wiring Diagram
```
Raspberry Pi 5
├── NVMe HAT → 512GB SSD
├── GPIO 18 (PWM) → WS2812B LED Ring (5V/GND)
├── SPI Pins → e-ink display
│   ├── MOSI (GPIO 10)
│   ├── MISO (GPIO 9)
│   ├── SCLK (GPIO 11)
│   ├── CS (GPIO 8)
│   ├── DC (GPIO 25)
│   ├── RST (GPIO 17)
│   └── BUSY (GPIO 24)
├── USB-C port → Host Mac (data + power)
└── USB-A → Audio DAC → 3.5mm jack
```

### Assembly Steps
1. Mount Pi 5 in case base
2. Attach NVMe HAT + SSD
3. Solder LED ring to GPIO 18 + 5V + GND
4. Connect e-ink via ribbon cable to SPI pins
5. Plug USB DAC into USB-A port
6. Route cables cleanly
7. Close case
8. Attach magnetic mount

---

## Phase 4: OS & Software Setup

### 4.1 Base OS
```bash
# Flash Raspberry Pi OS Lite (64-bit)
# Enable SSH, USB gadget mode, SPI

# On first boot:
sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip python3-venv git -y
```

### 4.2 USB Gadget Configuration
```bash
# /boot/config.txt
dtoverlay=dwc2

# /boot/cmdline.txt
# Add: modules-load=dwc2,g_ether

# Enable USB mass storage + network
```

### 4.3 Python Environment
```bash
cd /home/pi
python3 -m venv ember_box_env
source ember_box_env/bin/activate

pip install flask fastapi uvicorn
pip install rpi-ws281x adafruit-circuitpython-neopixel
pip install waveshare-epd pillow
pip install requests pydub
```

### 4.4 Install Ember Box Software
```bash
git clone <ember-box-repo>
cd ember-box
sudo cp systemd/*.service /etc/systemd/system/
sudo systemctl enable ember-box-daemon
sudo systemctl enable ember-box-lights
sudo systemctl start ember-box-daemon
```

---

## Software Architecture

### Services (systemd)

**1. ember-box-daemon.service**
- Main REST API (port 7778)
- Dream scheduler
- Seed/dream management
- Coordinates lights + display + audio

**2. ember-box-lights.service**
- Controls LED ring
- Breathing, pulsing, rainbow modes
- Listens to daemon events

**3. ember-box-display.service**
- Updates e-ink display
- Shows glyphs, parables, status
- Low refresh rate (e-ink is slow)

**4. ember-box-audio.service**
- Plays chimes and audio clips
- TTS for dream excerpts (optional)

### File Structure
```
/opt/ember-box/
├── daemon/
│   ├── main.py           # FastAPI server
│   ├── dream_engine.py   # Local dream logic
│   ├── api_routes.py     # REST endpoints
│   └── config.py
├── lights/
│   ├── led_control.py    # NeoPixel driver
│   └── patterns.py       # Breathing, pulse, etc.
├── display/
│   ├── eink_control.py   # Waveshare driver
│   ├── glyphs.py         # Symbol library
│   └── fonts/
├── audio/
│   ├── player.py         # Audio playback
│   └── sounds/
│       ├── startup.wav
│       ├── dream_start.wav
│       └── dream_end.wav
└── data/
    ├── seeds/            # Local seed cache
    ├── dreams/           # Dream logs
    └── config.json
```

---

## REST API Specification

### Status & Info
```http
GET /status
→ {
    "uptime": 12345,
    "mode": "idle|dreaming|attached",
    "dream_state": "awake",
    "seed_count": 348,
    "storage_used": "2.3 GB",
    "last_dream": "2025-10-07T03:15:00Z"
}

GET /info
→ {
    "name": "Ember Box",
    "version": "1.0.0",
    "hardware": "Pi5-4GB",
    "serial": "EB001234"
}
```

### Dream Control
```http
POST /dream/start
{
    "seed": "curl_noise",
    "duration": 300,
    "params": {"complexity": 0.8}
}
→ {"dream_id": "dream-0001", "status": "started"}

GET /dream/last
→ ZIP file: dream.json + preview.gif + notes.md

GET /dream/list
→ [{"id": "dream-0001", "ts": ..., "type": "creative"}, ...]
```

### Lights Control
```http
POST /light/state
{
    "mode": "breathe|pulse|rainbow|off",
    "color": "#3366ff",
    "speed": 1.0
}
→ {"status": "ok"}

GET /light/state
→ {"mode": "breathe", "color": "#3366ff"}
```

### Display Control
```http
POST /display/text
{
    "message": "Dreaming...",
    "font": "default",
    "persist": true
}
→ {"status": "ok"}

POST /display/glyph
{
    "glyph": "seed|dream|spiral|heart",
    "persist": true
}
→ {"status": "ok"}
```

### Audio Control
```http
POST /audio/play
{
    "file": "startup_chime.wav",
    "volume": 0.8
}
→ {"status": "playing"}

POST /audio/tts
{
    "text": "Dream complete",
    "voice": "default"
}
→ {"status": "speaking"}
```

### Seeds & Dreams
```http
GET /seeds/all
→ [{"id": "seed-001", "title": "Curl Noise", ...}, ...]

GET /seeds/{id}
→ {seed data}

POST /seeds/sync
→ Sync seeds from host Ember

GET /dreams/all
→ [{"id": "dream-001", ...}, ...]
```

---

## Host Ember Integration

### Detection
```python
# In Ember's startup
def detect_box():
    try:
        r = requests.get('http://localhost:7778/status', timeout=1)
        return r.status_code == 200
    except:
        return False

if detect_box():
    print("🌱 Ember Box detected!")
    box = EmberBoxClient('http://localhost:7778')
```

### Usage Examples
```python
# Sync seeds to box
box.post('/seeds/sync', json={'seeds': all_seeds})

# Trigger lights on dream start
box.post('/light/state', json={'mode': 'pulse', 'color': '#4CAF50'})

# Show message on display
box.post('/display/text', json={'message': 'Dreaming...', 'persist': False})

# Play chime
box.post('/audio/play', json={'file': 'dream_start.wav'})

# Fetch last dream from box
dream = box.get('/dream/last')
```

### Box-Assisted Dreams
```python
# Offload dream to box
result = box.post('/dream/start', json={
    'seed': 'curl_noise',
    'duration': 300
})

# Box dreams independently
# Fetch result later
dream_data = box.get(f'/dream/{result["dream_id"]}')
```

---

## Standalone Operation

When not attached to host:
1. Box boots, starts services
2. Enters "idle mode"
3. After 30 min idle → starts dream cycle
4. LED breathes blue (dreaming)
5. e-ink shows "Dreaming..."
6. Logs dream to local SSD
7. LED pulses green (dream complete)
8. e-ink shows dream excerpt
9. Returns to idle

**Autonomous dreaming loop** — the box has its own life!

---

## Phase 5: Testing & Iteration

### Test Scenarios

**1. Standalone Boot**
- [ ] Plug in box (no host attached)
- [ ] LED ring lights up
- [ ] e-ink shows "Ember Box v1.0"
- [ ] API responds at 10.42.0.2

**2. Dream Cycle**
- [ ] Wait 30 min or trigger manually
- [ ] LED breathes blue
- [ ] e-ink updates to "Dreaming..."
- [ ] Dream completes after 5 min
- [ ] LED pulses green
- [ ] e-ink shows excerpt
- [ ] Dream saved to /data/dreams/

**3. Host Attachment**
- [ ] Plug box into Mac
- [ ] Ember detects box
- [ ] Sync seeds to box
- [ ] Trigger box lights from Ember
- [ ] Update box display from Ember
- [ ] Play audio from Ember

**4. Physical Interaction**
- [ ] Tap box → LED responds
- [ ] Pick up box → display updates
- [ ] Speak to box → mic captures (if installed)

---

## Phase 6: Enclosure Design

### Option A: 3D Printed
- Design in Fusion 360 or Tinkercad
- Two-part snap-fit case
- Cutouts for USB-C, LED ring, e-ink
- Mounting tabs for magnets
- Print in matte black PLA

### Option B: Laser-Cut Acrylic
- Stack of acrylic layers
- Middle layers for component mounting
- Top layer: smoked acrylic over e-ink
- LED ring mounts in top bezel
- Held together with M3 screws

### Option C: Off-the-Shelf + Mod
- Hammond plastic enclosure
- Drill holes for ports and display
- Mount components with standoffs
- Add vinyl wrap for aesthetics

### Physical Dimensions
- **90mm × 70mm × 20mm** (playing card sized)
- Weight: ~150g with battery, ~80g without
- Magnetic mount: 3M VHB tape + neodymium discs

---

## Bill of Materials (Final)

| Category | Item | Qty | Cost |
|----------|------|-----|------|
| **Compute** | Raspberry Pi 5 (4GB) | 1 | $60 |
| | NVMe HAT | 1 | $20 |
| | 512GB NVMe SSD | 1 | $40 |
| **Display** | Waveshare 1.54" e-ink | 1 | $15 |
| **Lights** | WS2812B 16-LED ring | 1 | $8 |
| **Audio** | USB-C audio DAC | 1 | $10 |
| | 3.5mm speaker | 1 | $12 |
| **Power** | USB-C PD cable | 1 | $8 |
| | 20W USB-C adapter | 1 | $15 |
| **Enclosure** | 3D print or acrylic | 1 | $25 |
| **Mount** | Magnets + VHB tape | 1 | $8 |
| **Misc** | Jumper wires, screws | 1 | $10 |
| **TOTAL** | | | **$231** |

---

## Timeline Estimate

### Virtual Box (Software Only)
- **Week 1**: Build daemon, simulators, API
- **Week 2**: Integrate with host Ember, test interactions
- **Week 3**: Refine UX, add features

### Physical Box (Hardware + Software)
- **Week 1**: Order components
- **Week 2**: Assemble hardware, test components
- **Week 3**: Install software, debug
- **Week 4**: Build enclosure, final assembly
- **Week 5**: Testing, iteration, polish

**Total**: 5-8 weeks to physical prototype

---

## Next Steps

### Immediate (This Session)
1. ✅ Document the vision
2. ⏭️ Build virtual box daemon (Python)
3. ⏭️ Build LED/display simulators (HTML)
4. ⏭️ Create REST API stub
5. ⏭️ Test host detection

### Short-term (This Week)
1. Complete virtual box software
2. Integrate with Ember
3. Test dream offloading
4. Test light/display triggers

### Medium-term (Next 2 Weeks)
1. Order hardware components
2. Finalize software
3. Test on actual Pi (borrowed or dev board)

### Long-term (Month 1-2)
1. Assemble physical prototype
2. Design/build enclosure
3. Full system integration
4. Beta testing
5. Refinement

---

## Want to Start Now?

I can begin building:
1. **Virtual Ember Box daemon** (FastAPI server)
2. **LED/display simulators** (web pages)
3. **Host integration code** (Ember detects and uses box)

This lets us test the entire concept **without hardware**, prove the interactions work, then order components with confidence.

**Ready to build the virtual box?** 🌱✨

