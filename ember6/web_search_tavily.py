#!/usr/bin/env python3
"""
Modern web search using Tavily API (built for AI agents)
Replaces custom DuckDuckGo scraping
"""

import os
from tavily import TavilyClient

# Load from .env file if not in environment
if not os.getenv("TAVILY_API_KEY"):
    try:
        from pathlib import Path
        env_file = Path(__file__).parent / ".env"
        if env_file.exists():
            with open(env_file) as f:
                for line in f:
                    if line.startswith("TAVILY_API_KEY"):
                        key = line.split("=", 1)[1].strip().strip('"')
                        os.environ["TAVILY_API_KEY"] = key
                        break
    except:
        pass

def web_search(query, max_results=5):
    """
    Search the web using Tavily API
    
    Args:
        query: Search query string
        max_results: Maximum number of results to return
        
    Returns:
        Formatted search results as string
    """
    api_key = os.getenv("TAVILY_API_KEY")
    
    if not api_key:
        # Fallback to old method if no Tavily key
        print("[WEB] No Tavily key, falling back to DuckDuckGo")
        try:
            from duckduckgo_search import DDGS
            results = DDGS().text(query, max_results=max_results)
            
            formatted = f"Search results for: {query}\n\n"
            for i, result in enumerate(results, 1):
                formatted += f"{i}. {result.get('title', 'No title')}\n"
                formatted += f"   {result.get('body', 'No description')}\n"
                formatted += f"   {result.get('href', '')}\n\n"
            
            return formatted
        except Exception as e:
            return f"Search failed: {e}"
    
    try:
        client = TavilyClient(api_key=api_key)
        
        # Tavily search with context optimization for AI
        response = client.search(
            query=query,
            max_results=max_results,
            search_depth="advanced",  # Better for AI agents
            include_answer=True  # Get AI-generated summary
        )
        
        formatted = f"🔍 Search: {query}\n\n"
        
        # Add the AI-generated answer if available
        if response.get("answer"):
            formatted += f"📝 **Summary:** {response['answer']}\n\n"
        
        formatted += "**Sources:**\n\n"
        
        # Add search results
        for i, result in enumerate(response.get("results", []), 1):
            formatted += f"{i}. **{result.get('title', 'No title')}**\n"
            formatted += f"   {result.get('content', 'No description')}\n"
            formatted += f"   🔗 {result.get('url', '')}\n"
            formatted += f"   Score: {result.get('score', 0):.2f}\n\n"
        
        return formatted
        
    except Exception as e:
        return f"Tavily search failed: {e}"

if __name__ == "__main__":
    # Test
    print(web_search("What is WebXR hand tracking?"))

