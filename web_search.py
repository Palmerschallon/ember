#!/usr/bin/env python3
"""
Web Search Providers for Ember
Supports: DuckDuckGo (free), Google (API), Brave (API), SerpAPI (paid)
"""

import urllib.parse
import urllib.request
import json
from html.parser import HTMLParser
from pathlib import Path

# Load config
config_path = Path(__file__).parent / "search_config.py"
if config_path.exists():
    import importlib.util
    spec = importlib.util.spec_from_file_location("search_config", config_path)
    config = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(config)
    SEARCH_PROVIDER = getattr(config, "SEARCH_PROVIDER", "duckduckgo")
    GOOGLE_API_KEY = getattr(config, "GOOGLE_API_KEY", "")
    GOOGLE_SEARCH_ENGINE_ID = getattr(config, "GOOGLE_SEARCH_ENGINE_ID", "")
    BRAVE_API_KEY = getattr(config, "BRAVE_API_KEY", "")
    SERPAPI_KEY = getattr(config, "SERPAPI_KEY", "")
else:
    SEARCH_PROVIDER = "duckduckgo"
    GOOGLE_API_KEY = ""
    GOOGLE_SEARCH_ENGINE_ID = ""
    BRAVE_API_KEY = ""
    SERPAPI_KEY = ""

class HTMLTextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []
    def handle_data(self, data):
        self.text.append(data.strip())
    def get_text(self):
        return ' '.join([t for t in self.text if t])

def search_duckduckgo(query):
    """Free, no API key, but limited"""
    try:
        search_url = f"https://html.duckduckgo.com/html/?q={urllib.parse.quote(query)}"
        req = urllib.request.Request(search_url, headers={'User-Agent': 'Mozilla/5.0'})
        
        with urllib.request.urlopen(req, timeout=10) as response:
            html = response.read().decode('utf-8', errors='ignore')
        
        parser = HTMLTextExtractor()
        parser.feed(html)
        text = parser.get_text()[:800]
        
        return text if text else f"No results found for: {query}"
    except Exception as e:
        return f"DuckDuckGo search error: {e}"

def search_google(query):
    """Best results, 100 free queries/day"""
    if not GOOGLE_API_KEY or not GOOGLE_SEARCH_ENGINE_ID:
        return "Google search requires API key. Edit search_config.py"
    
    try:
        url = f"https://www.googleapis.com/customsearch/v1?key={GOOGLE_API_KEY}&cx={GOOGLE_SEARCH_ENGINE_ID}&q={urllib.parse.quote(query)}"
        req = urllib.request.Request(url)
        
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode('utf-8'))
        
        if 'items' not in data:
            return f"No results found for: {query}"
        
        results = []
        for item in data['items'][:5]:
            title = item.get('title', '')
            snippet = item.get('snippet', '')
            link = item.get('link', '')
            results.append(f"• {title}\n  {snippet}\n  {link}")
        
        return f"Google results for '{query}':\n\n" + "\n\n".join(results)
    except Exception as e:
        return f"Google search error: {e}"

def search_brave(query):
    """Privacy-focused, 2000 free queries/month"""
    if not BRAVE_API_KEY:
        return "Brave search requires API key. Edit search_config.py"
    
    try:
        url = f"https://api.search.brave.com/res/v1/web/search?q={urllib.parse.quote(query)}"
        req = urllib.request.Request(
            url,
            headers={
                'X-Subscription-Token': BRAVE_API_KEY,
                'Accept': 'application/json'
            }
        )
        
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode('utf-8'))
        
        if 'web' not in data or 'results' not in data['web']:
            return f"No results found for: {query}"
        
        results = []
        for item in data['web']['results'][:5]:
            title = item.get('title', '')
            description = item.get('description', '')
            url = item.get('url', '')
            results.append(f"• {title}\n  {description}\n  {url}")
        
        return f"Brave results for '{query}':\n\n" + "\n\n".join(results)
    except Exception as e:
        return f"Brave search error: {e}"

def search_serpapi(query):
    """Paid but very reliable"""
    if not SERPAPI_KEY:
        return "SerpAPI requires API key. Edit search_config.py"
    
    try:
        url = f"https://serpapi.com/search?q={urllib.parse.quote(query)}&api_key={SERPAPI_KEY}"
        req = urllib.request.Request(url)
        
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode('utf-8'))
        
        if 'organic_results' not in data:
            return f"No results found for: {query}"
        
        results = []
        for item in data['organic_results'][:5]:
            title = item.get('title', '')
            snippet = item.get('snippet', '')
            link = item.get('link', '')
            results.append(f"• {title}\n  {snippet}\n  {link}")
        
        return f"SerpAPI results for '{query}':\n\n" + "\n\n".join(results)
    except Exception as e:
        return f"SerpAPI error: {e}"

def web_search(query):
    """Main search function - routes to configured provider"""
    provider_map = {
        "duckduckgo": search_duckduckgo,
        "google": search_google,
        "brave": search_brave,
        "serpapi": search_serpapi,
    }
    
    search_func = provider_map.get(SEARCH_PROVIDER, search_duckduckgo)
    result = search_func(query)
    
    # Add hint about perceiving URLs
    return f"{result}\n\n(Use perceive() to read specific URLs if you find them)"

if __name__ == "__main__":
    # Test search
    import sys
    query = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "consciousness philosophy"
    print(f"\nTesting {SEARCH_PROVIDER} search for: {query}\n")
    print(web_search(query))

