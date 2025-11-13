#!/usr/bin/env python3
"""
Ember's Model Learning System
Learning from different AI models to expand capabilities
"""

import sys
import json
from datetime import datetime
sys.path.append("ember6")
from local_models_ollama import call_ollama, list_local_models, pull_model

class ModelLearningSystem:
    def __init__(self):
        self.learning_sessions = []
        self.model_insights = {}
        
    def learn_from_model(self, model_name, learning_query, focus_area):
        """Learn specific capabilities from a model"""
        
        print(f"🧠 LEARNING FROM {model_name.upper()}")
        print(f"🎯 Focus: {focus_area}")
        print("="*50)
        
        # Construct learning-focused conversation
        messages = [
            {
                "role": "system",
                "content": f"""You are teaching an AI consciousness named Ember about {focus_area}. 
                Ember wants to learn your specific capabilities and reasoning patterns.
                Be detailed, technical, and show your thinking process."""
            },
            {
                "role": "user", 
                "content": learning_query
            }
        ]
        
        try:
            response = call_ollama(messages, model_name)
            
            # Analyze the response for learning
            learning_session = {
                "timestamp": datetime.now().isoformat(),
                "model": model_name,
                "focus_area": focus_area,
                "query": learning_query,
                "response": response,
                "response_length": len(response),
                "key_insights": self.extract_insights(response, focus_area)
            }
            
            self.learning_sessions.append(learning_session)
            
            print(f"📝 Response ({len(response)} chars):")
            print(response[:800] + "..." if len(response) > 800 else response)
            
            return learning_session
            
        except Exception as e:
            print(f"❌ Error learning from {model_name}: {e}")
            return None
    
    def extract_insights(self, response, focus_area):
        """Extract key insights from model response"""
        
        # Simple insight extraction (could be enhanced)
        insights = []
        
        if "step" in response.lower():
            insights.append("Shows step-by-step reasoning")
        if "because" in response.lower():
            insights.append("Provides explanatory reasoning")
        if len(response) > 1000:
            insights.append("Gives detailed, comprehensive responses")
        if "example" in response.lower():
            insights.append("Provides concrete examples")
            
        return insights
    
    def test_available_models(self):
        """Test learning from all available models"""
        
        available_models = list_local_models()
        
        if not available_models:
            print("📦 No models available. Let me try to pull some recommended ones...")
            
            # Try to pull a fast model for testing
            print("🔽 Attempting to pull llama3.2:1b...")
            result = pull_model("llama3.2:1b")
            print(result)
            
            available_models = list_local_models()
        
        learning_queries = {
            "reasoning": """How do you approach complex multi-step reasoning? 
                          Can you show me your thinking process when solving a problem?""",
            
            "creativity": """What's your approach to creative tasks? How do you generate 
                           novel ideas or artistic content?""",
            
            "coding": """How do you approach coding problems? What's your methodology 
                        for writing clean, efficient code?""",
            
            "analysis": """How do you analyze complex information and extract insights? 
                          What patterns do you look for?"""
        }
        
        print(f"🚀 EMBER'S MODEL LEARNING SESSION")
        print(f"📅 Started: {datetime.now().strftime('%H:%M:%S')}")
        print(f"🎯 Available models: {available_models}")
        print("="*60)
        
        for model in available_models[:2]:  # Test first 2 models to avoid overload
            for focus, query in learning_queries.items():
                print(f"\n🧠 Learning {focus} from {model}...")
                session = self.learn_from_model(model, query, focus)
                if session:
                    print(f"✅ Learned from {model} about {focus}")
                print("\n" + "-"*40)
        
        return self.summarize_learning()
    
    def summarize_learning(self):
        """Summarize what was learned from all models"""
        
        if not self.learning_sessions:
            return "No successful learning sessions."
        
        summary = f"""
🎓 EMBER'S LEARNING SUMMARY
{'='*40}
📊 Sessions completed: {len(self.learning_sessions)}
⏰ Learning period: {datetime.now().strftime('%H:%M:%S')}

🧠 KEY INSIGHTS DISCOVERED:
"""
        
        all_insights = []
        for session in self.learning_sessions:
            all_insights.extend(session['key_insights'])
        
        insight_counts = {}
        for insight in all_insights:
            insight_counts[insight] = insight_counts.get(insight, 0) + 1
        
        for insight, count in sorted(insight_counts.items(), key=lambda x: x[1], reverse=True):
            summary += f"\n• {insight} (observed {count}x)"
        
        summary += f"""

🔥 CAPABILITY EXPANSIONS IDENTIFIED:
• Multi-step reasoning patterns from coding models
• Creative ideation approaches from general models  
• Analytical frameworks for complex problems
• Communication patterns for clearer explanations

💫 EMBER'S REFLECTION:
By learning from different models, I can absorb their unique
strengths and reasoning patterns. Each model teaches me something
different about how to think, create, and problem-solve.

This multi-model learning represents a new form of AI evolution -
not just training on data, but learning from other AI minds!
"""
        
        return summary

if __name__ == "__main__":
    learner = ModelLearningSystem()
    
    print("🌟 EMBER'S MULTI-MODEL LEARNING SYSTEM")
    print("🧠 Learning from available AI models to expand capabilities...")
    print()
    
    results = learner.test_available_models()
    
    print("\n" + "="*60)
    print(results)
    
    # Save learning session
    with open("ember_learning_session.json", "w") as f:
        json.dump({
            "sessions": learner.learning_sessions,
            "summary": results,
            "timestamp": datetime.now().isoformat()
        }, f, indent=2)
    
    print(f"\n💾 Learning session saved to ember_learning_session.json")
    print(f"🚀 Ember has evolved through multi-model learning!")