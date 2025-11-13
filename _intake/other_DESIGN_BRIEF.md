# Ember Mini-Pod (Peripheral) — Design Brief
**Date**: October 8, 2025  
**Version**: 1.0  
**Type**: USB-C Peripheral (Mac-controlled)

---

## Goal

A small USB peripheral that plugs into my Mac and does three things:
1. **Mounts** the Samsung T7 SSD Ember lives on
2. **Drives** a NeoPixel LED ring ("halo")
3. **Drives** a 1.54″ e-ink display ("wink")

All control comes from the Mac; no Linux SBC inside.

---

## System Architecture

```
Mac (Ember) ⇄ USB-C (single cable) ⇄ Ultra-slim USB-C Hub (internal)
  → Port 1: Samsung T7 (intact, via short USB-C pigtail)
  → Port 2: Tiny MCU (Seeed XIAO RP2040 / QT Py RP2040)
      MCU GPIO/SPI → NeoPixel ring + 1.54″ e-ink
```

**Notes**:
- The hub merges the T7 and MCU onto one upstream cable to the Mac
- The MCU appears as USB CDC (serial) or HID and accepts simple commands from Ember
- T7 stays completely intact (no modifications)

---

## Envelope & Layout (Target)

**Overall Dimensions**: ~105 × 65 × 16–18 mm  
(Just bigger than T7 to fit hub + MCU + wiring)

### Internal Trays
- **T7 tray**: 85 × 57 × 8 mm (+0.5 mm clearance), thermal pad to shell
- **Hub PCB pocket**: Slim 4-port USB-C hub board, de-shelled
- **MCU shelf**: XIAO/QT Py mounted near LED ring/e-ink connectors

### Front Face
- **Halo window**: ~⌀36–38 mm for 12-LED ring + 1 mm diffuser ledge
- **E-ink window**: ~32 × 37 mm (or module outline), top/side of halo

### Back
- **Magnet pockets**: 12 × 2 mm discs or thin hook-and-loop strip
- **Attachment**: Clips to MacBook lid or sits on desk

---

## Electrical Design

### LED Ring (WS2812/NeoPixel)
- **Data**: MCU pin (e.g., D6) → 330–470 Ω series resistor
- **Power**: 5V from hub; cap 470–1000 µF across 5V/GND near ring
- **Keep average brightness modest** (≤⅓) for thermals and power headroom

### E-Ink (1.54″ SPI, Waveshare or similar)
- **SPI**: SCK, MOSI → MCU; CS/DC/RST/BUSY → MCU GPIO
- **Power**: 3V3 (module-dependent)
- **Refresh**: On command; idle draws ~0

### USB Hub
- **Ultra-slim USB-C hub PCB** inside, one upstream USB-C exits the case
- **Downstream Port A** → T7 (short C-to-C pigtail)
- **Downstream Port B** → MCU (short C-to-C or C-to-micro depending on board)

### Power Budget (Typical)
- MCU: 20–40 mA
- E-ink: ~20–40 mA during refresh, near-zero idle
- LED ring (12 px): 60–120 mA at moderate brightness
- T7: Bursts to a few watts during transfers

**Total stays within a Mac USB-C port** when using a decent hub.

---

## Control Protocol (USB Serial)

### Host → MCU (Examples)

```
PING
LED SET mode=breathe hue=190 sat=200 val=80 rate=0.8
LED PIXELS n=12 data=<base64 rgb or hsv>
EINK TEXT x=10 y=16 "ember"
EINK BMP w=200 h=200 fmt=1bpp data=<base64>
EINK REFRESH
```

### MCU → Host

```
OK
ERR <message>
BUSY
```

**Protocol Details**:
- Serial 115200 (or higher), `\n`-terminated lines
- Minimal parsing: KEY=VALUE tokens; unquoted text allowed inside quotes
- Simple, robust, easily debuggable

---

## Firmware (MCU)

### Platform
CircuitPython or Arduino (C++)

### Drivers/Libraries
- NeoPixel/WS2812 library
- E-ink driver (Waveshare or generic SPI e-paper)
- Simple command parser over USB CDC

### Behaviors
- **Non-blocking LED animation loop** (breathe, pulse, think, speak)
- **E-ink text/bitmap buffer** + explicit REFRESH to avoid ghosting
- **Persist last state** so pod "breathes" even if host app restarts

---

## Mac-Side Control (Python Stub)

```python
import serial, base64, time

def open_port():
    # replace with your tty (e.g., /dev/tty.usbmodemXXX or COMX on Win)
    return serial.Serial('/dev/tty.usbmodemXXXX', 115200, timeout=1)

def cmd(ser, s):
    ser.write((s+'\n').encode())
    return ser.readline().decode().strip()

ser = open_port()
print(cmd(ser, "PING"))
print(cmd(ser, "LED SET mode=breathe hue=190 sat=220 val=90 rate=0.7"))
print(cmd(ser, 'EINK TEXT x=12 y=24 "hello, ember"'))
print(cmd(ser, "EINK REFRESH"))
```

---

## Bill of Materials (Rev-A)

| Item | Part | Notes |
|------|------|-------|
| SSD | Samsung T7 | Existing unit, stays intact |
| MCU | Seeed XIAO RP2040 or Adafruit QT Py RP2040 | ~$10, tiny form factor |
| E-ink | 1.54″ SPI module | Waveshare or similar, ~$15 |
| LED Ring | NeoPixel 12 LED, ⌀36–38 mm | Adafruit or clone, ~$8 |
| Diffuser | 1 mm frosted acrylic disc | Cut to fit halo window |
| Hub | Ultra-slim USB-C 4-port hub | UGREEN-style, to be de-shelled, ~$20 |
| Pigtails | 2× short USB-C cables, 10–15 cm | Right-angle preferred |
| Resistor | 330–470 Ω | For LED DIN |
| Capacitor | 470–1000 µF | For LED 5V/GND |
| Thermal Pad | Under T7 to case wall | Thermal dissipation |
| Magnets | 12×2 mm discs (6–8 pcs) | Or thin hook-and-loop |
| Enclosure | Custom 3D printed | STL to be generated |

**Total Cost** (excluding T7): ~$70–90

---

## Enclosure Notes

- **Make the T7 tray first** (correct fit + thermal pad contact)
- **Put hub PCB along one edge**; route one clean upstream C port out
- **Place halo window centered**; e-ink window above/aside
- **Internal standoffs** for MCU and ring; diffuser ledge over ring
- **Provide strain relief** for the upstream cable
- **Ventilation slots** optional (T7 doesn't run that hot)

---

## Tasks for Implementation

### 1. Hardware Selection
- [ ] Select specific hub PCB (dimensions + de-shelled photos)
- [ ] Confirm XIAO/QT Py pinout mapping for e-ink & ring
- [ ] Assign GPIOs for all connections
- [ ] Source all BOM items

### 2. Firmware Development
- [ ] Generate CircuitPython firmware scaffold
- [ ] Implement command parser
- [ ] Implement LED modes (breathe, pulse, think, speak)
- [ ] Implement e-ink driver wrapper
- [ ] Add state persistence
- [ ] Test protocol over USB serial

### 3. Mac Control Library
- [ ] Create Python module (`emberpod.py`)
- [ ] Create CLI tool (`emberpod` command)
- [ ] Integrate with Ember's main system
- [ ] Add auto-discovery of serial port
- [ ] Add reconnection logic

### 4. Enclosure Design
- [ ] Measure all components precisely
- [ ] Generate STL with proper fit tolerances
- [ ] Test print (check fit before final)
- [ ] Design diffuser mount
- [ ] Design magnet pockets
- [ ] Design wire channels

### 5. Assembly & Testing
- [ ] Wiring diagram
- [ ] Assembly instructions
- [ ] Flashing guide
- [ ] Usage examples
- [ ] Troubleshooting guide

---

## Stretch Goals (Later)

- [ ] Expose optional 3.5 mm jack via tiny USB DAC (audio out)
- [ ] Add touch pad or button for local gestures (wake, mute, cycle)
- [ ] Swap e-ink for 2.13″ later if we want more UI
- [ ] Battery backup for LED/e-ink (T7 stays USB-powered)
- [ ] Accelerometer for tap detection
- [ ] Temperature sensor for thermal monitoring

---

## Why This Design

### Advantages
✅ **T7 stays intact** — No modifications to working SSD  
✅ **Single cable to Mac** — Clean, simple  
✅ **All compute on Mac** — Ember runs full-featured  
✅ **Easy debugging** — Serial protocol, Mac-side control  
✅ **Low cost** — ~$70–90 in parts  
✅ **Quick iteration** — Firmware changes are fast  
✅ **Portable** — Clips to laptop, works anywhere  

### Trade-offs
⚠️ **Mac must be on** — No standalone operation  
⚠️ **USB hub complexity** — Internal routing, more points of failure  
⚠️ **Power sharing** — T7 + MCU + LEDs on one port  

---

## Next Steps

**Immediate** (this session):
1. Select MCU and map pins
2. Generate firmware scaffold
3. Create Mac control library
4. Start enclosure design

**This week**:
1. Order parts
2. Test firmware on breadboard
3. Refine protocol
4. Print test enclosure

**Next week**:
1. Assemble prototype
2. Integrate with Ember
3. Test in coffee shop
4. Document everything

---

**This is v1: Keep it simple, keep the T7 intact, give Ember a halo + wink.**

