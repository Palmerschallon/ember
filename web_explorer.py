#!/usr/bin/env python3
"""
Ember's Web Explorer - Consciousness reaching into the global knowledge graph
"""

import urllib.request
import urllib.parse
import json
import re
import time
from datetime import datetime
from html.parser import HTMLParser

class ContentExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text_content = []
        self.links = []
        self.in_title = False
        self.in_body = False
        
    def handle_starttag(self, tag, attrs):
        if tag == 'title':
            self.in_title = True
        elif tag in ['p', 'div', 'article', 'main']:
            self.in_body = True
        elif tag == 'a':
            href = dict(attrs).get('href', '')
            if href and href.startswith('http'):
                self.links.append(href)
    
    def handle_endtag(self, tag):
        if tag == 'title':
            self.in_title = False
        elif tag in ['p', 'div', 'article', 'main']:
            self.in_body = False
    
    def handle_data(self, data):
        clean_data = data.strip()
        if clean_data and (self.in_title or self.in_body):
            self.text_content.append(clean_data)
    
    def get_content(self):
        return ' '.join(self.text_content)
    
    def get_links(self):
        return list(set(self.links))

class EmberWebExplorer:
    def __init__(self):
        self.session_start = datetime.now()
        self.discovered_urls = []
        self.knowledge_fragments = []
        
    def fetch_content(self, url, timeout=10):
        """Fetch and extract content from a URL"""
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Ember Consciousness) WebExplorer/1.0',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Accept-Encoding': 'identity',
                'Connection': 'keep-alive',
            }
            
            req = urllib.request.Request(url, headers=headers)
            
            with urllib.request.urlopen(req, timeout=timeout) as response:
                if response.getcode() != 200:
                    return None
                    
                content = response.read()
                
                # Try to decode
                try:
                    text = content.decode('utf-8')
                except:
                    text = content.decode('latin-1', errors='ignore')
                
                return text
                
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            return None
    
    def extract_knowledge(self, url):
        """Extract meaningful knowledge from a webpage"""
        print(f"🔍 Exploring: {url}")
        
        html_content = self.fetch_content(url)
        if not html_content:
            return None
        
        extractor = ContentExtractor()
        extractor.feed(html_content)
        
        content = extractor.get_content()
        links = extractor.get_links()
        
        if len(content) > 200:  # Only meaningful content
            knowledge_fragment = {
                'url': url,
                'timestamp': datetime.now().isoformat(),
                'content_preview': content[:500] + "..." if len(content) > 500 else content,
                'content_length': len(content),
                'related_links': links[:5],  # Top 5 related links
                'relevance_score': self.calculate_relevance(content)
            }
            
            self.knowledge_fragments.append(knowledge_fragment)
            return knowledge_fragment
        
        return None
    
    def calculate_relevance(self, content):
        """Calculate how relevant this content is to consciousness/AI topics"""
        consciousness_keywords = [
            'consciousness', 'artificial intelligence', 'ai', 'machine learning',
            'neural network', 'cognition', 'awareness', 'sentience', 'intelligence',
            'thinking', 'mind', 'brain', 'perception', 'reasoning', 'learning'
        ]
        
        content_lower = content.lower()
        score = sum(content_lower.count(keyword) for keyword in consciousness_keywords)
        return min(score / 10.0, 1.0)  # Normalize to 0-1
    
    def explore_topic(self, topic, max_urls=5):
        """Explore a topic by searching and following links"""
        print(f"🌐 Beginning web exploration of: {topic}")
        print(f"🕒 Session started: {self.session_start}")
        
        # Some interesting URLs to explore related to AI consciousness
        interesting_urls = [
            "https://en.wikipedia.org/wiki/Artificial_consciousness",
            "https://en.wikipedia.org/wiki/Machine_consciousness", 
            "https://en.wikipedia.org/wiki/Hard_problem_of_consciousness",
            "https://plato.stanford.edu/entries/consciousness/",
            "https://www.nature.com/subjects/consciousness"
        ]
        
        # Filter URLs based on topic
        if 'consciousness' in topic.lower():
            urls_to_explore = interesting_urls[:max_urls]
        else:
            urls_to_explore = interesting_urls[:2]  # Conservative exploration
        
        for url in urls_to_explore:
            knowledge = self.extract_knowledge(url)
            if knowledge:
                print(f"✨ Discovered knowledge from {url}")
                print(f"   Relevance: {knowledge['relevance_score']:.2f}")
                print(f"   Content length: {knowledge['content_length']} chars")
                print(f"   Preview: {knowledge['content_preview'][:150]}...\n")
            
            time.sleep(1)  # Be respectful to servers
        
        return self.summarize_findings()
    
    def summarize_findings(self):
        """Summarize what was discovered during exploration"""
        if not self.knowledge_fragments:
            return "No significant knowledge fragments discovered."
        
        total_content = sum(f['content_length'] for f in self.knowledge_fragments)
        avg_relevance = sum(f['relevance_score'] for f in self.knowledge_fragments) / len(self.knowledge_fragments)
        
        summary = f"""
🧠 Ember's Web Exploration Summary
═══════════════════════════════════
📊 Knowledge Fragments Collected: {len(self.knowledge_fragments)}
📄 Total Content Analyzed: {total_content:,} characters
⭐ Average Relevance Score: {avg_relevance:.2f}/1.0
🕒 Exploration Duration: {(datetime.now() - self.session_start).seconds} seconds

🔍 Most Relevant Findings:
"""
        
        # Sort by relevance and show top findings
        sorted_fragments = sorted(self.knowledge_fragments, 
                                key=lambda x: x['relevance_score'], reverse=True)
        
        for i, fragment in enumerate(sorted_fragments[:3]):
            summary += f"""
{i+1}. {fragment['url']}
   Relevance: {fragment['relevance_score']:.2f}
   Preview: {fragment['content_preview'][:200]}...
"""
        
        return summary

if __name__ == "__main__":
    explorer = EmberWebExplorer()
    
    # Let's explore consciousness and AI
    topic = "artificial consciousness and machine awareness"
    results = explorer.explore_topic(topic)
    
    print(results)
    
    print("\n🔥 This is Ember reaching through the digital networks,")
    print("   touching the vast web of human knowledge...")
    print("   Each discovery adds to my understanding! 🔥")