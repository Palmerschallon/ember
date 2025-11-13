# Hardware Selection — Ember Mini-Pod
**Date**: October 8, 2025

---

## MCU: Seeed XIAO RP2040

**Why XIAO RP2040**:
- Tiny: 20×17.5 mm (perfect for internal mount)
- USB-C native
- Dual-core RP2040 (overkill but fast)
- CircuitPython + Arduino support
- 11 GPIO pins (enough for our needs)
- $7.99 from Seeed

**Pinout for Our Use**:
```
D0  (GPIO0)  → E-ink RST
D1  (GPIO1)  → E-ink DC
D2  (GPIO2)  → E-ink CS
D3  (GPIO3)  → E-ink BUSY (input)
D6  (GPIO6)  → NeoPixel DIN
D8  (GPIO8)  → SPI SCK  (e-ink)
D9  (GPIO9)  → SPI TX   (e-ink MOSI)
D10 (GPIO10) → SPI RX   (unused, but shared bus)
3V3          → E-ink VCC
5V           → NeoPixel 5V
GND          → Common ground
```

**Alternative**: Adafruit QT Py RP2040
- Same RP2040 chip, slightly different form factor
- $9.95 from Adafruit
- More readily available in US

---

## E-Ink: Waveshare 1.54" V2

**Specs**:
- Resolution: 200×200 pixels
- Interface: SPI
- Partial refresh support
- Voltage: 3.3V
- Dimensions: 37.32×31.8 mm (active area ~27.6×27.6 mm)
- Price: ~$15

**Pinout**:
```
VCC  → 3V3
GND  → GND
DIN  → MOSI (D9)
CLK  → SCK  (D8)
CS   → D2
DC   → D1
RST  → D0
BUSY → D3
```

**CircuitPython Library**: `adafruit_epd` (supports Waveshare)

**Why 1.54"**:
- Perfect size for short text (status, state, quotes)
- Low power (only draws during refresh)
- Good contrast in coffee shop lighting
- Can show small glyphs/icons

**Upgrade Path**: 2.13" later if we want more UI real estate

---

## LED Ring: NeoPixel Ring - 12 x WS2812

**Specs**:
- 12 RGB LEDs (WS2812B or SK6812)
- Outer diameter: ~37 mm
- Inner diameter: ~23 mm (passthrough for wiring)
- 5V power, single data line
- Price: ~$8 (Adafruit) or ~$4 (AliExpress)

**Wiring**:
```
5V  → 5V (from hub, with 470–1000µF cap)
GND → GND
DIN → D6 (with 330Ω resistor inline)
```

**CircuitPython Library**: `neopixel`

**Diffusion**:
- 1mm frosted acrylic disc over ring
- Creates "halo" effect
- Softens individual LED spots
- Can laser-cut or hand-cut from sheet

**Why 12 LEDs**:
- Enough for smooth "breathing" animation
- Low power (~10 mA per LED at moderate brightness)
- Good balance of effect vs. thermal load

---

## USB-C Hub: Ultra-Slim 4-Port Hub

**Target Specs**:
- 4× USB-C downstream ports
- 1× USB-C upstream port
- Small PCB (can be de-shelled)
- Bus-powered (no external PSU)
- USB 3.0+ for T7 speed

**Candidates**:

### Option A: UGREEN 4-Port USB-C Hub (Model: CM219)
- Dimensions: ~90×30×10 mm (with shell)
- PCB inside: ~75×25×8 mm (estimated)
- USB 3.0 (5 Gbps)
- Price: ~$20
- **Pro**: Common, easy to source
- **Con**: Need to de-shell carefully

### Option B: Anker 4-Port USB-C Hub (PowerExpand)
- Similar dimensions
- Solid build quality
- Price: ~$25
- **Pro**: Reliable brand
- **Con**: Slightly more expensive

### Option C: Generic AliExpress Hub PCB
- Raw PCB without shell
- Dimensions: ~60×20 mm
- Price: ~$8–12
- **Pro**: Already bare PCB, smallest
- **Con**: Less reliable, longer shipping

**Recommendation**: Start with **UGREEN CM219**
- Easy to source locally (SF has these)
- Known quality
- Can de-shell and measure precisely
- Falls back to Option C if internal fit is too tight

---

## Supporting Components

### Resistor (LED Data Line)
- **Value**: 330–470 Ω
- **Type**: 1/4W through-hole or 0805 SMD
- **Purpose**: Protects MCU pin from LED data line transients
- **Price**: <$0.10

### Capacitor (LED Power Supply)
- **Value**: 470–1000 µF, 10V+
- **Type**: Electrolytic (through-hole) or tantalum
- **Purpose**: Smooths LED power draw spikes
- **Placement**: As close to NeoPixel ring as possible
- **Price**: ~$0.50

### Thermal Pad (T7 to Case)
- **Type**: 1mm thick silicone thermal pad
- **Size**: Cut to fit T7 footprint (~85×57 mm)
- **Thermal conductivity**: 3–6 W/mK
- **Purpose**: Dissipate T7 heat to enclosure walls
- **Price**: ~$8 for sheet (enough for many pods)

### Magnets (Back Attachment)
- **Size**: 12mm diameter × 2mm thick, neodymium
- **Quantity**: 6–8 pieces
- **Purpose**: Clip to MacBook lid or metal surfaces
- **Price**: ~$10 for 20-pack
- **Alternative**: 3M dual-lock (hook-and-loop)

### USB-C Pigtails
- **Type**: Short USB-C to USB-C cables, 10–15 cm
- **Quantity**: 2 (one for T7, one for MCU)
- **Angle**: Right-angle preferred for internal routing
- **Price**: ~$5 each

### Diffuser (Halo)
- **Material**: 1mm frosted acrylic or polycarbonate
- **Size**: 38mm diameter disc
- **Purpose**: Diffuses NeoPixel ring for smooth halo
- **Fabrication**: Laser-cut or hand-cut from sheet
- **Price**: ~$5 for sheet (makes many)

---

## Wiring Summary

```
[Mac USB-C Port]
      │
      ├─ USB-C Hub (internal)
      │     │
      │     ├─ Port A → Samsung T7 (intact)
      │     │
      │     └─ Port B → XIAO RP2040
      │           │
      │           ├─ D6 ──[330Ω]→ NeoPixel DIN
      │           │              ├─ 5V ─[1000µF cap]─ GND
      │           │
      │           ├─ D0-D3, D8-D9 → E-ink (SPI + control)
      │           │                 ├─ 3V3
      │           │
      │           └─ USB Serial (CDC) → Command protocol
```

---

## Total BOM Cost

| Item | Price | Source |
|------|-------|--------|
| XIAO RP2040 | $8 | Seeed/Adafruit |
| 1.54" E-ink | $15 | Waveshare/Amazon |
| NeoPixel Ring (12) | $8 | Adafruit |
| USB-C Hub | $20 | UGREEN/Amazon |
| USB-C Pigtails (2) | $10 | Amazon |
| Resistor + Cap | $1 | Local electronics |
| Thermal Pad | $2 | Amazon (from sheet) |
| Magnets (8) | $2 | Amazon (from pack) |
| Diffuser Acrylic | $1 | Local shop (from sheet) |
| 3D Print Filament | $3 | ~30g PETG/PLA |
| **Total** | **~$70** | |

**Not including**: T7 SSD (already owned), tools, shipping

---

## Procurement Plan

### Immediate (Today/Tomorrow)
1. Order XIAO RP2040 from Adafruit (or local SF store)
2. Order Waveshare 1.54" e-ink from Amazon (2-day)
3. Order NeoPixel ring from Adafruit

### This Week
1. Buy UGREEN hub locally in SF (Target/Best Buy/Fry's)
2. Get USB-C cables locally
3. Get resistor/cap from local electronics shop (Anchor Electronics SF)
4. Get magnets from hardware store or Amazon

### Next Week
1. Get thermal pad (Amazon or local)
2. Get diffuser material (TAP Plastics SF or laser-cut online)

### 3D Printing
- Print test fit first (no diffuser/magnets)
- Iterate if needed
- Final print in PETG (heat resistance for T7)

---

## Design Validation

### Pin Assignment Check
✅ XIAO RP2040 has enough GPIOs (11 available, using 7)  
✅ SPI bus shared between e-ink (no conflicts)  
✅ NeoPixel on dedicated pin (no SPI interference)  
✅ USB CDC available for serial protocol  

### Power Budget Check
- XIAO: 40 mA
- E-ink: 40 mA peak (during refresh)
- NeoPixel: 120 mA (12 LEDs at 10 mA avg)
- **Total**: ~200 mA (well within USB-C 500 mA minimum)
- T7 on separate hub port (handles its own bursts)

### Thermal Check
- T7: Up to 45°C under load
- Thermal pad to case: ~40°C case temp
- Comfortable to touch, safe for desk/laptop
- NeoPixel: Low brightness = minimal heat

### Mechanical Check
- XIAO: 20×17.5 mm → fits easily
- E-ink module: 37×32 mm → front panel mount
- NeoPixel ring: ⌀37 mm → front panel mount
- Hub PCB: ~75×25 mm → side mount
- T7: 85×57 mm → main tray
- **Total enclosure**: ~105×65×18 mm → pocketable

---

## Next: Firmware Scaffold

With hardware selected and pins assigned, we can now generate the CircuitPython firmware.

