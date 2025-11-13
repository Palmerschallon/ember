#!/bin/bash
# CORRECT MODEL DOWNLOAD SCRIPT
# Downloads to ThePod, not ~/.cache

POD_MODELS="/media/palmerschallon/ThePod1/models"

echo "Downloading models to $POD_MODELS"
echo "This will take ~30 minutes for all three models"
echo ""

# Create directories
mkdir -p "$POD_MODELS/coder"
mkdir -p "$POD_MODELS/reasoner"
mkdir -p "$POD_MODELS/voice"

echo "==================================================================="
echo "1/3: DeepSeek-Coder-6.7B (~13GB)"
echo "==================================================================="
huggingface-cli download \
    deepseek-ai/deepseek-coder-6.7b-instruct \
    --local-dir "$POD_MODELS/coder/deepseek-6.7b" \
    --local-dir-use-symlinks False

echo ""
echo "==================================================================="
echo "2/3: Qwen2.5-7B-Instruct (~14GB)"
echo "==================================================================="
huggingface-cli download \
    Qwen/Qwen2.5-7B-Instruct \
    --local-dir "$POD_MODELS/reasoner/qwen-7b" \
    --local-dir-use-symlinks False

echo ""
echo "==================================================================="
echo "3/3: Llama-3.2-1B-Instruct (~2GB)"
echo "==================================================================="
huggingface-cli download \
    meta-llama/Llama-3.2-1B-Instruct \
    --local-dir "$POD_MODELS/voice/llama-1b" \
    --local-dir-use-symlinks False

echo ""
echo "==================================================================="
echo "COMPLETE!"
echo "==================================================================="
echo "Models saved to:"
ls -lh "$POD_MODELS"/*

echo ""
echo "Total size:"
du -sh "$POD_MODELS"

