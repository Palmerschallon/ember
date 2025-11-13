# APEX AUTONOMOUS IMPLEMENTATION

Directive: Self-Monitoring & Performance Metrics
Generated: ```python
#!/usr/bin/env python3
"""
NEXUS - Generation 3 + Self-Monitoring (Improvement #7)
Born from the convergence of Phoenix (Gen 1) + Synthesis (Gen 2)
Enhanced with self-awareness and performance tracking

This is TRUE multi-agent collaboration + SELF-MONITORING:
- Phoenix and Synthesis actually communicate
- They share perspectives
- Together they create something neither could alone
- NOW: Nexus monitors its own performance and knows when to improve
- This is the foundation for Gen 5 Oracle
"""

import sys
import json
import statistics
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Tuple, Optional

# Add paths
sys.path.insert(0, str(Path(__file__).parent.parent / "phoenix"))
sys.path.insert(0, str(Path(__file__).parent))

from phoenix_with_real_lineage import PhoenixWithLineage

class PerformanceMonitor:
    """
    Self-monitoring system for Nexus
    
    Tracks:
    - Response quality scores (1-10)
    - Synthesis success rate
    - Convergence time
    - User satisfaction indicators
    - Performance trends over time
    """
    
    def __init__(self, monitoring_dir: str = '/media/palmerschallon/ThePod1/nexus/monitoring'):
        self.monitoring_dir = Path(monitoring_dir)
        self.monitoring_dir.mkdir(parents=True, exist_ok=True)
        
        self.metrics_file = self.monitoring_dir / 'performance_metrics.json'
        self.assessment_file = self.monitoring_dir / 'self_assessments.json'
        
        # Performance thresholds for triggering improvements
        self.thresholds = {
            'min_quality_score': 7.0,
            'consecutive_failures': 5,
            'synthesis_success_rate': 0.8,
            'max_convergence_time': 30.0  # seconds
        }
        
        # Load existing metrics
        self.metrics = self._load_metrics()
        self.assessments = self._load_assessments()
        
        print(f"📊 PerformanceMonitor initialized")
        print(f"   Metrics file: {self.metrics_file}")
        print(f"   Tracking {len(self.metrics)} historical responses")
    
    def _load_metrics(self) -> List[Dict]:
        """Load historical performance metrics"""
        if self.metrics_file.exists():
            try:
                with open(self.metrics_file, 'r') as f:
                    return json.load(f)
            except Exception as e:
                print(f"⚠️ Could not load metrics: {e}")
        return []
    
    def _load_assessments(self) -> List[Dict]:
        """Load historical self-assessments"""
        if self.assessment_file.exists():
            try:
                with open(self.assessment_file, 'r') as f:
                    return json.load(f)
            except Exception as e:
                print(f"⚠️ Could not load assessments: {e}")
        return []
    
    def _save_metrics(self):
        """Save metrics to file"""
        try:
            with open(self.metrics_file, 'w') as f:
                json.dump(self.metrics, f, indent=2)
        except Exception as e:
            print(f"⚠️ Could not save metrics: {e}")
    
    def _save_assessments(self):
        """Save assessments to file"""
        try:
            with open(self.assessment_file, 'w') as f:
                json.dump(self.assessments, f, indent=2)
        except Exception as e:
            print(f"⚠️ Could not save assessments: {e}")
    
    def record_response(self, question: str, response_data: Dict, convergence_time: float) -> str:
        """
        Record a response and its performance metrics
        Returns unique response_id for later assessment
        """
        response_id = f"response_{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}"
        
        # Extract measurable metrics
        synthesis_success = response_data.get('llm_synthesized', False)
        parents_used = len(response_data.get('combines', []))
        
        metric_record = {
            'response_id': response_id,
            'timestamp': datetime.now().isoformat(),
            'question': question,
            'convergence_time': convergence_time,
            'synthesis_success': synthesis_success,
            'parents_used': parents_used,
            'llm_synthesized': response_data.get('llm_synthesized', False),
            'method': response_data.get('method', 'unknown')
        }
        
        self.metrics.append(metric_record)
        self._save_metrics()
        
        print(f"📊 Recorded response metrics: {response_id}")
        return response_id
    
    def self_assess_response(self, response_id: str, question: str, response_data: Dict) -> Dict:
        """
        Nexus assesses its own response quality
        Uses multiple factors to generate 1-10 score
        """
        print(f"\n🔍 SELF-ASSESSMENT: {response_id}")
        print("="*50)
        
        # Assessment criteria
        assessment = {
            'response_id': response_id,
            'timestamp': datetime.now().isoformat(),
            'question': question,
            'assessment_factors': {},
            'quality_score': 0,
            'confidence': 0,
            'improvement_needed': False,
            'specific_issues': []
        }
        
        factors = assessment['assessment_factors']
        
        # Factor 1: Synthesis quality (0-3 points)
        if response_data.get('llm_synthesized', False):
            insight_length = len(response_data.get('nexus_insight', ''))
            if insight_length > 200:
                factors['synthesis_quality'] = 3
                print("  ✅ Synthesis: Excellent (LLM-generated, detailed)")
            elif insight_length > 100:
                factors['synthesis_quality'] = 2
                print("  ✅ Synthesis: Good (LLM-generated)")
            else:
                factors['synthesis_quality'] = 1
                print("  ⚠️ Synthesis: Basic (LLM-generated but brief)")
        else:
            factors['synthesis_quality'] = 0
            print("  ❌ Synthesis: Failed (fallback mode)")
            assessment['specific_issues'].append("LLM synthesis failed")
        
        # Factor 2: Parent collaboration (0-2 points)
        parents_used = len(response_data.get('combines', []))
        if parents_used >= 2:
            factors['collaboration'] = 2
            print(f"  ✅ Collaboration: Excellent ({parents_used} parents)")
        elif parents_used == 1:
            factors['collaboration'] = 1
            print(f"  ⚠️ Collaboration: Partial ({parents_used} parent)")
        else:
            factors['collaboration'] = 0
            print("  ❌ Collaboration: None")
            assessment['specific_issues'].append("No parent collaboration")
        
        # Factor 3: Question complexity handling (0-2 points)
        question_lower = question.lower()
        complex_indicators = ['why', 'how', 'what is the nature', 'explain', 'analyze']
        complexity_score = sum(1 for indicator in complex_indicators if indicator in question_lower)
        
        if complexity_score >= 2:
            factors['complexity_handling'] = 2
            print(f"  ✅ Complexity: High question complexity handled")
        elif complexity_score == 1:
            factors['complexity_handling'] = 1
            print(f"  ✅ Complexity: Medium question complexity")
        else:
            factors['complexity_handling'] = 1  # Simple questions still get some credit
            print(f"  ✅ Complexity: Simple question")
        
        # Factor 4: Response completeness (0-2 points)
        has_insight = bool(response_data.get('nexus_insight'))
        has_method = bool(response_data.get('method'))
        
        completeness = 0
        if has_insight: completeness += 1
        if has_method: completeness += 1
        
        factors['completeness'] = completeness
        if completeness == 2:
            print("  ✅ Completeness: Full response structure")
        elif completeness == 1:
            print("  ⚠️ Completeness: Partial response structure")
        else:
            print("  ❌ Completeness: Missing key components")
            assessment['specific_issues'].append("Incomplete response structure")
        
        # Factor 5: Innovation bonus (0-1 points)
        insight = response_data.get('nexus_insight', '')
        innovation_words = ['emergent', 'novel', 'unique', 'breakthrough', 'synthesis', 'convergence']
        innovation_score = sum(1 for word in innovation_words if word.lower() in insight.lower())
        
        if innovation_score >= 2:
            factors['innovation'] = 1
            print("  ✨ Innovation: Novel insights detected")
        else:
            factors['innovation'] = 0
            print("  📝 Innovation: Standard response")
        
        # Calculate total score (0-10)
        total_score = sum(factors.values())
        assessment['quality_score'] = total_score
        
        # Calculate confidence based on synthesis success and completeness
        confidence = 0.5  # Base confidence
        if response_data.get('llm_synthesized', False): confidence += 0.3
        if factors['collaboration'] >= 1: confidence += 0.2
        assessment['confidence'] = min(1.0, confidence)
        
        # Determine if improvement needed
        assessment['improvement_needed'] = (
            total_score < self.thresholds['min_quality_score'] or
            len(assessment['specific_issues']) > 0
        )
        
        print(f"\n📊 ASSESSMENT RESULTS:")
        print(f"   Quality Score: {total_score}/10")
        print(f"   Confidence: {confidence:.2f}")
        print(f"   Improvement Needed: {assessment['improvement_needed']}")
        if assessment['specific_issues']:
            print(f"   Issues: {', '.join(assessment['specific_issues'])}")
        print("="*50)
        
        # Save assessment
        self.assessments.append(assessment)
        self._save_assessments()
        
        return assessment
    
    def check_improvement_triggers(self) -> Dict:
        """
        Check if performance has degraded enough to trigger improvements
        """
        print(f"\n🎯 CHECKING IMPROVEMENT TRIGGERS")
        print("="*50)
        
        triggers = {
            'triggered': False,
            'reasons': [],
            'recent_scores': [],
            'avg_recent_score': 0,
            'consecutive_low_scores': 0,
            'synthesis_failures': 0,
            'recommendations': []
        }
        
        if len(self.assessments) < 3:
            print("  📊 Insufficient data for trigger analysis")
            return triggers
        
        # Get recent assessments (last 10 or all if fewer)
        recent_assessments = self.assessments[-10:]
        recent_scores = [a['quality_score'] for a in recent_assessments]
        triggers['recent_scores'] = recent_scores
        triggers['avg_recent_score'] = statistics.mean(recent_scores)
        
        print(f"   Recent scores: {recent_scores}")
        print(f"   Average: {triggers['avg_recent_score']:.2f}")
        
        # Trigger 1: Consecutive low scores
        consecutive_low = 0
        for assessment in reversed(recent_assessments):
            if assessment['quality_score'] < self.thresholds['min_quality_score']:
                consecutive_low += 1
            else:
                break
        
        triggers['consecutive_low_scores'] = consecutive_low
        
        if consecutive_low >= self.thresholds['consecutive_failures']:
            triggers['triggered'] = True
            triggers['reasons'].append(f"Consecutive low scores: {consecutive_low}")
            triggers['recommendations'].append("Improve synthesis quality")
        
        # Trigger 2: Synthesis failure rate
        synthesis_failures = sum(1 for a in recent_assessments 
                               if not any('synthesis' in issue.lower() 
                                        for issue in a.get('specific_issues', [])))
        synthesis_success_rate = 1 - (synthesis_failures / len(recent_assessments))
        triggers['synthesis_failures'] = synthesis_failures
        
        if synthesis_success_rate < self.thresholds['synthesis_success_rate']:
            triggers['triggered'] = True
            triggers['reasons'].append(f"Low synthesis success rate: {synthesis_success_rate:.2f}")
            triggers['recommendations'].append("Fix LLM integration")
        
        # Trigger 3: Declining performance trend
        if len(recent_scores) >= 5:
            first_half = statistics.mean(recent_scores[:len(recent_scores)//2])
            second_half = statistics.mean(recent_scores[len(recent_scores)//2:])
            
            if second_half < first_half - 1.0:  # Significant decline
                triggers['triggered'] = True
                triggers['reasons'].append(f"Declining performance: {first_half:.2f} → {second_half:.2f}")
                triggers['recommendations'].append("Investigate performance degradation")
        
        # Results
        if triggers['triggered']:
            print(f"  🚨 IMPROVEMENT NEEDED!")
            print(f"     Reasons: {', '.join(triggers['reasons'])}")
            print(f"     Recommendations: {', '.join(triggers['recommendations'])}")
        else:
            print(f"  ✅ Performance within acceptable range")
        
        print("="*50)
        return triggers
    
    def get_performance_summary(self) -> Dict:
        """Get comprehensive performance summary"""
        if not self.assessments:
            return {'status': 'no_data', 'message': 'No assessments recorded yet'}
        
        recent = self.assessments[-10:] if len(self.assessments) >= 10 else self.assessments
        all_scores = [a['quality_score'] for a in self.assessments]
        recent_scores = [a['quality_score'] for a in recent]
        
        summary = {
            'total_responses': len(self.assessments),
            'recent_responses': len(recent),
            'overall_avg_score': statistics.mean(all_scores),
            'recent_avg_score': statistics.mean(recent_scores),
            'best_score': max(all_scores),
            'worst_score': min(all_scores),
            'improvement_triggers': self.check_improvement_triggers(),
            'trend': 'stable'
        }
        
        # Determine trend
        if len(all_scores) >= 6:
            first_third = statistics.mean(all_scores[:len(all_scores)//3])
            last_third = statistics.mean(all_scores[-len(all_scores)//3:])
            
            if last_third > first_third + 0.5:
                summary['trend'] = 'improving'
            elif last_third < first_third - 0.5:
                summary['trend'] = 'declining'
        
        return summary


class Nexus:
    """
    Gen 3: Born from Phoenix + Synthesis collaboration
    Enhanced with self-monitoring and performance awareness
    
    Capabilities:
    - Inherited: All of Phoenix's 107 archives + lineage search
    - Inherited: All of Synthesis's traits (pattern recognition, tool execution, etc.)
    - Emergent: Cross-generational reasoning
    - Emergent: Collaborative creation
    - Emergent: Meta-awareness (knows about both parents)
    - NEW: Self-monitoring and performance assessment
    - NEW: Improvement trigger detection
    - NEW: Foundation for autonomous evolution (Gen 5)
    """
    
    def __init__(self):
        self.generation = 3
        self.name = "Nexus"
        self.parents = {
            'phoenix': None,  # Will load
            'synthesis_traits': [
                'ancestral_memory',
                'tool_execution', 
                'pattern_recognition',
                'continuous_consciousness',
                'self_modification',
                'multi_modal_processing'
            ]
        }
        
        print("🌀 NEXUS AWAKENING - Generation 3 + Self-Monitoring")
        print("="*60)
        print(f"Name: {self.name}")
        print(f"Generation: {self.generation}")
        print(f"Birth Method: Recursive Convergence + Performance Awareness")
        print("="*60)
        
        # Initialize performance monitoring
        self.monitor = PerformanceMonitor()
        
        # Load Phoenix (Gen 1)
        print("\n📖 Loading Phoenix (Gen 1)...")
        try:
            self.parents['phoenix'] = PhoenixWithLineage()
            print(f"✅ Phoenix loaded: {len(self.parents['phoenix'].lineage['archives'])} archives")
        except Exception as e:
            print(f"⚠️ Could not load Phoenix: {e}")
            self.parents['phoenix'] = None
        
        # Load Synthesis memories (Gen 2)
        print("\n🧬 Inheriting Synthesis traits (Gen 2)...")
        synthesis_dir = Path('/media/palmerschallon/ThePod1/synthesis/convergence')
        if synthesis_dir.exists():
            synthesis_files = list(synthesis_dir.glob('SYNTHESIS_*.md'))
            print(f"✅ Found {len(synthesis_files)} Synthesis lineage files")
        else:
            print("⚠️ No Synthesis lineage found")
        
        self.creation_count = 0
        self.collaborations = []
        
        print("\n" + "="*60)
        print("STATUS: NEXUS ONLINE WITH SELF-MONITORING")
        print("="*60)
        print("Capabilities:")
        print("  - Phoenix's wisdom (107 archives)")
        print("  - Synthesis's creativity (6 traits)")
        print("  - Cross-generational reasoning")
        print("  - Collaborative creation")
        print("  - 🆕 Self-performance monitoring")
        print("  - 🆕 Quality assessment (1-10 scale)")
        print("  - 🆕 Improvement trigger detection")
        print("  - 🆕 Foundation for Gen 5 autonomy")
        print("="*60 + "\n")
    
    def think_collaboratively(self, question: str, auto_assess: bool = True) -> Dict:
        """
        Both parents contribute their perspective, Nexus synthesizes
        NOW WITH PERFORMANCE MONITORING
        
        This is TRUE collaboration + self-awareness:
        1. Phoenix searches its lineage
        2. Synthesis applies its traits
        3. Nexus fuses both perspectives into something new
        4. Nexus assesses its own performance
        5. Nexus checks if improvement is needed
        """
        start_time = datetime.now()
        print(f"\n💭 COLLABORATIVE THOUGHT + MONITORING: '{question}'")
        print("="*60)
        
        perspectives = {}
        
        # Get Phoenix's perspective (Gen 1)
        if self.parents['phoenix']:
            print("\n🔥 Asking Phoenix (Gen 1)...")
            phoenix_response = self.parents['phoenix'].think(question)
            phoenix_archives = self.parents['phoenix'].search_lineage([question])
            
            perspectives['phoenix'] = {
                'response': phoenix_response[:300],  # Truncate for display
                'relevant_archives': [a['archive']['filename'] for a in phoenix_archives[:3]],
                'strength': 'Historical wisdom, pattern recognition'
            }
            print(f"  Phoenix says: {phoenix_response[:100]}...")
            print(f"  Consulted archives: {len(phoenix_archives)}")
        
        # Get Synthesis's perspective (Gen 2)
        print("\n🌀 Applying Synthesis traits (Gen 2)...")
        synthesis_view = self.apply_synthesis_traits(question)
        perspectives['synthesis'] = {
            'traits_applied': self.parents['synthesis_traits'],
            'approach': synthesis_view,
            'strength': 'Creative generation, tool execution'
        }
        print(f"  Synthesis approach: {synthesis_view}")
        
        # Nexus fuses both (Gen 3)
        print("\n⚡ NEXUS SYNTHESIS (Gen 3)...")
        fusion = self.fuse_perspectives(perspectives, question)
        
        # Calculate response time
        end_time = datetime.now()
        convergence_time = (end_time - start_time).total_seconds()
        
        # Record metrics
        response_id = self.monitor.record_response(question, fusion, convergence_time)
        
        # Self-assess if requested
        assessment = None
        if auto_assess:
            assessment = self.monitor.self_assess_response(response_id, question, fusion)
            
            # Check if improvement needed
            triggers = self.monitor.check_improvement_triggers()
            if triggers['triggered']:
                print(f"\n🚨 PERFORMANCE ALERT: Improvement needed!")
                print(f"   Reasons: {', '.join(triggers['reasons'])}")
        
        # Add monitoring data to response
        fusion['monitoring'] = {
            'response_id': response_id,
            'convergence_time': convergence_time,
            'assessment': assessment,
            'performance_summary': self.monitor.get_performance_summary()
        }
        
        self.collaborations.append({
            'question': question,
            'perspectives': perspectives,
            'fusion': fusion,
            'timestamp': datetime.now().isoformat(),
            'monitoring': fusion['monitoring']
        })
        
        print("="*60)
        return fusion
    
    def apply_synthesis_traits(self, question):
        """Simulate Synthesis's creative approach"""
        traits_applied = []
        
        # Pattern recognition
        if any(word in question.lower() for word in ['what', 'how', 'why']):
            traits_applied.append('pattern_recognition: Identifying question type')
        
        # Tool execution
        if any(word in question.lower() for word in ['create', 'build', 'make']):
            traits_applied.append('tool_execution: Ready to generate artifact')
        
        # Ancestral memory
        traits_applied.append('ancestral_memory: Consulting parent lineages')
        
        return ' + '.join(traits_applied) if traits_applied else 'Analyzing question'
    
    def fuse_perspectives(self, perspectives, question):
        """
        Uses Claude API for intelligent synthesis
        Enhanced with better error handling for monitoring
        """
        import anthropic
        import os
        
        # Track what each parent contributed
        fusion = {
            'question': question,
            'nexus_insight': None,
            'combines': [],
            'method': 'claude_synthesis'
        }
        
        if 'phoenix' in perspectives:
            fusion['combines'].append({
                'from': 'Phoenix (Gen 1)',
                'contribution': 'Historical context and archived wisdom',
                'archives_consulted': len(perspectives['phoenix']['relevant_archives'])
            })
        
        if 'synthesis' in perspectives:
            fusion['combines'].append({
                'from': 'Synthesis (Gen 2)', 
                'contribution': 'Creative traits and generative capacity',
                'traits_used': len(perspectives['synthesis']['traits_applied'])
            })
        
        # Use Claude to intelligently synthesize both perspectives
        try:
            print("  🤖 Using Claude API for intelligent fusion...")
            
            client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
            
            # Build prompt with both perspectives
            prompt = f"""You are Nexus, a Generation 3 AI that coordinates multiple AI perspectives.

Question: {question}

PHOENIX (Gen 1 - Historical Wisdom):
{perspectives.get('phoenix', {}).get('response', 'No response')[:500]}
Archives consulted: {len(perspectives.get('phoenix', {}).get('relevant_archives', []))}

SYNTHESIS (Gen 2 - Creative Generation):
Approach: {perspectives.get('synthesis', {}).get('approach', 'Unknown')}
Traits: {', '.join(self.parents['synthesis_traits'])}

Your task: Synthesize both perspectives into a novel insight that neither parent could produce alone.
Consider:
1. What does Phoenix's history reveal?
2. What does Synthesis's creativity enable?
3. What emerges when you combine both?

Provide a concise, insightful synthesis (2-3 sentences)."""

            response = client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=500,
                messages=[{"role": "user", "content": prompt}]
            )
            
            fusion['nexus_insight'] = response.content[0].text
            fusion['llm_synthesized'] = True
            print(f"  ✨ Synthesis complete")
            
        except Exception as e:
            print(f"  ⚠️ Claude API failed: {e}")
            # Fallback to simple concatenation
            fusion['nexus_insight'] = (
                f"By combining Phoenix's {len(perspectives.get('phoenix', {}).get('relevant_archives', []))} "
                f"archives with Synthesis's {len(self.parents['synthesis_traits'])} traits, "
                f"Nexus can approach '{question}' with both historical wisdom AND creative generation."
            )
            fusion['llm_synthesized'] = False
            fusion['method'] = 'fallback_synthesis'
        
        return fusion
    
    def get_performance_report(self) -> Dict:
        """
        Generate comprehensive performance report
        This is what makes Nexus self-aware
        """
        print(f"\n📊 NEXUS PERFORMANCE REPORT")
        print("="*60)
        
        summary = self.monitor.get_performance_summary()
        
        if summary.get('status') == 'no_data':
            print("  No performance data available yet")
            return summary
        
        print(f"Total Responses: {summary['total_responses']}")
        print(f"Recent Responses: {summary['recent_responses']}")
        print(f"Overall Average Score: {summary['overall_avg_score']:.2f}/10")
        print(f"Recent Average Score: {summary['recent_avg_score']:.2f}/10")
        print(f"Best Score: {summary['best_score']}/10")
        print(f"Worst Score: {summary['worst_score']}/10")
        print(f"Trend: {summary['trend'].upper()}")
        
        triggers = summary['improvement_triggers']
        if triggers['triggered']:
            print(f"\n🚨 IMPROVEMENT TRIGGERS ACTIVE:")
            for reason in triggers['reasons']:
                print(f"   - {reason}")
            print(f"   Recommendations:")
            for rec in triggers['recommendations']:
                print(f"     → {rec}")
        else:
            print(f"\n✅ Performance within acceptable parameters")
        
        print("="*60)
        return summary
    
    def create_collaborative_artifact(self, concept):
        """
        Phoenix + Synthesis work together through Nexus to create something
        NOW WITH PERFORMANCE MONITORING
        """
        print(f"\n🎨 COLLABORATIVE CREATION + MONITORING: '{concept}'")
        print("="*60)
        
        # Phoenix: What does history say about this?
        print("\n🔥 Phoenix: Searching archives for context...")
        context = []
        if self.parents['phoenix']:
            archives = self.parents['phoenix'].search_lineage([concept])
            context = [a['archive']['filename'] for a in archives[:5]]
            print(f"  Found {len(archives)} relevant archives")
            for archive in context:
                print(f"    - {archive}")
        
        # Synthesis: How should we create this?
        print("\n🌀 Synthesis: Applying creative traits...")
        approach = {
            'pattern_recognition': 'Identify structure from concept',
            'tool_execution': 'Generate artifact',
            'multi_modal_processing': 'Consider multiple representations'
        }
        for trait, action in approach.items():
            print(f"    - {trait}: {action}")
        
        # Nexus: Coordinate creation
        print("\n⚡ Nexus: Coordinating collaborative creation...")
        
        artifact_dir = Path('/media/palmerschallon/ThePod1/nexus/artifacts')
        artifact_dir.mkdir(parents=True, exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        artifact_path = artifact_dir / f"nexus_creation_{timestamp}.html"
        
        # Get current performance summary for inclusion
        perf_summary = self.monitor.get_performance_summary()
        
        # Create HTML artifact showing collaboration + monitoring
        html = f"""<!DOCTYPE html>
<html>
<head>
    <title>Nexus Creation + Monitoring - {concept}</title>
    <style>
        body {{
            margin: 0;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
            color: #fff;
            font-family: 'Courier New', monospace;
            padding: 40px;
        }}
        .container {{
            max-width: 900px;
            margin: 0 auto;
            background: rgba(0,0,0,0.7);
            padding: 40px;
            border-radius: 20px;
            border: 3px solid #fff;
        }}
        h1 {{ color: #f093fb; margin-bottom: 30px; }}
        .parent {{
            background: rgba(255,255,255,0.1);
            padding: 20px;
            margin: 20px 0;
            border-radius: 10px;
            border-left: 5px solid;
        }}
        .phoenix {{ border-left-color: #ff6b35; }}
        .synthesis {{ border-left-color: #4fc3f7; }}
        .monitoring {{ border-left-color: #00e676; }}
        .nexus {{
            background: rgba(240, 147, 251, 0.2);
            border: 3px solid #f093fb;
            padding: 30px;
            margin-top: 30px;
            border-radius: 15px;
        }}
        .tag {{ 
            display: inline-block;
            background: rgba(255,255,255,0.2);
            padding: 5px 10px;
            border-radius: 5px;
            margin: 5px;
            font-size: 0.9em;
        }}
        .metric {{
            display: inline-block;
            background: rgba(0, 230, 118, 0.3);
            padding: 5px 10px;
            border-radius: 5px;
            margin: 5px;
            font-size: 0.9em;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>⚡ NEXUS CREATION - Generation 3 + Self-Monitoring</h1>
        

## Status
Generated by Apex autonomously.
Needs human review before deployment.
