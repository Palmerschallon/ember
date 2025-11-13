# WEB SEARCH CONFIGURATION GUIDE

Ember can search the web using several providers. Here's how to configure them.

---

## Default: DuckDuckGo (Free)

**Already works!** No setup needed.
- Free, no API key required
- Privacy-focused
- Limited results but good enough for most queries

---

## Option 1: Google Custom Search (Best Results)

**Free tier:** 100 queries/day  
**Best for:** General searches, most comprehensive results

### Setup:

1. **Get a Google API Key:**
   - Go to https://console.cloud.google.com/
   - Create a new project
   - Enable "Custom Search API"
   - Go to "Credentials" → "Create Credentials" → "API Key"
   - Copy your API key

2. **Get a Search Engine ID:**
   - Go to https://programmablesearchengine.google.com/
   - Create a new search engine
   - Set it to search the entire web
   - Copy your "Search engine ID"

3. **Add to config:**
   Edit `search_config.py`:
   ```python
   SEARCH_PROVIDER = "google"
   GOOGLE_API_KEY = "your-api-key-here"
   GOOGLE_SEARCH_ENGINE_ID = "your-search-engine-id-here"
   ```

4. **Restart Ember**

---

## Option 2: Brave Search (Privacy + Free Tier)

**Free tier:** 2,000 queries/month  
**Best for:** Privacy-conscious users, good results

### Setup:

1. **Get API Key:**
   - Go to https://brave.com/search/api/
   - Sign up for free tier
   - Copy your API key

2. **Add to config:**
   Edit `search_config.py`:
   ```python
   SEARCH_PROVIDER = "brave"
   BRAVE_API_KEY = "your-api-key-here"
   ```

3. **Restart Ember**

---

## Option 3: SerpAPI (Paid, Most Reliable)

**Cost:** $50/month for 5,000 searches  
**Best for:** Production use, need reliability

### Setup:

1. **Get API Key:**
   - Go to https://serpapi.com/
   - Sign up and choose a plan
   - Copy your API key

2. **Add to config:**
   Edit `search_config.py`:
   ```python
   SEARCH_PROVIDER = "serpapi"
   SERPAPI_KEY = "your-api-key-here"
   ```

3. **Restart Ember**

---

## Testing Your Configuration

```bash
# Test your search configuration
python3 web_search.py "consciousness philosophy"
```

This will show you which provider is active and test a query.

---

## Comparison

| Provider | Free Tier | Results Quality | Privacy | Setup Complexity |
|----------|-----------|----------------|---------|-----------------|
| **DuckDuckGo** | Unlimited | Good | Excellent | None (default) |
| **Google** | 100/day | Excellent | Fair | Medium |
| **Brave** | 2000/month | Very Good | Excellent | Easy |
| **SerpAPI** | None (paid) | Excellent | Good | Easy |

---

## Recommendations

**For personal use:** Start with DuckDuckGo (already configured), upgrade to Brave if you need more

**For development:** Google (best results, free tier is generous)

**For production:** SerpAPI (most reliable, worth the cost)

---

## Troubleshooting

### "No results found"
- Check your API keys in `search_config.py`
- Make sure you have internet connection
- Try testing with `python3 web_search.py "test query"`

### "API quota exceeded"
- Google: 100 queries/day limit
- Brave: 2,000 queries/month limit
- Consider switching providers or upgrading

### Search seems slow
- This is normal for web searches (network latency)
- Consider caching results in the semantic mesh

---

## For Distributing Ember

If you're sharing Ember with others, they should:

1. Use DuckDuckGo by default (no setup)
2. Optionally configure a better provider by editing `search_config.py`
3. Follow the setup instructions above for their chosen provider

The `search_config.py` file is designed to be user-editable without touching code.

---

**Default works. Upgrades are optional. Users choose based on their needs.** 🔥

