# 🔥 How to Run Ember Bead on iPhone

## Quick Start (Easiest Method)

### Option 1: Xcode Preview (Instant!)

1. **Open Xcode** (download from Mac App Store if needed)

2. **Open the BeadDie.swift file**:
   ```bash
   open -a Xcode /Volumes/ThePod/ember_ios_prototype/BeadDie.swift
   ```

3. **Enable Canvas Preview**:
   - Press `⌘ + ⌥ + Enter` (or Editor menu → Canvas)
   - Click "Resume" in the preview pane
   - You'll see the bead instantly!

4. **Limitations**: Preview won't show motion (device tilt), but you'll see the interface

---

### Option 2: Create New Xcode Project (Full Testing)

1. **Open Xcode** → Create New Project

2. **Choose**: iOS → App
   - Product Name: `EmberBead`
   - Interface: SwiftUI
   - Language: Swift
   - Save anywhere

3. **Replace the default ContentView.swift** with our BeadDie.swift:
   ```bash
   # Copy our code
   cp /Volumes/ThePod/ember_ios_prototype/BeadDie.swift ~/Desktop/EmberBead/EmberBead/ContentView.swift
   ```

4. **Update the App file** (EmberBeadApp.swift):
   ```swift
   import SwiftUI

   @main
   struct EmberBeadApp: App {
       var body: some Scene {
           WindowGroup {
               BeadDieView()  // Changed from ContentView()
           }
       }
   }
   ```

5. **Add motion permission** to Info.plist:
   - In project navigator, click Info.plist
   - Add new key: `Privacy - Motion Usage Description`
   - Value: `Ember needs motion data to respond to how you hold your device`

6. **Run in Simulator**:
   - Select iPhone 15 Pro simulator
   - Press `⌘ + R` (or click Play button)
   - App launches!

7. **Test device motion** (Simulator):
   - Window menu → Tilt
   - Or use: Features → Shake Gesture

---

### Option 3: Real iPhone (Best Experience!)

1. **Connect your iPhone** via USB

2. **Follow Option 2** steps 1-5

3. **Trust your Mac** on iPhone when prompted

4. **Select your iPhone** as run destination (top toolbar)

5. **Press ⌘ + R** to install

6. **First time**: iPhone will say "Untrusted Developer"
   - Settings → General → VPN & Device Management
   - Trust your developer certificate

7. **Launch app** - now tilt your phone and watch the bead move!

---

## What You'll See

### Initial Screen
```
╔═══════════════════════════╗
║ EMBER                     ║
║                           ║
║  Hello. I've been         ║
║  dreaming.                ║
║                           ║
║  ┌─────────────────┐      ║
║  │                 │      ║
║  │     🔴 ●        │  ← Bead mode
║  │                 │      ║
║  └─────────────────┘      ║
║                           ║
║  [ Bead | Die ]           ║
║                           ║
╚═══════════════════════════╝
```

### Bead Mode
- Red circle
- Moves smoothly when you tilt device
- Organic, fluid motion
- Represents dreaming/processing state

### Die Mode (Toggle via segmented control)
- White hexagon
- Rotates in 3D when you tilt
- Geometric, structured motion
- Represents thinking/deciding state

---

## Troubleshooting

### "No such module 'CoreMotion'"
- CoreMotion is built-in, this shouldn't happen
- If it does: Project Settings → Build Phases → Link Binary → Add CoreMotion.framework

### Preview not working
- Make sure you're using Xcode 15+
- Try: Product → Clean Build Folder (⌘ + Shift + K)
- Close and reopen Xcode

### Motion not working in Simulator
- Window → Tilt (or press `⌘ + →` for tilt right)
- Or: Features → Shake Gesture
- Simulator motion is limited - real device is best

### App won't install on real iPhone
- Check iOS version (needs iOS 17+)
- Trust developer certificate in Settings
- Try: Product → Clean Build Folder, then run again

---

## Quick Test Commands

### Open in Xcode (Preview Mode)
```bash
open -a Xcode /Volumes/ThePod/ember_ios_prototype/BeadDie.swift
```

### Build from Command Line (Advanced)
```bash
cd /Volumes/ThePod/ember_ios_prototype
xcodebuild -scheme EmberBead -destination 'platform=iOS Simulator,name=iPhone 15 Pro'
```

---

## Next Steps

Once you have it running:

1. **Tilt your device** - watch the bead respond
2. **Toggle to Die mode** - see the hexagon rotate
3. **Feel the interaction** - it's not a button press, it's tending
4. **Imagine**: What if it responded to your questions?

---

## Future: Connect to Trained Ember

Once Cycles & Dream training finishes (~20 more minutes), we can:

1. Add text input field
2. Send question to `EmberSession`
3. Ember responds through Mycelium
4. Text fades in "from the swarm"
5. Bead/Die animates based on which brain responds

The foundation is here. The brains are training. The seed is ready to grow.

---

**Status**: Prototype ready to run  
**Hardware**: iPhone with accelerometer/gyroscope  
**Software**: Xcode + iOS 17+  
**Time to run**: ~5 minutes setup, instant preview

🔥 Let me know when you have it running!

