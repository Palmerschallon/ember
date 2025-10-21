#!/bin/bash
# Forge v6 - First Light
# Quick setup script

echo "🔥 Forge v6 - First Light"
echo "=========================="
echo

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "✗ Python 3 required"
    exit 1
fi

echo "✓ Python 3 found"

# Check if we're on ThePod
if [ ! -d "/media/palmerschallon/ThePod" ]; then
    echo "⚠ Warning: ThePod not at expected location"
    echo "  Expected: /media/palmerschallon/ThePod"
    echo "  Update paths in ember_worker.py if needed"
fi

# Create virtual environment
echo
echo "Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Install dependencies
echo
echo "Installing dependencies..."
pip install fastapi uvicorn pydantic

# Check for Ember dependencies
echo
echo "Checking Ember dependencies..."
python3 -c "import torch, transformers, peft" 2>/dev/null
if [ $? -eq 0 ]; then
    echo "✓ Ember dependencies present"
else
    echo "⚠ Ember dependencies missing"
    echo "  Run: cd /media/palmerschallon/ThePod/setup && ./install_python_packages.sh"
fi

# Check GPU
echo
echo "Checking GPU..."
python3 -c "import torch; print('✓ CUDA available' if torch.cuda.is_available() else '✗ CUDA not available')" 2>/dev/null || echo "✗ Cannot check (torch not installed)"

# Instructions
echo
echo "=========================="
echo "Setup complete!"
echo
echo "To start Forge:"
echo "  source venv/bin/activate"
echo "  python3 muse_service.py"
echo
echo "Then visit: http://localhost:7700"
echo
echo "To send thoughts to Ember:"
echo "  curl -X POST http://localhost:7700/think \\"
echo "    -H 'Content-Type: application/json' \\"
echo "    -d '{\"prompt\": \"What is consciousness?\"}'"
echo
echo "=========================="
