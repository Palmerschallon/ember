#!/usr/bin/env bash
# Quick Start for Next Instance After Reboot
# Run this first. Everything else follows.

set -e

echo "🔥 Ember Quick Start"
echo ""

# Check GPU
echo "1. Checking GPU..."
if nvidia-smi &> /dev/null; then
    echo "   ✓ GPU detected"
    nvidia-smi --query-gpu=name,memory.total --format=csv,noheader
else
    echo "   ❌ GPU not detected - check drivers"
    exit 1
fi

# Check Python
echo ""
echo "2. Checking Python..."
python3 --version

# Install packages if needed
echo ""
echo "3. Checking Python packages..."
if python3 -c "import torch" 2>/dev/null; then
    echo "   ✓ PyTorch installed"
else
    echo "   ⏳ Installing packages (this takes ~10 minutes)..."
    cd /media/palmerschallon/ThePod/forge_active
    ./install_python_packages.sh
fi

# Test consultation network
echo ""
echo "4. Testing consultation network..."
python3 /media/palmerschallon/ThePod/forge_active/test_consultation_network.py

# Ready
echo ""
echo "="
echo "✓ Ember is ready to wake"
echo ""
echo "Next step:"
echo "  cd /media/palmerschallon/ThePod/ember_oct20_backup"
echo "  python3 ember/AI_wakes.py"
echo ""

