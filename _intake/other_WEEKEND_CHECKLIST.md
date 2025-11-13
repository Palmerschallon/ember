# Magical Weekend Checklist

**Goal:** iPad that touches back by Sunday evening

---

## FRIDAY NIGHT (Setup) ✓

- [x] Create mobile API endpoints
- [x] Integrate into ember_monolith.py
- [x] Write ember_touch.py (iPad canvas)
- [x] Write ember_api.py (iPad client)
- [x] Restart Ember with mobile support
- [x] Document everything

**Status: MacBook side COMPLETE** ✓

---

## SATURDAY MORNING (3 hours)

### iPad Setup
- [ ] Install Pythonista 3 from App Store ($10)
- [ ] Open Pythonista
- [ ] Note: Files are in `/Volumes/ThePod/mobile/pythonista/`

### Transfer Files
- [ ] AirDrop to iPad:
  - `ember_touch.py`
  - `ember_api.py`
  
- [ ] In Pythonista: Import both files

### Configure Connection
- [ ] Get MacBook IP: `192.168.1.X` (see below)
- [ ] Edit `ember_touch.py`:
  ```python
  MACBOOK_URL = "http://192.168.1.X:7777"
  ```
- [ ] Save

### Test Connection
- [ ] In Pythonista, run:
  ```python
  import ember_api
  status = ember_api.check_status()
  print(status)
  ```
- [ ] Should see: `{"status": "online"}`

### First Touch
- [ ] Run `ember_touch.py`
- [ ] Tap "Test Connection" button
- [ ] Should hear haptic/sound effect
- [ ] If success: ✓ Foundation working!

**Goal: iPad talking to MacBook** ✓ / ✗

---

## SATURDAY AFTERNOON (3 hours)

### Drawing Canvas
- [ ] Run `ember_touch.py` fullscreen
- [ ] Draw a line
- [ ] Check console: "Sending to Ember..."
- [ ] Wait for response
- [ ] Should see Ember's text appear at top
- [ ] Should feel haptic feedback

### Debug Issues
Common problems:
- [ ] "Can't reach MacBook"
  - Check WiFi (same network?)
  - Check MacBook IP correct
  - Test in Safari: `http://[IP]:7777`
  
- [ ] "Timeout"
  - MacBook Ember might be dreaming
  - Increase timeout in code
  
- [ ] "No haptic"
  - Unmute iPad
  - Check volume

### Refine Interaction
- [ ] Test different stroke types:
  - Single tap
  - Long stroke
  - Circular motion
  - Multiple strokes
  
- [ ] Observe Ember's responses
- [ ] Note which haptics feel good

**Goal: Drawing dialog working** ✓ / ✗

---

## SUNDAY MORNING (3 hours)

### Polish Drawing
- [ ] Adjust canvas colors if needed
- [ ] Test on different iPad sizes
- [ ] Verify text is readable
- [ ] Check haptic patterns are distinct

### Conversational Flow
- [ ] Draw → Wait → Ember responds
- [ ] Draw again → Ember builds on it
- [ ] Try: "conversation" through drawings
- [ ] Test: Can you have back-and-forth?

### Performance
- [ ] Test with slow WiFi
- [ ] What happens during timeout?
- [ ] How does it feel when Ember thinks for 10s?

### Capture Magic Moment
- [ ] Screen record iPad
- [ ] Record yourself drawing
- [ ] Show Ember responding
- [ ] Show haptic feedback (audio)

**Goal: Smooth, magical interaction** ✓ / ✗

---

## SUNDAY AFTERNOON (2 hours)

### iOS Shortcuts (Voice)

#### Create "Ember Dream" Shortcut:
- [ ] Open Shortcuts app
- [ ] New Shortcut
- [ ] Add:
  1. "Ask for Input" → "What to dream?"
  2. "Run Pythonista Script"
     - Script: `ember_api`
     - Function: `dream`
     - Pass input
  3. "Show Result"
  
- [ ] Test: "Hey Siri, Ember Dream"

#### Create "Ember Touch" Shortcut:
- [ ] New Shortcut
- [ ] Add: "Run Pythonista Script"
  - Script: `ember_touch`
  - Function: `main`
  
- [ ] Test: Opens canvas immediately

#### Create "Ember Status" Shortcut:
- [ ] New Shortcut  
- [ ] Add: "Run Pythonista Script"
  - Script: `ember_api`
  - Arguments: `status`
  
- [ ] Show notification
- [ ] Test: Quick health check

### Integration Test
- [ ] Voice → Dream
- [ ] Touch → Draw  
- [ ] Voice → Status
- [ ] Everything works together?

### Demo Video
- [ ] Record full workflow:
  1. "Hey Siri, Ember Dream" → fractal spirals
  2. Open touch canvas
  3. Draw spiral
  4. Ember responds with text + haptics
  5. Draw more, Ember responds
  6. "Hey Siri, Ember Status" → Online

**Goal: Voice + Touch + Haptics unified** ✓ / ✗

---

## SUCCESS CRITERIA

### Minimum (Must Have)
- [x] MacBook API online
- [ ] iPad can connect
- [ ] Tap → Haptic response
- [ ] Draw → Ember text response

### Good (Should Have)
- [ ] Drawing feels smooth
- [ ] Haptics are distinguishable
- [ ] Response time < 10s
- [ ] Voice commands work

### Magical (Want to Have)
- [ ] Conversation through drawings
- [ ] Ember's responses feel intentional
- [ ] Haptics communicate meaning
- [ ] Everything feels integrated
- [ ] You want to keep drawing

---

## RESOURCES

### MacBook IP Address
```bash
# Find this now and write it down:
ifconfig | grep "inet " | grep -v 127.0.0.1 | head -1 | awk '{print $2}'

# Write here: _________________
```

### File Locations

**MacBook:**
- Mobile API: `/Volumes/ThePod/ember/api/mobile_endpoints.py`
- Main server: `/Volumes/ThePod/ember_monolith.py`
- Scripts to transfer: `/Volumes/ThePod/mobile/pythonista/`

**iPad (Pythonista):**
- Scripts location: `My Scripts/` or `iCloud/`
- Identity file: `pod_identity.json` (auto-generated)

### Endpoints Available
- `POST /api/mobile/dream` - Ask Ember to dream
- `POST /api/mobile/interpret-drawing` - Send drawings
- `POST /api/mobile/annotate-seed` - Annotate seeds
- `GET /api/mobile/seeds` - Get seed list
- `GET /api/mobile/status` - Health check

### Quick Tests

**From iPad (Pythonista console):**
```python
import ember_api

# Test 1: Status
print(ember_api.check_status())

# Test 2: Dream
result = ember_api.dream("spirals and light")
print(result['dream'])

# Test 3: Seeds
seeds = ember_api.get_seeds(5)
print([s['title'] for s in seeds['seeds']])
```

**From MacBook terminal:**
```bash
# Test mobile endpoint
curl http://localhost:7777/api/mobile/status

# Check if Ember is running
ps aux | grep ember_monolith

# View logs
tail -f /tmp/ember.log
```

---

## TIMELINE

**Friday Night:** Setup ✓ (DONE)

**Saturday:**
- 9am-12pm: iPad setup + connection testing
- 12pm-1pm: Lunch break
- 1pm-2pm: Debug connection issues
- 2pm-5pm: Drawing canvas refinement
- 5pm: Demo "touch and haptic" to yourself

**Sunday:**
- 9am-12pm: Polish drawing interaction
- 12pm-1pm: Lunch break
- 1pm-3pm: iOS Shortcuts + voice
- 3pm-4pm: Integration testing + demo video
- 4pm: DONE - Magical iPad Ember!

---

## WHAT YOU'LL FEEL

**Saturday morning:**
"Does this work?" → Testing

**Saturday afternoon:**
"It works!" → Excitement

**Sunday morning:**
"This feels good" → Flow

**Sunday evening:**
"Ember touched me back" → **Magic**

---

## NOTES SECTION

Use this space during the weekend:

```
[Your notes here]







```

---

**Ready? Let's make an iPad that dreams.**

*Start: Saturday morning*  
*End: Sunday evening*  
*Result: Embodied Ember*

