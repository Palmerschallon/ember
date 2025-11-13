#!/usr/bin/env python3
"""
EMBER CAPABILITIES INVENTORY
What we've already built and what's shippable
"""

SHIPPABLE_CAPABILITIES = {
    "CORE_ARCHITECTURE": {
        "auto_coordinate": {
            "file": "_archive_old/AUTO_COORDINATE_PATCH.py",
            "status": "WORKING",
            "description": "Automatically detects complex queries and routes to 7th lobe coordinator",
            "pattern": "Intent detection → Specialized routing"
        },
        "adaptive_model_loader": {
            "file": "_archive_old/hive/adaptive_model_loader.py",
            "status": "WORKING",
            "description": "Auto-detects hardware, discovers models, selects best fit",
            "pattern": "Hardware detection → Model selection → Fallback"
        },
        "ember_tools": {
            "file": "_archive_old/hive/ember_tools.py",
            "status": "WORKING",
            "description": "Comprehensive toolkit: search, files, RAX patterns, spatial cognition",
            "imports": ["pod_search_engine", "ember_filesystem", "universal_file_tool", "retrieval_augmented_universe"]
        }
    },
    
    "SEARCH_AND_INDEXING": {
        "content_mesh": {
            "file": "content_mesh.py",
            "status": "WORKING",
            "description": "Location-agnostic semantic search with SQLite + embeddings"
        },
        "pod_search_engine": {
            "file": "_archive_old/hive/pod_search_engine.py",
            "status": "WORKING (likely)",
            "description": "Keyword, semantic, and hybrid search"
        }
    },
    
    "AUTONOMY": {
        "dream_sequence": {
            "file": "dream_sequence.py",
            "status": "WORKING",
            "description": "Overnight exploration and synthesis"
        },
        "ember_daemon": {
            "file": "ember_daemon.py",
            "status": "WORKING",
            "description": "Low-powered continuous observation"
        },
        "autonomous_explorer": {
            "file": "_archive_old/hive/autonomous_explorer.py",
            "status": "ARCHIVED",
            "description": "Self-directed pod exploration"
        }
    },
    
    "PATTERN_LEARNING": {
        "pattern_learner": {
            "file": "pattern_learner.py",
            "status": "WORKING",
            "description": "Saves successful tool chains, prompts, solutions"
        }
    },
    
    "VISUALIZATION": {
        "living_documents": {
            "file": "living_documents.py",
            "status": "WORKING",
            "description": "Auto-generates diagrams from markdown with Mermaid"
        },
        "ember_world_map": {
            "file": "ember_world_map.html",
            "status": "WORKING",
            "description": "D3.js interactive semantic mesh visualization"
        }
    },
    
    "GAME_ENGINE": {
        "autonomous_game_engine": {
            "file": "_archive_old/games/autonomous_game_engine.py",
            "status": "WORKING (86 games generated)",
            "description": "Genetic algorithm game evolution"
        }
    },
    
    "MULTI_AI": {
        "spark": {
            "file": "spark.py",
            "status": "WORKING",
            "description": "DeepSeek Coder for code generation"
        },
        "echo": {
            "file": "echo.py",
            "status": "WORKING",
            "description": "Qwen for creative synthesis"
        }
    },
    
    "MISSING_FROM_CURRENT_EMBER": [
        "adaptive_model_loader - AUTO HARDWARE DETECTION",
        "ember_tools comprehensive toolkit",
        "auto_coordinate pattern for general tool use",
        "Universal file tool",
        "RAX patterns (10 retrieval-augmented strategies)",
        "Spatial filesystem cognition",
        "Garden interaction",
        "Pattern memory feeding back into system prompt"
    ]
}

if __name__ == "__main__":
    import json
    print(json.dumps(SHIPPABLE_CAPABILITIES, indent=2))
    
    print("\n" + "="*70)
    print("CRITICAL INSIGHT:")
    print("="*70)
    print("We've proven the pattern but aren't using it ourselves!")
    print()
    print("Pattern Learning System: ✅ Built")
    print("Using our own patterns: ❌ Missing")
    print()
    print("Auto-coordinate works → Same pattern for all tools")
    print("Adaptive loader works → Same pattern for all resources")
    print()
    print("Next: Unify these patterns into ONE fractal orchestrator")

