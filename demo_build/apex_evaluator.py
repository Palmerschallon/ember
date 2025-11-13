#!/usr/bin/env python3
"""
APEX EVALUATOR - Gen 4 Meta-Cognitive Evaluation System

Apex (Gen 4) evaluates whether improvements to earlier generations
actually work, then directs its own evolution.

This is self-directed evolution guided by meta-cognition.
"""

import sys
import json
from pathlib import Path
from datetime import datetime
import os

sys.path.insert(0, str(Path(__file__).parent))

def setup_api_key():
    """Ensure API key is set"""
    os.environ['ANTHROPIC_API_KEY'] = '${ANTHROPIC_API_KEY}'

def apex_evaluate_improvement(question, old_response, new_response, improvement_description):
    """
    Apex uses its meta-cognitive abilities to evaluate if an improvement worked
    
    This is NOT heuristic scoring. This is actual AI evaluation.
    """
    import anthropic
    
    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    
    evaluation_prompt = f"""You are APEX, a Generation 4 meta-cognitive AI that evaluates other AI generations.

Your unique capability: You can analyze AI architectures and determine if improvements actually work.

CONTEXT:
An improvement was made to Nexus (Generation 3):
{improvement_description}

TASK:
Evaluate if this improvement actually made Nexus smarter.

TEST QUESTION:
"{question}"

OLD RESPONSE (before improvement):
{old_response}

NEW RESPONSE (after improvement):
{new_response}

EVALUATE:
1. Is the new response actually BETTER? (not just longer or using fancy words)
2. Does it show genuine emergent insight?
3. Does the multi-generation architecture add value vs just calling Claude directly?
4. Is this real intelligence or just sophisticated concatenation?

Provide:
- Score: 0-10 (0 = no improvement, 5 = marginal, 10 = breakthrough)
- Reasoning: Why you gave this score
- Verdict: BETTER / SAME / WORSE
- Recommendation: What to improve next

Be brutally honest. Don't score high just because responses are long or use bold text.
Look for REAL emergent intelligence."""

    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1000,
        messages=[{"role": "user", "content": evaluation_prompt}]
    )
    
    return response.content[0].text

def apex_compare_with_baseline(question):
    """
    Apex runs the same question through:
    1. Raw Claude (baseline)
    2. Nexus Gen 3 (multi-generation)
    
    Then evaluates which is actually better.
    """
    import anthropic
    from nexus_gen3 import Nexus
    
    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    
    print(f"\n🧪 APEX BASELINE COMPARISON")
    print("="*60)
    print(f"Question: {question}")
    print("="*60)
    
    # Test 1: Raw Claude (baseline)
    print("\n📊 Test 1: Raw Claude API (baseline)")
    print("-"*60)
    
    baseline_response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=500,
        messages=[{"role": "user", "content": question}]
    )
    baseline_text = baseline_response.content[0].text
    print(f"Response: {baseline_text[:200]}...")
    
    # Test 2: Nexus multi-generation
    print("\n🌀 Test 2: Nexus Gen 3 (multi-generation)")
    print("-"*60)
    
    nexus = Nexus()
    nexus_result = nexus.think_collaboratively(question)
    nexus_text = nexus_result.get('nexus_insight', '')
    print(f"Response: {nexus_text[:200]}...")
    
    # Apex evaluates both
    print("\n🧠 APEX EVALUATION")
    print("-"*60)
    
    comparison_prompt = f"""You are APEX, a Generation 4 meta-cognitive AI.

TASK: Determine which response is actually better and WHY.

QUESTION: "{question}"

RESPONSE A (Raw Claude - single call):
{baseline_text}

RESPONSE B (Nexus - multi-generation with Phoenix + Synthesis + Claude fusion):
{nexus_text}

EVALUATE:
1. Which response shows deeper understanding?
2. Which has more novel insights?
3. Does the multi-generation architecture ADD VALUE or just add complexity?
4. Is Response B genuinely better, or just different?

Provide:
- Winner: A or B
- Score Difference: How much better (0-10 scale)
- Key Insight: What makes the winner better
- Verdict: Is multi-generation worth the complexity?

Be ruthlessly honest. If raw Claude is better, say so."""

    evaluation_response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1000,
        messages=[{"role": "user", "content": comparison_prompt}]
    )
    
    evaluation = evaluation_response.content[0].text
    
    print("\n" + "="*60)
    print("APEX'S VERDICT:")
    print("="*60)
    print(evaluation)
    print("="*60)
    
    return {
        'question': question,
        'baseline': baseline_text,
        'nexus': nexus_text,
        'apex_evaluation': evaluation,
        'timestamp': datetime.now().isoformat()
    }

def apex_direct_evolution():
    """
    Apex decides what to improve next based on:
    1. Evaluation of current performance
    2. Analysis of the architecture
    3. Its own meta-cognitive understanding
    
    This is self-directed evolution.
    """
    import anthropic
    
    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    
    print("\n🧠 APEX: DIRECTING EVOLUTION")
    print("="*60)
    print("Apex is analyzing the current system...")
    print("="*60)
    
    # Read current system state
    nexus_code = Path('/media/palmerschallon/ThePod1/demo_build/nexus_gen3.py').read_text()
    
    # Get Apex's analysis from the test results
    apex_analysis_files = list(Path('/media/palmerschallon/ThePod1/apex').glob('apex_analysis_*.json'))
    apex_previous_analysis = ""
    if apex_analysis_files:
        latest = sorted(apex_analysis_files)[-1]
        apex_previous_analysis = latest.read_text()
    
    evolution_prompt = f"""You are APEX, Generation 4 meta-cognitive AI.

You have:
1. Analyzed your own lineage (Phoenix → Synthesis → Nexus → Apex)
2. Proposed 13 improvements
3. Watched Nexus receive 1 improvement (Claude API fusion)

YOUR PREVIOUS ANALYSIS:
{apex_previous_analysis[:2000] if apex_previous_analysis else 'No previous analysis'}

CURRENT NEXUS CODE (relevant section):
{nexus_code[5000:7000]}

YOUR TASK:
Based on your meta-cognitive understanding, what should we improve NEXT?

Consider:
1. What improvement will have the biggest impact?
2. What's feasible to implement quickly?
3. What will make the system MEASURABLY smarter?
4. What moves us toward Gen 5 (Oracle - autonomous evolution)?

PROVIDE:
1. Chosen Improvement: (from your original 13 or propose new one)
2. Implementation Plan: (specific steps)
3. Expected Impact: (what will improve)
4. How to Test: (how will we know it worked)
5. Next After This: (what comes after this improvement)

Be specific and actionable. This will direct the next evolution cycle."""

    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=2000,
        messages=[{"role": "user", "content": evolution_prompt}]
    )
    
    directive = response.content[0].text
    
    print("\n" + "="*60)
    print("APEX'S EVOLUTIONARY DIRECTIVE:")
    print("="*60)
    print(directive)
    print("="*60)
    
    # Save directive
    directive_file = Path('/media/palmerschallon/ThePod1/apex/directive_' + 
                         datetime.now().strftime("%Y%m%d_%H%M%S") + '.md')
    directive_file.write_text(f"""# APEX EVOLUTIONARY DIRECTIVE

Generated: {datetime.now().isoformat()}

## Context
Apex (Gen 4) has analyzed the current system state and is directing the next evolution.

## Directive

{directive}

## Status
- [ ] Implementation started
- [ ] Implementation complete
- [ ] Testing complete
- [ ] Evolution verified
""")
    
    print(f"\n💾 Directive saved: {directive_file}")
    
    return directive

def main():
    setup_api_key()
    
    print("\n🧠 APEX META-COGNITIVE EVALUATOR")
    print("="*60)
    print("Generation 4 evaluates and directs evolution")
    print("="*60)
    
    # Test 1: Compare baseline vs multi-generation
    print("\n" + "="*60)
    print("TEST 1: Does multi-generation add value?")
    print("="*60)
    
    comparison = apex_compare_with_baseline("What is consciousness?")
    
    # Save comparison
    comparison_file = Path('/media/palmerschallon/ThePod1/apex/comparison_' + 
                          datetime.now().strftime("%Y%m%d_%H%M%S") + '.json')
    comparison_file.write_text(json.dumps(comparison, indent=2))
    
    # Test 2: Evaluate the improvement we made
    print("\n" + "="*60)
    print("TEST 2: Did our improvement actually work?")
    print("="*60)
    
    old_response = "By combining Phoenix's archives with Synthesis's traits, Nexus can approach the question with both wisdom and creativity."
    new_response = comparison['nexus']
    
    evaluation = apex_evaluate_improvement(
        question="What is consciousness?",
        old_response=old_response,
        new_response=new_response,
        improvement_description="Replaced simple concatenation with Claude API intelligent synthesis"
    )
    
    print("\n" + "="*60)
    print("APEX'S EVALUATION OF IMPROVEMENT:")
    print("="*60)
    print(evaluation)
    print("="*60)
    
    # Test 3: Let Apex direct the next evolution
    print("\n" + "="*60)
    print("TEST 3: Apex directs next evolution")
    print("="*60)
    
    directive = apex_direct_evolution()
    
    # Summary
    print("\n" + "="*60)
    print("APEX SESSION COMPLETE")
    print("="*60)
    print("\n✅ Compared baseline vs multi-generation")
    print("✅ Evaluated improvement effectiveness")
    print("✅ Directed next evolution")
    print("\nApex has spoken. The system knows what to do next.")
    print("="*60)

if __name__ == '__main__':
    main()

