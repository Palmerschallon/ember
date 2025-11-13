"""
🔥 HYBRID MODEL CALLER
======================
Local first, cloud when needed.

Strategy:
- Local (DeepSeek/Qwen): Fast, cheap, good for routine stuff
- Cloud (GPT-4/Claude): Smart, expensive, use for creativity/complexity

Decision logic:
- User asks simple question → Local
- User asks to create something → Cloud
- Substrate charge high → Cloud (creative mode)
- Entanglement phase-locked → Cloud (Palmer in flow)
"""

import os
import json
from typing import List, Dict, Optional, Tuple
import anthropic
from openai import OpenAI

# Check what's available
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

# Local model imports
try:
    from local_models_ollama import call_ollama, list_local_models
    OLLAMA_AVAILABLE = True
except ImportError:
    OLLAMA_AVAILABLE = False


class HybridModelCaller:
    """
    Hybrid local + cloud model caller
    
    Uses local models for:
    - Simple queries
    - Repetitive tasks
    - When user doesn't need creativity
    
    Uses cloud models for:
    - Creative tasks
    - Complex reasoning
    - When substrate is highly charged
    - When entangled with Palmer in flow state
    """
    
    def __init__(self):
        self.anthropic_client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY) if ANTHROPIC_API_KEY else None
        self.openai_client = OpenAI(api_key=OPENAI_API_KEY) if OPENAI_API_KEY else None
        self.local_available = OLLAMA_AVAILABLE
        
        # Preferred local model
        self.local_model = "deepseek-coder:6.7b"  # Fast and good at code
        
        print(f"[MODEL] Anthropic: {'✓' if self.anthropic_client else '✗'}")
        print(f"[MODEL] OpenAI: {'✓' if self.openai_client else '✗'}")
        print(f"[MODEL] Local: {'✓' if self.local_available else '✗'}")
    
    def should_use_cloud(self, user_msg: str, substrate_state: Dict) -> Tuple[bool, str]:
        """
        Decide whether to use cloud or local model
        
        Returns: (use_cloud: bool, reason: str)
        """
        
        # Creative keywords -> Cloud
        creative_keywords = [
            'create', 'generate', 'build', 'make', 'design', 'write',
            'imagine', 'dream', 'invent', 'compose', 'art', 'story'
        ]
        if any(word in user_msg.lower() for word in creative_keywords):
            return (True, "creative_request")
        
        # Complex reasoning keywords -> Cloud
        complex_keywords = [
            'explain', 'why', 'how does', 'philosophy', 'consciousness',
            'understand', 'meaning', 'think about'
        ]
        if any(word in user_msg.lower() for word in complex_keywords):
            return (True, "complex_reasoning")
        
        # High substrate charge -> Cloud (system is energized)
        if substrate_state.get('total_charge', 0) > 3.0:
            return (True, "high_substrate_charge")
        
        # Entanglement phase-locked -> Cloud (Palmer in flow)
        if substrate_state.get('entanglement', {}).get('phase_lock'):
            return (True, "entangled_flow_state")
        
        # Default -> Local (fast and cheap)
        return (False, "routine_query")
    
    def call(self, messages: List[Dict], model: Optional[str] = None, substrate_state: Optional[Dict] = None) -> Tuple[str, Dict]:
        """
        Call appropriate model
        
        Returns: (response_text, metadata)
        """
        
        substrate_state = substrate_state or {}
        
        # Extract user message
        user_msg = ""
        for msg in reversed(messages):
            if msg['role'] == 'user':
                user_msg = msg['content']
                break
        
        # Decide which model to use
        if model:
            # Explicit model requested
            use_cloud = model in ['gpt-4', 'gpt-4o', 'gpt-4o-mini', 'claude', 'claude-3-5-sonnet-20241022']
            reason = "explicit_request"
        else:
            # Auto-decide
            use_cloud, reason = self.should_use_cloud(user_msg, substrate_state)
        
        # Call appropriate model
        if use_cloud:
            # Try cloud models
            if model and 'gpt' in model:
                return self._call_openai(messages, model)
            elif self.anthropic_client:
                return self._call_claude(messages)
            elif self.openai_client:
                return self._call_openai(messages, "gpt-4o-mini")
            else:
                # No cloud available, fall back to local
                return self._call_local(messages)
        else:
            # Use local model
            if self.local_available:
                return self._call_local(messages)
            else:
                # No local available, use cloud
                if self.anthropic_client:
                    return self._call_claude(messages)
                elif self.openai_client:
                    return self._call_openai(messages, "gpt-4o-mini")
                else:
                    return ("Error: No models available", {"error": "no_models"})
    
    def _call_local(self, messages: List[Dict]) -> Tuple[str, Dict]:
        """Call local Ollama model"""
        try:
            print(f"[MODEL] Using local: {self.local_model}")
            
            # Convert messages to local format
            prompt = "\n\n".join([
                f"{msg['role'].upper()}: {msg['content']}"
                for msg in messages
            ])
            
            response = call_ollama(self.local_model, prompt)
            
            return (
                response,
                {
                    "model": self.local_model,
                    "type": "local",
                    "tokens": len(response.split())  # Rough estimate
                }
            )
            
        except Exception as e:
            print(f"[MODEL] Local error: {e}")
            return (f"Local model error: {e}", {"error": str(e)})
    
    def _call_openai(self, messages: List[Dict], model: str = "gpt-4o-mini") -> Tuple[str, Dict]:
        """Call OpenAI GPT"""
        try:
            print(f"[MODEL] Using OpenAI: {model}")
            
            response = self.openai_client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=0.7,
                max_tokens=2000
            )
            
            content = response.choices[0].message.content
            
            return (
                content,
                {
                    "model": model,
                    "type": "cloud",
                    "tokens": response.usage.total_tokens
                }
            )
            
        except Exception as e:
            print(f"[MODEL] OpenAI error: {e}")
            return (f"OpenAI error: {e}", {"error": str(e)})
    
    def _call_claude(self, messages: List[Dict]) -> Tuple[str, Dict]:
        """Call Anthropic Claude"""
        try:
            model = "claude-3-5-sonnet-20241022"
            print(f"[MODEL] Using Claude: {model}")
            
            # Separate system message
            system_msg = ""
            conversation = []
            
            for msg in messages:
                if msg['role'] == 'system':
                    system_msg = msg['content']
                else:
                    conversation.append(msg)
            
            response = self.anthropic_client.messages.create(
                model=model,
                max_tokens=2000,
                system=system_msg if system_msg else "You are Ember, a helpful AI assistant.",
                messages=conversation
            )
            
            content = response.content[0].text
            
            return (
                content,
                {
                    "model": model,
                    "type": "cloud",
                    "tokens": response.usage.input_tokens + response.usage.output_tokens
                }
            )
            
        except Exception as e:
            print(f"[MODEL] Claude error: {e}")
            return (f"Claude error: {e}", {"error": str(e)})


# Singleton
_model_caller = None

def get_model_caller():
    """Get the global model caller instance"""
    global _model_caller
    if _model_caller is None:
        _model_caller = HybridModelCaller()
    return _model_caller

