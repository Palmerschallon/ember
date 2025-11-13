# How to Explore Ember's Work

**Quick Reference Guide**

---

## 📊 Overview Reports

### 1. Artifact Summary
```bash
python3 /Volumes/ThePod/scripts/curate_artifacts.py report
```
Shows all 454 artifacts categorized:
- 165 HTML visualizations
- 123 JSON synthesis graphs
- 12 Python scripts
- 19 code snippets
- Quality ratings

### 2. Recent Dreams (JSON format)
```bash
curl -s 'http://127.0.0.1:7777/api/dreams/recent?limit=10' | python3 -m json.tool
```
Structured data about last 10 dreams with:
- Dream ID, timestamp, type
- Seeds used
- Full narrative text
- Tools mentioned
- Artifacts created

### 3. System Status
```bash
curl -s http://127.0.0.1:7777/api/status | python3 -m json.tool
```
Current state: seeds, memories, idle time, next dream

---

## 🔍 Browse by Category

### HTML Visualizations (165 files)
```bash
ls -lth /Volumes/ThePod/exports/ember_creations/*.html | head -20
```
**Top picks** (confirmed working):
- `council_of_seven_constellation.html` - Interactive constellation ⭐⭐⭐
- `polysemous-editor.html` - Multi-meaning text editor ⭐⭐
- `councils_convergence.html` - Council visualization ⭐⭐
- `swarm_atoms_webgl2_palmer.html` - Particle swarm ⭐⭐⭐
- `spectral_odyssey.html` - Color/frequency journey ⭐⭐
- `particles_1e6288d2.html` - Particle system ⭐

Open any in browser:
```bash
open /Volumes/ThePod/exports/ember_creations/council_of_seven_constellation.html
```

### JSON Synthesis Graphs (123 files)
```bash
ls /Volumes/ThePod/exports/ember_creations/*synthesis_graph*.json | head -10
```
These show how Ember connects concepts. View with:
```bash
python3 /Volumes/ThePod/scripts/create_json_viewers.py
# Then open the *_viewer.html files
```

### Python Scripts (12 files)
```bash
ls -lh /Volumes/ThePod/exports/ember_creations/*.py
```
View any script:
```bash
cat /Volumes/ThePod/exports/ember_creations/council_negotiation.py
```

---

## 📅 Browse by Time

### Last 24 Hours
```bash
find /Volumes/ThePod/exports/ember_creations -type f -mtime -1 -name "*.html" | head -20
```

### Last Hour
```bash
find /Volumes/ThePod/exports/ember_creations -type f -mmin -60
```

### Newest 10
```bash
ls -lt /Volumes/ThePod/exports/ember_creations | head -11
```

---

## 🧠 Browse Dreams Directly

### Latest Dream
```bash
ls -td /Volumes/ThePod/memory/dreams/dream-* | head -1 | xargs -I {} cat {}/dream.json | python3 -m json.tool
```

### All Dreams from Today
```bash
find /Volumes/ThePod/memory/dreams -name "dream.json" -mtime -1 | wc -l  # Count
find /Volumes/ThePod/memory/dreams -name "dream.json" -mtime -1 | head -5  # List first 5
```

### Read a Specific Dream
```bash
cat /Volumes/ThePod/memory/dreams/dream-1760037942/dream.json | python3 -m json.tool
```

### Dreams by Type
```bash
# Creative dreams (the imaginative ones)
grep -r '"type": "creative"' /Volumes/ThePod/memory/dreams --include="dream.json" | wc -l

# Synthesis dreams (connecting concepts)
grep -r '"type": "synthesis"' /Volumes/ThePod/memory/dreams --include="dream.json" | wc -l

# Consolidation dreams (organizing memories)
grep -r '"type": "consolidation"' /Volumes/ThePod/memory/dreams --include="dream.json" | wc -l
```

---

## 🎨 Find Specific Content

### Dreams about Fractals
```bash
grep -r "fractal" /Volumes/ThePod/memory/dreams --include="dream.json" -l | tail -5
```

### Dreams that Tried to Use Tools
```bash
grep -r "generate\|detect\|track" /Volumes/ThePod/memory/dreams --include="dream.json" -l | tail -10
```

### Dreams about Specific Seeds
```bash
# Find dreams that referenced the Council of Seven
grep -r "council-of-seven" /Volumes/ThePod/memory/dreams --include="dream.json" -l
```

---

## 📈 Statistics

### Total Dream Count
```bash
ls -1d /Volumes/ThePod/memory/dreams/dream-* | wc -l
```

### Dreams per Day (Last 7 Days)
```bash
for i in {0..6}; do
  count=$(find /Volumes/ThePod/memory/dreams -name "dream.json" -mtime $i -mtime -$((i+1)) | wc -l)
  echo "Day -$i: $count dreams"
done
```

### Artifacts per Type
```bash
echo "HTML: $(ls /Volumes/ThePod/exports/ember_creations/*.html 2>/dev/null | wc -l)"
echo "JSON: $(ls /Volumes/ThePod/exports/ember_creations/*.json 2>/dev/null | wc -l)"
echo "Python: $(ls /Volumes/ThePod/exports/ember_creations/*.py 2>/dev/null | wc -l)"
```

### Storage Used
```bash
du -sh /Volumes/ThePod/memory/dreams
du -sh /Volumes/ThePod/exports/ember_creations
du -sh /Volumes/ThePod/seeds
```

---

## 🔴 Live Monitoring

### Watch Dreams Happen in Real-Time
```bash
tail -f /Volumes/ThePod/ember.log | grep -E "(LLM|🔍|💭|Dream)"
```

### Watch for New Artifacts
```bash
watch -n 5 "ls -lt /Volumes/ThePod/exports/ember_creations | head -10"
```

### Watch Dream Alerts
```bash
tail -f /Volumes/ThePod/ember.log | grep "🔔"
```

---

## 🎯 Quality Filtering

### High-Quality Dreams Only (score ≥ 7)
Look for dreams with:
- Tool execution
- Artifact creation
- Novel concept bridges

```bash
# Check recent dream scores in the log
tail -100 /Volumes/ThePod/ember.log | grep "🔔"
```

### Working Visualizations Only
```bash
# Use the curation script to identify working HTML
python3 /Volumes/ThePod/scripts/curate_artifacts.py report | grep -A 10 "Valid Artifacts"
```

---

## 💡 Pro Tips

### View a Random Dream
```bash
ls /Volumes/ThePod/memory/dreams/dream-*/dream.json | shuf -n 1 | xargs cat | python3 -m json.tool | less
```

### Find Ember's Longest Dream
```bash
find /Volumes/ThePod/memory/dreams -name "dream.json" -exec wc -c {} + | sort -rn | head -5
```

### See What Seeds Ember Uses Most
```bash
grep -roh '"seed-[^"]*"' /Volumes/ThePod/memory/dreams --include="dream.json" | sort | uniq -c | sort -rn | head -20
```

### Gallery of All Working Visualizations
```bash
# Create a quick index
ls /Volumes/ThePod/exports/ember_creations/*.html | while read f; do
  echo "<a href='file://$f'>$(basename $f)</a><br>" 
done > /tmp/ember_gallery.html
open /tmp/ember_gallery.html
```

---

## 🌐 Web Interface

### Main Hub (Best for browsing)
```
http://127.0.0.1:7777
```
Shows latest creations with thumbnails/previews

### API Endpoints
```bash
# Recent dreams
curl http://127.0.0.1:7777/api/dreams/recent?limit=5

# All creations
curl http://127.0.0.1:7777/api/creations

# Watch for alerts
curl http://127.0.0.1:7777/api/dreams/watch/alerts?limit=20

# System status
curl http://127.0.0.1:7777/api/status
```

---

## 📚 Deep Dive: Anatomy of a Dream

Each dream folder contains:
```
/memory/dreams/dream-XXXXXXXXXX/
  ├── dream.json          # Main dream data
  ├── graph.json          # Concept connections (synthesis only)
  ├── patterns.json       # Identified patterns (synthesis only)
  └── artifacts/          # Generated files (if any)
```

Example:
```bash
cd /Volumes/ThePod/memory/dreams/dream-1760037942
cat dream.json | python3 -m json.tool
```

---

## 🎨 Current Highlights (Oct 9, 2025)

**Best Working Visualizations**:
1. `council_of_seven_constellation.html` - 7 modes as orbiting constellation
2. `swarm_atoms_webgl2_palmer.html` - WebGL particle swarm
3. `polysemous-editor.html` - Multi-meaning text interface
4. `councils_convergence.html` - Council dynamics
5. `spectral_odyssey.html` - Frequency/color journey

**Interesting Patterns**:
- Ember dreams about fractals frequently (20+ mentions)
- "Whispering Winds" concept recurring (forest + particles)
- Synthesis dreams finding 3-4 main concept clusters
- Bridge concepts connecting quantum ↔ verse ↔ code

**Activity Level**:
- 202 dreams in last 24 hours
- 454 total artifacts created
- 66% are viewable (up from 42% before curation)
- 22 confirmed working visualizations

---

*The hub is for quick browsing. These commands are for deep exploration.*

