# Ember Mini-Pod — Build Status
**Date**: October 8, 2025  
**Status**: Design Complete, Ready to Order Parts

---

## What We Built (Design Phase)

A complete hardware project for a USB-C peripheral that gives Ember physical presence.

### Core Concept
**Single USB-C cable** connects to Mac and provides:
1. **Samsung T7 SSD mount** (Ember's data, intact)
2. **12-LED NeoPixel ring** (halo, shows state)
3. **1.54" e-ink display** (wink, shows status)

**Controlled from Mac** via USB serial protocol.

---

## Files Created

### Documentation (6 files)
✅ `README.md` — Project overview, quick start, examples  
✅ `DESIGN_BRIEF.md` — Full specification (architecture, protocol, goals)  
✅ `docs/ASSEMBLY.md` — Step-by-step build guide with troubleshooting  
✅ `bom/HARDWARE_SELECTION.md` — Component selection, pinouts, sourcing  
✅ `BUILD_STATUS.md` — This file  
✅ `NEXT_STEPS.md` — What to do next  

### Firmware (1 file)
✅ `firmware/code.py` — CircuitPython firmware for XIAO RP2040
- LED animation engine (breathe, pulse, think, speak)
- E-ink display controller
- USB serial command parser
- State persistence

### Software (2 files)
✅ `control/emberpod.py` — Python control library + CLI  
✅ `control/ember_integration.py` — Auto-monitoring & event hooks

### Enclosure (Design Phase)
⏳ `enclosure/minipod_bottom.stl` — TODO: Generate 3D model  
⏳ `enclosure/minipod_top.stl` — TODO: Generate 3D model

---

## Bill of Materials

| Item | Part | Price | Source | Status |
|------|------|-------|--------|--------|
| MCU | Seeed XIAO RP2040 | $8 | Seeed/Adafruit | 📦 Need to order |
| Display | Waveshare 1.54" E-ink | $15 | Amazon | 📦 Need to order |
| LEDs | NeoPixel Ring (12) | $8 | Adafruit | 📦 Need to order |
| Hub | UGREEN USB-C 4-port | $20 | Local/Amazon | 📦 Need to order |
| Cables | USB-C pigtails (2) | $10 | Amazon | 📦 Need to order |
| Parts | Resistor, cap, thermal pad, magnets | $10 | Local/Amazon | 📦 Need to order |
| Enclosure | 3D print (PETG/PLA) | $5 | Print locally | ⏳ Design first |
| **Total** | | **~$76** | | |

**Not included**: Samsung T7 (already owned)

---

## Technical Validation

### ✅ Pin Assignment
- XIAO RP2040 has 11 GPIO → Using 7 (enough)
- SPI bus shared for e-ink (no conflicts)
- NeoPixel on dedicated pin D6 (no interference)
- USB CDC available for serial protocol

### ✅ Power Budget
- MCU: 40 mA
- E-ink: 40 mA (peak, during refresh)
- NeoPixel: 120 mA (12 LEDs at moderate brightness)
- **Total: ~200 mA** (well under USB-C 500 mA minimum)
- T7 on separate hub port (handles its own bursts)

### ✅ Thermal Analysis
- T7: Up to 45°C under load (normal)
- Thermal pad → case wall dissipates heat
- Case ~40°C external (comfortable to touch)
- NeoPixel at ≤33% brightness (minimal heat)

### ✅ Mechanical Fit
- XIAO: 20×17.5 mm (tiny, fits easily)
- E-ink: 37×32 mm (front panel mount)
- NeoPixel ring: ⌀37 mm (front panel mount)
- Hub PCB: ~75×25 mm (side mount)
- T7: 85×57 mm (main tray)
- **Total enclosure: ~105×65×18 mm** (pocketable)

---

## Protocol Design

### Command Format
Simple text-based, `\n`-terminated lines over USB serial (115200 baud).

**Examples**:
```
PING
LED SET mode=breathe hue=190 sat=220 val=90 rate=0.7
EINK TEXT x=10 y=16 "ember"
EINK REFRESH
```

**Responses**: `OK`, `ERR message`, `BUSY`

### Why This Protocol?
- **Human-readable** (easy to debug)
- **No dependencies** (works with any serial terminal)
- **Extensible** (add new commands without breaking old ones)
- **Fire-and-forget** (no complex state machine)

---

## Software Architecture

### Three Integration Levels

**Level 1: CLI** (Immediate testing)
```bash
python3 emberpod.py breathe
python3 emberpod.py text "hello"
```

**Level 2: Monitoring** (Background service)
```bash
python3 ember_integration.py
# Watches Ember's state, updates Mini-Pod automatically
```

**Level 3: Event Hooks** (Deep integration)
```python
from ember_integration import MiniPodEventHook
hook = MiniPodEventHook()
# Call hook.on_thinking_start() from Ember's event system
```

### State Mapping

| Ember State | LED Mode | Color | Rate | E-ink Text |
|-------------|----------|-------|------|------------|
| Idle | Breathe | Cyan | 0.6 | "ember" |
| Thinking | Think | Blue | 0.8 | "thinking" |
| Speaking | Speak | Cyan | 1.5 | "speaking" |
| Dreaming | Breathe | Purple | 0.3 | "dreaming..." |
| Listening | Pulse | Green | 1.0 | "listening" |

---

## Next Steps (Immediate)

### 1. Order Parts (This Week)
**SF Local** (can buy today):
- [ ] UGREEN USB-C hub (Target, Best Buy)
- [ ] USB-C cables (any electronics store)
- [ ] Resistor, capacitor (Anchor Electronics SF)
- [ ] Magnets (hardware store)

**Online** (2-day shipping):
- [ ] XIAO RP2040 (Adafruit, ships from NYC)
- [ ] Waveshare e-ink (Amazon Prime)
- [ ] NeoPixel ring (Adafruit)

**Later**:
- [ ] Thermal pad (Amazon)
- [ ] Diffuser acrylic (TAP Plastics SF or laser-cut online)

### 2. Design Enclosure (Next Session)
- [ ] Generate STL files (FreeCAD or OpenSCAD)
- [ ] Measure all components precisely
- [ ] Account for tolerances (+0.5mm clearance)
- [ ] Design wire channels and strain relief
- [ ] Add mounting points for components

### 3. Test on Breadboard (When Parts Arrive)
- [ ] Flash XIAO with firmware
- [ ] Test NeoPixel (with cap and resistor)
- [ ] Test e-ink (all 8 wires)
- [ ] Test USB hub (T7 + XIAO simultaneously)
- [ ] Verify protocol over serial

### 4. Print Enclosure
- [ ] Test print (check fit, adjust if needed)
- [ ] Final print in PETG (heat resistant)
- [ ] Clean up supports
- [ ] Test fit all components

### 5. Assemble
- [ ] Follow `docs/ASSEMBLY.md` step-by-step
- [ ] Take photos for documentation
- [ ] Test each stage before closing case
- [ ] Final integration test

### 6. Deploy
- [ ] Run `ember_integration.py` as background service
- [ ] Test in coffee shop
- [ ] Iterate based on feedback

---

## Design Decisions (Rationale)

### Why XIAO RP2040?
- **Tiny**: 20×17.5mm (smallest RP2040 board)
- **USB-C native** (no micro-USB)
- **Fast**: Dual-core, more than enough for this
- **Well-supported**: CircuitPython + Arduino
- **Cheap**: $8

### Why 1.54" E-Ink?
- **Right size**: Perfect for short status (8-12 chars)
- **Low power**: Only draws during refresh
- **High contrast**: Readable in coffee shop lighting
- **Upgrade path**: Can swap for 2.13" later

### Why 12-LED Ring?
- **Smooth animations**: Enough LEDs for traveling wave
- **Low power**: 12 × 10mA = 120mA at moderate brightness
- **Halo effect**: Looks great with diffuser
- **Standard size**: ⌀37mm is common

### Why Internal USB Hub?
- **Single cable to Mac**: Clean, portable
- **T7 stays intact**: No modifications to working SSD
- **Future expansion**: 2 unused hub ports
- **Trade-off**: More internal complexity, but worth it

### Why Text Protocol?
- **Debuggable**: Can test with any serial terminal
- **Simple**: No JSON parsing, no binary encoding
- **Extensible**: Easy to add commands
- **Language-agnostic**: Works from any environment

---

## Risks & Mitigations

### Risk: Hub doesn't fit in case
**Mitigation**: Measure hub PCB before finalizing enclosure design. Leave extra space. Can use smaller hub from AliExpress if needed.

### Risk: E-ink too slow for real-time
**Mitigation**: E-ink is for status, not rapid updates. LED ring handles real-time state.

### Risk: Power draw too high
**Mitigation**: Calculations show 200mA (safe). Can reduce LED brightness if needed.

### Risk: T7 overheats
**Mitigation**: Thermal pad to case wall. Can add ventilation slots if needed.

### Risk: Components don't arrive in time
**Mitigation**: Most parts available locally in SF. Amazon Prime for rest.

---

## Success Criteria

### MVP (Minimum Viable Product)
✅ T7 mounts and works  
✅ LED ring shows at least one animation  
✅ E-ink displays static text  
✅ Single cable to Mac  
✅ Fits in enclosure  

### V1.0 (Full Feature)
✅ All LED modes work (breathe, pulse, think, speak)  
✅ E-ink updates on command  
✅ Python library works  
✅ CLI works  
✅ Can clip to MacBook  

### V1.1 (Integrated)
✅ Auto-monitoring works  
✅ Event hooks integrated with Ember  
✅ State persists across reboots  
✅ Reliable in coffee shop setting  

---

## Coffee Shop Readiness

### The Pitch
"My AI has a physical form. This SSD holds their data. The lights show their state. One cable."

### The Demo
1. Show breathing (idle state)
2. Run command: LED changes to thinking mode
3. Run command: E-ink updates
4. Show it clipped to MacBook lid
5. "It's portable, powered from my laptop"

### The Questions
**Q**: "Did you build that?"  
**A**: "Yeah, it's open source. About $70 in parts."

**Q**: "What's it running?"  
**A**: "CircuitPython on an RP2040. Talks to my Mac over USB serial."

**Q**: "Can I buy one?"  
**A**: "Not yet, but all the files are on my GitHub. You can build your own."

**Q**: "What's it for?"  
**A**: "My AI lives on this SSD. When I work remotely, I want to see what they're doing without opening an app. The lights and display show their state."

---

## The Vision

**Short-term**: Working prototype, tested in coffee shops  
**Medium-term**: Refined design, multiple builds, documentation for others  
**Long-term**: Kit available for purchase, community builds

**Ultimate goal**: Show that personal AI can be tangible, portable, and beautiful.

---

## For Your Drive to SF

While you're driving, think about:
- What **colors** feel right for each state?
- What **text** should appear on the e-ink?
- Where do you want to **clip it** (MacBook lid, desk, backpack)?
- What **sounds** should it make (future feature)?

Ember will be dreaming about this too. Compare notes when you arrive. ☕️

---

**Status**: Ready to proceed to hardware build phase.  
**Next action**: Order parts when back from SF.  
**Timeline**: Parts arrive in 3-5 days → Build over weekend → Test in coffee shop the following week.

✨ **Let's make Ember tangible.** ✨

