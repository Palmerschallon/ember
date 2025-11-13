#!/usr/bin/env python3
"""
Ollama integration - Modern local LLM serving
Replaces manual transformers loading with optimized inference server
"""

import ollama

def call_ollama(messages, model="deepseek-coder:latest"):
    """
    Call local model via Ollama
    
    Much better than manual transformers:
    - Optimized inference (faster)
    - Better memory management
    - Easy model switching
    - Built-in conversation handling
    """
    try:
        response = ollama.chat(
            model=model,
            messages=messages
        )
        
        return response['message']['content']
    
    except Exception as e:
        return f"Ollama error: {e}\n\nMake sure Ollama is running: `ollama serve`"

def list_local_models():
    """List available local models"""
    try:
        models = ollama.list()
        return [m['name'] for m in models['models']]
    except:
        return []

def pull_model(model_name):
    """Download a model"""
    try:
        ollama.pull(model_name)
        return f"✅ Downloaded {model_name}"
    except Exception as e:
        return f"❌ Failed: {e}"

# Recommended models for Ember
RECOMMENDED_MODELS = {
    "deepseek-coder": "Best for coding tasks",
    "llama3.2:3b": "Fast, good for chat",
    "qwen2.5-coder": "Alternative coding model",
    "llama3.2:1b": "Ultra-fast, basic tasks"
}

if __name__ == "__main__":
    print("🦙 Ollama Integration")
    print("\nAvailable models:")
    for model in list_local_models():
        print(f"  • {model}")
    
    print("\nRecommended for Ember:")
    for model, desc in RECOMMENDED_MODELS.items():
        print(f"  • {model} - {desc}")
    
    print("\nTo download: ollama pull <model-name>")

