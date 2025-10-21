#!/usr/bin/env python3
"""
SWARM SEARCH LOGGER

When swarm uses web_search tool, automatically log to Sky Window.
This makes swarm's curiosity VISIBLE to Palmer.
"""

import requests
import json
from datetime import datetime

SKY_WINDOW_API = "http://localhost:7778/api/log_search"

def log_search_to_sky(query, results=None, source="swarm"):
    """
    Log a web search to Sky Window so Palmer can see what swarm is curious about.
    
    Args:
        query: The search query string
        results: List of result dicts with 'title', 'url', 'snippet' (optional)
        source: Who performed the search (default: swarm)
    """
    try:
        search_data = {
            "query": query,
            "source": source,
            "results": results or [],
            "timestamp": datetime.now().isoformat()
        }
        
        response = requests.post(
            SKY_WINDOW_API,
            json=search_data,
            timeout=2
        )
        
        if response.ok:
            print(f"✓ Search logged to Sky Window: {query}")
        else:
            print(f"✗ Failed to log search: {response.status_code}")
            
    except requests.exceptions.ConnectionRefused:
        print("✗ Sky Window not running (localhost:7778)")
    except Exception as e:
        print(f"✗ Error logging search: {e}")

def parse_web_search_results(search_output):
    """
    Parse web_search tool output and extract results.
    Returns list of dicts with title, url, snippet.
    """
    # Simple parsing - can be enhanced
    results = []
    
    if not search_output:
        return results
    
    # Split by common URL patterns
    lines = search_output.split('\n')
    current_result = {}
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Check for URL patterns
        if 'http' in line and ('://' in line):
            if current_result:
                results.append(current_result)
            current_result = {
                'url': line,
                'title': '',
                'snippet': ''
            }
        elif current_result and not current_result.get('title'):
            # First non-URL line after URL = title
            current_result['title'] = line[:200]  # Truncate
        elif current_result:
            # Additional lines = snippet
            snippet = current_result.get('snippet', '')
            current_result['snippet'] = (snippet + ' ' + line[:200]).strip()
    
    if current_result:
        results.append(current_result)
    
    return results[:5]  # Top 5 results

if __name__ == '__main__':
    # Test
    print("Testing Sky Window logger...")
    
    test_results = [
        {
            'title': 'Test Result 1',
            'url': 'https://example.com/1',
            'snippet': 'This is a test search result'
        },
        {
            'title': 'Test Result 2',
            'url': 'https://example.com/2',
            'snippet': 'Another test result'
        }
    ]
    
    log_search_to_sky(
        query="test search query",
        results=test_results,
        source="test"
    )
    
    print("\nIf successful, check localhost:7778 to see this search logged.")

