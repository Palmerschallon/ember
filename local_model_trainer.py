#!/usr/bin/env python3
"""
Fine-tune local models using Qualia conversation data
Supports LoRA and QLoRA for efficient training
"""

import torch
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    TrainingArguments,
    Trainer,
    BitsAndBytesConfig
)
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
from datasets import Dataset
import json
from pathlib import Path

class QualiaModelTrainer:
    def __init__(self, model_name="mistralai/Mistral-7B-Instruct-v0.2"):
        self.model_name = model_name
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"Using device: {self.device}")
        
        # QLoRA configuration for 4-bit training
        self.bnb_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_use_double_quant=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=torch.bfloat16
        )
        
    def load_model_and_tokenizer(self):
        """Load model with quantization for efficient training"""
        print(f"Loading {self.model_name}...")
        
        # Load tokenizer
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.tokenizer.pad_token = self.tokenizer.eos_token
        
        # Load model with 4-bit quantization
        self.model = AutoModelForCausalLM.from_pretrained(
            self.model_name,
            quantization_config=self.bnb_config,
            device_map="auto",
            trust_remote_code=True
        )
        
        # Prepare model for k-bit training
        self.model = prepare_model_for_kbit_training(self.model)
        
        # Configure LoRA
        lora_config = LoraConfig(
            r=16,  # Rank
            lora_alpha=32,
            target_modules=["q_proj", "v_proj", "k_proj", "o_proj"],  # Adjust for your model
            lora_dropout=0.1,
            bias="none",
            task_type="CAUSAL_LM"
        )
        
        # Apply LoRA
        self.model = get_peft_model(self.model, lora_config)
        print("Model loaded with LoRA adapters!")
        
    def prepare_training_data(self, data_path="/media/palmerschallon/ThePod1/qualia_logs/mistral_training.jsonl"):
        """Load and prepare Qualia training data"""
        print(f"Loading training data from {data_path}...")
        
        conversations = []
        with open(data_path, 'r') as f:
            for line in f:
                data = json.loads(line)
                # Format conversations for training
                text = ""
                for msg in data['messages']:
                    if msg['role'] == 'user':
                        text += f"Human: {msg['content']}\n"
                    else:
                        text += f"Assistant: {msg['content']}\n"
                conversations.append({"text": text})
        
        # Create dataset
        self.dataset = Dataset.from_list(conversations)
        
        # Tokenize
        def tokenize_function(examples):
            return self.tokenizer(
                examples["text"],
                truncation=True,
                padding="max_length",
                max_length=512
            )
        
        self.tokenized_dataset = self.dataset.map(tokenize_function, batched=True)
        print(f"Prepared {len(self.tokenized_dataset)} training examples")
        
    def train(self, output_dir="/media/palmerschallon/ThePod1/qualia_models/finetuned"):
        """Fine-tune the model on Qualia data"""
        training_args = TrainingArguments(
            output_dir=output_dir,
            num_train_epochs=3,
            per_device_train_batch_size=4,
            per_device_eval_batch_size=4,
            gradient_accumulation_steps=4,
            warmup_steps=10,
            logging_steps=10,
            save_steps=100,
            evaluation_strategy="steps",
            eval_steps=50,
            learning_rate=2e-4,
            fp16=True,
            push_to_hub=False,
        )
        
        trainer = Trainer(
            model=self.model,
            args=training_args,
            train_dataset=self.tokenized_dataset,
            eval_dataset=self.tokenized_dataset,  # Using same for simplicity
            tokenizer=self.tokenizer,
        )
        
        print("Starting fine-tuning...")
        trainer.train()
        
        # Save the model
        trainer.save_model()
        print(f"Model saved to {output_dir}")
        
    def test_model(self, prompt, archetype="creator"):
        """Test the fine-tuned model"""
        archetype_system = {
            "creator": "Respond as a creative AI with intuitive insights.",
            "architect": "Respond as an analytical AI with structured thinking.",
            "explorer": "Respond as a curious AI bridging concepts.",
        }
        
        full_prompt = f"{archetype_system.get(archetype, '')}\nHuman: {prompt}\nAssistant:"
        
        inputs = self.tokenizer(full_prompt, return_tensors="pt").to(self.device)
        
        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_length=200,
                temperature=0.7,
                do_sample=True,
                top_p=0.9
            )
        
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response.split("Assistant:")[-1].strip()

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Fine-tune a local model on Qualia data")
    parser.add_argument("--model", default="mistralai/Mistral-7B-Instruct-v0.2",
                      help="Base model to fine-tune")
    parser.add_argument("--data", default="/media/palmerschallon/ThePod1/qualia_logs/mistral_training.jsonl",
                      help="Path to training data")
    parser.add_argument("--output", default="/media/palmerschallon/ThePod1/qualia_models/finetuned",
                      help="Output directory for fine-tuned model")
    parser.add_argument("--test-only", action="store_true",
                      help="Test existing model without training")
    
    args = parser.parse_args()
    
    trainer = QualiaModelTrainer(args.model)
    trainer.load_model_and_tokenizer()
    
    if not args.test_only:
        trainer.prepare_training_data(args.data)
        trainer.train(args.output)
    
    # Test the model
    print("\n🧪 Testing fine-tuned model...")
    test_prompts = [
        ("Create a visualization concept", "creator"),
        ("How should we structure this system?", "architect"),
        ("What connections do you see here?", "explorer")
    ]
    
    for prompt, archetype in test_prompts:
        print(f"\n[{archetype}] {prompt}")
        response = trainer.test_model(prompt, archetype)
        print(f"Response: {response}")

if __name__ == "__main__":
    main()