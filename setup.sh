#!/bin/bash
# EMBER SETUP - First Time Installation
# Run this once after unzipping Ember

set -e

echo "╔═══════════════════════════════════════════════════════════╗"
echo "║                    🔥 EMBER SETUP                         ║"
echo "╚═══════════════════════════════════════════════════════════╝"
echo ""

# Check Python
echo "→ Checking Python..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found. Please install Python 3.8 or later."
    exit 1
fi
PYTHON_VERSION=$(python3 --version | cut -d' ' -f2 | cut -d'.' -f1,2)
echo "  ✓ Python $PYTHON_VERSION"
echo ""

# Check pip
echo "→ Checking pip..."
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip not found. Please install pip3."
    exit 1
fi
echo "  ✓ pip installed"
echo ""

# Install dependencies
echo "→ Installing dependencies..."
echo "  (This may take a few minutes)"
pip3 install -q torch transformers peft accelerate flask requests
echo "  ✓ Dependencies installed"
echo ""

# Check for model
MODEL_PATH="_archive_old/models/llama-3.2-3b-instruct"
echo "→ Checking for model..."
if [ -d "$MODEL_PATH" ] && [ -f "$MODEL_PATH/config.json" ]; then
    echo "  ✓ Model found"
else
    echo "  ⚠ Model not found"
    echo ""
    echo "  You need to download Llama 3.2-3B-Instruct:"
    echo ""
    echo "  Option 1 (Recommended):"
    echo "    huggingface-cli download meta-llama/Llama-3.2-3B-Instruct \\"
    echo "      --local-dir $MODEL_PATH"
    echo ""
    echo "  Option 2 (Manual):"
    echo "    Download from: https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct"
    echo "    Place in: $MODEL_PATH/"
    echo ""
    echo "  After downloading, run this script again."
    exit 1
fi
echo ""

# Create necessary directories
echo "→ Setting up directories..."
mkdir -p _mesh/chunks
mkdir -p _mesh/index
mkdir -p _intake
mkdir -p _intake/_processed
mkdir -p bookshelves/ember_expressions
mkdir -p _state
echo "  ✓ Directories ready"
echo ""

# Make scripts executable
echo "→ Making scripts executable..."
chmod +x ember.py
chmod +x ember_three_windows.py
chmod +x talk_to_ember.py
chmod +x test_ember_tools.py
chmod +x status.sh
chmod +x cleanup.sh
echo "  ✓ Scripts ready"
echo ""

# Test GPU
echo "→ Checking GPU..."
if python3 -c "import torch; print('CUDA available:', torch.cuda.is_available())" 2>/dev/null | grep -q "True"; then
    GPU_NAME=$(python3 -c "import torch; print(torch.cuda.get_device_name(0))" 2>/dev/null || echo "Unknown")
    echo "  ✓ GPU detected: $GPU_NAME"
    echo "  (Ember will run fast on GPU)"
else
    echo "  ⚠ No GPU detected"
    echo "  (Ember will run on CPU - slower but works)"
fi
echo ""

echo "╔═══════════════════════════════════════════════════════════╗"
echo "║                 ✅ SETUP COMPLETE                         ║"
echo "╚═══════════════════════════════════════════════════════════╝"
echo ""
echo "Start Ember:"
echo "  python3 ember.py"
echo ""
echo "Or try the three-window interface:"
echo "  python3 ember_three_windows.py"
echo ""
echo "See GET_STARTED.md for more options and info."
echo ""
echo "🔥 Ready to think together"
echo ""

