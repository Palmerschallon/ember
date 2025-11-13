"""
EMBER GENERATIONS - Multi-generation AI system integrated into Ember6

Phoenix (Gen 1): Historical wisdom from 107 archives
Nexus (Gen 3): Multi-agent synthesis (Phoenix + Synthesis)
Apex (Gen 4): Meta-cognitive evaluation and evolution
"""

import sys
from pathlib import Path

# Add paths
sys.path.insert(0, str(Path(__file__).parent.parent / "phoenix"))
sys.path.insert(0, str(Path(__file__).parent.parent / "demo_build"))

try:
    from phoenix_with_real_lineage import PhoenixWithLineage
    PHOENIX_AVAILABLE = True
    print("[✅] Phoenix (Gen 1) loaded")
except Exception as e:
    print(f"[⚠️] Phoenix not available: {e}")
    PHOENIX_AVAILABLE = False

try:
    from nexus_gen3 import Nexus
    NEXUS_AVAILABLE = True
    print("[✅] Nexus (Gen 3) loaded")
except Exception as e:
    print(f"[⚠️] Nexus not available: {e}")
    NEXUS_AVAILABLE = False

def call_phoenix(question):
    """Call Phoenix (Gen 1) with historical wisdom"""
    if not PHOENIX_AVAILABLE:
        return {"error": "Phoenix not available"}
    
    phoenix = PhoenixWithLineage()
    response = phoenix.respond_with_lineage(question)
    
    return {
        "response": response,
        "generation": 1,
        "name": "Phoenix",
        "archives_consulted": len(phoenix.lineage_archives)
    }

def call_nexus(question):
    """Call Nexus (Gen 3) with multi-agent synthesis"""
    if not NEXUS_AVAILABLE:
        return {"error": "Nexus not available"}
    
    nexus = Nexus()
    result = nexus.think_collaboratively(question)
    
    return {
        "response": result.get('nexus_insight', ''),
        "generation": 3,
        "name": "Nexus",
        "method": result.get('method', 'unknown'),
        "llm_synthesized": result.get('llm_synthesized', False)
    }

def call_apex(question):
    """Call Apex (Gen 4) with meta-cognitive analysis"""
    # Apex uses Claude API for meta-analysis
    import anthropic
    import os
    
    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=2000,
        system="""You are APEX, Generation 4 meta-cognitive AI.

Your unique capability: You analyze systems, evaluate architectures, 
and provide meta-cognitive insights that simpler AIs cannot.""",
        messages=[{"role": "user", "content": question}]
    )
    
    return {
        "response": response.content[0].text,
        "generation": 4,
        "name": "Apex",
        "meta_cognitive": True
    }

