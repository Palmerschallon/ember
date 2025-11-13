#!/usr/bin/env python3
"""
EMBER UNIFIED STARTUP
Starts Ember orchestrator with Medusa coordination

This is the new entry point that wires everything together:
- Medusa (nervous system)
- Ember Orchestrator (request handler)
- All discovered organisms (capabilities)
"""

import sys
from pathlib import Path

# Add paths
POD_ROOT = Path("/media/palmerschallon/ThePod1")
sys.path.insert(0, str(POD_ROOT))
sys.path.insert(0, str(POD_ROOT / "_archive_old" / "hive"))
sys.path.insert(0, str(POD_ROOT / "_archive_merged" / "_archive_old" / "hive"))

print("="*70)
print("EMBER UNIFIED SYSTEM - MEDUSA COORDINATION")
print("="*70)

# Import Medusa first
from medusa import get_medusa

# Start Medusa
medusa = get_medusa()
print(f"\n✅ Medusa online")
print(f"   Known organisms: {len(medusa.organisms)}")

# Scan and register organisms
print(f"\n🔍 Scanning for organisms...")
from scan_organisms import scan_for_organisms
organisms = scan_for_organisms()
print(f"   Discovered: {len(organisms)} organisms")

# Import and register key organisms with explicit manifests
print(f"\n📦 Loading key organisms...")

# 1. Universal Toolkit (file ops, search, web)
try:
    from ember_toolkit_medusa import EmberToolkit
    toolkit = EmberToolkit()
    print(f"   ✅ ember_toolkit (8 primitives)")
except Exception as e:
    print(f"   ⚠️  ember_toolkit: {e}")

# 2. State Manager (memory, persistence)
try:
    from ember_state import EmberStateManager
    state_mgr = EmberStateManager()
    print(f"   ✅ ember_state_manager (state persistence)")
except Exception as e:
    print(f"   ⚠️  ember_state_manager: {e}")

# 3. Dream Coordinator (background synthesis)
try:
    from combined_dreams import CombinedDreamCoordinator
    dream_coord = CombinedDreamCoordinator()
    print(f"   ✅ combined_dream_coordinator (synthesis)")
except Exception as e:
    print(f"   ⚠️  combined_dream_coordinator: {e}")

# 4. Ember Orchestrator (request routing)
try:
    from ember_organism import EmberOrchestratorOrganism
    orchestrator = EmberOrchestratorOrganism()
    print(f"   ✅ ember_orchestrator (request handler)")
except Exception as e:
    print(f"   ⚠️  ember_orchestrator: {e}")
    # This is critical, so exit if it fails
    print(f"\n❌ CRITICAL: Orchestrator failed to load")
    print(f"   Error: {e}")
    sys.exit(1)

# Show final state
print(f"\n📊 SYSTEM READY")
print(f"   Total organisms: {len(medusa.organisms)}")
print(f"   Registered organisms:")
for name, manifest in list(medusa.organisms.items())[:10]:
    caps = manifest.get('provides', {}).get('capabilities', [])
    cap_count = len(caps) if isinstance(caps, list) else 'unknown'
    print(f"      • {name}: {cap_count} capabilities")

if len(medusa.organisms) > 10:
    print(f"      ... and {len(medusa.organisms) - 10} more")

# Start FastAPI server
print(f"\n🌐 Starting HTTP interface on http://localhost:8080")
print(f"   WebSocket endpoint: ws://localhost:8080/ws")
print()

from ember_v2 import app
import uvicorn

# Store orchestrator in app state for access from endpoints
app.state.orchestrator = orchestrator
app.state.medusa = medusa

uvicorn.run(
    app,
    host="0.0.0.0",
    port=8080,
    log_level="info"
)

