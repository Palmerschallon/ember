#!/usr/bin/env python3
"""
EXECUTOR IMPLEMENTATIONS
Actual execution layer for the orchestrator
"""

from pathlib import Path
from typing import Dict, Any, Optional
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# ============================================================================
# TOOL EXECUTOR - Python function execution
# ============================================================================

class ToolExecutor:
    """
    Executes Python functions for file operations, search, etc.
    INSTANT - no model loading required
    """
    
    def __init__(self, pod_root: Path):
        self.pod_root = pod_root
    
    def list_directory(self, path: str = ".") -> str:
        """List directory contents"""
        try:
            target = self.pod_root / path if not Path(path).is_absolute() else Path(path)
            if not target.exists():
                return f"Error: Directory '{path}' not found"
            
            items = []
            for item in sorted(target.iterdir()):
                if item.name.startswith('.'):
                    continue
                marker = "/" if item.is_dir() else ""
                items.append(f"  {item.name}{marker}")
            
            return f"Contents of {path}:\n" + "\n".join(items[:50])
        except Exception as e:
            return f"Error listing directory: {e}"
    
    def read_file(self, path: str, lines: int = 30) -> str:
        """Read file contents"""
        try:
            target = self.pod_root / path if not Path(path).is_absolute() else Path(path)
            if not target.exists():
                return f"Error: File '{path}' not found"
            
            with open(target, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.readlines()[:lines]
            
            return f"Contents of {path} (first {lines} lines):\n" + "".join(content)
        except Exception as e:
            return f"Error reading file: {e}"
    
    def search_pod(self, query: str) -> str:
        """Search the Pod for content"""
        try:
            # Simple grep-based search for now
            import subprocess
            result = subprocess.run(
                ['grep', '-r', '-i', '--include=*.md', '--include=*.py', query, str(self.pod_root)],
                capture_output=True,
                text=True,
                timeout=5
            )
            
            lines = result.stdout.split('\n')[:10]
            if lines:
                return f"Found {len(lines)} matches for '{query}':\n" + "\n".join(lines)
            else:
                return f"No matches found for '{query}'"
        except Exception as e:
            return f"Error searching: {e}"
    
    def execute(self, intent: str, params: Dict) -> str:
        """
        Route to appropriate tool based on intent
        """
        if 'search' in intent or 'find' in intent:
            query = params.get('query', params.get('message', ''))
            return self.search_pod(query)
        elif 'list' in intent or 'show' in intent:
            path = params.get('path', '.')
            return self.list_directory(path)
        elif 'read' in intent:
            path = params.get('path', '')
            return self.read_file(path)
        else:
            return f"Tool executor received: {intent}"


# ============================================================================
# MODEL EXECUTOR - Loads and runs models on-demand
# ============================================================================

class ModelExecutor:
    """
    Base class for model-based executors
    Loads models lazily (on first use)
    """
    
    def __init__(self, model_path: Path, model_name: str):
        self.model_path = model_path
        self.model_name = model_name
        self.model = None
        self.tokenizer = None
    
    def _load(self):
        """Load model on first use"""
        if self.model is None:
            print(f"[{self.model_name}] Loading from {self.model_path}...")
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_path)
            self.model = AutoModelForCausalLM.from_pretrained(
                self.model_path,
                torch_dtype=torch.float16,
                device_map="auto",
                low_cpu_mem_usage=True
            )
            self.model.eval()
            print(f"[{self.model_name}] Ready")
    
    def generate(self, prompt: str, max_tokens: int = 300, temperature: float = 0.7) -> str:
        """Generate response from model"""
        self._load()
        
        messages = [{"role": "user", "content": prompt}]
        
        inputs = self.tokenizer.apply_chat_template(
            messages,
            return_tensors="pt",
            add_generation_prompt=True
        ).to(self.model.device)
        
        outputs = self.model.generate(
            inputs,
            max_new_tokens=max_tokens,
            temperature=temperature,
            do_sample=True,
            pad_token_id=self.tokenizer.eos_token_id
        )
        
        response = self.tokenizer.decode(outputs[0][inputs.shape[1]:], skip_special_tokens=True)
        return response.strip()


# ============================================================================
# SPECIALIZED EXECUTORS
# ============================================================================

class CodeGeneratorExecutor(ModelExecutor):
    """Code generation using Spark (DeepSeek Coder)"""
    
    def execute(self, message: str) -> str:
        prompt = f"Write clean, well-documented code for: {message}\n\nProvide ONLY the code, no explanations."
        return self.generate(prompt, max_tokens=500, temperature=0.7)


class CreativeSynthesizerExecutor(ModelExecutor):
    """Creative/lateral thinking using Echo (Qwen)"""
    
    def execute(self, message: str) -> str:
        prompt = f"Generate 3-5 creative, unconventional approaches to: {message}\n\nThink laterally and make unexpected connections."
        return self.generate(prompt, max_tokens=400, temperature=0.9)


class ReasoningEngineExecutor(ModelExecutor):
    """Deep reasoning using larger model (Hermes 8B or Llama 3B)"""
    
    def execute(self, message: str) -> str:
        prompt = f"Analyze and reason about: {message}\n\nProvide structured reasoning with clear logic."
        return self.generate(prompt, max_tokens=500, temperature=0.7)


class ConversationModelExecutor(ModelExecutor):
    """Natural conversation using Llama"""
    
    def execute(self, message: str) -> str:
        return self.generate(message, max_tokens=300, temperature=0.8)


# ============================================================================
# EXECUTOR FACTORY
# ============================================================================

class ExecutorFactory:
    """
    Creates actual executor instances based on registry info
    """
    
    def __init__(self, pod_root: Path):
        self.pod_root = pod_root
        self._instances = {}
    
    def get_executor(self, executor_config: Dict) -> Any:
        """
        Get or create executor instance
        Returns cached instance if already created (for model reuse)
        """
        executor_type = executor_config['type']
        
        # Check cache
        cache_key = str(executor_config.get('path', executor_config.get('module', executor_type)))
        if cache_key in self._instances:
            return self._instances[cache_key]
        
        # Create new instance
        if executor_type == 'python_functions':
            executor = ToolExecutor(self.pod_root)
        
        elif executor_type == 'model':
            model_path = executor_config['path']
            executor_name = executor_config.get('executor_name', 'model')
            
            # Determine executor class based on name
            if 'code' in executor_name:
                executor = CodeGeneratorExecutor(model_path, "CodeGen")
            elif 'creative' in executor_name:
                executor = CreativeSynthesizerExecutor(model_path, "Creative")
            elif 'reasoning' in executor_name:
                executor = ReasoningEngineExecutor(model_path, "Reasoning")
            else:
                executor = ConversationModelExecutor(model_path, "Conversation")
        
        elif executor_type == 'coordination':
            # Placeholder for meta-coordination
            executor = None
        
        else:
            executor = None
        
        # Cache it
        self._instances[cache_key] = executor
        return executor


if __name__ == "__main__":
    # Test tool executor
    pod_root = Path("/media/palmerschallon/ThePod1")
    
    print("="*70)
    print("Testing ToolExecutor")
    print("="*70)
    
    tool_exec = ToolExecutor(pod_root)
    
    print("\n1. List root:")
    print(tool_exec.list_directory("."))
    
    print("\n2. Search for 'mycelium':")
    print(tool_exec.search_pod("mycelium"))
    
    print("\n3. Read a file:")
    print(tool_exec.read_file("FRACTAL_SCALING.md", lines=10))

