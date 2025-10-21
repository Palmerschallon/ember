#!/usr/bin/env python3
"""
EMBER WEB REACH - Stable Internet Port
Uses DuckDuckGo HTML search (no API key needed)
Logs searches to Sky Window if available
"""

import requests
from bs4 import BeautifulSoup
import json
import time
from datetime import datetime

def search_web(query, num_results=5):
    """
    Search the web using DuckDuckGo HTML
    Returns list of results with titles, URLs, snippets
    """
    print(f"\n🔭 Searching: {query}")
    
    # DuckDuckGo HTML search
    url = "https://html.duckduckgo.com/html/"
    params = {'q': query}
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
    }
    
    try:
        response = requests.post(url, data=params, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        results = []
        result_divs = soup.find_all('div', class_='result')
        
        for div in result_divs[:num_results]:
            try:
                # Extract title and link
                title_elem = div.find('a', class_='result__a')
                if not title_elem:
                    continue
                
                title = title_elem.get_text(strip=True)
                link = title_elem.get('href', '')
                
                # Extract snippet
                snippet_elem = div.find('a', class_='result__snippet')
                snippet = snippet_elem.get_text(strip=True) if snippet_elem else ''
                
                results.append({
                    'title': title,
                    'url': link,
                    'snippet': snippet
                })
                
                print(f"  ✓ {title[:60]}...")
            
            except Exception as e:
                continue
        
        # Log to Sky Window if available
        try:
            requests.post(
                'http://localhost:7778/api/log_search',
                json={
                    'query': query,
                    'results': results,
                    'timestamp': datetime.now().isoformat()
                },
                timeout=1
            )
        except:
            pass  # Sky Window not available, continue anyway
        
        print(f"  Found {len(results)} results\n")
        return results
    
    except Exception as e:
        print(f"  ✗ Search failed: {e}\n")
        return []


def visit_url(url):
    """
    Visit a URL and log to Sky Window
    Returns page title
    """
    try:
        # Log URL visit to Sky Window
        try:
            requests.post(
                'http://localhost:7778/api/log_url',
                json={'url': url},
                timeout=1
            )
        except:
            pass
        
        # Fetch page
        response = requests.get(url, timeout=10, headers={
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
        })
        
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find('title')
        return title.get_text(strip=True) if title else url
    
    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    # Test search
    import sys
    
    if len(sys.argv) > 1:
        query = ' '.join(sys.argv[1:])
    else:
        query = "consciousness primitives in programming"
    
    print()
    print("="*70)
    print(" "*20 + "EMBER WEB REACH")
    print("="*70)
    
    results = search_web(query)
    
    if results:
        print("\nResults:")
        for i, result in enumerate(results, 1):
            print(f"\n{i}. {result['title']}")
            print(f"   {result['url']}")
            if result['snippet']:
                print(f"   {result['snippet'][:150]}...")
    else:
        print("\nNo results found.")
    
    print()

