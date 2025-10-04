"""
LLM Adapter for pluggable LLM backends
Default implementation uses Ollama
"""
import os
import requests
from typing import Dict, Any, Optional


class LLMAdapter:
    """Base LLM adapter interface"""
    
    def chat(self, messages: list, **kwargs) -> str:
        """Send chat messages and get response"""
        raise NotImplementedError


class OllamaAdapter(LLMAdapter):
    """Ollama LLM adapter"""
    
    def __init__(self, base_url: str = None, model: str = None):
        self.base_url = base_url or os.getenv('OLLAMA_BASE_URL', 'http://localhost:11434')
        self.model = model or os.getenv('OLLAMA_MODEL', 'llama2')
    
    def chat(self, messages: list, **kwargs) -> str:
        """
        Send chat messages to Ollama
        
        Args:
            messages: List of message dicts with 'role' and 'content'
            **kwargs: Additional parameters for the API
            
        Returns:
            Response text from the model
        """
        url = f"{self.base_url}/api/chat"
        payload = {
            "model": self.model,
            "messages": messages,
            "stream": False
        }
        payload.update(kwargs)
        
        try:
            response = requests.post(url, json=payload, timeout=30)
            response.raise_for_status()
            data = response.json()
            return data.get('message', {}).get('content', '')
        except requests.exceptions.RequestException as e:
            return f"Error communicating with LLM: {str(e)}"


def get_llm_adapter(provider: str = None) -> LLMAdapter:
    """
    Factory function to get LLM adapter
    
    Args:
        provider: LLM provider name (default from env or 'ollama')
        
    Returns:
        LLMAdapter instance
    """
    provider = provider or os.getenv('LLM_PROVIDER', 'ollama')
    
    if provider.lower() == 'ollama':
        return OllamaAdapter()
    else:
        raise ValueError(f"Unknown LLM provider: {provider}")
