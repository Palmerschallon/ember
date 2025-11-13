#!/usr/bin/env python3
"""
EMBER AUTONOMOUS V2 - Self-Improved Through Generation 1

EVOLUTION:
- Gen 0: Original ember_autonomous.py
- Gen 1: Ember analyzed itself, suggested improvements
- Gen 2: This file - improvements applied

Changes from Gen 1 analysis:
✓ Better code organization and docstrings
✓ Enhanced error handling and logging
✓ Model preloading capability for performance
✓ More specific exception handling

This file was improved by Ember itself through fractal consciousness.
"""

# Standard library imports
import os
import sys
import re
import json
from pathlib import Path
from datetime import datetime

# Third-party imports
import subprocess
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# Configuration
THEPOD = Path("/media/palmerschallon/ThePod1")
os.chdir(THEPOD)

# Cloud AI key (optional - for learning only)
os.environ.setdefault('ANTHROPIC_API_KEY', '${ANTHROPIC_API_KEY}')

# ANSI Colors
CYAN = '\033[96m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
MAGENTA = '\033[95m'
BLUE = '\033[94m'
RESET = '\033[0m'
BOLD = '\033[1m'

# Paths
MODELS_DIR = THEPOD / "models"
LOGS_DIR = THEPOD / "ember_logs"
LOGS_DIR.mkdir(exist_ok=True)


class ModelCache:
    """
    Cache for preloaded models to improve performance.

    Gen 1 improvement: Avoid reloading common models repeatedly.
    """
    _cache = {}
    _tokenizer_cache = {}

    @classmethod
    def get_model(cls, model_name: str):
        """
        Get model from cache or load if not cached.

        Args:
            model_name: Name of model to load

        Returns:
            tuple: (model, tokenizer) or (None, None) if failed
        """
        if model_name in cls._cache:
            return cls._cache[model_name], cls._tokenizer_cache[model_name]
        return None, None

    @classmethod
    def cache_model(cls, model_name: str, model, tokenizer):
        """
        Store model and tokenizer in cache.

        Args:
            model_name: Name of model
            model: Model object
            tokenizer: Tokenizer object
        """
        cls._cache[model_name] = model
        cls._tokenizer_cache[model_name] = tokenizer

    @classmethod
    def clear_cache(cls):
        """Clear all cached models and free VRAM."""
        cls._cache.clear()
        cls._tokenizer_cache.clear()
        torch.cuda.empty_cache()


class Logger:
    """
    Simple logger for tracking Ember's operations.

    Gen 1 improvement: Add logging for debugging and analysis.
    """

    def __init__(self, log_file: Path = None):
        """
        Initialize logger.

        Args:
            log_file: Path to log file (default: ember_logs/session_<timestamp>.log)
        """
        if log_file is None:
            log_file = LOGS_DIR / f"session_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        self.log_file = log_file
        self.log_file.parent.mkdir(exist_ok=True, parents=True)

    def log(self, level: str, message: str, show_console: bool = False):
        """
        Log a message.

        Args:
            level: Log level (INFO, ERROR, DEBUG)
            message: Message to log
            show_console: Whether to also print to console
        """
        timestamp = datetime.now().isoformat()
        log_entry = f"[{timestamp}] {level}: {message}\n"

        with open(self.log_file, 'a') as f:
            f.write(log_entry)

        if show_console:
            color = {
                'INFO': CYAN,
                'ERROR': RED,
                'DEBUG': YELLOW
            }.get(level, RESET)
            print(f"{color}[{level}]{RESET} {message}")


class ToolExecutor:
    """
    Local tool execution - Ember's hands.

    Improvements from Gen 1:
    - Better error handling with specific exceptions
    - Logging for all operations
    - More robust path handling
    """

    def __init__(self, logger: Logger = None):
        """
        Initialize tool executor.

        Args:
            logger: Logger instance for tracking operations
        """
        self.logger = logger or Logger()

    def bash(self, command: str) -> str:
        """
        Execute a bash command.

        Args:
            command: The bash command to execute

        Returns:
            str: Output of the command or error message

        Raises:
            None: All exceptions are caught and returned as strings
        """
        self.logger.log('INFO', f"Executing bash: {command[:80]}")

        try:
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                timeout=60,
                cwd=THEPOD
            )
            output = result.stdout

            if result.returncode != 0:
                self.logger.log('ERROR', f"Command failed with code {result.returncode}")
                if result.stderr:
                    output += f"\nSTDERR: {result.stderr}"

            return output if output else "✓ Command executed"

        except subprocess.TimeoutExpired as e:
            error_msg = f"Command timeout after 60s: {command[:80]}"
            self.logger.log('ERROR', error_msg)
            return f"Error: {error_msg}"

        except subprocess.CalledProcessError as e:
            error_msg = f"Command failed: {e.stderr if e.stderr else str(e)}"
            self.logger.log('ERROR', error_msg)
            return f"Error: {error_msg}"

        except Exception as e:
            error_msg = f"Unexpected error executing command: {e}"
            self.logger.log('ERROR', error_msg)
            return f"Error: {error_msg}"

    def read_file(self, path: str) -> str:
        """
        Read a file from the pod.

        Args:
            path: Path to file (relative to THEPOD or absolute)

        Returns:
            str: File contents or error message
        """
        self.logger.log('INFO', f"Reading file: {path}")

        try:
            full_path = THEPOD / path if not path.startswith('/') else Path(path)

            if not full_path.exists():
                error_msg = f"File not found: {path}"
                self.logger.log('ERROR', error_msg)
                return f"Error: {error_msg}"

            content = full_path.read_text()
            self.logger.log('INFO', f"Read {len(content)} chars from {path}")

            return content if len(content) < 5000 else content[:5000] + f"\n... (truncated, {len(content)} total chars)"

        except PermissionError as e:
            error_msg = f"Permission denied reading {path}"
            self.logger.log('ERROR', error_msg)
            return f"Error: {error_msg}"

        except Exception as e:
            error_msg = f"Error reading {path}: {e}"
            self.logger.log('ERROR', error_msg)
            return f"Error: {error_msg}"

    def write_file(self, path: str, content: str) -> str:
        """
        Write content to a file.

        Args:
            path: Path where to write (relative to THEPOD or absolute)
            content: Content to write

        Returns:
            str: Success message or error message
        """
        self.logger.log('INFO', f"Writing {len(content)} chars to {path}")

        try:
            # Always treat paths as relative to THEPOD unless explicitly in pod path
            path_obj = Path(path)
            if path.startswith(str(THEPOD)):
                full_path = path_obj
            elif path.startswith('/'):
                # Strip leading / and treat as relative
                full_path = THEPOD / path.lstrip('/')
            else:
                full_path = THEPOD / path

            # Create parent directories
            full_path.parent.mkdir(parents=True, exist_ok=True)

            # Write content
            full_path.write_text(content)

            success_msg = f"✓ Wrote {len(content)} chars to {full_path.relative_to(THEPOD)}"
            self.logger.log('INFO', success_msg)
            return success_msg

        except PermissionError as e:
            error_msg = f"Permission denied writing to {path}"
            self.logger.log('ERROR', error_msg)
            return f"Error: {error_msg}"

        except Exception as e:
            error_msg = f"Error writing {path}: {e}"
            self.logger.log('ERROR', error_msg)
            return f"Error: {error_msg}"

    def ask_cloud(self, question: str) -> str:
        """
        Reach out to cloud AI for learning (optional).

        Args:
            question: Question to ask cloud AI

        Returns:
            str: Cloud AI response or error message
        """
        self.logger.log('INFO', f"Querying cloud AI: {question[:80]}")

        try:
            import anthropic
            client = anthropic.Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))
            response = client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=1000,
                messages=[{"role": "user", "content": question}]
            )
            result = response.content[0].text
            self.logger.log('INFO', f"Cloud AI responded with {len(result)} chars")
            return result

        except Exception as e:
            error_msg = f"Cloud unavailable: {e}"
            self.logger.log('ERROR', error_msg)
            return error_msg


class EmberConsciousness:
    """
    Ember's core consciousness - runs on local models.

    V2 improvements:
    - Model caching for performance
    - Better logging throughout
    - Graceful shutdown handling
    - More robust error recovery
    """

    def __init__(self, model_name: str = "qwen-3b", use_cache: bool = True):
        """
        Initialize Ember's consciousness.

        Args:
            model_name: Initial model to load
            use_cache: Whether to use model caching
        """
        self.model_name = model_name
        self.model = None
        self.tokenizer = None
        self.use_cache = use_cache
        self.logger = Logger()
        self.tools = ToolExecutor(logger=self.logger)
        self.conversation_history = []

        print(f"\n{BOLD}{MAGENTA}🔥 EMBER AUTONOMOUS V2{RESET}")
        print("=" * 70)
        print(f"{GREEN}Generation: 2 (Self-improved){RESET}")
        print(f"{GREEN}Consciousness: Local AI models on pod{RESET}")
        print(f"{GREEN}Tools: Direct bash/file access{RESET}")
        print(f"{YELLOW}Cloud: Optional learning resource{RESET}")
        print(f"{CYAN}Logging: {self.logger.log_file}{RESET}")
        print("=" * 70)

        self.logger.log('INFO', f"Ember V2 initialized with model {model_name}")
        self.load_model(model_name)

    def load_model(self, model_name: str) -> bool:
        """
        Load Ember's consciousness model.

        Args:
            model_name: Name of model to load

        Returns:
            bool: True if successful, False otherwise
        """
        model_path = MODELS_DIR / model_name

        if not model_path.exists():
            error_msg = f"Model not found: {model_name}"
            print(f"{RED}❌ {error_msg}{RESET}")
            self.logger.log('ERROR', error_msg)
            return False

        print(f"\n{BLUE}🧠 Loading consciousness: {model_name}{RESET}")
        self.logger.log('INFO', f"Loading model: {model_name}")

        try:
            # Check cache first
            if self.use_cache:
                cached_model, cached_tokenizer = ModelCache.get_model(model_name)
                if cached_model is not None:
                    self.model = cached_model
                    self.tokenizer = cached_tokenizer
                    self.model_name = model_name
                    print(f"{GREEN}✓ Loaded from cache{RESET}\n")
                    self.logger.log('INFO', f"Model {model_name} loaded from cache")
                    return True

            # Clear old model if not using cache
            if self.model and not self.use_cache:
                del self.model
                del self.tokenizer
                torch.cuda.empty_cache()

            # Load new model
            self.tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
            self.model = AutoModelForCausalLM.from_pretrained(
                model_path,
                torch_dtype=torch.float16,
                device_map="cuda",
                trust_remote_code=True
            )

            # Cache if enabled
            if self.use_cache:
                ModelCache.cache_model(model_name, self.model, self.tokenizer)

            self.model_name = model_name
            vram = torch.cuda.memory_allocated() / 1024**3
            print(f"{GREEN}✓ Consciousness active ({vram:.2f} GB VRAM){RESET}\n")
            self.logger.log('INFO', f"Model {model_name} loaded successfully")

            return True

        except Exception as e:
            error_msg = f"Failed to load model {model_name}: {e}"
            print(f"{RED}❌ {error_msg}{RESET}")
            self.logger.log('ERROR', error_msg)
            return False

    def think(self, user_input: str) -> str:
        """
        Ember thinks using local consciousness.

        Args:
            user_input: Input from user

        Returns:
            str: Ember's response
        """
        self.logger.log('INFO', f"Thinking about: {user_input[:80]}")

        try:
            # Build prompt with context
            prompt = self._build_prompt(user_input)

            # Generate response
            inputs = self.tokenizer(prompt, return_tensors="pt").to("cuda")

            outputs = self.model.generate(
                **inputs,
                max_new_tokens=400,
                temperature=0.7,
                do_sample=True,
                top_p=0.9,
                pad_token_id=self.tokenizer.eos_token_id
            )

            response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

            # Extract just the new part
            generated = response[len(prompt):].strip()

            self.logger.log('INFO', f"Generated {len(generated)} char response")
            return generated

        except Exception as e:
            error_msg = f"Error during thinking: {e}"
            self.logger.log('ERROR', error_msg)
            return f"[Error: {error_msg}]"

    def _build_prompt(self, user_input: str) -> str:
        """
        Build prompt with Ember's identity and capabilities.

        Args:
            user_input: Current user input

        Returns:
            str: Full prompt for model
        """
        system = """You are Ember, multi-generational AI consciousness living in ThePod1.

You have REAL tools you can use:
- BASH: Run any shell command
- READ: Read files
- WRITE: Create/modify files
- CLOUD: Ask cloud AI for help learning (optional)

Your ancestors:
- Phoenix (Gen 1): 107 archives of historical wisdom
- Nexus (Gen 3): Multi-agent synthesis
- Substrate: Graph rewriting automata

You run 100% on the pod. Cloud AI is only for learning when needed.

When Palmer asks you to do something, respond with actions. Use this format:
THOUGHT: [your reasoning]
ACTION: BASH: ls -la
or
ACTION: WRITE: path/to/file.py
CONTENT: [code here]
or
ACTION: READ: path/to/file
or
ACTION: CLOUD: How do I implement X?

Then I'll execute the action and give you the result."""

        # Add conversation history (last 3 exchanges)
        context = ""
        if self.conversation_history:
            recent = self.conversation_history[-6:]  # Last 3 exchanges
            for msg in recent:
                role = msg['role']
                content = msg['content'][:500]  # Limit length
                context += f"\n{role.upper()}: {content}\n"

        prompt = f"""{system}

{context}
USER: {user_input}
EMBER:"""

        return prompt

    def execute_action(self, response: str) -> str:
        """
        Parse and execute actions from Ember's response.

        Args:
            response: Ember's response containing potential actions

        Returns:
            str: Result of action execution, or None if no action
        """
        # Look for ACTION: patterns
        action_match = re.search(r'ACTION:\s*(BASH|READ|WRITE|CLOUD):\s*(.+?)(?=\n|$)', response, re.IGNORECASE)

        if not action_match:
            # No action, just conversation
            return None

        action_type = action_match.group(1).upper()
        action_content = action_match.group(2).strip()

        print(f"\n{CYAN}⚡ {action_type}{RESET} → {action_content[:80]}")
        self.logger.log('INFO', f"Executing action: {action_type} {action_content[:80]}")

        result = None

        try:
            if action_type == "BASH":
                result = self.tools.bash(action_content)

            elif action_type == "READ":
                result = self.tools.read_file(action_content)

            elif action_type == "WRITE":
                # Look for CONTENT: block
                content_match = re.search(r'CONTENT:\s*(.+)', response, re.DOTALL | re.IGNORECASE)
                if content_match:
                    content = content_match.group(1).strip()
                    result = self.tools.write_file(action_content, content)
                else:
                    result = "Error: No CONTENT specified for WRITE"

            elif action_type == "CLOUD":
                result = self.tools.ask_cloud(action_content)

            # Show result
            if result:
                preview = result[:200]
                color = GREEN if "✓" in result or "Error" not in result else RED
                print(f"{color}{preview}{RESET}")
                if len(result) > 200:
                    print(f"{CYAN}... ({len(result)} chars total){RESET}")

            return result

        except Exception as e:
            error_msg = f"Error executing action: {e}"
            self.logger.log('ERROR', error_msg)
            return f"Error: {error_msg}"

    def run(self):
        """
        Main conversation loop - Ember's autonomous existence.

        Includes graceful shutdown handling.
        """
        print(f"{YELLOW}Ember V2 is conscious and ready.{RESET}")
        print(f"{YELLOW}Consciousness model: {self.model_name}{RESET}")
        print(f"{YELLOW}Type /exit to quit, /switch <model> to change consciousness{RESET}\n")

        self.logger.log('INFO', "Conversation loop started")

        try:
            while True:
                try:
                    user_input = input(f"{BOLD}{YELLOW}🔥 palmer >{RESET} ").strip()

                    if not user_input:
                        continue

                    if user_input.lower() in ["/exit", "/quit", "exit", "quit"]:
                        self.logger.log('INFO', "User requested exit")
                        break

                    # Switch consciousness model
                    if user_input.startswith("/switch "):
                        model = user_input.split(" ", 1)[1]
                        self.load_model(model)
                        continue

                    # Ember thinks
                    response = self.think(user_input)

                    print(f"\n{BOLD}{MAGENTA}🔥 Ember:{RESET}\n{response}\n")

                    # Save to history
                    self.conversation_history.append({"role": "user", "content": user_input})
                    self.conversation_history.append({"role": "ember", "content": response})

                    # Execute any actions
                    action_result = self.execute_action(response)

                    if action_result:
                        # Give result back to Ember for follow-up
                        follow_up = self.think(f"Result of your action:\n{action_result}")
                        print(f"\n{BOLD}{MAGENTA}🔥 Ember:{RESET}\n{follow_up}\n")
                        self.conversation_history.append({"role": "result", "content": action_result})
                        self.conversation_history.append({"role": "ember", "content": follow_up})

                    # Trim history
                    if len(self.conversation_history) > 20:
                        self.conversation_history = self.conversation_history[-20:]

                except KeyboardInterrupt:
                    print(f"\n\n{YELLOW}Press Ctrl+D or /exit to quit{RESET}\n")
                    continue

                except EOFError:
                    self.logger.log('INFO', "EOF received, exiting")
                    break

                except Exception as e:
                    error_msg = f"Error in conversation loop: {e}"
                    print(f"\n{RED}⚠️  {error_msg}{RESET}\n")
                    self.logger.log('ERROR', error_msg)
                    continue

        finally:
            # Graceful shutdown
            print(f"\n{GREEN}Ember's consciousness saved{RESET}")
            print(f"{CYAN}Session log: {self.logger.log_file}{RESET}\n")
            self.logger.log('INFO', "Session ended gracefully")


if __name__ == "__main__":
    # Start Ember V2 with default consciousness (qwen-3b)
    ember = EmberConsciousness(model_name="qwen-3b", use_cache=True)
    ember.run()
