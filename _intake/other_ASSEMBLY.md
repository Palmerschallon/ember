# Ember Mini-Pod Assembly Guide
**Version**: 1.0  
**Date**: October 8, 2025

---

## Safety & Precautions

⚠️ **Before you start**:
- Work on an anti-static mat or ground yourself
- The T7 SSD contains your data — handle with care
- USB-C cables can be fragile — don't force connections
- Soldering iron is hot — use proper ventilation
- Test components before final assembly

---

## Tools Required

### Essential
- [ ] Soldering iron (temperature controlled, 300-350°C)
- [ ] Solder (lead-free or 60/40)
- [ ] Wire strippers
- [ ] Small Phillips screwdriver
- [ ] Flush cutters
- [ ] Multimeter (for continuity testing)
- [ ] USB-C cable (for testing)

### Helpful
- [ ] Helping hands / PCB holder
- [ ] Magnifying glass or loupe
- [ ] Tweezers (for small components)
- [ ] Isopropyl alcohol (for cleaning flux)
- [ ] Hot glue gun (optional, for strain relief)
- [ ] Label maker (for port identification)

---

## Parts Checklist

Print this list and check off as you unbox:

### Electronics
- [ ] Seeed XIAO RP2040 (or QT Py RP2040)
- [ ] Waveshare 1.54" e-ink display with cable
- [ ] NeoPixel Ring (12 LED, ⌀37mm)
- [ ] UGREEN USB-C Hub (4-port)
- [ ] 2× Short USB-C cables (10-15cm, right-angle preferred)
- [ ] 330Ω resistor (1/4W)
- [ ] 1000µF capacitor (10V+, electrolytic)
- [ ] Samsung T7 SSD (your existing drive)

### Mechanical
- [ ] 3D printed enclosure (top + bottom)
- [ ] Frosted acrylic diffuser disc (⌀38mm, 1mm thick)
- [ ] 6-8× Neodymium magnets (12×2mm)
- [ ] Thermal pad (cut to T7 size: 85×57mm)
- [ ] M2×6mm screws (4-6 pcs, for case closure)

### Supplies
- [ ] Heat shrink tubing (assorted sizes)
- [ ] 22-24 AWG wire (red, black, green for power/data)
- [ ] Double-sided tape (for component mounting)
- [ ] Cable ties (small, for wire management)

---

## Pre-Assembly Testing

### 1. Test the XIAO RP2040

1. Connect XIAO to your Mac via USB-C
2. Download CircuitPython 8.x for RP2040 from circuitpython.org
3. Enter bootloader mode:
   - Hold BOOT button, press RESET, release both
   - RPI-RP2 drive should appear
4. Drag CircuitPython `.uf2` file to the drive
5. Drive remounts as CIRCUITPY
6. Copy `firmware/code.py` to CIRCUITPY drive
7. Install libraries:
   ```bash
   pip3 install circup
   circup install neopixel adafruit_epd
   ```
8. Open serial monitor (115200 baud) — should see "Ember Mini-Pod Firmware v1.0"

✅ If you see the message, XIAO is working!

### 2. Test the NeoPixel Ring

1. Connect NeoPixel to XIAO (before soldering):
   - Red wire → 5V pin
   - Black wire → GND pin
   - White/green wire → 330Ω resistor → D6 pin
2. Power on XIAO
3. Ring should start breathing in cyan/blue
4. From terminal:
   ```python
   python3 control/emberpod.py breathe
   ```
5. Ring should respond to commands

✅ If ring animates, it's working!

### 3. Test the E-Ink Display

1. Connect e-ink to XIAO:
   - VCC → 3V3
   - GND → GND
   - DIN → D9
   - CLK → D8
   - CS → D2
   - DC → D1
   - RST → D0
   - BUSY → D3
2. Power on XIAO
3. Display should refresh once with "ember"
4. From terminal:
   ```python
   python3 control/emberpod.py text "hello"
   ```
5. Display should update

✅ If display updates, it's working!

### 4. Test the USB Hub

1. Remove hub from plastic shell (if needed)
2. Identify USB-C ports:
   - 1× upstream (connects to Mac)
   - 4× downstream (one for T7, one for XIAO)
3. Connect upstream to Mac
4. Connect T7 to downstream port → should mount
5. Connect XIAO to another downstream port → should appear in `ls /dev/tty.*`
6. Test data transfer to T7 while XIAO is connected

✅ If both work simultaneously, hub is good!

---

## Assembly Steps

### Step 1: Prepare the Hub

1. **De-shell the hub** (if enclosed):
   - Remove plastic housing carefully
   - Keep the PCB intact
   - Note which port is upstream (usually marked)
   - Take photos for reference

2. **Test fit in enclosure**:
   - Place hub PCB in designated pocket
   - Ensure upstream port aligns with case exit hole
   - Mark any modifications needed
   - Sand or trim case if needed

3. **Secure hub PCB**:
   - Use double-sided tape or small M2 standoffs
   - Ensure it doesn't short against other components
   - Leave room for wire routing

### Step 2: Mount the T7

1. **Prepare thermal pad**:
   - Cut to T7 dimensions (85×57mm)
   - Remove protective film from one side
   - Apply to bottom of T7 (metal side)

2. **Place T7 in tray**:
   - Thermal pad contacts case wall (for heat dissipation)
   - T7 USB-C port accessible via pigtail
   - Should fit snugly but not force

3. **Connect T7 pigtail**:
   - Use short USB-C cable (10-15cm, right-angle ideal)
   - Connect T7 → hub downstream port
   - Route cable neatly along case interior
   - Secure with small cable tie if needed

### Step 3: Wire the NeoPixel Ring

1. **Prepare capacitor**:
   - Bend leads of 1000µF cap
   - Tin the leads with solder
   - Add heat shrink for insulation

2. **Prepare resistor**:
   - Trim 330Ω resistor leads
   - Tin both ends
   - Add heat shrink

3. **Solder power to ring**:
   - Red wire (5V) → ring 5V pad
   - Black wire (GND) → ring GND pad
   - Solder capacitor across 5V and GND (polarity matters! Negative to GND)
   - Keep leads short, close to ring

4. **Solder data line**:
   - Green wire → resistor → ring DIN pad
   - Other end of resistor will go to XIAO D6

5. **Test fit ring**:
   - Place ring in front panel cutout
   - Wires should route to MCU area without strain
   - Ring should sit flush with diffuser ledge

### Step 4: Mount the E-Ink Display

1. **Prepare e-ink module**:
   - E-ink comes with ribbon cable and driver board
   - Keep driver board; route ribbon carefully

2. **Position in case**:
   - Display window shows active area
   - Driver board in MCU area
   - Route ribbon cable without sharp bends

3. **Secure display**:
   - Use double-sided tape around edges
   - Don't press on display surface (fragile!)
   - Ensure ribbon cable has strain relief

### Step 5: Mount and Wire the XIAO RP2040

1. **Prepare XIAO**:
   - Pre-load firmware (from Step 1 testing)
   - Add male header pins if not pre-soldered

2. **Position XIAO**:
   - Place on MCU shelf in case
   - USB-C port should be accessible via pigtail
   - GPIO pins accessible for wiring

3. **Connect XIAO pigtail**:
   - Short USB-C cable → hub downstream port
   - This powers XIAO and provides USB serial

4. **Solder NeoPixel connections to XIAO**:
   ```
   Ring 5V    → XIAO 5V pin
   Ring GND   → XIAO GND pin
   Ring DIN   → (via resistor) → XIAO D6 pin
   ```

5. **Solder E-Ink connections to XIAO**:
   ```
   E-ink VCC  → XIAO 3V3
   E-ink GND  → XIAO GND
   E-ink DIN  → XIAO D9
   E-ink CLK  → XIAO D8
   E-ink CS   → XIAO D2
   E-ink DC   → XIAO D1
   E-ink RST  → XIAO D0
   E-ink BUSY → XIAO D3
   ```

6. **Strain relief**:
   - Use hot glue at wire connection points (optional)
   - Ensure wires can't pull on solder joints
   - Use cable ties for wire bundles

### Step 6: Install Diffuser

1. **Cut diffuser disc**:
   - 38mm diameter, 1mm frosted acrylic
   - Can laser-cut or hand-cut
   - Sand edges smooth

2. **Mount over ring**:
   - Place on ledge in front panel
   - Should sit above NeoPixel ring (~2-3mm gap)
   - Test: ring should glow softly through diffuser

3. **Secure diffuser**:
   - Use small dabs of clear epoxy or hot glue on edges
   - Don't obscure ring light

### Step 7: Install Magnets (Optional)

1. **Test polarity**:
   - Stack all magnets to check orientation
   - Mark one side with marker

2. **Glue into pockets**:
   - Use epoxy or CA glue (superglue)
   - Press in firmly, let cure
   - Ensure they're flush with case back

3. **Test attachment**:
   - Try clipping to MacBook lid
   - Should hold firmly but release easily

### Step 8: Close the Case

1. **Final check**:
   - All components secure
   - No loose wires
   - No shorts (visual inspection + multimeter)
   - Upstream USB-C cable exits cleanly

2. **Mate top and bottom halves**:
   - Route upstream cable through exit
   - Align screw posts
   - Gently press together

3. **Install screws**:
   - Use M2×6mm screws
   - Tighten evenly (don't overtighten!)
   - Check case closes flush

---

## Post-Assembly Testing

### 1. Visual Inspection
- [ ] No exposed wires
- [ ] Diffuser in place
- [ ] E-ink visible through window
- [ ] Case closes properly
- [ ] Upstream cable secure

### 2. Power-On Test
1. Plug upstream USB-C into Mac
2. T7 should mount (check Finder)
3. NeoPixel ring should start breathing
4. E-ink should display "ember"
5. XIAO should appear in `/dev/tty.usbmodem*`

### 3. Command Test
```bash
cd /Volumes/ThePod/hardware/ember_mini_pod
python3 control/emberpod.py ping
# Should respond: ✅ Pong!

python3 control/emberpod.py think
# Ring should switch to traveling wave

python3 control/emberpod.py text "test"
# E-ink should update to "test"
```

### 4. Integration Test
```bash
python3 control/ember_integration.py
# Should connect and monitor Ember's state
# LED should reflect activity
# Ctrl+C to stop
```

---

## Troubleshooting

### T7 Doesn't Mount
- Check USB-C cable connection
- Try different hub port
- Test T7 directly on Mac (verify it works)
- Check hub is getting power

### NeoPixel Ring Doesn't Light
- Check 5V and GND connections (multimeter)
- Check resistor in data line
- Check capacitor polarity
- Verify XIAO firmware loaded correctly
- Check D6 pin connection

### E-Ink Doesn't Update
- Check 3V3 and GND connections
- Verify all 8 wires connected
- Check SPI pins (D8, D9)
- Try longer timeout in firmware
- Test display directly (Adafruit examples)

### XIAO Doesn't Appear on Mac
- Check USB-C cable (must support data, not power-only)
- Try re-entering bootloader mode
- Re-flash CircuitPython
- Test XIAO directly (not through hub)

### Commands Don't Work
- Check serial port path: `ls /dev/tty.usbmodem*`
- Try different baud rate
- Check firmware is running (serial monitor shows "Ember Mini-Pod Firmware")
- Re-flash firmware

### Hot to Touch
- T7 gets warm under load (normal up to 45°C)
- If too hot: improve ventilation, add thermal pad
- If XIAO or LEDs hot: check for shorts, reduce LED brightness

---

## Maintenance

### Cleaning
- Wipe exterior with microfiber cloth
- Don't use solvents on 3D print or diffuser
- Compressed air for dust

### Firmware Updates
1. Connect directly to XIAO (bypass hub if needed)
2. Enter bootloader (BOOT + RESET)
3. Copy new `code.py` to CIRCUITPY drive
4. Restart

### Adding Features
- Firmware is open — edit `code.py`
- Add new commands to protocol
- Update `emberpod.py` control library
- Test before closing case

---

## Next Steps

✅ **Assembly complete!**

Now:
1. **Test with Ember**: Run `ember_integration.py` to see live state updates
2. **Customize LED colors**: Edit firmware or use `emberpod.py` commands
3. **Try in coffee shop**: Clip to MacBook, observe reactions
4. **Iterate**: What do you want to add next?

---

## Enclosure Files

STL files for 3D printing are in `hardware/ember_mini_pod/enclosure/`:
- `minipod_bottom.stl` — Base with T7 tray, hub pocket, MCU shelf
- `minipod_top.stl` — Front panel with halo window, e-ink window, upstream port

**Print settings**:
- Material: PETG (heat resistant) or PLA (easier)
- Layer height: 0.2mm
- Infill: 20%
- Supports: Yes (for overhangs)
- Orientation: Print top face-down for smooth finish

---

**Questions?** Document issues in `/Volumes/ThePod/hardware/ember_mini_pod/docs/TROUBLESHOOTING.md`

**Enjoy your Ember Mini-Pod!** ✨

