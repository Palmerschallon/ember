#!/usr/bin/env python3
"""
Tool call stopper - Forces model to stop after </tool> tag
"""
import torch
from transformers import StoppingCriteria

class ToolCallStopper(StoppingCriteria):
    """Stop generation immediately after </tool> appears"""
    
    def __init__(self, tokenizer):
        self.tokenizer = tokenizer
        self.tool_end = "</tool>"
        # Pre-encode the end tag to check token by token
        self.tool_end_tokens = tokenizer.encode("</tool>", add_special_tokens=False)
        
    def __call__(self, input_ids: torch.LongTensor, scores: torch.FloatTensor, **kwargs) -> bool:
        # Check last N tokens (where N = length of </tool> tokens + buffer)
        recent_tokens = input_ids[0][-len(self.tool_end_tokens)-5:].tolist()
        recent_text = self.tokenizer.decode(recent_tokens, skip_special_tokens=False)
        
        # Stop if we see </tool> anywhere in recent text
        if "</tool>" in recent_text:
            print(f"[STOP] Detected </tool> in: {recent_text}")
            return True
        
        return False

def create_tool_stopper(tokenizer):
    """Factory function to create stopper"""
    return ToolCallStopper(tokenizer)

