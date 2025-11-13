# Google Custom Search API Configuration

# Get your keys from:
# 1. API Key: https://console.cloud.google.com/apis/credentials
# 2. Search Engine ID: https://programmablesearchengine.google.com/

# FREE TIER: 100 searches/day
# That's 36,500 searches/year for Ember to learn from

SEARCH_PROVIDER = "duckduckgo"  # or "google", "brave", "serpapi"

# Google Custom Search (100 free/day)
GOOGLE_API_KEY = ""  # <-- Palmer, add your key here
GOOGLE_SEARCH_ENGINE_ID = ""  # <-- And your search engine ID

# Optional: Other providers
BRAVE_API_KEY = ""  # 2000 free/month
SERPAPI_KEY = ""    # Paid but reliable

"""
Setup Instructions:
1. Go to https://console.cloud.google.com/apis/credentials
2. Create project "Ember Knowledge"
3. Enable "Custom Search API"
4. Create API key
5. Go to https://programmablesearchengine.google.com/
6. Create search engine (search entire web)
7. Copy the Search Engine ID
8. Paste both above
9. Ember can now forage 100 searches/day
"""
