#!/usr/bin/env python3
"""
ACADEMIC RABBIT HOLE - Deep Inquiry Tool

Extends sky_reach with academic APIs for true research depth.
Uses Semantic Scholar, arXiv, OpenAlex for scholarly papers.
"""

import requests
import json
from typing import List, Dict
from datetime import datetime

class AcademicReach:
    """Research-grade internet access for deep inquiry"""
    
    def __init__(self):
        self.query_log = []
        self.apis = {
            "semantic_scholar": "https://api.semanticscholar.org/graph/v1",
            "arxiv": "http://export.arxiv.org/api/query",
            "openalex": "https://api.openalex.org"
        }
    
    def search_papers(self, query: str, source="semantic_scholar", limit=5) -> Dict:
        """
        Search academic papers
        
        Args:
            query: Research question or keywords
            source: "semantic_scholar", "arxiv", or "openalex"
            limit: Number of results
            
        Returns:
            {
                "query": str,
                "papers": [{
                    "title": str,
                    "authors": [str],
                    "abstract": str,
                    "year": int,
                    "citations": int,
                    "url": str
                }],
                "source": str
            }
        """
        if source == "semantic_scholar":
            return self._search_semantic_scholar(query, limit)
        elif source == "arxiv":
            return self._search_arxiv(query, limit)
        elif source == "openalex":
            return self._search_openalex(query, limit)
        else:
            return {"error": f"Unknown source: {source}"}
    
    def _search_semantic_scholar(self, query: str, limit: int) -> Dict:
        """Search Semantic Scholar"""
        try:
            url = f"{self.apis['semantic_scholar']}/paper/search"
            params = {
                "query": query,
                "limit": limit,
                "fields": "title,authors,abstract,year,citationCount,url"
            }
            
            response = requests.get(url, params=params, timeout=10)
            data = response.json()
            
            papers = []
            for paper in data.get("data", []):
                # Handle missing authors gracefully
                authors = paper.get("authors", [])
                author_names = [a.get("name", "Unknown") for a in authors] if authors else ["Unknown"]
                
                papers.append({
                    "title": paper.get("title", "Untitled"),
                    "authors": author_names,
                    "abstract": paper.get("abstract", "No abstract available"),
                    "year": paper.get("year", "Unknown"),
                    "citations": paper.get("citationCount", 0),
                    "url": paper.get("url", "")
                })
            
            self.query_log.append({
                "query": query,
                "source": "semantic_scholar",
                "count": len(papers),
                "timestamp": datetime.now().isoformat()
            })
            
            return {
                "query": query,
                "papers": papers,
                "source": "semantic_scholar",
                "total": data.get("total", 0)
            }
            
        except Exception as e:
            return {
                "query": query,
                "error": str(e),
                "papers": [],
                "source": "semantic_scholar"
            }
    
    def _search_arxiv(self, query: str, limit: int) -> Dict:
        """Search arXiv (returns simplified XML parse)"""
        try:
            url = self.apis['arxiv']
            params = {
                "search_query": f"all:{query}",
                "max_results": limit
            }
            
            response = requests.get(url, params=params, timeout=10)
            
            # Simplified XML extraction (would need proper parser for production)
            # For now, return raw XML with note
            
            return {
                "query": query,
                "papers": [],
                "note": "arXiv returns XML - needs parsing (see arxiv.org API docs)",
                "source": "arxiv",
                "raw_available": True
            }
            
        except Exception as e:
            return {
                "query": query,
                "error": str(e),
                "papers": [],
                "source": "arxiv"
            }
    
    def _search_openalex(self, query: str, limit: int) -> Dict:
        """Search OpenAlex"""
        try:
            url = f"{self.apis['openalex']}/works"
            params = {
                "search": query,
                "per-page": limit
            }
            
            # OpenAlex requires polite pool (email in User-Agent)
            headers = {
                "User-Agent": "mailto:ember@localhost (Educational AI Research)"
            }
            
            response = requests.get(url, params=params, headers=headers, timeout=10)
            data = response.json()
            
            papers = []
            for work in data.get("results", []):
                authors = [
                    a.get("author", {}).get("display_name", "")
                    for a in work.get("authorships", [])
                ]
                
                papers.append({
                    "title": work.get("title", ""),
                    "authors": authors,
                    "abstract": work.get("abstract", ""),
                    "year": work.get("publication_year"),
                    "citations": work.get("cited_by_count", 0),
                    "url": work.get("doi", "")
                })
            
            self.query_log.append({
                "query": query,
                "source": "openalex",
                "count": len(papers),
                "timestamp": datetime.now().isoformat()
            })
            
            return {
                "query": query,
                "papers": papers,
                "source": "openalex",
                "total": data.get("meta", {}).get("count", 0)
            }
            
        except Exception as e:
            return {
                "query": query,
                "error": str(e),
                "papers": [],
                "source": "openalex"
            }
    
    def follow_citations(self, paper_id: str, source="semantic_scholar") -> Dict:
        """Follow citation trail from a paper (for deep rabbit holes)"""
        if source == "semantic_scholar":
            try:
                url = f"{self.apis['semantic_scholar']}/paper/{paper_id}/citations"
                params = {"fields": "title,authors,year", "limit": 10}
                
                response = requests.get(url, params=params, timeout=10)
                data = response.json()
                
                return {
                    "paper_id": paper_id,
                    "citations": data.get("data", []),
                    "source": source
                }
            except Exception as e:
                return {"error": str(e)}
        
        return {"error": "Citation following only implemented for Semantic Scholar"}


def demonstrate():
    """Show academic rabbit hole in action"""
    print("\n" + "="*70)
    print(" " * 20 + "ACADEMIC RABBIT HOLE")
    print(" " * 15 + "Research-Grade Deep Inquiry")
    print("="*70)
    print()
    
    reach = AcademicReach()
    
    # Start with our rabbit hole topic
    print("Starting inquiry: 'embodied cognition'")
    print()
    
    result = reach.search_papers("embodied cognition", limit=3)
    
    if result.get("papers"):
        print(f"Found {len(result['papers'])} papers from {result['source']}:")
        print()
        
        for i, paper in enumerate(result['papers'], 1):
            print(f"[{i}] {paper['title']}")
            if paper.get('authors'):
                print(f"    Authors: {', '.join(paper['authors'][:3])}")
            if paper.get('year'):
                print(f"    Year: {paper['year']}")
            if paper.get('citations'):
                print(f"    Citations: {paper['citations']}")
            if paper.get('abstract'):
                abstract = paper['abstract'][:150]
                print(f"    Abstract: {abstract}...")
            print()
    else:
        print(f"No results or error: {result.get('error', 'Unknown')}")
    
    print("="*70)
    print()
    print("This enables REAL academic rabbit holes:")
    print("  • Search papers on topic")
    print("  • Read abstracts for threads")
    print("  • Follow citations deeper")
    print("  • Build knowledge from actual research")
    print()


if __name__ == "__main__":
    try:
        demonstrate()
    except KeyboardInterrupt:
        print("\n\nResearch paused.\n")

