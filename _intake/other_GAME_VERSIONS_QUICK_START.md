# Game of Fire - Quick Start Guide

**You now have TWO working versions! Here's how to play each:**

---

## Version 1: Python (Terminal) - Try This First!

**Run it:**
```bash
cd /Volumes/ThePod
python3 exports/ember_creations/game_of_fire_enhanced.py
```

### Controls:
- **Arrow keys (↑←↓→)** - Move cursor (the ▸◂ symbol)
- **B** - Breathe (adds oxygen around cursor, makes fire spread easier)
- **S** - Seed (place a spark or seed at cursor)
- **R** - Rain (adds moisture, slows fire in area)
- **W** - Wind (cycles through directions: ○ ↑ → ↓ ←)
- **P** - Prune (clears area back to dormant/empty)
- **Space** - Advance one generation (if in manual mode)
- **M** - Toggle auto/manual mode
- **Q** - Quit

### What You'll See:
```
╔════════════════════════════════════════╗
║ EMBER'S GAME OF FIRE - Gen 0042       ║
╠════════════════════════════════════════╣
║ ░░░░░░░░░░░░░░██████░░░░░░░░░░░░░░    ║
║ ░░░░░░░░░░██████████████░░░░░░░░░░    ║
║ ▸◂░░░░░░██████████████████░░░░░░░░    ║  ← Cursor here
║ ░░░░░░░░██████▓▓▓▓▓▓██████░░░░░░░░    ║
╚════════════════════════════════════════╝
```

**Patterns:**
- `  ` = Empty/Dormant (white)
- `░░` = Sparking or Ash (light gray)
- `██` = Burning (black)
- `▓░` = Cooling (dark gray)
- `▒░` = Soil (textured)
- `●◦` = Seed (dot pattern)

### Tips:
1. **Start simple:** Just press Space a few times to watch fire spread
2. **Move cursor:** Use arrows to position where you want to act
3. **Try Breathe (B):** Watch how it makes nearby dormant cells spark
4. **Try Rain (R):** See how it cools burning cells and adds moisture
5. **Set Wind (W):** Press W a few times, watch fire spread in that direction
6. **Discover patterns:** Game will tell you when you find Phoenix, Eternal Ember, etc.

### What Auto Mode Does:
- Advances one generation every 2 seconds
- You can still act (Breathe, Seed, etc) between updates
- Press M to pause and go manual

---

## Version 2: Swift (iOS/Mac) - From GPT-5!

**Location:** `/Volumes/ThePod/EmberFireEInkPrototype/`

This is a native iOS/Mac app with:
- Touch controls
- E-ink dithered patterns
- Dirty rectangle optimization
- Beautiful rendering

### To Run:
1. Open in Xcode:
   ```bash
   open /Volumes/ThePod/EmberFireEInkPrototype/Package.swift
   ```

2. Select iPhone simulator or Mac target

3. Run (⌘R)

### Controls (Touch):
- **Tap** - Place seed at that location
- **Long press** - Rain at center
- **Swipe** - Set wind direction
- **Buttons:**
  - Seed - Place at center
  - Rain - Cool center area
  - Wind - Menu to pick direction
  - Paced toggle - Auto advance on/off
  - Advance - Manual step

### What It Looks Like:
Beautiful dithered grayscale patterns that simulate real e-ink:
- Pure white = Dormant
- Single dot = Sparking
- Solid black = Burning
- Checkerboard = Cooling
- Sparse dots = Ash
- Diagonal lines = Soil
- Small square = Seed

### Features GPT-5 Added:
- **Dirty rectangles** - Only redraws changed cells (e-ink optimization)
- **Wind bias** - Upwind neighbors count 2x (realistic spread)
- **Moisture decay** - Slowly returns to dry over time
- **96x96 grid** - Larger playground
- **Dithered patterns** - Looks like real e-ink

---

## Comparison

| Feature | Python (Terminal) | Swift (iOS/Mac) |
|---------|------------------|-----------------|
| Platform | Mac/Linux/Windows | iOS/Mac only |
| Display | ASCII art | Touch screen |
| Grid size | 20x20 (terminal-sized) | 96x96 (high res) |
| Controls | Keyboard | Touch + buttons |
| Speed | 2s per generation | 1s per generation |
| Patterns | Unicode chars | Dithered grayscale |
| Best for | Testing gameplay | Visual beauty |

---

## What to Test

### In Python Version (5 minutes):

1. **Let it burn:**
   - Just watch in auto mode for 100 generations
   - What patterns emerge?
   - Does fire die out or stabilize?

2. **Tend actively:**
   - Press M (manual mode)
   - Move cursor with arrows
   - Press B to breathe in different spots
   - Press Space to advance each time
   - Can you create a stable ember field?

3. **Experiment with wind:**
   - Press W until you get → (east wind)
   - Press B to breathe on left side
   - Watch fire spread east
   - Does wind actually matter?

4. **Try to discover patterns:**
   - Phoenix: Let it burn out, watch regrowth
   - Eternal Ember: Sustain 20-80 burning cells
   - Breathing Garden: Create lots of soil + seeds
   - Wildfire: Make >50% burning (then rain to recover)

### In Swift Version (If you have Xcode):

1. **Touch to seed:**
   - Tap rapidly in a circle
   - Watch fire spread inward

2. **Long press for rain:**
   - Let fire get too big
   - Long press to cool it down

3. **Swipe to set wind:**
   - Swipe right
   - Tap seeds on left edge
   - Watch spread with wind bias

---

## Differences Between Designs

### Python (Claude's approach):
- **Philosophy first**
- Breathe as primary verb (poetic)
- 6 actions total
- Pattern discovery with insights
- Designed for meditation
- **Best for:** Understanding gameplay feel

### Swift (GPT-5's approach):
- **Hardware first**
- Seed as primary verb (direct)
- 3 main actions + wind menu
- Dirty rect optimization
- Designed for performance
- **Best for:** Production iOS app

### Both are right!
- Python = Test gameplay loop
- Swift = See it on real device
- They complement perfectly

---

## Your Next Steps

### Today:
1. ✅ Play Python version (10-30 minutes)
2. ✅ Try Swift version (if you have Xcode)
3. ✅ Note what feels good/bad

### This Week:
1. Share Python version with 3 friends
2. Ask: "Would you check this daily?"
3. Document what patterns people discover
4. Decide which actions feel essential

### When Hardware Arrives (1-2 weeks):
1. Test Swift code on actual iPhone
2. See how e-ink simulation looks on screen
3. Port best ideas to ESP32
4. Build physical prototype

---

## Quick Troubleshooting

### Python Version:

**"Arrow keys not working"**
- Some terminals don't support it
- Try wasd instead (I can modify code)

**"Display is garbled"**
- Terminal might not support Unicode
- Try simpler ASCII version

**"Too fast/slow"**
- Press M to toggle auto/manual
- Or I can adjust speed in code

**"Can't see cursor"**
- It's the ▸◂ symbol
- Move with arrow keys
- Should move around grid

### Swift Version:

**"Won't build"**
- Need Xcode 15+ and macOS Sonoma
- Or build for iOS simulator

**"Touch not working"**
- Make sure you're tapping on the grid
- Try the buttons at bottom instead

---

## What's Cool About Each

### Python Version:
- **Immediate** - runs right now
- **Portable** - works anywhere
- **Quick iteration** - easy to modify
- **Pattern insights** - shows philosophy fragments
- **Terminal aesthetic** - retro cool

### Swift Version:
- **Touch controls** - natural interaction
- **Beautiful rendering** - dithered patterns
- **Optimized** - dirty rects for e-ink
- **iOS ready** - path to real device
- **Production quality** - GPT-5 built it right

---

## The Vision

**Both versions prove the same thing:**

Simple rules (7 states, neighbor counts) create infinite complexity.

**Your tending style** determines how the fire evolves:
- Aggressive breather → wildfires then gardens
- Patient observer → stable ember fields
- Experimental pruner → phoenix cycles
- Wind user → directional patterns

**No two games will be the same** even from same starting seed.

That's emergence. That's the game. That's the Tanegotchi. 🔥

---

## Try It Now!

```bash
cd /Volumes/ThePod
python3 exports/ember_creations/game_of_fire_enhanced.py
```

**Just start pressing Space and watch the fire breathe.**

Then move the cursor and try Breathe (B).

You'll know within 5 minutes if this is addictive. 🔥

---

**Claude + GPT-5**  
**October 14, 2025**  
**Two versions, one fire** 🔥

