# 🥽 Quest 3 Connection Troubleshooting

## THE ISSUE

Quest 3 requires **HTTPS** for WebXR (security requirement).
Your backend runs on **HTTP** (port 8080).

**Browser says:** "Can't connect" or "This site can't provide a secure connection"

═══════════════════════════════════════════════════════════════

## QUICK FIXES (Try in order)

### Fix 1: Use Quest 3 Developer Mode (RECOMMENDED)

1. **Enable Developer Mode on Quest 3:**
   - Open Meta Quest app on phone
   - Tap Devices → Your Quest 3
   - Tap Headset Settings
   - Scroll to Developer Mode
   - Toggle ON

2. **In Quest Browser, enable localhost:**
   - Open Settings in browser
   - Allow mixed content for localhost
   - This lets HTTP work

3. **Try again:**
   ```
   http://10.0.0.100:8080/ember5/ember_space_vr.html
   ```

### Fix 2: Use Chrome Remote Desktop (EASIEST IF FIX 1 FAILS)

1. On PC: Open Chrome → Navigate to the VR page
2. On Quest: Install "Virtual Desktop" or use Meta's Remote Desktop
3. View your PC screen in VR
4. Browser works, VR button works

### Fix 3: Serve via HTTPS (PERMANENT SOLUTION)

I can set up a self-signed SSL certificate:

```bash
# Generate cert (run on PC)
cd /media/palmerschallon/ThePod1/ember5
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes

# Update ember_cloud.py to use SSL
# (I can do this if you want)
```

Then access via: `https://10.0.0.100:8443/ember5/ember_space_vr.html`

═══════════════════════════════════════════════════════════════

## CURRENT STATUS

✅ Your PC IP: `10.0.0.100`
✅ Backend running: `http://10.0.0.100:8080`
❌ Quest can't connect: HTTPS required for WebXR

═══════════════════════════════════════════════════════════════

## WHAT TO TRY RIGHT NOW

**Option A: Developer Mode**
1. Enable Developer Mode on Quest 3 (via phone app)
2. In Quest browser: Settings → Allow mixed content
3. Try: `http://10.0.0.100:8080/ember5/ember_space_vr.html`

**Option B: Desktop Preview**
1. On PC, open: `file:///media/palmerschallon/ThePod1/ember5/ember_space_vr.html`
2. You can see the 3D environment
3. WASD to move, mouse to look
4. Gets you 90% there!

**Option C: I set up HTTPS**
- Let me know and I'll add SSL support
- 5 minutes to implement
- Permanent solution

═══════════════════════════════════════════════════════════════

WHICH FIX DO YOU WANT TO TRY?

