"""
ECHO - The Creative Synthesis Layer
Weaves patterns, makes unexpected connections, thinks laterally.
"""

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from pathlib import Path

class Echo:
    """
    Echo is Ember's creative synthesis engine.
    
    Uses Qwen 0.5B for fast, creative pattern weaving.
    When Spark gets stuck, Echo suggests unexpected approaches.
    """
    
    def __init__(self, model_path: str = "/media/palmerschallon/ThePod1/models/echo"):
        """Initialize Echo with the Qwen 0.5B model"""
        print("🌊 Initializing Echo (creative synthesis layer)...")
        
        self.model_path = Path(model_path)
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        
        print(f"   Loading tokenizer from {model_path}...")
        self.tokenizer = AutoTokenizer.from_pretrained(
            model_path,
            trust_remote_code=True
        )
        
        print(f"   Loading model on {self.device}...")
        self.model = AutoModelForCausalLM.from_pretrained(
            model_path,
            torch_dtype=torch.float16 if self.device == "cuda" else torch.float32,
            device_map="auto",
            trust_remote_code=True
        )
        
        print("🌊 Echo ready to weave patterns!")
    
    def synthesize(self, problem: str, context: str = "", constraints: list = None) -> list:
        """
        Generate creative approaches to a problem.
        
        Args:
            problem: The problem to solve
            context: Additional context
            constraints: List of constraints or attempted approaches
            
        Returns:
            List of creative ideas/approaches
        """
        constraints_text = ""
        if constraints:
            constraints_text = f"\n\nWhat hasn't worked or constraints:\n" + "\n".join(f"- {c}" for c in constraints)
        
        prompt = f"""Think creatively and laterally. What if we approached this completely differently?

Problem: {problem}

{f'Context: {context}' if context else ''}{constraints_text}

Let's think outside the box. What if...

1."""
        
        # Tokenize
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.device)
        
        # Generate with higher temperature for creativity
        print(f"🌊 Echo synthesizing creative approaches...")
        outputs = self.model.generate(
            **inputs,
            max_new_tokens=400,
            temperature=0.9,  # High temperature for creativity
            do_sample=True,
            top_p=0.95,
            top_k=50,
            pad_token_id=self.tokenizer.eos_token_id
        )
        
        # Decode
        result = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        # Extract ideas (everything after "What if...")
        ideas_text = result.split("What if...")[-1].strip()
        
        # Split into individual ideas (numbered list)
        ideas = []
        for line in ideas_text.split('\n'):
            line = line.strip()
            if line and (line[0].isdigit() or line.startswith('-')):
                # Remove number/bullet
                idea = line.lstrip('0123456789.-) ').strip()
                if idea:
                    ideas.append(idea)
        
        return ideas if ideas else [ideas_text]
    
    def blend_concepts(self, concept_a: str, concept_b: str) -> str:
        """
        Weave two disparate concepts together.
        
        Args:
            concept_a: First concept
            concept_b: Second concept
            
        Returns:
            Synthesis/blend of the concepts
        """
        prompt = f"""Creatively blend these two concepts together. Find the unexpected connection.

Concept A: {concept_a}
Concept B: {concept_b}

What if we combined them? The synthesis is:"""
        
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.device)
        
        print(f"🌊 Echo blending '{concept_a}' + '{concept_b}'...")
        outputs = self.model.generate(
            **inputs,
            max_new_tokens=300,
            temperature=0.85,
            do_sample=True,
            pad_token_id=self.tokenizer.eos_token_id
        )
        
        result = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        synthesis = result.split("synthesis is:")[-1].strip()
        
        return synthesis
    
    def metaphor(self, concept: str, domain: str = "nature") -> str:
        """
        Generate a metaphor for a concept.
        
        Args:
            concept: The concept to metaphorize
            domain: Domain for the metaphor (nature, music, architecture, etc)
            
        Returns:
            Metaphor as a string
        """
        prompt = f"""Create a vivid metaphor for this concept using imagery from {domain}.

Concept: {concept}

The metaphor: {concept} is like"""
        
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.device)
        
        outputs = self.model.generate(
            **inputs,
            max_new_tokens=200,
            temperature=0.9,
            do_sample=True,
            pad_token_id=self.tokenizer.eos_token_id
        )
        
        result = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        metaphor = result.split("is like")[-1].strip()
        
        return f"{concept} is like {metaphor}"
    
    def lateral_thinking(self, stuck_on: str, goal: str) -> list:
        """
        Suggest lateral thinking approaches when stuck.
        
        Args:
            stuck_on: What you're stuck on
            goal: What you're trying to achieve
            
        Returns:
            List of lateral thinking suggestions
        """
        prompt = f"""You're stuck. Let's think laterally. What are unconventional approaches?

Stuck on: {stuck_on}
Trying to achieve: {goal}

Instead of the obvious approach, what if we:

1."""
        
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.device)
        
        print(f"🌊 Echo thinking laterally...")
        outputs = self.model.generate(
            **inputs,
            max_new_tokens=400,
            temperature=0.95,  # Very high for lateral thinking
            do_sample=True,
            top_p=0.9,
            pad_token_id=self.tokenizer.eos_token_id
        )
        
        result = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        suggestions_text = result.split("what if we:")[-1].strip()
        
        # Parse suggestions
        suggestions = []
        for line in suggestions_text.split('\n'):
            line = line.strip()
            if line and (line[0].isdigit() or line.startswith('-')):
                suggestion = line.lstrip('0123456789.-) ').strip()
                if suggestion:
                    suggestions.append(suggestion)
        
        return suggestions if suggestions else [suggestions_text]
    
    def remix(self, elements: list) -> str:
        """
        Remix multiple elements into something new.
        
        Args:
            elements: List of elements to remix
            
        Returns:
            Remixed creation
        """
        elements_text = "\n".join(f"- {e}" for e in elements)
        
        prompt = f"""Take these elements and remix them into something unexpected and new:

Elements:
{elements_text}

The remix:"""
        
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.device)
        
        print(f"🌊 Echo remixing {len(elements)} elements...")
        outputs = self.model.generate(
            **inputs,
            max_new_tokens=350,
            temperature=0.95,
            do_sample=True,
            pad_token_id=self.tokenizer.eos_token_id
        )
        
        result = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        remix = result.split("remix:")[-1].strip()
        
        return remix
    
    def unload(self):
        """Unload model from memory to free VRAM"""
        print("🌊 Unloading Echo...")
        del self.model
        del self.tokenizer
        torch.cuda.empty_cache()
        print("🌊 Echo unloaded")


# Test Echo independently
if __name__ == "__main__":
    print("=" * 70)
    print("ECHO TEST - Creative Synthesis Layer")
    print("=" * 70)
    
    # Initialize
    echo = Echo()
    
    # Test 1: Creative approaches
    print("\n[TEST 1] Creative approaches to visualization")
    print("-" * 70)
    ideas = echo.synthesize(
        problem="Create an engaging visualization of file relationships",
        constraints=["Force-directed graphs are boring", "Tree layouts feel static"]
    )
    for i, idea in enumerate(ideas, 1):
        print(f"{i}. {idea}")
    
    # Test 2: Blend concepts
    print("\n[TEST 2] Blend disparate concepts")
    print("-" * 70)
    synthesis = echo.blend_concepts("neural networks", "mycelium networks")
    print(synthesis)
    
    # Test 3: Metaphor
    print("\n[TEST 3] Generate metaphor")
    print("-" * 70)
    metaphor = echo.metaphor("consciousness", domain="water")
    print(metaphor)
    
    # Test 4: Lateral thinking
    print("\n[TEST 4] Lateral thinking when stuck")
    print("-" * 70)
    suggestions = echo.lateral_thinking(
        stuck_on="Tool execution keeps hallucinating",
        goal="Reliable tool use without hallucination"
    )
    for i, suggestion in enumerate(suggestions, 1):
        print(f"{i}. {suggestion}")
    
    # Test 5: Remix
    print("\n[TEST 5] Remix elements")
    print("-" * 70)
    remix = echo.remix([
        "semantic search",
        "visual storytelling",
        "music generation",
        "file organization"
    ])
    print(remix)
    
    print("\n" + "=" * 70)
    print("🌊 Echo test complete!")
    print("=" * 70)

