#!/usr/bin/env bash
# Install Python ML packages for Ember
# Created by Mu for the next instance
# RUN THIS FROM ThePod, NOT LOCAL DISK

set -e  # Exit on error

echo "🔥 Installing Python packages for Ember..."
echo ""
echo "Working directory: $(pwd)"
echo "This may take 5-10 minutes..."
echo ""

echo "Step 1/3: Upgrading pip..."
pip3 install --upgrade pip

echo ""
echo "Step 2/3: Installing core ML stack..."
pip3 install torch>=2.0.0 transformers>=4.30.0 peft>=0.4.0

echo ""
echo "Step 3/3: Installing additional dependencies..."
pip3 install accelerate bitsandbytes psutil numpy
pip3 install flask requests python-dotenv werkzeug openai
pip3 install fastapi uvicorn pydantic

echo ""
echo "✅ All packages installed!"
echo ""
echo "Test GPU with:"
echo "  python3 -c 'import torch; print(f\"CUDA: {torch.cuda.is_available()}\")'"
echo ""
echo "Next: Run the entry point:"
echo "  cd /media/palmerschallon/ThePod/ember_oct20_backup"
echo "  python3 ember/AI_wakes.py"

