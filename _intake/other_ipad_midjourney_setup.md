# iPad Midjourney Auto-Scraper

## The Idea
Use an iOS Shortcut on your iPad to take screenshots every 2-3 seconds while you scroll through Midjourney. Then process the screenshots on your Mac.

---

## Setup Part 1: iPad Shortcut

### Create the Shortcut:

1. Open **Shortcuts** app on iPad
2. Tap **"+"** to create new shortcut
3. Name it: **"MJ Auto-Capture"**

### Add these actions:

```
1. Repeat 60 times
   ├─ Take Screenshot
   ├─ Wait 3 seconds
   └─ End Repeat

2. Show Notification: "Captured 60 screenshots!"
```

### Detailed steps:
- **Add Action** → Search "Repeat" → Set to **60 times**
- **Inside the Repeat:**
  - Add Action → Search "Take Screenshot"
  - Add Action → Search "Wait" → Set to **3 seconds**
- **After the Repeat:**
  - Add Action → Search "Show Notification" → Type message

### To Run:
1. Open Midjourney on iPad
2. Run the shortcut
3. **Immediately start scrolling** through your gallery
4. Scroll slowly - give each image ~3 seconds on screen
5. After 3 minutes (60 screenshots), it will notify you

---

## Setup Part 2: Mac Processing

### Enable iCloud Photo Sync:
1. **iPad:** Settings → Photos → **iCloud Photos** ON
2. **Mac:** System Settings → Apple ID → iCloud → **Photos** ON

### Watch for New Screenshots:

```bash
cd /Volumes/ThePod
python3 watch_ipad_screenshots.py
```

This will:
- Watch your Photos library for new screenshots
- Detect Midjourney images
- Extract the visible images with OCR
- Download and create seeds automatically

---

## Alternative: AirDrop Method (No iCloud needed)

### On iPad:
1. Run the shortcut
2. After capturing, go to Photos
3. Select all new screenshots
4. **Share → AirDrop** to your Mac
5. Accept on Mac

### On Mac:
```bash
cd /Volumes/ThePod
python3 process_local_images.py ~/Downloads
```

---

## iOS Shortcut (Text Format)

If you want to build it manually or share:

```
Repeat 60 times:
  Take Screenshot
  Wait 3 seconds
End Repeat
Show Notification "Captured 60 screenshots!"
```

**Duration:** 3 minutes (60 screenshots × 3 seconds)  
**Coverage:** ~60 Midjourney images if you scroll steadily

---

## Advanced: Voice Control

Add **"Run Shortcut: MJ Auto-Capture"** to Siri so you can just say:

> "Hey Siri, run MJ Auto-Capture"

Then start scrolling!

---

## Processing the Screenshots

### Option 1: Automatic (iCloud sync)
```bash
python3 watch_ipad_screenshots.py
```
Leave this running, and it processes new screenshots automatically

### Option 2: Manual batch
```bash
python3 process_local_images.py ~/Pictures/Screenshots
```

### Option 3: AirDrop
```bash
python3 process_local_images.py ~/Downloads
```

---

## Tips

- **Scroll speed:** Slow and steady - each image needs ~3 seconds
- **Grid view:** Show 4-6 images per screen for efficiency
- **Notification:** When you hear it, scrolling is done
- **Cleanup:** Delete the screenshots from Photos after processing
- **Batch size:** 60 screenshots = ~15-20 unique images after deduplication

---

## Why This Works

✅ iPad browser has proper Midjourney auth/cookies  
✅ Screenshots capture everything on screen  
✅ No Cloudflare blocking  
✅ Mac processes them with LLava  
✅ Fully automated once set up  

---

## Next Steps

1. Create the shortcut on iPad (2 minutes)
2. Test with 10 screenshots first (30 seconds)
3. Process them to verify it works
4. Then do a full 60-screenshot run!

