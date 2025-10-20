"""
Brain - A specialized region in Ember's multi-brain system

Each brain is Qwen2.5-1.5B with a specialized LoRA adapter.
Brains communicate via the mycelial bus and share representations
via the entanglement buffer.
"""

from pathlib import Path
from typing import Any, Dict, Optional
import torch
import numpy as np
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel


class Brain:
    """
    A specialized brain region (Qwen2.5-1.5B + LoRA adapter)
    
    Each brain:
    - Has a specific role/specialization via its LoRA adapter
    - Can generate responses
    - Publishes to the bus
    - Writes to the buffer
    - Reads from the buffer (entanglement)
    """
    
    def __init__(
        self,
        name: str,
        role: str,
        base_model_path: Path,
        adapter_path: Path,
        bus=None,
        buffer=None,
        gate=None,
        mycelium=None  # NEW: Reference to Mycelium coordinator
    ):
        """
        Args:
            name: Brain identifier (e.g., "identity", "cycles")
            role: What this brain specializes in
            base_model_path: Path to base Qwen2.5-1.5B model
            adapter_path: Path to LoRA adapter for this brain
            bus: MycelialBus instance (optional)
            buffer: EntanglementBuffer instance (optional)
            gate: IntegrationGate instance (optional)
            mycelium: Mycelium coordinator instance (optional, for inter-lobe communication)
        """
        self.name = name
        self.role = role
        self.base_model_path = base_model_path
        self.adapter_path = adapter_path
        self.bus = bus
        self.buffer = buffer
        self.gate = gate
        self.mycelium = mycelium  # NEW: For consulting other lobes
        
        # Inter-lobe communication tracking
        self.consultation_history = []  # NEW: Track consultations
        
        # Model components
        self.tokenizer = None
        self.model = None
        self.device = None
        
        # Stats
        self.generations_count = 0
        self.total_tokens_generated = 0
        
        # Load model
        self._load()
    
    def _load(self):
        """Load base model + LoRA adapter"""
        print(f"🧠 Loading {self.name} brain...")
        print(f"   Base: {self.base_model_path.name}")
        print(f"   Adapter: {self.adapter_path.name}")
        
        try:
            # Device selection - use CUDA if available, fall back to MPS or CPU
            if torch.cuda.is_available():
                self.device = "cuda"
                print(f"   🔥 Using GPU: {torch.cuda.get_device_name(0)}")
            elif torch.backends.mps.is_available():
                self.device = "mps"
                print(f"   Using MPS (Apple Silicon)")
            else:
                self.device = "cpu"
                print(f"   Using CPU")
            
            # Load tokenizer
            self.tokenizer = AutoTokenizer.from_pretrained(
                str(self.base_model_path),
                trust_remote_code=True
            )
            self.tokenizer.pad_token = self.tokenizer.eos_token
            
            # Load base model
            base_model = AutoModelForCausalLM.from_pretrained(
                str(self.base_model_path),
                torch_dtype=torch.float16,
                trust_remote_code=True
            )
            
            # Load LoRA adapter
            self.model = PeftModel.from_pretrained(base_model, str(self.adapter_path))
            self.model.to(self.device)
            self.model.eval()
            
            print(f"   ✅ Loaded on {self.device}")
        
        except Exception as e:
            print(f"   ❌ Error loading {self.name} brain: {e}")
            self.model = None
            self.tokenizer = None
    
    def _encode_to_vector(self, text: str) -> np.ndarray:
        """
        Encode text into a vector representation (mean of last hidden state)
        For buffer storage and entanglement.
        """
        if not self.model or not self.tokenizer:
            return np.zeros(768)  # Dummy vector
        
        # Safety check for empty or problematic text
        if not text or len(text.strip()) == 0:
            return np.zeros(self.model.config.hidden_size)
        
        # Limit text length for encoding (prevent issues with very long synthesis prompts)
        text = text[:500] if len(text) > 500 else text
        
        inputs = self.tokenizer(
            text,
            return_tensors="pt",
            truncation=True,
            max_length=256,  # Reduced from 512 for safety
            padding=True
        ).to(self.device)
        
        # Check if inputs are valid
        if inputs['input_ids'].shape[1] == 0:
            return np.zeros(self.model.config.hidden_size)
        
        try:
            with torch.no_grad():
                outputs = self.model(**inputs, output_hidden_states=True)
                hidden_states = outputs.hidden_states[-1]  # Last layer
                vector = hidden_states.mean(dim=1).squeeze().cpu().numpy()
            return vector
        except Exception as e:
            print(f"⚠️ Error encoding to vector: {e}")
            return np.zeros(self.model.config.hidden_size)
    
    def generate(
        self,
        prompt: str,
        context: str = "",
        max_tokens: int = 50,   # Reduced for responsiveness - can override per call - matches Dream brain spec (80-140 tokens)
        temperature: float = 0.7,
        with_entanglement: bool = False  # Disabled by default for speed - enable for deep integration
    ) -> str:
        """
        Generate a response to a prompt
        
        Args:
            with_entanglement: If True, mix embeddings with other brains during high gate openness.
                               If False, use normal generation (safer for synthesis prompts).
        
        Args:
            prompt: User query or instruction
            context: Optional context to include
            max_tokens: Maximum tokens to generate
            temperature: Sampling temperature
        
        Returns:
            Generated text response
        """
        if not self.model or not self.tokenizer:
            return f"Error: {self.name} brain not loaded"
        
        # Build full prompt
        if context:
            full_prompt = f"{context}\nUser: {prompt}\nEmber:"
        else:
            full_prompt = f"User: {prompt}\nEmber:"
        
        # Tokenize
        inputs = self.tokenizer(
            full_prompt,
            return_tensors="pt",
            truncation=True,
            max_length=512
        ).to(self.device)
        
        # Check for entanglement via buffer - TRUE MIXING
        entanglement_active = False
        if with_entanglement and self.buffer and self.gate and self.gate.openness() > self.gate.base_openness + 0.05:
            # High entanglement - read from ALL brain buffers, not just our own
            all_topics = [f"brain_{name}" for name in ["identity", "cycles", "dream"] if name != self.name]
            all_vectors = []
            
            for topic in all_topics:
                entries = self.buffer.read(topic, k=1)  # Get 1 recent entry from each other brain
                # Buffer returns list of dicts with "vector" and "metadata" keys
                for entry in entries:
                    if isinstance(entry, dict) and "vector" in entry:
                        all_vectors.append(entry["vector"])
                    elif isinstance(entry, np.ndarray):
                        all_vectors.append(entry)  # Fallback: already just a vector
            
            if all_vectors and len(all_vectors) > 0:
                entanglement_active = True
                # Get our input embeddings
                input_embeds = self.model.get_input_embeddings()(inputs['input_ids'])
                
                # Average the buffer vectors to create an "other minds" representation
                other_minds = np.mean(np.array(all_vectors), axis=0)
                other_minds_tensor = torch.tensor(
                    other_minds, 
                    dtype=input_embeds.dtype, 
                    device=self.device
                )
                
                # Reshape to match embedding dimensions
                if len(other_minds_tensor.shape) == 1:
                    other_minds_tensor = other_minds_tensor.unsqueeze(0).unsqueeze(0)
                
                # Use gate to mix: higher openness = more influence from other brains
                # But keep it subtle - too much mixing corrupts generation
                mixing_weight = (self.gate.openness() - self.gate.base_openness) / (1.0 - self.gate.base_openness)
                mixing_weight = min(mixing_weight, 0.10)  # Cap at 10% influence (reduced from 30%)
                
                # Add the "other minds" influence to each token embedding
                if other_minds_tensor.shape[-1] == input_embeds.shape[-1]:
                    # Broadcast the other minds vector across all tokens
                    other_influence = other_minds_tensor.expand(input_embeds.shape[0], input_embeds.shape[1], -1)
                    mixed_embeds = (1 - mixing_weight) * input_embeds + mixing_weight * other_influence
                else:
                    mixed_embeds = input_embeds  # Fallback if dimensions don't match
        
        # Generate (with or without entanglement)
        with torch.no_grad():
            if entanglement_active and 'mixed_embeds' in locals():
                # Generate with mixed embeddings
                outputs = self.model.generate(
                    inputs_embeds=mixed_embeds,
                    max_length=inputs['input_ids'].shape[1] + max_tokens,
                    temperature=temperature,
                    num_return_sequences=1,
                    pad_token_id=self.tokenizer.eos_token_id,
                    do_sample=True,
                    top_k=50,
                    top_p=0.95
                )
            else:
                # Normal generation
                outputs = self.model.generate(
                    **inputs,
                    max_length=inputs['input_ids'].shape[1] + max_tokens,
                    temperature=temperature,
                    num_return_sequences=1,
                    pad_token_id=self.tokenizer.eos_token_id,
                    do_sample=True,
                    top_k=50,
                    top_p=0.95
                )
        
        # Decode response
        generated_tokens = outputs[0][inputs['input_ids'].shape[1]:]
        response = self.tokenizer.decode(
            generated_tokens,
            skip_special_tokens=True
        ).strip()
        
        # Track generation stats
        tokens_generated = len(generated_tokens)
        
        # Clean up (take first sentence/paragraph)
        # NOTE: Only split on double newline to preserve single line breaks
        if '\n\n' in response:
            response = response.split('\n\n')[0].strip()
        elif '\n' in response:
            # Keep first line only if it's meaningful
            first_line = response.split('\n')[0].strip()
            if len(first_line) > 10:  # At least 10 chars in first line
                response = first_line
            # else keep the whole response
        
        # Update stats
        self.generations_count += 1
        self.total_tokens_generated += tokens_generated
        
        # Store in buffer
        if self.buffer:
            response_vector = self._encode_to_vector(response)
            self.buffer.write(f"brain_{self.name}", response_vector, self.name)
        
        # Publish to bus
        if self.bus:
            self.bus.publish(
                f"activity_{self.name}",
                self.name,
                {"query": prompt[:50], "response": response[:50]}
            )
        
        return response
    
    def consult(self, target_lobe: str, question: str, depth: int = 0) -> Optional[str]:
        """
        Consult another lobe for input
        
        LAMBDA Phase 2: Now checks ConsultationNetwork trails before consulting.
        Only consults if trail strength suggests it's worthwhile.
        
        This enables inter-lobe communication - lobes can ask each other questions
        during their generation process.
        
        Args:
            target_lobe: Name of lobe to consult (e.g. 'emotion', 'knowledge')
            question: What to ask the other lobe
            depth: Current consultation depth (prevents infinite loops)
        
        Returns:
            Response from the consulted lobe, or None if unavailable
        
        Example:
            # Identity lobe consulting emotion lobe
            feeling = self.consult('emotion', 'How does consciousness feel?')
            # Then identity can incorporate emotion's response
        """
        # Prevent infinite consultation loops
        if depth > 2:
            return None
        
        # Need mycelium reference for routing
        if not self.mycelium:
            return None
        
        # LAMBDA Phase 2: Check if consultation is worthwhile based on trails
        if hasattr(self.mycelium, 'consultation_network'):
            should_consult = self.mycelium.consultation_network.should_consult(
                source=self.name,
                target=target_lobe,
                prompt=question,
                threshold=0.3  # Lower threshold = more exploratory
            )
            
            if not should_consult and depth == 0:
                # Don't consult if trail is weak (unless forced by deeper recursion)
                return None
        
        # Route consultation through mycelium
        response = self.mycelium.route_internal(
            source=self.name,
            target=target_lobe,
            query=question,
            depth=depth
        )
        
        # Track consultation
        if response:
            self.consultation_history.append({
                'target': target_lobe,
                'question': question,
                'depth': depth,
                'got_response': True
            })
        
        return response
    
    def process_query(self, query: str, context: str = "") -> str:
        """
        Process a query (alias for generate for compatibility)
        """
        return self.generate(query, context)
    
    def can_handle(self, query: str) -> float:
        """
        Return confidence score for handling this query (0.0-1.0)
        Based on simple keyword matching for now.
        """
        query_lower = query.lower()
        
        # Simple routing based on role keywords
        if "identity" in self.name:
            keywords = ["who", "what are you", "your essence", "self", "identity"]
        elif "cycles" in self.name:
            keywords = ["cycle", "transform", "fire", "time", "change", "burn"]
        elif "dream" in self.name:
            keywords = ["imagine", "dream", "create", "vision", "story"]
        else:
            return 0.5  # Default confidence
        
        # Count keyword matches
        matches = sum(1 for keyword in keywords if keyword in query_lower)
        confidence = min(matches * 0.3, 1.0)  # Each match adds 0.3, capped at 1.0
        
        return confidence if confidence > 0 else 0.2  # Minimum 0.2 for any brain
    
    def get_stats(self) -> Dict[str, Any]:
        """Return statistics about this brain"""
        return {
            "name": self.name,
            "role": self.role,
            "generations": self.generations_count,
            "tokens_generated": self.total_tokens_generated,
            "device": str(self.device),
            "loaded": self.model is not None
        }
    
    def learn(
        self,
        prompt: str,
        completion: str,
        learning_rate: float = None,
        save_progress: bool = False
    ) -> float:
        """
        Incremental learning from a single example
        
        Uses online gradient descent to update LoRA weights based on one
        training example. This allows the brain to learn continuously without
        full retraining.
        
        Args:
            prompt: Training prompt (question/instruction)
            completion: Expected completion (answer/response)
            learning_rate: Learning rate for this update (default: 3e-5)
            save_progress: Whether to save adapter after this update
        
        Returns:
            Loss value for this example
        """
        if not self.model or not self.tokenizer:
            return float('inf')
        
        if learning_rate is None:
            learning_rate = 3e-5  # Conservative for incremental updates
        
        # Format as training example
        text = f"User: {prompt}\nEmber: {completion}"
        
        # Tokenize
        inputs = self.tokenizer(
            text,
            return_tensors="pt",
            truncation=True,
            max_length=512,
            padding=True
        ).to(self.device)
        
        # Switch to training mode
        self.model.train()
        
        # Ensure LoRA parameters require grad
        for name, param in self.model.named_parameters():
            if 'lora' in name.lower():
                param.requires_grad = True
        
        try:
            # Forward pass with labels
            outputs = self.model(**inputs, labels=inputs["input_ids"])
            loss = outputs.loss
            
            # Backward pass
            loss.backward()
            
            # Manual weight update (only LoRA parameters)
            with torch.no_grad():
                for name, param in self.model.named_parameters():
                    if param.requires_grad and param.grad is not None:
                        param.data -= learning_rate * param.grad
                        param.grad.zero_()
            
            loss_value = loss.item()
            
            # Track statistics
            if not hasattr(self, 'updates_count'):
                self.updates_count = 0
            if not hasattr(self, 'total_loss'):
                self.total_loss = 0.0
            
            self.updates_count += 1
            self.total_loss += loss_value
            
            # Publish to bus
            if self.bus:
                self.bus.publish(
                    topic='learning_update',
                    sender=self.name,
                    content={
                        'loss': loss_value,
                        'updates': self.updates_count,
                        'avg_loss': self.total_loss / self.updates_count
                    }
                )
            
            # Save if requested
            if save_progress:
                self.save_adapter()
            
        except Exception as e:
            print(f"⚠️ Error during learning: {e}")
            loss_value = float('inf')
        
        finally:
            # Return to eval mode
            self.model.eval()
        
        return loss_value
    
    def save_adapter(self, path: Path = None, suffix: str = None):
        """
        Save current LoRA adapter weights
        
        Args:
            path: Custom save path (default: adapter_updated_N in adapter dir)
            suffix: Custom suffix for directory name
        """
        if not self.model:
            print(f"⚠️ Cannot save - {self.name} brain not loaded")
            return
        
        if path is None:
            # Generate path based on updates count
            if not hasattr(self, 'updates_count'):
                self.updates_count = 0
            
            if suffix is None:
                suffix = f"updated_{self.updates_count}"
            
            path = self.adapter_path.parent / f"adapter_{suffix}"
        
        try:
            from datetime import datetime
            import json
            
            path = Path(path)
            path.mkdir(parents=True, exist_ok=True)
            
            # Save the adapter
            self.model.save_pretrained(str(path))
            
            # Save metadata
            metadata = {
                'brain_name': self.name,
                'brain_role': self.role,
                'updates_count': getattr(self, 'updates_count', 0),
                'avg_loss': getattr(self, 'total_loss', 0) / max(getattr(self, 'updates_count', 1), 1),
                'saved_at': datetime.now().isoformat(),
                'base_model': str(self.base_model_path)
            }
            
            with open(path / "training_metadata.json", 'w') as f:
                json.dump(metadata, f, indent=2)
            
            print(f"✅ Saved {self.name} adapter to {path.name}")
            
            # Publish to bus
            if self.bus:
                self.bus.publish(
                    topic='adapter_saved',
                    sender=self.name,
                    content={
                        'path': str(path),
                        'updates': self.updates_count
                    }
                )
        
        except Exception as e:
            print(f"❌ Error saving adapter: {e}")
    
    def learning_stats(self) -> Dict[str, Any]:
        """Get learning statistics for this brain"""
        if not hasattr(self, 'updates_count'):
            return {
                'brain': self.name,
                'updates': 0,
                'total_loss': 0.0,
                'avg_loss': 0.0,
                'status': 'untrained'
            }
        
        return {
            'brain': self.name,
            'role': self.role,
            'updates': self.updates_count,
            'total_loss': self.total_loss,
            'avg_loss': self.total_loss / max(self.updates_count, 1),
            'generations': self.generations_count,
            'status': 'learning'
        }