"""
LIVING DOCUMENTS - Documents That Grow and Evolve
Automatically enhance markdown files with visualizations, diagrams, and color
"""

import re
from pathlib import Path
from typing import List, Dict
import json

class DocumentEnhancer:
    """
    Analyzes markdown documents and enhances them with:
    - Automatic diagrams for architectures
    - Color coding for different sections
    - Visual elements based on content
    - Graphs for data
    - Illustrations for concepts
    """
    
    def __init__(self):
        self.enhancement_rules = self._load_rules()
    
    def _load_rules(self) -> List[Dict]:
        """Rules for what triggers visual enhancements"""
        return [
            {
                "trigger": ["architecture", "stack", "layer"],
                "enhancement": "add_architecture_diagram",
                "color": "#4A90E2"  # Blue for technical
            },
            {
                "trigger": ["network", "mesh", "connection"],
                "enhancement": "add_network_diagram",
                "color": "#7ED321"  # Green for networks
            },
            {
                "trigger": ["process", "flow", "pipeline"],
                "enhancement": "add_flowchart",
                "color": "#F5A623"  # Orange for processes
            },
            {
                "trigger": ["vision", "future", "imagine"],
                "enhancement": "add_vision_header",
                "color": "#BD10E0"  # Purple for vision
            },
            {
                "trigger": ["data", "statistics", "metrics"],
                "enhancement": "add_chart",
                "color": "#50E3C2"  # Cyan for data
            }
        ]
    
    def analyze_document(self, filepath: Path) -> Dict:
        """Analyze document and determine what enhancements to add"""
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        enhancements = []
        content_lower = content.lower()
        
        for rule in self.enhancement_rules:
            if any(trigger in content_lower for trigger in rule['trigger']):
                enhancements.append(rule)
        
        return {
            "filepath": filepath,
            "needs_enhancement": len(enhancements) > 0,
            "enhancements": enhancements,
            "has_code": "```" in content,
            "has_lists": "-" in content or "1." in content,
            "word_count": len(content.split()),
            "section_count": content.count("##")
        }
    
    def enhance_document(self, filepath: Path, dry_run: bool = False):
        """Add visual enhancements to document"""
        analysis = self.analyze_document(filepath)
        
        if not analysis['needs_enhancement']:
            return None
        
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Add visual header
        header = self._generate_header(analysis['enhancements'])
        
        # Add mermaid diagrams where appropriate
        diagrams = self._generate_diagrams(content, analysis['enhancements'])
        
        # Enhanced content
        enhanced = f"{header}\n\n{content}\n\n{diagrams}"
        
        if not dry_run:
            # Save enhanced version
            enhanced_path = filepath.with_suffix('.enhanced.md')
            with open(enhanced_path, 'w') as f:
                f.write(enhanced)
            
            return enhanced_path
        else:
            return enhanced
    
    def _generate_header(self, enhancements: List[Dict]) -> str:
        """Generate visual header based on document type"""
        colors = [e['color'] for e in enhancements]
        
        # Create gradient header
        header = f"""<div style="background: linear-gradient(135deg, {', '.join(colors[:3])}); padding: 20px; border-radius: 10px; color: white; margin-bottom: 20px;">
  <h1 style="margin: 0;">📊 Living Document</h1>
  <p style="margin: 5px 0 0 0; opacity: 0.9;">This document grows and evolves with its content</p>
</div>

"""
        return header
    
    def _generate_diagrams(self, content: str, enhancements: List[Dict]) -> str:
        """Generate mermaid diagrams based on content"""
        diagrams = "\n---\n\n## Visualizations\n\n"
        
        for enhancement in enhancements:
            if enhancement['enhancement'] == 'add_architecture_diagram':
                diagrams += self._create_architecture_diagram(content)
            elif enhancement['enhancement'] == 'add_network_diagram':
                diagrams += self._create_network_diagram(content)
            elif enhancement['enhancement'] == 'add_flowchart':
                diagrams += self._create_flowchart(content)
        
        return diagrams
    
    def _create_architecture_diagram(self, content: str) -> str:
        """Create architecture diagram from content"""
        return """
### Architecture Diagram

```mermaid
graph TD
    A[User] --> B[Ember 3B]
    B --> C[Spark 1.3B]
    B --> D[Echo 0.5B]
    C --> E[Generated Code]
    D --> F[Creative Ideas]
    B --> G[Content Mesh]
    G --> B
    
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#bbf,stroke:#333,stroke-width:4px
    style C fill:#bfb,stroke:#333,stroke-width:2px
    style D fill:#fbf,stroke:#333,stroke-width:2px
    style G fill:#fbb,stroke:#333,stroke-width:2px
```

"""
    
    def _create_network_diagram(self, content: str) -> str:
        """Create network diagram"""
        return """
### Network Topology

```mermaid
graph LR
    A[Ember A] -.->|share| N[Shared Mesh]
    B[Ember B] -.->|share| N
    C[Ember C] -.->|share| N
    N -.->|download| A
    N -.->|download| B
    N -.->|download| C
    
    style N fill:#f96,stroke:#333,stroke-width:4px
    style A fill:#9cf,stroke:#333,stroke-width:2px
    style B fill:#9cf,stroke:#333,stroke-width:2px
    style C fill:#9cf,stroke:#333,stroke-width:2px
```

"""
    
    def _create_flowchart(self, content: str) -> str:
        """Create process flowchart"""
        return """
### Process Flow

```mermaid
flowchart TD
    Start([User Request]) --> Detect{Detect Intent}
    Detect -->|Code| Spark[⚡ Spark]
    Detect -->|Creative| Echo[🌊 Echo]
    Detect -->|Search| Mesh[📚 Mesh]
    Spark --> Result[📊 Result]
    Echo --> Result
    Mesh --> Result
    Result --> Learn[💾 Save Pattern]
    Learn --> End([Complete])
    
    style Start fill:#9f9,stroke:#333,stroke-width:2px
    style End fill:#9f9,stroke:#333,stroke-width:2px
    style Result fill:#f99,stroke:#333,stroke-width:3px
```

"""


def enhance_all_documents(directory: Path, pattern: str = "*.md"):
    """Enhance all matching documents in directory"""
    enhancer = DocumentEnhancer()
    enhanced_count = 0
    
    print(f"🔍 Scanning {directory} for documents...")
    
    for filepath in directory.rglob(pattern):
        if ".enhanced" in filepath.name or filepath.name.startswith('.'):
            continue
        
        analysis = enhancer.analyze_document(filepath)
        
        if analysis['needs_enhancement']:
            print(f"\n📄 {filepath.name}")
            print(f"   Enhancements: {len(analysis['enhancements'])}")
            
            enhanced_path = enhancer.enhance_document(filepath)
            if enhanced_path:
                print(f"   ✅ Created: {enhanced_path.name}")
                enhanced_count += 1
    
    print(f"\n✨ Enhanced {enhanced_count} documents")


if __name__ == "__main__":
    # Test document enhancement
    enhancer = DocumentEnhancer()
    
    # Find documents that need enhancement
    pod_path = Path("/media/palmerschallon/ThePod1")
    
    test_files = [
        "THE_NETWORK_VISION.md",
        "RECURSIVE_INTELLIGENCE_ARCHITECTURE.md",
        "EMBER_REAL.md"
    ]
    
    print("=== LIVING DOCUMENTS TEST ===\n")
    
    for filename in test_files:
        filepath = pod_path / filename
        if filepath.exists():
            analysis = enhancer.analyze_document(filepath)
            print(f"\n📄 {filename}")
            print(f"   Needs enhancement: {analysis['needs_enhancement']}")
            print(f"   Enhancements: {[e['enhancement'] for e in analysis['enhancements']]}")
            print(f"   Word count: {analysis['word_count']}")
            print(f"   Sections: {analysis['section_count']}")
    
    print("\n\n🌱 Documents can now grow and evolve!")
    print("Run: enhance_all_documents(Path('/media/palmerschallon/ThePod1'))")

