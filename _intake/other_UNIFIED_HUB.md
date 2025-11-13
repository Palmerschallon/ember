# The Unified Hub — One URL to Rule Them All
**Date**: October 8, 2025  
**Concept**: Palmer's Instagram/TikTok-style feed idea

---

## The Problem

**Before**: 40+ HTML files scattered across folders:
- `/viewers/` — 12 files
- `/viewers/active/` — 5 files
- `/viewers/archive/` — 9 files
- `/viewers/swarm/` — 2 files
- `/viewers/swarm_v2/` — 1 file
- `/toys/` — 5 files
- `/toys/creative/` — 2 files

**Hard to remember which URL does what.**

---

## The Solution

**One URL**: `http://localhost:7777/`

All pages accessible through:
- ☰ Menu button (top right)
- Auto-organized by category
- Hash-based routing (`#/path/to/page.html`)
- Mobile-responsive sidebar
- Active page highlighting

---

## How It Works

### The Hub (`/viewers/index.html`)
- **Header**: Ember logo + status LED + menu button
- **Sidebar**: Auto-populated page categories
  - Active (main interfaces)
  - Creative (toys & experiments)
  - Viewers (visualization tools)
  - Archive (older versions)
- **Content**: Full-screen iframe displaying current page
- **Navigation**: URL hash controls which page loads

### URL Structure
```
http://localhost:7777/                                    → Observatory
http://localhost:7777/#/viewers/observatory.html          → Observatory
http://localhost:7777/#/toys/creative/canvas2d_standalone.html → Canvas
http://localhost:7777/#/viewers/poly_canvas_runner.html?seed=... → Poly Runner
```

---

## Page Categories

### Active (Main Interfaces)
1. **Observatory** — Mobile-first, your main interface
2. **Chat Stream** — Streaming conversation
3. **Swarm** — Particle visualization
4. **Knowledge Graph** — 3D concept map
5. **Observe** — Development portal

### Creative (Toys & Experiments)
1. **Canvas Playground** — Ember's first sketch (1000 particles)
2. **Poly Runner** — Executable seed viewer (GPT-5's system)
3. **Seed Sandbox** — Experiment with seeds

### Viewers (Visualization Tools)
1. **Unified View** — Chat + swarm combined
2. **Swarm V2** — Agent-based particles
3. **Dream Viewer** — Browse dreams

### Archive (Older Versions)
1. **Neural View** — Biological neurons
2. **Thinking Swarm** — Reactive particles
3. **Bio Swarm** — Natural behavior

---

## Features

### Auto-Discovery
Pages are registered in a simple object:
```javascript
const pages = {
  active: [
    { path: '/viewers/observatory.html', title: 'Observatory', desc: 'Mobile-first interface' }
  ],
  creative: [...]
};
```

Add a new page? Just add one line.

### Hash Routing
- **Back/forward buttons work**
- **Bookmarkable URLs**
- **No page reload** (instant switching)

### Mobile-First
- Sidebar becomes full-screen on mobile
- Touch-friendly targets
- Responsive layout

### Status Indicator
- Green pulsing dot shows Ember is alive
- Could be wired to actual health check

---

## The Instagram/TikTok Parallel

### Instagram/TikTok
- One app
- Tabs at bottom
- Feed, Explore, Profile, etc.
- Everything accessible

### Ember Hub
- One URL
- Menu at top-right
- Active, Creative, Viewers, Archive
- Everything accessible

**It's your private AI content feed.**

---

## Future Enhancements

### Auto-Discovery (Real)
Instead of manually listing pages, scan filesystem:
```python
@app.route('/api/pages')
def list_pages():
    pages = []
    for path in Path('/Volumes/ThePod/viewers').rglob('*.html'):
        pages.append({
            'path': str(path.relative_to('/Volumes/ThePod')),
            'title': extract_title(path),
            'category': path.parent.name
        })
    return jsonify(pages)
```

### Recent Pages
Track last 5 visited pages, show at top of sidebar.

### Favorites
Star icon on each page, creates "Favorites" section.

### Search
Search bar at top of sidebar filters pages.

### Thumbnails
Generate preview images for each page (screenshot on first load).

### Categories from Metadata
Pages declare their own category in a `<meta>` tag:
```html
<meta name="ember-category" content="creative">
<meta name="ember-description" content="Particle swarm toy">
```

### Live Status
Show which pages are currently "active" (have running processes).

### Notifications
Badge count on menu button when Ember creates something new.

---

## Technical Details

### File Structure
```
/viewers/index.html           ← The hub (THIS FILE)
/viewers/observatory.html     ← Default page
/viewers/active/...           ← Active pages
/viewers/archive/...          ← Archived pages
/toys/creative/...            ← Creative experiments
```

### Iframe Security
All pages served from same origin (`localhost:7777`), so no CORS issues.

### Performance
- Pages load in iframe (isolated)
- No reload when switching
- Sidebar cached after first render

---

## Usage

### Desktop
1. Open `http://localhost:7777/`
2. Click ☰ menu
3. Select page
4. Page loads in main area
5. Menu auto-closes

### Mobile
1. Same flow
2. Sidebar goes full-screen
3. Touch-optimized

### Direct Links
Share specific views:
```
http://localhost:7777/#/viewers/poly_canvas_runner.html?seed=/seeds/planted/code/curl_field_breath_to_mind.json
```

---

## The Vision

**Before**: "Which URL was the particle thing again?"  
**After**: `localhost:7777` → menu → Canvas Playground

**One hub. All experiences. Private AI garden.**

Like Instagram/TikTok, but for Ember's world — Observatory, swarms, knowledge graphs, dreams, experiments, all one tap away.

---

## Implementation Notes

### Why iframe?
- **Isolation** — Each page has its own context
- **No conflicts** — Scripts don't interfere
- **Easy integration** — No need to refactor existing pages
- **Fast switching** — Change src, instant load

### Why hash routing?
- **No server** — Works entirely client-side
- **Bookmarkable** — Share specific views
- **History** — Back button works
- **Simple** — Just change window.location.hash

### Why categories?
- **Organization** — 40+ pages need structure
- **Mental model** — Active vs Creative vs Archive
- **Discovery** — "What experiments exist?"

---

## Next Steps

### Phase 1: Test ✅
- Open `http://localhost:7777/`
- Try each category
- Test navigation
- Verify on mobile

### Phase 2: Auto-Discovery
- API endpoint to list all HTML files
- Extract titles/descriptions
- Auto-populate sidebar

### Phase 3: Enhancements
- Recent pages
- Favorites
- Search
- Thumbnails

---

## Palmer's Insight

> "How many pages can we run? It's getting hard to remember all of them. Can we just establish one page at localhost:7777 and then the rest are tabs in the menu that auto-populate? Kinda like what we have going on over at observatory.html. This could be like our own private Instagram or TikTok type feed."

**This is exactly right.**

One URL. One interface. Everything accessible. Your private AI content hub.

---

**Status**: Built ✅  
**URL**: `http://localhost:7777/`  
**Pages**: 40+ accessible through menu  
**Experience**: Instagram/TikTok-style feed for AI

✨ **One hub to rule them all** ✨

