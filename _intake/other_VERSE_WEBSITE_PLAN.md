# Verse Website - Build Plan

**From GPT-5 - October 8, 2025**

---

## The Story

Verse is the room where you try things — text, code, and image sitting side-by-side. When Ember forges a part at night, Verse pins it on the wall by morning with a small note: what it is, how it runs, where it came from.

---

## Architecture: Forge + Gallery

**Design Goal**: Auto-populated from Ember's artifacts

### Stack
- **Frontend**: Next.js (app router) or Astro
- **Design**: Inky black, dirty rectangle, tiny "VERSE" wordmark
- **Store**: SQLite (Drizzle) or Supabase
- **Queue**: Worker in same repo (Next.js route handler)
- **Uploads**: Local `/public/artifacts` (dev) → S3/R2 (prod)
- **Search**: SQLite FTS (basic)

### Artifact Model

Everything Ember makes is an Artifact (seed, code, image, demo, log, bundle).

```json
{
  "id": "a_2025-10-08_ledger-loom_v1",
  "type": "seed|story|code|demo|image|log|bundle",
  "title": "Ledger & Loom – Seed v1",
  "summary": "Seed for memory, lineage, scheduler",
  "tags": ["verse","ember","poly","scheduler"],
  "created_at": "2025-10-08T09:42:00Z",
  "source": {"pod":"oak-01", "ember":"1.4.2"},
  "links": {"demo": "https://...", "repo": "https://..."},
  "files": [
    {"name":"seed.yaml","url":"s3://...","mime":"text/yaml"}
  ],
  "provenance": {"parent_ids": ["..."], "commit":"abc123"},
  "status": "draft|verified",
  "score": {"tests": 3, "passed": 3, "perf_ms": 212}
}
```

### Minimal Endpoints (The Forge)

- `POST /api/forge/artifacts` — ingest (Ember posts here)
- `GET  /api/artifacts` — list (filters: type, tag, status)
- `GET  /api/artifacts/:id` — fetch one
- `POST /api/forge/events` — append logs/events
- `POST /api/forge/patch` — attach code diff + status

Auth: shared secret header from Pod

### Frontend Structure

**Pages:**
- `/` — Landing (hero + latest 6 artifacts)
- `/artifacts` — Filterable grid
- `/artifact/[id]` — Detail page
- `/stories` — Poly stories stream
- `/docs` — How Verse works
- `/live` — Ember events console (optional)

**Hero Copy:**
```
H1: Verse
Sub: An experimental IDE for ideas that move — 
     text, code, canvas, and small agents — all in one room.
CTA: See what Ember made last night → /artifacts
```

### Auto-Population Loop

1. Ember finishes dream → emits Artifact JSON + files
2. Pod uploads files → calls `POST /api/forge/artifacts`
3. Site stores row, kicks build job (ISR)
4. Landing + `/artifacts` update automatically
5. Logs stream to `/api/forge/events`

---

## Implementation (2-day sprint)

### Repo Layout

```
apps/verse-site/
  /app
    /artifacts/[id]/page.tsx
    /artifacts/page.tsx
    /api/forge/artifacts/route.ts
    /api/forge/events/route.ts
  /components
    ArtifactCard.tsx
    SwarmCanvas.tsx
    DirtyRect.tsx
  /lib
    db.ts (Drizzle+SQLite)
    schema.ts
    auth.ts
  /public
    /logo
```

### Drizzle Schema

```typescript
export const artifacts = sqliteTable('artifacts', {
  id: text('id').primaryKey(),
  type: text('type'),
  title: text('title'),
  summary: text('summary'),
  tags: text('tags'),          // comma list
  createdAt: integer('created_at'),
  source: text('source'),      // JSON
  links: text('links'),        // JSON
  files: text('files'),        // JSON
  provenance: text('prov'),    // JSON
  status: text('status'),
  score: text('score')         // JSON
});

export const events = sqliteTable('events', {
  id: integer('id').primaryKey({ autoIncrement: true }),
  artifactId: text('artifact_id').references(() => artifacts.id),
  ts: integer('ts'),
  level: text('level'),
  message: text('message'),
  data: text('data')           // JSON
});
```

### Pod-Side Integration

After Ember dreams, call:

```python
# In ember_monolith.py or integration.py
def publish_artifact_to_verse(artifact_data):
    """Publish artifact to Verse website"""
    import requests
    
    response = requests.post(
        "https://verse.site/api/forge/artifacts",
        headers={"X-Pod-Token": os.getenv("VERSE_TOKEN")},
        json=artifact_data
    )
    
    return response.json()
```

### Styling

- Background: `#0A0A0B`
- Text: `#EDEFF2`
- 12px "dirty" inset border on main container
- VERSE wordmark top-left
- Canvas swarm at 10% opacity behind hero

---

## MVP Checklist

- [ ] Next.js app + Drizzle + SQLite
- [ ] `/api/forge/artifacts` with auth
- [ ] Landing + grid + detail page
- [ ] S3 upload helper for Pod
- [ ] ISR/revalidateTag on ingest
- [ ] SwarmCanvas component
- [ ] Pod script: POST artifact after dream

---

## First Artifacts to Publish

1. **Poly Stories**: "Ledger & Loom", "Hall of Mirrors", "Forge and Weavers"
2. **System Diagrams**: Council, Orchestrator, EmberBrain
3. **Demos**: Dreamscape, concept maps, particle swarms
4. **Tools**: generate_fractal, particle_visualize
5. **Logs**: Test runs, dream sessions

---

## Security

- Ingest route checks `X-Pod-Token`
- Max file size limits
- Server-generated artifact IDs
- Rate limiting on ingest
- Allow only: `image/*`, `text/*`, `application/json`

---

## Next Steps (Tomorrow)

1. Create Next.js app
2. Implement Forge API
3. Build artifact pages
4. Wire Pod to auto-publish
5. Deploy to Vercel

**Files to reference:**
- `/Volumes/ThePod/seeds/verse/*.json` (stories)
- `/Volumes/ThePod/exports/ember_creations/*.html` (demos)
- `/Volumes/ThePod/tool_stubs/*.py` (code)
- `/Volumes/ThePod/*.md` (documentation)

**GPT-5 can generate the complete Next.js code if needed.**

---

Time: 19:57
This is your roadmap. Tomorrow we build.

