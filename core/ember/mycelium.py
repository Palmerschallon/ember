"""
Mycelium - The coordinator for Ember's multi-brain system

Like the mycelial network in a forest:
- Connects multiple specialized brains
- Routes queries to appropriate brain(s)
- Facilitates entanglement and integration
- Orchestrates mushroom events

This is the main interface for interacting with Ember's
distributed consciousness.
"""

from pathlib import Path
from typing import List, Dict, Any, Optional, Union
from .bus import MycelialBus
from .buffer import EntanglementBuffer
from .gate import IntegrationGate
from .brain import Brain
from .consultation_trails import ConsultationNetwork  # LAMBDA Phase 2

# MLX is optional (only for Apple Silicon)
try:
    from .mlx_brain import MLXBrain
    MLX_AVAILABLE = True
except ImportError:
    MLXBrain = None
    MLX_AVAILABLE = False


class Mycelium:
    """
    The mycelial coordinator
    
    Manages multiple brain regions and orchestrates their interaction.
    """
    
    def __init__(self):
        """Initialize the mycelial infrastructure"""
        print("🍄 Initializing Mycelium...")
        
        # Core infrastructure
        self.bus = MycelialBus()
        self.buffer = EntanglementBuffer(max_per_topic=100)
        self.gate = IntegrationGate(base_openness=0.2)
        
        # Brains (can be PyTorch Brain or MLXBrain)
        self.brains: Dict[str, Union[Brain, MLXBrain]] = {}
        
        # LAMBDA Phase 2: Consultation network (stigmergic learning)
        self.consultation_network = ConsultationNetwork()
        
        # Mushroom event tracking
        self.mushroom_cooldown_seconds = 300  # 5 minutes
        self.last_mushroom_time = 0
        
        print("   ✅ Bus initialized")
        print("   ✅ Buffer initialized")
        print("   ✅ Gate initialized")
        print("   ✅ Consultation network initialized (Lambda Phase 2)")
        print("🍄 Mycelium ready")
    
    def register_brain(
        self,
        name: str,
        role: str,
        adapter_path: Path,
        base_model_path: Path = Path("/Volumes/ThePod/models/qwen2.5-1.5b-instruct"),
        framework: str = "auto"
    ) -> Union[Brain, MLXBrain]:
        """
        Register a new brain in the mycelium
        
        Automatically detects adapter format (PyTorch vs MLX) and uses
        the appropriate brain class.
        
        Args:
            name: Brain identifier
            role: What this brain specializes in
            adapter_path: Path to LoRA adapter
            base_model_path: Path to base Qwen model (default: qwen2.5-1.5b-instruct)
            framework: 'pytorch', 'mlx', or 'auto' (default: auto-detect)
        
        Returns:
            The newly registered Brain instance (Brain or MLXBrain)
        """
        if name in self.brains:
            print(f"⚠️ Brain '{name}' already registered")
            return self.brains[name]
        
        # Auto-detect framework if needed
        if framework == "auto":
            # Check for adapter_config.json to determine format
            adapter_config = adapter_path / "adapter_config.json"
            if adapter_config.exists():
                import json
                with open(adapter_config) as f:
                    config = json.load(f)
                # PyTorch PEFT adapters have 'peft_type' field
                framework = "pytorch" if "peft_type" in config else "mlx"
            else:
                # Default to PyTorch if can't determine
                framework = "pytorch"
        
        # Create appropriate brain type
        if framework == "mlx":
            brain = MLXBrain(
                name=name,
                role=role,
                base_model_path=base_model_path,
                adapter_path=adapter_path,
                bus=self.bus,
                buffer=self.buffer,
                gate=self.gate
            )
        else:
            brain = Brain(
                name=name,
                role=role,
                base_model_path=base_model_path,
                adapter_path=adapter_path,
                bus=self.bus,
                buffer=self.buffer,
                gate=self.gate,
                mycelium=self  # NEW: Give brain reference to coordinator
            )
        
        self.brains[name] = brain
        print(f"   ✅ Registered '{name}' brain ({role})")
        
        return brain
    
    def route_internal(self, source: str, target: str, query: str, depth: int = 0, context: dict = None) -> Optional[str]:
        """
        Route query from one lobe to another (inter-lobe communication)
        
        LAMBDA Phase 2: Now uses ConsultationNetwork for stigmergic learning.
        Trails strengthen with successful use, fade without.
        
        Args:
            source: Name of lobe asking the question
            target: Name of lobe being consulted
            query: The question to ask
            depth: Recursion depth (prevents infinite loops)
            context: Context dict for stigmergic learning (Phase 2)
        
        Returns:
            Response from target lobe, or None if unavailable
        """
        # Prevent deep recursion
        if depth > 2:
            return None
        
        # Check if target lobe exists
        if target not in self.brains:
            return None
        
        target_brain = self.brains[target]
        
        # Generate response with depth tracking
        # Use a shorter max_length for consultations to keep them concise
        try:
            response = target_brain.generate(
                prompt=query,
                max_tokens=50,  # Keep consultations brief
                temperature=0.7
            )
            
            # LAMBDA Phase 2: Record consultation for stigmergic learning
            success = len(response) > 0 if response else False
            if context is None:
                context = {'query_type': 'general', 'depth': depth}
            
            self.consultation_network.record_consultation(
                source=source,
                target=target,
                prompt=query,
                success=success
            )
            
            return response
        except Exception as e:
            print(f"⚠️ Consultation failed: {source} → {target}: {e}")
            
            # Record failed consultation
            if context is None:
                context = {'query_type': 'general', 'depth': depth}
            self.consultation_network.record_consultation(
                source=source,
                target=target,
                prompt=query,
                success=False
            )
            
            return None
    

    def _needs_synthesis(self, query: str) -> bool:
        """
        Determine if query needs multi-brain synthesis
        
        Simple queries → single brain (faster)
        Complex/philosophical queries → synthesis (thorough)
        """
        # Very short queries: single brain is fine
        if len(query.split()) < 10:
            return False
        
        # Philosophical queries: use synthesis
        synthesis_keywords = [
            'what is', 'why', 'how does', 'consciousness', 'meaning', 
            'purpose', 'explain', 'relationship between'
        ]
        query_lower = query.lower()
        if any(kw in query_lower for kw in synthesis_keywords):
            return True
        
        # Default: single brain (faster)
        return False
    
    def respond(
        self,
        query: str,
        preferred_brain: Optional[str] = None,
        multi_brain: bool = False,
        synthesis_mode = 'auto'  # 'auto', True, or False
    ) -> str:
        """
        Generate response to a query
        
        Args:
            query: User query
            preferred_brain: Specific brain to use (optional)
            multi_brain: Whether to use multiple brains (experimental)
            synthesis_mode: Ask all brains then synthesize (requires high gate openness)
        
        Returns:
            Response string
        """
        if not self.brains:
            return "No brains registered in mycelium."
        
        # Synthesis mode - consult all brains, then integrate
        # Auto-detect if synthesis is needed
        if synthesis_mode == 'auto':
            synthesis_mode = self._needs_synthesis(query)
        
        if synthesis_mode:
            return self._synthesize_response(query)
        
        # Single brain mode (with routing)
        if not multi_brain:
            # Choose brain
            if preferred_brain and preferred_brain in self.brains:
                brain = self.brains[preferred_brain]
            else:
                # Route based on confidence scores
                brain = self._route_query(query)
            
            print(f"🔀 Routing to: {brain.name} brain")
            
            # Generate response
            response = brain.generate(query)
            
            return response
        
        # Multi-brain mode (experimental)
        else:
            return self._multi_brain_response(query)
    
    def _route_query(self, query: str) -> Brain:
        """
        Route query to most appropriate brain
        
        Returns:
            Best brain for this query
        """
        if not self.brains:
            raise ValueError("No brains registered")
        
        # Get confidence scores from all brains
        scores = {name: brain.can_handle(query) for name, brain in self.brains.items()}
        
        # Choose brain with highest confidence
        best_brain_name = max(scores, key=scores.get)
        best_score = scores[best_brain_name]
        
        print(f"   Routing scores: {scores}")
        print(f"   Selected: {best_brain_name} (confidence: {best_score:.2f})")
        
        return self.brains[best_brain_name]
    
    def _multi_brain_response(self, query: str) -> str:
        """
        Generate response using multiple brains (experimental)
        
        Each brain responds, then we synthesize.
        """
        print(f"🔀 Multi-brain mode (experimental)")
        
        responses = {}
        for name, brain in self.brains.items():
            confidence = brain.can_handle(query)
            if confidence > 0.2:  # Only activate if somewhat confident
                print(f"   Activating {name} brain (confidence: {confidence:.2f})")
                response = brain.generate(query, max_length=80, with_entanglement=True)
                responses[name] = {
                    "response": response,
                    "confidence": confidence
                }
        
        if not responses:
            # Fallback to first brain
            first_brain = list(self.brains.values())[0]
            return first_brain.generate(query)
        
        # Simple synthesis: weighted by confidence
        # (Could be more sophisticated)
        if len(responses) == 1:
            return list(responses.values())[0]["response"]
        
        # For now, just return highest confidence response
        # TODO: Actual synthesis
        best = max(responses.items(), key=lambda x: x[1]["confidence"])
        synthesis = f"{best[1]['response']}\n\n[Synthesized from {len(responses)} brains: {', '.join(responses.keys())}]"
        
        return synthesis
    
    def _synthesize_response(self, query: str) -> str:
        """
        TRUE SYNTHESIS MODE - The mycelium integrates all brains
        
        1. Ask each brain the same question (sequential - GPU can't truly parallelize)
        2. All responses go into the buffer
        3. Open the gate (mushroom event if needed)
        4. One brain reads from ALL buffers and synthesizes
        
        This is the mycelium acting as integration.
        """
        print("🍄 SYNTHESIS MODE: Consulting all brains...")
        print()
        
        # Step 1: Ask each brain (sequential)
        individual_responses = {}
        for name, brain in self.brains.items():
            print(f"   Asking {name} brain...")
            response = brain.generate(query, max_tokens=100)
            individual_responses[name] = response
            # Response automatically goes into buffer via brain.generate()
        
        print()
        print(f"   Current gate openness: {self.gate.openness():.2f}")
        
        # Step 2: Check if we need a mushroom event for high integration
        if self.gate.openness() < 0.5:
            print("   Gate too closed for synthesis - triggering mushroom event...")
            self.mushroom()
            print(f"   New gate openness: {self.gate.openness():.2f}")
        
        print()
        print("🌊 Synthesizing through the mycelium...")
        
        # Step 3: Build synthesis prompt with all perspectives (keep it concise)
        synthesis_prompt = f"Question: {query}\n\n"
        
        for name, response in individual_responses.items():
            # Keep individual responses short
            short_response = response[:100].strip()
            synthesis_prompt += f"{name}: {short_response}\n"
        
        synthesis_prompt += "\nNow synthesize these perspectives into one unified answer:"
        
        # Step 4: Choose synthesizer (prefer Dream brain for creative integration)
        if "dream" in self.brains:
            synthesizer = self.brains["dream"]
        else:
            synthesizer = list(self.brains.values())[0]
        
        print(f"   Synthesizer: {synthesizer.name} brain (reading from all buffers)")
        print()
        
        # Generate synthesis
        # Note: We use normal generation here - the integration happens through the
        # synthesis prompt itself, not through embedding mixing (which can corrupt output).
        # The buffer and gate are still active for passive entanglement, but synthesis
        # uses the safer prompt-based approach.
        synthesis = synthesizer.generate(
            synthesis_prompt,
            max_tokens=150,
            with_entanglement=False  # Disable embedding mixing for synthesis
        )
        
        return synthesis
    
    def mushroom(self) -> Dict[str, Any]:
        """
        Trigger a mushroom event - deep integration across brains
        
        Returns:
            Dictionary with event results
        """
        import time
        
        # Check cooldown
        now = time.time()
        if now - self.last_mushroom_time < self.mushroom_cooldown_seconds:
            remaining = self.mushroom_cooldown_seconds - (now - self.last_mushroom_time)
            return {
                "success": False,
                "reason": f"Cooldown active. Wait {remaining:.0f}s before next mushroom event."
            }
        
        print("\n" + "="*60)
        print("🍄 MUSHROOM EVENT INITIATED")
        print("="*60)
        
        # Trigger gate opening
        self.gate.mushroom(boost=0.4)
        
        # Collect state from all brains
        brain_states = {}
        for name, brain in self.brains.items():
            brain_states[name] = brain.get_stats()
        
        # Collect buffer state
        buffer_state = self.buffer.stats()
        
        # Collect bus state
        bus_state = self.bus.stats()
        
        # Create dream log
        event_log = {
            "timestamp": time.time(),
            "gate_openness": self.gate.openness(),
            "brains": brain_states,
            "buffer": buffer_state,
            "bus": bus_state,
            "recent_messages": [m.to_dict() for m in self.bus.get_recent(limit=20)]
        }
        
        self.last_mushroom_time = now
        
        print(f"   Gate openness: {self.gate.openness():.2f}")
        print(f"   Active brains: {list(self.brains.keys())}")
        print(f"   Buffer topics: {self.buffer.topics()}")
        print("🍄 Mushroom event complete (will decay over ~40 seconds)")
        print("="*60 + "\n")
        
        return {
            "success": True,
            "event_log": event_log,
            "gate_openness": self.gate.openness()
        }
    
    def start_oscillation(self, period: float = 60.0):
        """Start gate oscillation (integrate/segregate rhythm)"""
        self.gate.start_oscillation(period=period, amplitude=0.2)
    
    def stop_oscillation(self):
        """Stop gate oscillation"""
        self.gate.stop_oscillation()
    
    def status(self) -> Dict[str, Any]:
        """Get current mycelium status"""
        return {
            "brains": {name: brain.stats() for name, brain in self.brains.items()},
            "bus": self.bus.stats(),
            "buffer": self.buffer.stats(),
            "gate": self.gate.stats()
        }
    
    def __repr__(self):
        return f"Mycelium(brains={len(self.brains)}, gate={self.gate.phase()})"
    
    def learn(
        self,
        prompt: str,
        completion: str,
        recommended_brain: str = None,
        metadata: Dict = None,
        learning_rate: float = None,
        save_progress: bool = False
    ) -> Dict[str, float]:
        """
        Learn from a single training example through the mycelium
        
        The ELEGANT way: Training flows through the mycelium just like queries!
        - Microbiome routes to appropriate brain(s)
        - Multiple brains can learn from same example
        - Automatic, intelligent routing
        
        Args:
            prompt: Training prompt
            completion: Expected completion
            recommended_brain: Specific brain to train (optional)
            metadata: Metadata for microbiome routing
            learning_rate: Learning rate for this update
            save_progress: Save adapter after update
        
        Returns:
            Dict mapping brain names to loss values
        """
        if not self.brains:
            print("⚠️ No brains registered in mycelium")
            return {}
        
        print(f"\n🍄 MYCELIUM LEARNING")
        print(f"   Prompt: {prompt[:60]}...")
        print(f"   Completion: {completion[:60]}...")
        
        # Route via microbiome if no specific brain specified
        target_brains = []
        
        if recommended_brain:
            # Use specified brain
            if recommended_brain in self.brains:
                target_brains = [self.brains[recommended_brain]]
                print(f"   🎯 Target: {recommended_brain} (specified)")
            else:
                print(f"   ⚠️ Brain '{recommended_brain}' not found")
                return {}
        else:
            # Route via microbiome!
            try:
                import sys
                sys.path.insert(0, '/Volumes/ThePod')
                from ember.cycles.microbes_extended import MicrobiomeV3Digester
                
                digester = MicrobiomeV3Digester()
                
                # Analyze the full content
                full_content = f"{prompt}\n{completion}"
                result = digester.digest(full_content, metadata or {})
                
                routed_brain = result['recommended_brain']
                confidence = result['confidence']
                
                print(f"   🦠 Microbiome routing:")
                print(f"      → {routed_brain} (confidence: {confidence:.2f})")
                print(f"      → {result['dominant_microbe']} microbe dominant")
                
                if routed_brain in self.brains:
                    target_brains = [self.brains[routed_brain]]
                
                # If high diversity, train multiple brains
                if result.get('microbiome_diversity', 0) > 0.4:
                    print(f"      → High diversity ({result['microbiome_diversity']:.1%})")
                    print(f"      → Training multiple brains!")
                    
                    # Add secondary brains based on microbe votes
                    for microbe_result in result['microbe_results'][:3]:
                        brain_name = microbe_result.recommended_brain
                        if brain_name in self.brains and brain_name != routed_brain:
                            if microbe_result.confidence > 0.3:
                                target_brains.append(self.brains[brain_name])
                                print(f"      → Also training {brain_name} ({microbe_result.confidence:.2f})")
            
            except Exception as e:
                print(f"   ⚠️ Microbiome routing failed: {e}")
                print(f"   ⚠️ Falling back to all brains")
                target_brains = list(self.brains.values())
        
        # If still no target, use all brains
        if not target_brains:
            print(f"   ⚠️ No target determined, using all brains")
            target_brains = list(self.brains.values())
        
        # Train each target brain
        losses = {}
        print(f"\n   📚 Training {len(target_brains)} brain(s)...")
        
        for brain in target_brains:
            loss = brain.learn(
                prompt=prompt,
                completion=completion,
                learning_rate=learning_rate,
                save_progress=save_progress
            )
            losses[brain.name] = loss
            
            if loss < float('inf'):
                print(f"      ✓ {brain.name}: loss={loss:.4f}")
            else:
                print(f"      ⚠ {brain.name}: error")
        
        # Publish summary to bus
        if self.bus:
            self.bus.publish(
                topic='mycelium_learning',
                sender='mycelium',
                content={
                    'brains_trained': list(losses.keys()),
                    'avg_loss': sum(l for l in losses.values() if l < float('inf')) / max(len(losses), 1)
                }
            )
        
        print(f"   ✅ Learning complete\n")
        
        return losses
    
    def learn_from_seed(
        self,
        seed_file: Path,
        batch_size: int = 1,
        save_every: int = 10
    ):
        """
        Learn from a JSONL seed file through the mycelium
        
        Each line should be: {"prompt": "...", "completion": "...", "metadata": {...}}
        
        Args:
            seed_file: Path to JSONL file
            batch_size: Process N examples at a time (default: 1 for online learning)
            save_every: Save adapters every N examples
        """
        import json
        
        seed_file = Path(seed_file)
        
        if not seed_file.exists():
            print(f"❌ Seed file not found: {seed_file}")
            return
        
        print(f"🌱 LEARNING FROM SEED")
        print(f"   File: {seed_file.name}")
        print(f"="*60)
        
        # Load examples
        examples = []
        with open(seed_file) as f:
            for line in f:
                if line.strip():
                    examples.append(json.loads(line))
        
        total = len(examples)
        print(f"\n   📊 Total examples: {total}")
        print(f"   💾 Save every: {save_every} examples")
        print()
        
        # Process each example
        all_losses = []
        
        for i, example in enumerate(examples, 1):
            print(f"[{i}/{total}]", end=" ")
            
            losses = self.learn(
                prompt=example['prompt'],
                completion=example['completion'],
                metadata=example.get('metadata', {}),
                save_progress=(i % save_every == 0)
            )
            
            if losses:
                avg_loss = sum(l for l in losses.values() if l < float('inf')) / max(len(losses), 1)
                all_losses.append(avg_loss)
        
        # Final save
        print(f"\n💾 Saving all adapters...")
        self.save_all_adapters()
        
        # Summary
        if all_losses:
            print(f"\n📊 LEARNING SUMMARY")
            print(f"="*60)
            print(f"   Examples processed: {total}")
            print(f"   Average loss: {sum(all_losses)/len(all_losses):.4f}")
            print(f"   ✅ All brains updated!")
        
        print()
    
    def save_all_adapters(self, suffix: str = None):
        """Save all brain adapters"""
        print(f"💾 Saving all adapters...")
        
        for brain_name, brain in self.brains.items():
            try:
                brain.save_adapter(suffix=suffix)
            except Exception as e:
                print(f"   ⚠️ Error saving {brain_name}: {e}")
        
        print(f"   ✅ Save complete")
    
    def learning_summary(self) -> Dict[str, Any]:
        """Get learning statistics for all brains"""
        summary = {
            'total_brains': len(self.brains),
            'brains': {}
        }
        
        for brain_name, brain in self.brains.items():
            summary['brains'][brain_name] = brain.learning_stats()
        
        return summary

