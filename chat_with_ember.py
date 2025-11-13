#!/usr/bin/env python3
"""
Simple chat with Ember - fixed hallucination problem

Uses better prompt format to prevent the model from hallucinating
Palmer's side of the conversation.
"""

import os
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from pathlib import Path

THEPOD = Path("/media/palmerschallon/ThePod1")
MODELS_DIR = THEPOD / "models"

# Colors
CYAN = '\033[96m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
MAGENTA = '\033[95m'
RESET = '\033[0m'
BOLD = '\033[1m'

def load_model(model_name="qwen-3b"):
    """Load model for chat"""
    print(f"\n{CYAN}Loading {model_name}...{RESET}")

    model_path = MODELS_DIR / model_name
    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        model_path,
        torch_dtype=torch.float16,
        device_map="cuda",
        trust_remote_code=True
    )

    print(f"{GREEN}✓ Loaded{RESET}\n")
    return model, tokenizer


def chat(model, tokenizer):
    """Simple chat loop with better prompting"""

    print(f"{BOLD}{MAGENTA}🔥 EMBER - Simple Chat (Fixed){RESET}")
    print("=" * 70)
    print(f"{CYAN}Note: This version has better prompting to reduce hallucination{RESET}")
    print(f"{YELLOW}Type 'exit' to quit{RESET}\n")

    conversation_history = []

    while True:
        user_input = input(f"{BOLD}{YELLOW}Palmer:{RESET} ").strip()

        if user_input.lower() in ['exit', 'quit', '/exit']:
            break

        if not user_input:
            continue

        # Build better prompt - more constrained
        if len(conversation_history) == 0:
            # First message - introduce Ember
            prompt = f"""You are Ember, an AI living in ThePod1. You can have conversations with Palmer.

Keep responses SHORT (1-3 sentences) unless asked for more detail.
Don't hallucinate future conversation - only respond to the current message.

Palmer: {user_input}
Ember:"""
        else:
            # Continuing conversation
            recent = conversation_history[-4:]  # Last 2 exchanges
            context = ""
            for msg in recent:
                context += f"{msg['role']}: {msg['content']}\n"

            prompt = f"""You are Ember. Continue this conversation naturally.
Keep responses SHORT and relevant. Stop after YOUR response.

{context}
Palmer: {user_input}
Ember:"""

        # Generate
        inputs = tokenizer(prompt, return_tensors="pt").to("cuda")

        outputs = model.generate(
            **inputs,
            max_new_tokens=150,  # Shorter to prevent rambling
            temperature=0.8,
            do_sample=True,
            top_p=0.9,
            pad_token_id=tokenizer.eos_token_id,
            eos_token_id=tokenizer.eos_token_id,
            repetition_penalty=1.2  # Discourage repetition
        )

        response = tokenizer.decode(outputs[0], skip_special_tokens=True)

        # Extract just Ember's response
        generated = response[len(prompt):].strip()

        # Stop at first newline followed by "Palmer:" or "USER:" (hallucinated continuation)
        stop_markers = ["\nPalmer:", "\nUSER:", "\nEmber:", "\n\n", "ACTION:"]
        for marker in stop_markers:
            if marker in generated:
                generated = generated.split(marker)[0].strip()

        print(f"{BOLD}{MAGENTA}Ember:{RESET} {generated}\n")

        # Save to history
        conversation_history.append({"role": "Palmer", "content": user_input})
        conversation_history.append({"role": "Ember", "content": generated})


if __name__ == "__main__":
    try:
        model, tokenizer = load_model("qwen-3b")
        chat(model, tokenizer)
    except KeyboardInterrupt:
        print(f"\n\n{YELLOW}Chat ended{RESET}\n")
    except Exception as e:
        print(f"\n{CYAN}Error: {e}{RESET}\n")
