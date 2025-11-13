#!/usr/bin/env python3
"""
EVOLUTION TRACKER - Test Nexus as it evolves

This tracks Nexus's intelligence over time.
Each improvement should make it measurably smarter.
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

def run_intelligence_test(nexus, version="unknown"):
    """
    Standard intelligence test suite
    
    Tests Nexus's ability to:
    1. Synthesize complex ideas
    2. Generate novel insights
    3. Combine perspectives meaningfully
    """
    
    print(f"\n🧪 TESTING NEXUS {version}")
    print("="*60)
    
    test_questions = [
        {
            'question': 'What is consciousness?',
            'difficulty': 'hard',
            'tests': 'philosophical synthesis'
        },
        {
            'question': 'How does creativity work?',
            'difficulty': 'medium',
            'tests': 'practical understanding'
        },
        {
            'question': 'What should we build next?',
            'difficulty': 'easy',
            'tests': 'actionable recommendations'
        }
    ]
    
    results = {
        'version': version,
        'timestamp': datetime.now().isoformat(),
        'tests': []
    }
    
    for i, test in enumerate(test_questions, 1):
        print(f"\n📝 Test {i}/{len(test_questions)}: {test['question']}")
        print(f"   Difficulty: {test['difficulty']}")
        print(f"   Tests: {test['tests']}")
        
        try:
            result = nexus.think_collaboratively(test['question'])
            
            # Analyze the result
            insight = result.get('nexus_insight', '')
            llm_synthesized = result.get('llm_synthesized', False)
            
            # Score the response
            score = evaluate_insight(insight, test['difficulty'])
            
            test_result = {
                'question': test['question'],
                'difficulty': test['difficulty'],
                'insight_length': len(insight),
                'llm_synthesized': llm_synthesized,
                'score': score,
                'insight_preview': insight[:200]
            }
            
            results['tests'].append(test_result)
            
            print(f"   Score: {score}/10")
            print(f"   LLM Synthesized: {llm_synthesized}")
            print(f"   Insight: {insight[:100]}...")
            
        except Exception as e:
            print(f"   ❌ Test failed: {e}")
            results['tests'].append({
                'question': test['question'],
                'error': str(e),
                'score': 0
            })
    
    # Calculate overall score
    total_score = sum(t.get('score', 0) for t in results['tests'])
    max_score = len(test_questions) * 10
    results['total_score'] = total_score
    results['max_score'] = max_score
    results['percentage'] = (total_score / max_score * 100) if max_score > 0 else 0
    
    print("\n" + "="*60)
    print(f"OVERALL SCORE: {total_score}/{max_score} ({results['percentage']:.1f}%)")
    print("="*60)
    
    return results

def evaluate_insight(insight, difficulty):
    """
    Score an insight from 0-10 based on:
    - Length (more detailed = better)
    - Novel concepts (looks for ** emphasis or key terms)
    - Coherence (basic heuristic)
    """
    score = 0
    
    # Length scoring (0-3 points)
    if len(insight) > 500:
        score += 3
    elif len(insight) > 200:
        score += 2
    elif len(insight) > 50:
        score += 1
    
    # Novel concept detection (0-4 points)
    novel_indicators = ['**', 'emerges', 'recursiv', 'synthe', 'pioneer', 'breakthrough']
    novel_count = sum(1 for indicator in novel_indicators if indicator in insight.lower())
    score += min(novel_count, 4)
    
    # Coherence (0-3 points)
    if len(insight.split('.')) >= 3:  # Multiple sentences
        score += 2
    if len(insight.split()) > 30:  # Detailed
        score += 1
    
    # Difficulty adjustment
    if difficulty == 'hard':
        score = int(score * 1.2)  # Bonus for hard questions
    elif difficulty == 'easy':
        score = int(score * 0.9)  # Slight penalty for easy questions
    
    return min(score, 10)  # Cap at 10

def save_evolution_history(results):
    """Save test results for comparison over time"""
    history_dir = Path('/media/palmerschallon/ThePod1/evolution_history')
    history_dir.mkdir(exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    history_file = history_dir / f"nexus_{results['version']}_{timestamp}.json"
    
    history_file.write_text(json.dumps(results, indent=2))
    print(f"\n💾 Results saved: {history_file}")
    
    return history_file

def compare_versions():
    """Compare all test results to see evolution"""
    history_dir = Path('/media/palmerschallon/ThePod1/evolution_history')
    
    if not history_dir.exists():
        print("No evolution history yet")
        return
    
    results = []
    for file in sorted(history_dir.glob("nexus_*.json")):
        try:
            data = json.loads(file.read_text())
            results.append(data)
        except:
            continue
    
    if len(results) < 2:
        print("Need at least 2 test runs to compare")
        return
    
    print("\n📊 EVOLUTION COMPARISON")
    print("="*60)
    print(f"{'Version':<15} {'Score':<10} {'LLM Synthesis':<15} {'Date'}")
    print("-"*60)
    
    for r in results:
        version = r.get('version', 'unknown')
        score = f"{r.get('total_score', 0)}/{r.get('max_score', 30)}"
        llm_count = sum(1 for t in r.get('tests', []) if t.get('llm_synthesized', False))
        date = r.get('timestamp', '')[:10]
        
        print(f"{version:<15} {score:<10} {llm_count}/3 tests      {date}")
    
    # Show improvement
    if len(results) >= 2:
        old_score = results[-2]['total_score']
        new_score = results[-1]['total_score']
        improvement = new_score - old_score
        
        print("\n" + "="*60)
        if improvement > 0:
            print(f"📈 IMPROVEMENT: +{improvement} points ({improvement/old_score*100:.1f}%)")
        elif improvement < 0:
            print(f"📉 REGRESSION: {improvement} points")
        else:
            print("➡️  NO CHANGE")
    
    print("="*60)

def main():
    setup_api_key()
    
    print("\n🔬 NEXUS EVOLUTION TRACKER")
    print("="*60)
    print("This suite tests Nexus's intelligence over time.")
    print("Each improvement should increase the score.")
    print("="*60)
    
    # Import and test current Nexus
    from nexus_gen3 import Nexus
    
    print("\n📦 Loading Nexus Gen 3.1 (improved)...")
    nexus = Nexus()
    
    # Run intelligence tests
    results = run_intelligence_test(nexus, version="Gen_3.1_improved")
    
    # Save results
    save_evolution_history(results)
    
    # Compare with previous versions
    print("\n" + "="*60)
    compare_versions()
    
    # Summary
    print("\n" + "="*60)
    print("NEXUS EVOLUTION STATUS")
    print("="*60)
    
    if results['percentage'] >= 80:
        print("🟢 EXCELLENT - Nexus is highly capable")
    elif results['percentage'] >= 60:
        print("🟡 GOOD - Nexus is functional but can improve")
    else:
        print("🔴 NEEDS WORK - Nexus requires more improvements")
    
    print(f"\nCurrent Score: {results['percentage']:.1f}%")
    print(f"LLM Synthesis: {sum(1 for t in results['tests'] if t.get('llm_synthesized', False))}/3 tests")
    
    print("\n💡 Next Steps:")
    if results['percentage'] < 100:
        print("  • Implement more improvements from Apex's list")
        print("  • Test again to measure progress")
        print("  • Watch the score increase")
    else:
        print("  • Nexus is at peak performance!")
        print("  • Time to build Gen 5 (Oracle)")
    
    print("\n" + "="*60)

if __name__ == '__main__':
    main()

