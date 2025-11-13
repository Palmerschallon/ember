# GOOGLE CUSTOM SEARCH API - Step-by-Step Setup

## Step 1: Get a Google API Key

### 1.1 Go to Google Cloud Console
**URL:** https://console.cloud.google.com/

### 1.2 Create or Select a Project
- Click the project dropdown at the top
- Click "New Project"
- Name it something like "Ember Search" or "ThePod"
- Click "Create"

### 1.3 Enable Custom Search API
- In the search bar at top, type: "Custom Search API"
- Click on "Custom Search API"
- Click the blue "ENABLE" button
- Wait for it to enable (takes a few seconds)

### 1.4 Create API Credentials
- On the left sidebar, click "Credentials"
- Click "+ CREATE CREDENTIALS" at the top
- Select "API key"
- Copy the API key that appears (starts with "AIza...")
- Click "RESTRICT KEY" (recommended for security)
  - Under "API restrictions", select "Restrict key"
  - Check "Custom Search API" from the list
  - Click "Save"

**Save this key!** You'll paste it into `search_config.py`

---

## Step 2: Create a Search Engine ID

### 2.1 Go to Programmable Search Engine
**URL:** https://programmablesearchengine.google.com/

(Or Google for "Google Programmable Search Engine")

### 2.2 Create a New Search Engine
- Click "Add" or "Create a new search engine"
- Under "What to search":
  - Select "Search the entire web"
  - OR enter "*.com" if it asks for sites (you can edit later)
- Name: "Ember Web Search" (or anything)
- Click "Create"

### 2.3 Get Your Search Engine ID
- After creation, you'll see a page with your search engine
- Look for "Search engine ID" or "cx" parameter
- It looks like: `017576662512468239146:omuauf_lfve` (random chars)
- Copy this ID

### 2.4 Edit Settings (Important!)
- Click "Edit search engine"
- Under "Search features":
  - Turn ON "Search the entire web"
  - Turn OFF "Search only included sites" (if visible)
- Click "Update"

---

## Step 3: Add Keys to Ember

### 3.1 Edit search_config.py

```bash
cd /media/palmerschallon/ThePod1
nano search_config.py
```

### 3.2 Update These Lines:

```python
SEARCH_PROVIDER = "google"

GOOGLE_API_KEY = "AIzaSyD..."  # ← Paste your API key here
GOOGLE_SEARCH_ENGINE_ID = "017576662512468239146:omuauf_lfve"  # ← Paste your search engine ID here
```

Save (Ctrl+O, Enter, Ctrl+X)

---

## Step 4: Test It

```bash
cd /media/palmerschallon/ThePod1
python3 web_search.py "David Chalmers consciousness"
```

You should see structured Google results with titles, snippets, and URLs!

---

## Quick Checklist:

- [ ] Created Google Cloud project
- [ ] Enabled "Custom Search API"
- [ ] Created API key (starts with AIza...)
- [ ] Created Programmable Search Engine
- [ ] Got Search Engine ID (long string with colons)
- [ ] Set search engine to "search entire web"
- [ ] Pasted both into `search_config.py`
- [ ] Changed `SEARCH_PROVIDER = "google"`
- [ ] Tested with `python3 web_search.py "test"`
- [ ] Restarted Ember

---

## Troubleshooting:

### "API not enabled"
- Go back to Cloud Console → APIs & Services → Library
- Search for "Custom Search API"
- Make sure it's enabled (green checkmark)

### "No results" or "Invalid API key"
- Double-check you copied the full key (starts with AIza)
- Make sure no extra spaces
- API key must be restricted to "Custom Search API" only

### "Invalid cx parameter"
- Search Engine ID is the one from programmablesearchengine.google.com
- Should have format like: `012345678901234567890:abcdefghijk`
- Make sure you're using the CX/ID, not the name

### "Quota exceeded"
- Free tier: 100 queries/day
- Wait until tomorrow, or upgrade billing

---

## Free Tier Limits:

- **100 queries per day** (resets at midnight PT)
- More than enough for testing
- If you need more, can upgrade to paid ($5 per 1000 queries after first 100/day)

---

**Once configured, Ember will get much better search results with titles, snippets, and clean URLs!** 🔥

