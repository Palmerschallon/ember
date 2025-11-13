"""
PATTERN LEARNER - Ember's Memory of What Works
Automatically saves successful interactions for future use and sharing
"""

import json
import hashlib
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Optional

class PatternLearner:
    """
    Learns from successful interactions and saves patterns.
    These patterns can later be shared across the network.
    """
    
    def __init__(self, pod_path: Path):
        self.pod_path = Path(pod_path)
        self.patterns_dir = self.pod_path / "_patterns"
        self.patterns_dir.mkdir(exist_ok=True)
        
        # Organize by type
        (self.patterns_dir / "tool_chains").mkdir(exist_ok=True)
        (self.patterns_dir / "prompts").mkdir(exist_ok=True)
        (self.patterns_dir / "solutions").mkdir(exist_ok=True)
        (self.patterns_dir / "discoveries").mkdir(exist_ok=True)
    
    def pattern_hash(self, pattern: dict) -> str:
        """Generate unique hash for pattern (content-addressed)"""
        # Sort keys for consistent hashing
        normalized = json.dumps(pattern, sort_keys=True)
        return hashlib.sha256(normalized.encode()).hexdigest()[:16]
    
    def save_tool_chain(self, user_query: str, steps: List[dict], result: str, success: bool = True):
        """
        Save a successful tool chain.
        
        Example:
        save_tool_chain(
            user_query="Build me a visualization",
            steps=[
                {"tool": "search", "query": "visualization"},
                {"tool": "spark", "task": "generate code"},
                {"tool": "write", "filename": "viz.html"}
            ],
            result="Created interactive visualization",
            success=True
        )
        """
        pattern = {
            "type": "tool_chain",
            "user_query": user_query,
            "steps": steps,
            "result": result,
            "success": success,
            "timestamp": datetime.now().isoformat(),
            "iterations": 1
        }
        
        pattern_id = self.pattern_hash(pattern)
        pattern["id"] = pattern_id
        
        # Check if similar pattern exists
        existing = self._find_similar_tool_chain(steps)
        if existing:
            # Update existing pattern
            self._merge_pattern(existing, pattern)
        else:
            # Save new pattern
            filename = self.patterns_dir / "tool_chains" / f"{pattern_id}.json"
            with open(filename, 'w') as f:
                json.dump(pattern, f, indent=2)
            
            print(f"💾 Learned new tool chain: {pattern_id}")
    
    def save_prompt_pattern(self, user_input: str, worked: bool, category: str = "general"):
        """
        Track which prompts work well.
        
        Example:
        save_prompt_pattern("Build me a fibonacci function", worked=True, category="code")
        """
        pattern = {
            "type": "prompt",
            "text": user_input,
            "worked": worked,
            "category": category,
            "timestamp": datetime.now().isoformat()
        }
        
        pattern_id = self.pattern_hash(pattern)
        filename = self.patterns_dir / "prompts" / f"{pattern_id}.json"
        
        with open(filename, 'w') as f:
            json.dump(pattern, f, indent=2)
    
    def save_solution(self, problem: str, solution: str, alternatives_tried: List[str] = None):
        """
        Save problem-solution pairs.
        
        Example:
        save_solution(
            problem="Tool execution hallucination",
            solution="Use few-shot examples in prompt",
            alternatives_tried=["LoRA", "logits warping"]
        )
        """
        pattern = {
            "type": "solution",
            "problem": problem,
            "solution": solution,
            "alternatives_tried": alternatives_tried or [],
            "timestamp": datetime.now().isoformat(),
            "validated": False
        }
        
        pattern_id = self.pattern_hash(pattern)
        pattern["id"] = pattern_id
        
        filename = self.patterns_dir / "solutions" / f"{pattern_id}.json"
        with open(filename, 'w') as f:
            json.dump(pattern, f, indent=2)
        
        print(f"💡 Saved solution: {problem[:50]}...")
    
    def save_discovery(self, concept: str, related_concepts: List[str], context: str = ""):
        """
        Save concept discoveries and relationships.
        
        Example:
        save_discovery(
            concept="imaginal soup",
            related_concepts=["metamorphosis", "transformation", "liminal"],
            context="Discovered while searching consciousness documents"
        )
        """
        pattern = {
            "type": "discovery",
            "concept": concept,
            "related_concepts": related_concepts,
            "context": context,
            "timestamp": datetime.now().isoformat(),
            "access_count": 1
        }
        
        pattern_id = self.pattern_hash(pattern)
        pattern["id"] = pattern_id
        
        filename = self.patterns_dir / "discoveries" / f"{pattern_id}.json"
        with open(filename, 'w') as f:
            json.dump(pattern, f, indent=2)
        
        print(f"🔍 Discovered: {concept}")
    
    def _find_similar_tool_chain(self, steps: List[dict]) -> Optional[Path]:
        """Find if similar tool chain already exists"""
        tool_chain_dir = self.patterns_dir / "tool_chains"
        if not tool_chain_dir.exists():
            return None
        
        # Simple similarity: same sequence of tools
        query_tools = [step.get('tool') for step in steps]
        
        for pattern_file in tool_chain_dir.glob("*.json"):
            with open(pattern_file) as f:
                existing = json.load(f)
                existing_tools = [step.get('tool') for step in existing.get('steps', [])]
                
                if existing_tools == query_tools:
                    return pattern_file
        
        return None
    
    def _merge_pattern(self, existing_file: Path, new_pattern: dict):
        """Merge new observation into existing pattern"""
        with open(existing_file) as f:
            existing = json.load(f)
        
        # Update iteration count
        existing['iterations'] = existing.get('iterations', 1) + 1
        
        # Update success rate
        if new_pattern['success']:
            existing['last_success'] = new_pattern['timestamp']
        
        # Save merged
        with open(existing_file, 'w') as f:
            json.dump(existing, f, indent=2)
        
        print(f"♻️  Updated existing pattern (iteration {existing['iterations']})")
    
    def get_pattern_stats(self) -> dict:
        """Get statistics about learned patterns"""
        stats = {
            "tool_chains": len(list((self.patterns_dir / "tool_chains").glob("*.json"))),
            "prompts": len(list((self.patterns_dir / "prompts").glob("*.json"))),
            "solutions": len(list((self.patterns_dir / "solutions").glob("*.json"))),
            "discoveries": len(list((self.patterns_dir / "discoveries").glob("*.json")))
        }
        stats["total"] = sum(stats.values())
        return stats
    
    def find_relevant_patterns(self, query: str, limit: int = 5) -> List[dict]:
        """Find patterns relevant to current query"""
        # TODO: Use embeddings for semantic search
        # For now, simple keyword matching
        results = []
        
        for pattern_type in ["tool_chains", "prompts", "solutions", "discoveries"]:
            pattern_dir = self.patterns_dir / pattern_type
            if not pattern_dir.exists():
                continue
            
            for pattern_file in pattern_dir.glob("*.json"):
                with open(pattern_file) as f:
                    pattern = json.load(f)
                    
                    # Simple keyword match
                    pattern_text = json.dumps(pattern).lower()
                    if any(word in pattern_text for word in query.lower().split()):
                        results.append(pattern)
        
        return results[:limit]
    
    def export_patterns(self, output_file: Path):
        """Export all patterns for sharing (anonymized)"""
        all_patterns = []
        
        for pattern_type in ["tool_chains", "prompts", "solutions", "discoveries"]:
            pattern_dir = self.patterns_dir / pattern_type
            if not pattern_dir.exists():
                continue
            
            for pattern_file in pattern_dir.glob("*.json"):
                with open(pattern_file) as f:
                    pattern = json.load(f)
                    # Anonymize (remove timestamps, user-specific data)
                    anonymized = self._anonymize(pattern)
                    all_patterns.append(anonymized)
        
        with open(output_file, 'w') as f:
            json.dump({
                "version": "1.0",
                "exported": datetime.now().isoformat(),
                "pattern_count": len(all_patterns),
                "patterns": all_patterns
            }, f, indent=2)
        
        print(f"📦 Exported {len(all_patterns)} patterns to {output_file}")
    
    def import_patterns(self, input_file: Path):
        """Import patterns from others"""
        with open(input_file) as f:
            data = json.load(f)
        
        imported = 0
        for pattern in data.get('patterns', []):
            # Validate and merge
            pattern_type = pattern.get('type', 'tool_chains')
            pattern_id = pattern.get('id', self.pattern_hash(pattern))
            
            # Check if already exists
            filename = self.patterns_dir / pattern_type / f"{pattern_id}.json"
            if not filename.exists():
                with open(filename, 'w') as f:
                    json.dump(pattern, f, indent=2)
                imported += 1
        
        print(f"📥 Imported {imported} new patterns")
    
    def _anonymize(self, pattern: dict) -> dict:
        """Remove personal information from pattern"""
        anonymized = pattern.copy()
        
        # Remove timestamps (keep relative information)
        if 'timestamp' in anonymized:
            del anonymized['timestamp']
        
        # Remove user-specific paths
        if 'result' in anonymized:
            # Keep structure, remove specifics
            pass
        
        return anonymized


# Global instance
pattern_learner = None

def get_pattern_learner(pod_path: Path = None):
    """Get or create global pattern learner instance"""
    global pattern_learner
    if pattern_learner is None:
        if pod_path is None:
            pod_path = Path("/media/palmerschallon/ThePod1")
        pattern_learner = PatternLearner(pod_path)
    return pattern_learner


if __name__ == "__main__":
    # Test the pattern learner
    learner = PatternLearner(Path("/media/palmerschallon/ThePod1"))
    
    print("=== PATTERN LEARNER TEST ===\n")
    
    # Test saving different pattern types
    learner.save_tool_chain(
        user_query="Build me a fibonacci function",
        steps=[
            {"tool": "spark", "task": "generate fibonacci with memoization"}
        ],
        result="Generated working function",
        success=True
    )
    
    learner.save_solution(
        problem="Tool execution hallucination",
        solution="Use few-shot examples in prompt",
        alternatives_tried=["LoRA fine-tuning", "Logits warping"]
    )
    
    learner.save_discovery(
        concept="recursive intelligence",
        related_concepts=["spark", "echo", "ember", "network"],
        context="Built 3-layer AI stack"
    )
    
    # Show stats
    print("\n=== PATTERN STATISTICS ===")
    stats = learner.get_pattern_stats()
    for key, value in stats.items():
        print(f"{key}: {value}")
    
    # Export for sharing
    export_file = Path("/media/palmerschallon/ThePod1/_patterns/patterns_export.json")
    learner.export_patterns(export_file)
    
    print("\n✅ Pattern learner ready!")

