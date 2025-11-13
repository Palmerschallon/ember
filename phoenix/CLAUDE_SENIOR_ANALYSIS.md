# Claude (Cursor) - Senior Engineer Analysis

**Question:** Where should a "social feed" feature (users sharing AI creations) go in the ember6 codebase?

---

## My Architectural Analysis

### 1. Current Architecture Overview

**ember6 is a Flask backend with:**
- `ember.py` - Main Flask app (~3K lines, does EVERYTHING)
- `conversation_manager.py` - SQLite conversation persistence
- `cortex/` - Frontend UI files (HTML/JS)
- `_mesh/` - Persistent storage (content.db, conversations.db)
- Tool execution, LLM calls, file operations all in main file

**Problems I see:**
- Monolithic `ember.py` (violates single responsibility)
- No clear separation between API routes, business logic, and data access
- Social features (SOCIAL_DB reference on line 79) but not implemented
- No user model or authentication system

### 2. Where Social Feed Should Go

**SHORT ANSWER:** Don't add it to ember.py. Create a new service layer.

**RIGHT ARCHITECTURE:**

```
ember6/
├── ember.py                    # Flask routes ONLY (slim)
├── services/
│   ├── conversation_service.py # Existing conversation logic
│   ├── creation_service.py     # NEW: Creation CRUD
│   └── social_service.py       # NEW: Feed, likes, follows
├── models/
│   ├── user.py                 # NEW: User model
│   ├── creation.py             # NEW: Creation model
│   └── interaction.py          # NEW: Likes, comments
├── data/
│   ├── conversation_manager.py # Existing
│   └── social_repository.py    # NEW: Social data access
├── cortex/
│   ├── ember_ui.html           # Chat UI
│   └── social_feed.html        # NEW: Feed UI
```

### 3. What Files Need to Change

**Immediate Changes:**
1. **ember.py** - Add 3 new routes:
   - `GET /feed` - Fetch social feed
   - `POST /creations/:id/share` - Share a creation
   - `POST /creations/:id/like` - Like a creation

2. **conversation_manager.py** - NO CHANGES (good separation)

3. **NEW: `social_service.py`** - Business logic:
   - Filter feed by user preferences
   - Calculate trending creations
   - Handle privacy settings

4. **NEW: `social_repository.py`** - Data access:
   - Schema: `creations`, `users`, `likes`, `follows`
   - Queries for feed generation
   - SQLite initially, scalable to Postgres

5. **NEW: `cortex/social_feed.html`** - UI for browsing feed

### 4. Data Model

**Missing right now: User identity**

```sql
CREATE TABLE users (
    id TEXT PRIMARY KEY,
    username TEXT UNIQUE,
    created_at TIMESTAMP
);

CREATE TABLE creations (
    id TEXT PRIMARY KEY,
    user_id TEXT REFERENCES users(id),
    conversation_id TEXT REFERENCES conversations(id),
    content TEXT,  -- Code, image, etc.
    type TEXT,     -- 'code', 'image', 'html', etc.
    title TEXT,
    description TEXT,
    created_at TIMESTAMP,
    visibility TEXT  -- 'public', 'unlisted', 'private'
);

CREATE TABLE likes (
    user_id TEXT REFERENCES users(id),
    creation_id TEXT REFERENCES creations(id),
    created_at TIMESTAMP,
    PRIMARY KEY (user_id, creation_id)
);

CREATE TABLE follows (
    follower_id TEXT REFERENCES users(id),
    following_id TEXT REFERENCES users(id),
    created_at TIMESTAMP,
    PRIMARY KEY (follower_id, following_id)
);
```

### 5. Dependencies & Ripple Effects

**What this change touches:**

**Layer 1 - Data:**
- New database schema (4 tables)
- Migration needed for existing creations
- Index on `created_at` for feed queries

**Layer 2 - Backend:**
- New service classes (2 files)
- New routes in ember.py (3 endpoints)
- Authentication middleware (currently missing!)

**Layer 3 - Frontend:**
- New social_feed.html UI
- Updates to ember_ui.html (add "Share" button)
- WebSocket for real-time feed updates?

**Layer 4 - Infrastructure:**
- API rate limiting (prevent spam)
- Image/file hosting (if sharing images)
- Content moderation (if public)

### 6. Architecture Trade-offs

**Option A: Quick & Dirty (Add to ember.py)**
- ✅ Fast to implement (1-2 days)
- ❌ Makes ember.py even more bloated
- ❌ Hard to test
- ❌ Won't scale

**Option B: Proper Service Layer (My recommendation)**
- ✅ Clean separation of concerns
- ✅ Testable
- ✅ Scalable
- ❌ Takes longer (1 week)
- ❌ Requires refactoring

**Option C: Microservice**
- ✅ Fully decoupled
- ✅ Independently scalable
- ❌ Overkill for current scale
- ❌ Operational complexity

**I'd choose Option B.** Clean architecture now saves pain later.

### 7. Implementation Order

**Week 1: Foundation**
1. Create user model and auth (MUST HAVE FIRST)
2. Create creation model
3. Schema migration

**Week 2: Core Features**
4. POST /creations/:id/share endpoint
5. GET /feed endpoint (basic)
6. social_feed.html UI

**Week 3: Social Features**
7. Likes system
8. Follow system
9. Feed algorithm (trending, personalized)

**Week 4: Polish**
10. Real-time updates (WebSocket)
11. Content moderation
12. Performance optimization

### 8. Key Risks

**Risk 1: No authentication system**
- Currently ember6 has NO user model
- Can't share if we don't know who you are
- Must build auth FIRST

**Risk 2: Conversations != Creations**
- Conversations are chat history
- Creations are shareable artifacts
- Need to extract creations from conversations

**Risk 3: Scale**
- Feed queries can get expensive
- Will need caching layer eventually
- Start simple (chronological feed)

**Risk 4: Content**
- Users might share inappropriate content
- Need moderation strategy
- Start with "unlisted" links (no public discovery)

### 9. Simplest Possible First Step

**If you need to ship SOMETHING this week:**

```python
# Add to ember.py:
@app.route('/share/<conversation_id>')
def share_conversation(conversation_id):
    """Generate a shareable link to a conversation"""
    conv = get_conversation(conversation_id)
    if not conv:
        return "Not found", 404
    
    # Generate unique share token
    share_token = hashlib.sha256(conversation_id.encode()).hexdigest()[:12]
    
    # Store in social.db
    db = sqlite3.connect(SOCIAL_DB)
    db.execute("""
        INSERT OR REPLACE INTO shares (token, conversation_id, created_at)
        VALUES (?, ?, ?)
    """, (share_token, conversation_id, datetime.now()))
    db.commit()
    
    return jsonify({
        "url": f"https://ember.app/s/{share_token}"
    })

@app.route('/s/<share_token>')
def view_shared(share_token):
    """View a shared conversation"""
    db = sqlite3.connect(SOCIAL_DB)
    result = db.execute("""
        SELECT conversation_id FROM shares WHERE token = ?
    """, (share_token,)).fetchone()
    
    if not result:
        return "Not found", 404
        
    conv = get_conversation(result[0])
    return render_template('shared.html', conversation=conv)
```

**This gets you:**
- ✅ Shareable links in 1 day
- ✅ No refactoring needed
- ✅ Can iterate from here

**But eventually you'll need proper architecture.**

---

## Summary: Senior Engineer Take

**Where should it go?**
New service layer (`services/social_service.py`), not in ember.py

**What needs to change?**
- 4 new database tables (users, creations, likes, follows)
- 3 new routes in ember.py
- 2 new service files
- 1 new UI file
- Authentication system (currently missing)

**What's the right first step?**
Add simple shareable links first (1 day), then refactor to proper architecture (1 week)

**What's the biggest risk?**
No user model exists. Must build auth before social features make sense.

**What would I do?**
- This week: Simple shareable links (quick win)
- Next week: Refactor to service layer while it's still small
- Month 2: Add feed, likes, follows

**The key insight:**
ember.py is already too big. Don't make it worse. Social features need their own layer.

---

*Now let's see if Phoenix/Opus 4 reaches the same conclusions...* 🔥


