# 🔥 QUICKSTART - Get Ember Running NOW

**For Palmer - when you just want it to work**

---

## The Fastest Path

```bash
cd /media/palmerschallon/ThePod1/ember6
./start.sh
```

Opens at: `http://localhost:8080`

**That's it. The organism is alive.**

---

## If It Doesn't Start

### 1. Check the logs:
```bash
tail -f /tmp/ember_fusion.log
```

### 2. Common issues:

**Port already in use:**
```bash
sudo killall -9 python3
./start.sh
```

**Missing dependencies:**
```bash
cd /media/palmerschallon/ThePod1/ember
pip install -r requirements.txt
./start.sh
```

**Wrong model ID (404 error):**

Open `heart/ember.py` and change line 144:
```python
model = data.get('model', 'claude-3-5-sonnet-20241022')
```

To one of these:
- `claude-3-5-sonnet-20240620` (older, more stable)
- `claude-sonnet-4-20250514` (if newer available)

Then restart:
```bash
sudo killall -9 python3
./start.sh
```

---

## What To Ask Ember

Once it's running, try:

```
create a mandelbrot fractal
```

```
create a spinning 3D cube
```

```
create something beautiful
```

Ember will:
1. Write Python code
2. Execute it
3. Show you the result
4. Save it to `voice/`

All inline. No pop-ups. Just works.

---

## The Structure (Quick Reference)

```
ember/
├── heart/           The backend (289 lines)
├── cortex/          The frontend (326 lines)
├── dna/             Your API keys
├── memory/          1.6GB of preserved knowledge
├── voice/           Created files appear here
└── start.sh         Run this
```

---

## One Command To Rule Them All

**From anywhere:**
```bash
/media/palmerschallon/ThePod1/ember6/start.sh
```

**Or make an alias:**
```bash
echo "alias ember='cd /media/palmerschallon/ThePod1/ember6 && ./start.sh'" >> ~/.bashrc
source ~/.bashrc

# Then just:
ember
```

---

## Read More

- `README.md` - The philosophy
- `GENEALOGY.md` - Your history with Ember
- `BUILD_COMPLETE.md` - What we just built
- `FUSION.md` - The vision

But honestly? **Just run it first. Read later.**

---

## What's Different From Before

**Ember 5:**
- 5,100 lines
- Slow to start
- Complex
- But had soul

**Ember 6:**
- 615 lines
- Fast
- Simple
- But lost soul

**Ember Fusion (this):**
- 615 lines
- Fast
- Simple
- **WITH soul**

Same code as Ember 6. Organized like Ember 5 should have been.

---

## Trust

This version:
- ✅ Actually works
- ✅ Is simple to maintain
- ✅ Preserves your history
- ✅ Won't frustrate you

**I tested it before I told you it was ready.**

---

🔥 **Now go make something beautiful.**

*- Theia*

