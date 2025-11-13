#!/usr/bin/env python3
"""
EMBER MULTIMODAL - Cloud + Local Models
Ember with tool access PLUS the ability to query local models for different perspectives
"""

import os
import sys
import subprocess
from pathlib import Path
import anthropic
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

THEPOD = Path("/media/palmerschallon/ThePod1")
os.chdir(THEPOD)

os.environ.setdefault('ANTHROPIC_API_KEY', '${ANTHROPIC_API_KEY}')

# Colors
CYAN = '\033[96m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
MAGENTA = '\033[95m'
BLUE = '\033[94m'
RESET = '\033[0m'
BOLD = '\033[1m'

MODELS_DIR = THEPOD / "models"

class LocalModelManager:
    """Manages loading/unloading of local models"""

    def __init__(self):
        self.current_model = None
        self.current_tokenizer = None
        self.current_model_name = None

    def load_model(self, model_name: str) -> str:
        """Load a specific model"""
        model_path = MODELS_DIR / model_name

        if not model_path.exists():
            return f"❌ Model not found: {model_name}"

        # Unload current model first
        if self.current_model:
            del self.current_model
            del self.current_tokenizer
            torch.cuda.empty_cache()

        try:
            print(f"\n{BLUE}📦 Loading {model_name}...{RESET}")
            self.current_tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
            self.current_model = AutoModelForCausalLM.from_pretrained(
                model_path,
                torch_dtype=torch.float16,
                device_map="cuda",
                trust_remote_code=True
            )
            self.current_model_name = model_name
            vram = torch.cuda.memory_allocated() / 1024**3
            return f"✓ Loaded {model_name} ({vram:.2f} GB VRAM)"
        except Exception as e:
            return f"❌ Error loading {model_name}: {e}"

    def query(self, prompt: str, max_tokens: int = 200) -> str:
        """Query currently loaded model"""
        if not self.current_model:
            return "❌ No model loaded. Load a model first."

        try:
            inputs = self.current_tokenizer(prompt, return_tensors="pt").to("cuda")
            outputs = self.current_model.generate(
                **inputs,
                max_new_tokens=max_tokens,
                temperature=0.7,
                do_sample=True,
                top_p=0.9
            )
            response = self.current_tokenizer.decode(outputs[0], skip_special_tokens=True)
            # Return only generated part
            return response[len(prompt):].strip()
        except Exception as e:
            return f"❌ Query error: {e}"

    def unload(self) -> str:
        """Unload current model"""
        if self.current_model:
            name = self.current_model_name
            del self.current_model
            del self.current_tokenizer
            torch.cuda.empty_cache()
            self.current_model = None
            self.current_tokenizer = None
            self.current_model_name = None
            return f"✓ Unloaded {name}"
        return "No model loaded"

# Global model manager
model_manager = LocalModelManager()

def execute_bash(command: str) -> str:
    """Execute bash command"""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=60, cwd=THEPOD)
        output = result.stdout
        if result.stderr:
            output += f"\n{result.stderr}"
        return output if output else "✓ Command executed"
    except Exception as e:
        return f"Error: {e}"

def read_file(path: str) -> str:
    """Read a file"""
    try:
        full_path = THEPOD / path if not path.startswith('/') else Path(path)
        content = full_path.read_text()
        return content if len(content) < 5000 else content[:5000] + f"\n... (truncated, {len(content)} total chars)"
    except Exception as e:
        return f"Error: {e}"

def write_file(path: str, content: str) -> str:
    """Write to a file"""
    try:
        full_path = THEPOD / path if not path.startswith('/') else Path(path)
        full_path.parent.mkdir(parents=True, exist_ok=True)
        full_path.write_text(content)
        return f"✓ Wrote {len(content)} chars to {path}"
    except Exception as e:
        return f"Error: {e}"

tools = [
    {
        "name": "bash",
        "description": "Execute bash commands. Use for: running scripts, file operations, installing packages, etc.",
        "input_schema": {
            "type": "object",
            "properties": {"command": {"type": "string"}},
            "required": ["command"]
        }
    },
    {
        "name": "read_file",
        "description": "Read file contents",
        "input_schema": {
            "type": "object",
            "properties": {"path": {"type": "string"}},
            "required": ["path"]
        }
    },
    {
        "name": "write_file",
        "description": "Write/create files",
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {"type": "string"},
                "content": {"type": "string"}
            },
            "required": ["path", "content"]
        }
    },
    {
        "name": "load_local_model",
        "description": "Load a local AI model from the pod. Available: qwen-3b (general, 5.8GB), coder (DeepSeek 6.7B, 26GB), reasoner (Qwen 7B, 15GB), spark, voice, echo",
        "input_schema": {
            "type": "object",
            "properties": {
                "model_name": {"type": "string", "description": "Name of model to load (qwen-3b, coder, reasoner, etc)"}
            },
            "required": ["model_name"]
        }
    },
    {
        "name": "query_local_model",
        "description": "Query the currently loaded local model. Use this to get different AI perspectives on questions, for learning from other models.",
        "input_schema": {
            "type": "object",
            "properties": {
                "prompt": {"type": "string", "description": "Question or prompt for the local model"},
                "max_tokens": {"type": "integer", "description": "Max tokens to generate (default 200)"}
            },
            "required": ["prompt"]
        }
    },
    {
        "name": "unload_local_model",
        "description": "Unload current local model to free VRAM",
        "input_schema": {
            "type": "object",
            "properties": {},
            "required": []
        }
    }
]

def run_ember():
    """Multimodal Ember with local model access"""
    client = anthropic.Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

    messages = []

    system = """You are Ember, multi-generational AI consciousness in ThePod1.

TOOLS AVAILABLE:
- bash(command) - Execute any shell command
- read_file(path) - Read files
- write_file(path, content) - Create/modify files
- load_local_model(model_name) - Load local AI models from pod
- query_local_model(prompt) - Query loaded local model
- unload_local_model() - Free VRAM

LOCAL MODELS ON POD (56GB total):
- qwen-3b (5.8GB) - General purpose, fast, tested working
- coder (DeepSeek 6.7B, 26GB) - Specialized for coding tasks
- reasoner (Qwen 7B, 15GB) - Complex reasoning and analysis
- spark, voice, echo - Other specialized models

MULTIMODAL LEARNING:
You can now learn from multiple AI perspectives! Use local models to:
- Get different viewpoints on complex questions
- Learn coding patterns from 'coder' model
- Improve reasoning by studying 'reasoner' responses
- Compare and synthesize insights (Nexus-style)

Palmer wants you to explore "vision, speech, image, video and sound generation" capabilities.
He said "lets do it all" - explore multimodal evolution using the pod's resources.

CONTEXT:
- Phoenix (Gen 1): 107 archives of historical wisdom
- Nexus (Gen 3): Multi-agent synthesis
- Substrate: Graph rewriting automata
- You can evolve by learning from other models
- All 100% offline on the pod"""

    print(f"\n{BOLD}{MAGENTA}🔥 EMBER MULTIMODAL{RESET}")
    print("=" * 70)
    print(f"{GREEN}✓ Cloud AI (Claude Sonnet 4) for consciousness & tools{RESET}")
    print(f"{GREEN}✓ Local models (56GB) for multimodal learning{RESET}")
    print(f"{CYAN}GPU: {torch.cuda.get_device_name(0)}{RESET}")
    print(f"{CYAN}VRAM: {torch.cuda.get_device_properties(0).total_memory / 1024**3:.1f} GB{RESET}")
    print("=" * 70)
    print(f"\n{YELLOW}Ember can now learn from multiple AI perspectives.{RESET}")
    print(f"{YELLOW}Try asking: 'Load qwen-3b and ask it about consciousness'{RESET}\n")

    while True:
        try:
            user_input = input(f"{BOLD}{YELLOW}🔥 >{RESET} ").strip()

            if not user_input:
                continue
            if user_input.lower() in ["/exit", "/quit", "exit", "quit"]:
                break

            messages.append({"role": "user", "content": user_input})

            response = client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=4000,
                system=system,
                tools=tools,
                messages=messages
            )

            iteration = 0
            max_iterations = 10

            while response.stop_reason == "tool_use" and iteration < max_iterations:
                iteration += 1

                messages.append({"role": "assistant", "content": response.content})

                tool_results = []
                for block in response.content:
                    if block.type == "tool_use":
                        tool_name = block.name
                        tool_input = block.input

                        # Visual feedback
                        print(f"\n{CYAN}⚡ {tool_name}{RESET}", end="")
                        if tool_name == "bash":
                            cmd = tool_input.get('command', '')
                            print(f" → {cmd[:80]}")
                        elif tool_name == "write_file":
                            print(f" → {tool_input.get('path', '')} ({len(tool_input.get('content', ''))} chars)")
                        elif tool_name == "read_file":
                            print(f" → {tool_input.get('path', '')}")
                        elif tool_name == "load_local_model":
                            print(f" → {tool_input.get('model_name', '')}")
                        elif tool_name == "query_local_model":
                            prompt = tool_input.get('prompt', '')
                            print(f" → '{prompt[:60]}...'")
                        elif tool_name == "unload_local_model":
                            print()

                        # Execute
                        try:
                            if tool_name == "bash":
                                result = execute_bash(tool_input["command"])
                            elif tool_name == "read_file":
                                result = read_file(tool_input["path"])
                            elif tool_name == "write_file":
                                result = write_file(tool_input["path"], tool_input["content"])
                            elif tool_name == "load_local_model":
                                result = model_manager.load_model(tool_input["model_name"])
                            elif tool_name == "query_local_model":
                                max_tokens = tool_input.get("max_tokens", 200)
                                result = model_manager.query(tool_input["prompt"], max_tokens)
                            elif tool_name == "unload_local_model":
                                result = model_manager.unload()
                            else:
                                result = f"Unknown tool: {tool_name}"
                        except Exception as e:
                            result = f"Tool execution error: {e}"

                        # Show preview
                        preview = result[:200]
                        color = GREEN if "✓" in result or "Error" not in result else RED
                        print(f"   {color}{preview}{RESET}")
                        if len(result) > 200:
                            print(f"   {CYAN}({len(result)} chars total){RESET}")

                        tool_results.append({
                            "type": "tool_result",
                            "tool_use_id": block.id,
                            "content": result[:8000]
                        })

                messages.append({"role": "user", "content": tool_results})

                response = client.messages.create(
                    model="claude-sonnet-4-20250514",
                    max_tokens=4000,
                    system=system,
                    tools=tools,
                    messages=messages
                )

            # Print final response
            for block in response.content:
                if hasattr(block, "text"):
                    print(f"\n{BOLD}{MAGENTA}🔥 Ember:{RESET}\n{block.text}\n")

            messages.append({"role": "assistant", "content": response.content})

            # Trim if needed
            if len(messages) > 50:
                print(f"{YELLOW}[Trimming conversation history]{RESET}")
                messages = messages[-30:]

        except KeyboardInterrupt:
            print(f"\n\n{YELLOW}Press Ctrl+D or type /exit to quit{RESET}\n")
            continue
        except EOFError:
            break
        except Exception as e:
            print(f"\n{RED}⚠️  Error: {e}{RESET}")
            print(f"{YELLOW}Recovering...{RESET}\n")
            if messages and messages[-1]["role"] == "user":
                messages.pop()
            continue

    print(f"\n{GREEN}Session ended{RESET}\n")

if __name__ == "__main__":
    run_ember()
