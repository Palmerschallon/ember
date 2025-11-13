#!/usr/bin/env python3
"""
CAPABILITY SCANNER
Discovers and indexes all working systems on the Pod
Run this ONCE to build the index, then load it on every startup
"""

import json
import ast
from pathlib import Path
from datetime import datetime
from typing import Dict, List

POD_ROOT = Path("/media/palmerschallon/ThePod1")

def extract_docstring(file_path: Path) -> str:
    """Extract module docstring from Python file"""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            tree = ast.parse(content)
            docstring = ast.get_docstring(tree)
            return docstring if docstring else "No description"
    except:
        return "Could not parse"

def scan_python_files() -> Dict:
    """Scan for Python files and extract capabilities"""
    capabilities = {}
    
    # Key directories to scan
    search_paths = [
        POD_ROOT,  # Root level
        POD_ROOT / "_archive_old" / "hive",  # Archived working systems
        POD_ROOT / "essential" / "bookshelves",  # Knowledge base
    ]
    
    for search_path in search_paths:
        if not search_path.exists():
            continue
            
        for py_file in search_path.rglob("*.py"):
            # Skip test files, __pycache__, etc
            if any(skip in str(py_file) for skip in ['__pycache__', '.venv', 'test_', '_test.']):
                continue
            
            rel_path = py_file.relative_to(POD_ROOT)
            docstring = extract_docstring(py_file)
            
            # Extract key info
            name = py_file.stem
            
            # Categorize by keywords
            categories = []
            keywords_lower = (name + docstring).lower()
            
            if any(kw in keywords_lower for kw in ['api', 'fastapi', 'server', 'websocket']):
                categories.append('server')
            if any(kw in keywords_lower for kw in ['orchestrat', 'router', 'coordinate']):
                categories.append('orchestration')
            if any(kw in keywords_lower for kw in ['model', 'load', 'adaptive']):
                categories.append('model_management')
            if any(kw in keywords_lower for kw in ['tool', 'executor', 'file', 'search']):
                categories.append('tools')
            if any(kw in keywords_lower for kw in ['pattern', 'learn', 'memory']):
                categories.append('learning')
            if any(kw in keywords_lower for kw in ['dream', 'daemon', 'autonomous']):
                categories.append('autonomous')
            if any(kw in keywords_lower for kw in ['ui', 'interface', 'html']):
                categories.append('interface')
            
            if not categories:
                categories = ['utility']
            
            capabilities[str(rel_path)] = {
                'name': name,
                'description': docstring[:200],
                'categories': categories,
                'size_kb': py_file.stat().st_size // 1024,
                'last_modified': datetime.fromtimestamp(py_file.stat().st_mtime).isoformat()
            }
    
    return capabilities

def scan_markdown_knowledge() -> Dict:
    """Scan markdown files for documented knowledge"""
    knowledge = {}
    
    bookshelf = POD_ROOT / "essential" / "bookshelves"
    if not bookshelf.exists():
        return knowledge
    
    for md_file in bookshelf.rglob("*.md"):
        rel_path = md_file.relative_to(POD_ROOT)
        
        # Read first few lines for summary
        try:
            with open(md_file, 'r', encoding='utf-8', errors='ignore') as f:
                lines = f.readlines()[:5]
                summary = ' '.join(line.strip() for line in lines if line.strip())[:200]
        except:
            summary = "Could not read"
        
        knowledge[str(rel_path)] = {
            'title': md_file.stem,
            'summary': summary,
            'size_kb': md_file.stat().st_size // 1024,
            'last_modified': datetime.fromtimestamp(md_file.stat().st_mtime).isoformat()
        }
    
    return knowledge

def identify_key_systems(capabilities: Dict) -> Dict:
    """Identify the most important/useful systems"""
    key_systems = {}
    
    # Known important files
    important = {
        'ember_clean.py': 'Current Ember server (FastAPI + WebSocket + Llama 3B)',
        'ember_v2.py': 'New orchestrator-based server',
        'ember_orchestrator_clean.py': 'Request routing and executor management',
        'executors.py': 'Tool and model executors',
        'hardware_detect.py': 'Auto hardware detection and model selection',
        '_archive_old/hive/ember_mycelium.py': 'Original mycelium pattern (EARS → MYCELIUM → LOBES → VOICE)',
        '_archive_old/hive/adaptive_model_loader.py': 'Intelligent model discovery and loading',
        '_archive_old/hive/ember_tools.py': 'Comprehensive toolkit (search, files, RAX patterns)',
        '_archive_old/AUTO_COORDINATE_PATCH.py': 'Auto-detect complex queries and route to 7th lobe',
        'pattern_learner.py': 'Save successful tool chains and patterns',
        'content_mesh.py': 'Semantic search and indexing',
        'spark.py': 'Code generation (DeepSeek)',
        'echo.py': 'Creative synthesis (Qwen)',
    }
    
    for file_path, description in important.items():
        if file_path in capabilities:
            key_systems[file_path] = {
                **capabilities[file_path],
                'importance': 'HIGH',
                'why_important': description
            }
    
    return key_systems

def generate_index():
    """Generate complete capability index"""
    print("="*70)
    print("SCANNING POD CAPABILITIES")
    print("="*70)
    
    print("\n1. Scanning Python files...")
    capabilities = scan_python_files()
    print(f"   Found {len(capabilities)} Python files")
    
    print("\n2. Scanning knowledge base...")
    knowledge = scan_markdown_knowledge()
    print(f"   Found {len(knowledge)} knowledge documents")
    
    print("\n3. Identifying key systems...")
    key_systems = identify_key_systems(capabilities)
    print(f"   Identified {len(key_systems)} key systems")
    
    # Build index
    index = {
        'generated': datetime.now().isoformat(),
        'pod_root': str(POD_ROOT),
        'summary': {
            'total_capabilities': len(capabilities),
            'total_knowledge_docs': len(knowledge),
            'key_systems': len(key_systems)
        },
        'key_systems': key_systems,
        'all_capabilities': capabilities,
        'knowledge_base': knowledge
    }
    
    # Save index
    index_path = POD_ROOT / "CAPABILITIES.json"
    with open(index_path, 'w') as f:
        json.dump(index, f, indent=2)
    
    print(f"\n✅ Index saved to: {index_path}")
    print("="*70)
    
    # Print summary
    print("\nKEY SYSTEMS:")
    for path, info in key_systems.items():
        print(f"\n  {path}")
        print(f"    {info['why_important']}")
    
    return index

if __name__ == "__main__":
    index = generate_index()
    
    print("\n" + "="*70)
    print("CAPABILITY INDEX COMPLETE")
    print("="*70)
    print("\nNext steps:")
    print("1. Review CAPABILITIES.json")
    print("2. Update BOOTSTRAP.md to load this on startup")
    print("3. New AI instances will know what exists!")
    print("="*70)

