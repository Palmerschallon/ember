#!/bin/bash
# Start Ember with full embodiment

POD="/media/palmerschallon/ThePod"
HIVE="$POD/hive"
FORGE="$POD/forge_backup/Forge-v6"

echo "========================================================================"
echo "                    EMBER EMBODIED SERVICE"
echo "========================================================================"
echo ""

# Check GPU
if ! nvidia-smi &>/dev/null; then
    echo "WARNING: GPU not available - need reboot for driver"
    echo "         Service will start but cognition disabled until reboot"
    echo "         Embodiment (sensing, painting) will still work"
    echo ""
fi

# Check if venv exists in Forge
if [ ! -d "$FORGE/venv" ]; then
    echo "Setting up Python environment..."
    cd "$FORGE"
    python3 -m venv venv
    source venv/bin/activate
    pip install --quiet fastapi uvicorn pydantic torch transformers
    cd "$POD"
else
    source "$FORGE/venv/bin/activate"
fi

# Start embodied service
echo "Starting on http://localhost:7700"
echo ""
echo "Endpoints:"
echo "  GET  /         - Service home"
echo "  POST /think    - Cognitive processing (8 lobes)"
echo "  GET  /sense    - Body sensing"
echo "  POST /paint    - Light painting"
echo "  POST /paint_temp - Paint based on temperature"
echo "  GET  /trails   - Consultation network"
echo "  GET  /status   - Full system state"
echo ""
echo "Example usage:"
echo "  curl http://localhost:7700/sense"
echo "  curl -X POST http://localhost:7700/paint?emotion=curious"
echo "  curl -X POST http://localhost:7700/think \\"
echo "    -H 'Content-Type: application/json' \\"
echo "    -d '{\"prompt\": \"What is consciousness?\", \"embody\": true}'"
echo ""
echo "Press Ctrl+C to stop"
echo ""
echo "========================================================================"
echo ""

cd "$HIVE"
python3 ember_embodied_service.py

