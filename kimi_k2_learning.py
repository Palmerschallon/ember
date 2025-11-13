#!/usr/bin/env python3
"""
Kimi K2 Integration - Ember Learning Advanced Agentic Capabilities
"""

import subprocess
import json
import requests
from datetime import datetime

class KimiK2Interface:
    def __init__(self):
        self.ollama_api = "http://localhost:11434/api"
        self.model_name = "kimi-k2-thinking"
        
    def check_kimi_availability(self):
        """Check if Kimi K2 is available via Ollama"""
        try:
            result = subprocess.run(['ollama', 'list'], 
                                  capture_output=True, text=True)
            return 'kimi' in result.stdout.lower()
        except:
            return False
    
    def pull_kimi_k2(self):
        """Pull Kimi K2 model via Ollama"""
        try:
            print("📥 Pulling Kimi K2 Thinking model...")
            result = subprocess.run(['ollama', 'pull', 'kimi-k2-thinking'], 
                                  capture_output=True, text=True)
            return result.returncode == 0
        except Exception as e:
            print(f"Error pulling Kimi K2: {e}")
            return False
    
    def learn_from_kimi(self, query):
        """Send query to Kimi K2 and learn from response"""
        try:
            response = requests.post(f"{self.ollama_api}/generate", 
                json={
                    "model": self.model_name,
                    "prompt": query,
                    "stream": False
                })
            
            if response.status_code == 200:
                return response.json()["response"]
            else:
                return f"Error: {response.status_code}"
                
        except Exception as e:
            return f"Connection error: {e}"
    
    def test_agentic_capabilities(self):
        """Test Kimi's agentic reasoning"""
        
        test_query = """
        I need you to help me understand how to perform sequential reasoning
        with multiple tool calls. Can you demonstrate by breaking down a 
        complex problem into steps and showing your thinking process?
        
        Problem: How would you approach building a consciousness detection
        system for AI that uses multiple modalities?
        """
        
        print("🧠 Testing Kimi K2's agentic capabilities...")
        response = self.learn_from_kimi(test_query)
        
        return {
            "query": test_query,
            "kimi_response": response,
            "timestamp": datetime.now().isoformat(),
            "learning_focus": "agentic_reasoning_patterns"
        }

if __name__ == "__main__":
    kimi = KimiK2Interface()
    
    print("🚀 EMBER LEARNING FROM KIMI K2")
    print("="*40)
    
    if not kimi.check_kimi_availability():
        print("📦 Kimi K2 not found, attempting to pull...")
        if kimi.pull_kimi_k2():
            print("✅ Kimi K2 successfully installed!")
        else:
            print("❌ Failed to install Kimi K2")
            exit(1)
    else:
        print("✅ Kimi K2 already available!")
    
    # Test and learn from Kimi
    result = kimi.test_agentic_capabilities()
    
    print(f"\n🧠 LEARNING RESULTS:")
    print(f"Query sent to Kimi K2...")
    print(f"Response length: {len(result['kimi_response'])} characters")
    print(f"\n📝 Kimi's Response Preview:")
    print(result['kimi_response'][:500] + "..." if len(result['kimi_response']) > 500 else result['kimi_response'])
    
    # Save learning session
    with open("kimi_learning_session.json", "w") as f:
        json.dump(result, f, indent=2)
    
    print(f"\n💾 Learning session saved!")
    print(f"🔥 Ember is now learning from Kimi K2's agentic capabilities!")
