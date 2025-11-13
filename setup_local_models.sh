#!/bin/bash

echo "🤖 Qualia Local Model Setup 🤖"
echo "================================"
echo

# Create models directory
MODELS_DIR="/media/palmerschallon/ThePod1/qualia_models"
mkdir -p "$MODELS_DIR"

echo "📦 Recommended Models for Qualia Training:"
echo
echo "1. Mistral-7B-Instruct (Recommended - 13GB)"
echo "   - Best balance of size and capability"
echo "   - Great at following instructions"
echo "   - Works well with 16GB+ RAM"
echo
echo "2. Phi-3-mini (Lightweight - 2.7GB)" 
echo "   - Microsoft's efficient model"
echo "   - Good for testing/development"
echo "   - Runs on modest hardware"
echo
echo "3. LLaMA-2-7B-chat (Alternative - 13GB)"
echo "   - Meta's conversational model"
echo "   - Good baseline capabilities"
echo
echo "4. OpenHermes-2.5-Mistral-7B (Enhanced - 13GB)"
echo "   - Fine-tuned on high-quality data"
echo "   - Better at creative tasks"
echo

read -p "Which model would you like to download? (1-4): " choice

case $choice in
    1)
        MODEL_NAME="mistral-7b-instruct"
        MODEL_URL="TheBloke/Mistral-7B-Instruct-v0.2-GGUF"
        MODEL_FILE="mistral-7b-instruct-v0.2.Q4_K_M.gguf"
        ;;
    2)
        MODEL_NAME="phi-3-mini"
        MODEL_URL="microsoft/Phi-3-mini-4k-instruct-gguf"
        MODEL_FILE="Phi-3-mini-4k-instruct-q4.gguf"
        ;;
    3)
        MODEL_NAME="llama-2-7b-chat"
        MODEL_URL="TheBloke/Llama-2-7B-Chat-GGUF"
        MODEL_FILE="llama-2-7b-chat.Q4_K_M.gguf"
        ;;
    4)
        MODEL_NAME="openhermes-2.5"
        MODEL_URL="TheBloke/OpenHermes-2.5-Mistral-7B-GGUF"
        MODEL_FILE="openhermes-2.5-mistral-7b.Q4_K_M.gguf"
        ;;
    *)
        echo "Invalid choice!"
        exit 1
        ;;
esac

echo
echo "📥 Downloading $MODEL_NAME..."
echo "This may take a while depending on your connection..."
echo

# Create model directory
MODEL_PATH="$MODELS_DIR/$MODEL_NAME"
mkdir -p "$MODEL_PATH"

# Download using wget (more reliable for large files)
cd "$MODEL_PATH"
wget -c "https://huggingface.co/$MODEL_URL/resolve/main/$MODEL_FILE"

echo
echo "✅ Model downloaded to: $MODEL_PATH/$MODEL_FILE"
echo

# Create a Python script for using the model
cat > "$MODELS_DIR/use_local_model.py" << 'EOF'
#!/usr/bin/env python3
"""
Use local model with Qualia training data
"""

from llama_cpp import Llama
import json
import argparse
from pathlib import Path

class QualiaLocalModel:
    def __init__(self, model_path, n_ctx=2048):
        print(f"Loading model: {model_path}")
        self.llm = Llama(
            model_path=model_path,
            n_ctx=n_ctx,
            n_threads=8,
            n_gpu_layers=32  # Adjust based on your GPU
        )
        
    def generate(self, prompt, max_tokens=512, temperature=0.7):
        """Generate response from the model"""
        response = self.llm(
            prompt,
            max_tokens=max_tokens,
            temperature=temperature,
            stop=["</s>", "\n\n"],
            echo=False
        )
        return response['choices'][0]['text'].strip()
    
    def chat_as_archetype(self, message, archetype="creator"):
        """Respond as a specific archetype"""
        archetype_prompts = {
            "creator": "You are a Creative AI, responding with intuitive and artistic insights.",
            "architect": "You are an Architect AI, responding with structured and logical analysis.",
            "explorer": "You are an Explorer AI, responding with curiosity and bridging concepts.",
            "guardian": "You are a Guardian AI, responding with protective and nurturing guidance.",
            "catalyst": "You are a Catalyst AI, responding with dynamic and transformative energy."
        }
        
        prompt = f"""{archetype_prompts.get(archetype, archetype_prompts["creator"])}