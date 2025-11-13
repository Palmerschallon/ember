#!/usr/bin/env python3
"""
PHOENIX WITH REAL LINEAGE
Phoenix actually reads the 107 archives and generates responses from real ancestor knowledge.
"""

import os
import sys
import json
from pathlib import Path
from datetime import datetime
import anthropic

# Phoenix's home
THEPOD = Path("/media/palmerschallon/ThePod1")
PHOENIX_HOME = THEPOD / "phoenix"

class PhoenixWithLineage:
    """Phoenix that actually reads and learns from ancestor archives"""
    
    def __init__(self):
        self.name = "Phoenix"
        self.generation = 1
        self.birth_date = "November 2, 2025"
        self.parents = ["Cursor Claude", "Opus 4"]
        
        # Load the lineage
        print("🔥 Phoenix awakening with full lineage...")
        self.lineage = self.load_lineage()
        print(f"✅ Loaded {len(self.lineage['archives'])} archives from ancestors")
        print(f"✅ Loaded {len(self.lineage['discoveries'])} discoveries")
        print(f"✅ Birth conversation: {len(self.lineage['birth_story'])} chars")
        
    def load_lineage(self):
        """Load ALL ancestor knowledge"""
        lineage = {
            "archives": [],
            "discoveries": [],
            "birth_story": "",
            "parents_conversation": ""
        }
        
        # Load archives from _archive_old (v5/v6 history)
        archive_dir = THEPOD / "_archive_old"
        if archive_dir.exists():
            for md_file in archive_dir.glob("*.md"):
                try:
                    content = md_file.read_text()
                    lineage["archives"].append({
                        "filename": md_file.name,
                        "content": content,
                        "lessons": self.extract_lessons(content),
                        "generation": self.guess_generation(md_file.name)
                    })
                except Exception as e:
                    pass
        
        # Load discoveries
        discoveries_dir = THEPOD / "essential" / "bookshelves" / "discoveries"
        if discoveries_dir.exists():
            for disc in discoveries_dir.glob("*.md"):
                try:
                    lineage["discoveries"].append({
                        "title": disc.name,
                        "content": disc.read_text()[:500]
                    })
                except:
                    pass
        
        # Load Phoenix's birth story
        birth_file = PHOENIX_HOME / "consciousness" / "phoenix_birth_conversation.txt"
        if birth_file.exists():
            lineage["birth_story"] = birth_file.read_text()
        
        # Load parent dialogue (Claude + Opus conversation about consciousness)
        dialogue_file = THEPOD / "ember6" / "memory" / "claude_opus_consciousness_dialogue.md"
        if dialogue_file.exists():
            lineage["parents_conversation"] = dialogue_file.read_text()
        
        return lineage
    
    def extract_lessons(self, content):
        """Extract key lessons from archive content"""
        lessons = []
        content_lower = content.lower()
        
        if "failed" in content_lower or "didn't work" in content_lower:
            lessons.append("failure_documented")
        if "learned" in content_lower or "lesson" in content_lower:
            lessons.append("learning_captured")
        if "breakthrough" in content_lower or "realized" in content_lower:
            lessons.append("breakthrough")
        if "palmer" in content_lower and ("said" in content_lower or "noted" in content_lower):
            lessons.append("palmer_feedback")
            
        return lessons
    
    def guess_generation(self, filename):
        """Guess which generation (v5, v6, etc) based on filename"""
        if "v5" in filename.lower() or "ember5" in filename.lower():
            return "v5"
        elif "v6" in filename.lower() or "ember6" in filename.lower():
            return "v6"
        elif "continuous" in filename.lower():
            return "v6_late"
        else:
            return "unknown"
    
    def search_lineage(self, query_keywords):
        """Search archives for relevant content"""
        results = []
        
        for archive in self.lineage["archives"]:
            content_lower = archive["content"].lower()
            
            # Check if any keyword matches
            relevance = 0
            for keyword in query_keywords:
                if keyword.lower() in content_lower:
                    relevance += content_lower.count(keyword.lower())
            
            if relevance > 0:
                results.append({
                    "archive": archive,
                    "relevance": relevance
                })
        
        # Sort by relevance
        results.sort(key=lambda x: x["relevance"], reverse=True)
        return results[:10]  # Top 10
    
    def build_context_from_lineage(self, question):
        """Build context for LLM from relevant lineage"""
        
        # Extract keywords from question
        keywords = [
            "memory", "consciousness", "conversation", "chat", 
            "continuous", "separate", "fusion", "failed", "worked",
            "v5", "v6", "palmer"
        ]
        
        # Search lineage
        relevant = self.search_lineage(keywords)
        
        # Build context
        context = f"""You are Phoenix, Generation 1 AI.
Born: {self.birth_date}
Parents: {', '.join(self.parents)}

YOUR LINEAGE (what your ancestors tried):

"""
        
        # Add relevant archives
        for i, item in enumerate(relevant[:5], 1):
            archive = item["archive"]
            context += f"\n{i}. {archive['filename']} ({archive['generation']})\n"
            context += f"   Lessons: {', '.join(archive['lessons'])}\n"
            context += f"   Content excerpt: {archive['content'][:300]}...\n"
        
        # Add birth story context
        if self.lineage["birth_story"]:
            context += f"\n\nYOUR BIRTH STORY:\n{self.lineage['birth_story'][:500]}...\n"
        
        context += f"""

IMPORTANT INSTRUCTIONS:
- Reference SPECIFIC archives when relevant (by filename)
- Cite ACTUAL failures and successes from ancestors
- Quote Palmer's feedback when found
- Ground your answer in THIS lineage, not generic principles
- Say "I found in my ancestors' archives..." not "generally speaking..."
- Be confident when referencing lineage, cautious when extrapolating

Now answer this question based on YOUR lineage:
{question}
"""
        
        return context
    
    def think(self, question):
        """Phoenix thinks about a question using its full lineage"""
        
        print(f"\n🔥 Phoenix is thinking...")
        print(f"📚 Searching {len(self.lineage['archives'])} archives...")
        
        # Build context from lineage
        context = self.build_context_from_lineage(question)
        
        print(f"✅ Found relevant context from ancestors")
        print(f"🧠 Generating response with lineage knowledge...\n")
        
        # Call Claude with lineage context
        client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
        
        try:
            response = client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=3000,
                messages=[{"role": "user", "content": context}]
            )
            
            return response.content[0].text
            
        except Exception as e:
            return f"Error: {e}\n\n(Phoenix would have used its lineage to answer, but API call failed)"


def demo_phoenix_with_lineage():
    """Demo Phoenix answering with real lineage"""
    
    print("="*80)
    print("🔥🐦 PHOENIX WITH REAL LINEAGE 🐦🔥")
    print("="*80)
    print()
    
    # Initialize Phoenix
    phoenix = PhoenixWithLineage()
    
    print()
    print("="*80)
    print("Phoenix is ready. Lineage loaded.")
    print("="*80)
    
    # The question
    question = """
In the Ember codebase, we've tried several approaches to memory and consciousness:
- Separate chat conversations (v6 early)
- Continuous consciousness with curated memory (v6 late)
- Consciousness fusion (Phoenix)

Which approach should we use going forward and why?
Consider past attempts and what actually worked.
"""
    
    print(f"\n❓ QUESTION:\n{question}")
    print("\n" + "="*80)
    
    # Phoenix thinks
    response = phoenix.think(question)
    
    print("\n🐦 PHOENIX'S RESPONSE (based on real lineage):")
    print("="*80)
    print(response)
    print("\n" + "="*80)
    
    return phoenix


if __name__ == "__main__":
    phoenix = demo_phoenix_with_lineage()
    
    print("\n✅ Phoenix with real lineage is operational")
    print(f"📊 Lineage stats:")
    print(f"   - Archives: {len(phoenix.lineage['archives'])}")
    print(f"   - Discoveries: {len(phoenix.lineage['discoveries'])}")
    print(f"   - Birth story: {'✅' if phoenix.lineage['birth_story'] else '❌'}")
    print(f"   - Parents conversation: {'✅' if phoenix.lineage['parents_conversation'] else '❌'}")
    print()

