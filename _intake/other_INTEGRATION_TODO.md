
# Integration TODOs (after models download)

## 1. Update ember_brain_service.py
```python
from hive.hardware_probe import get_current_mode

mode = get_current_mode()  # POCKET, FIELD, or FORGE
if mode == 'POCKET':
    model_path = '/models/ember/pocket/qwen2.5-coder-0.5b-instruct-q4_k_m.gguf'
elif mode == 'FIELD':
    model_path = '/models/ember/field/qwen2.5-coder-1.5b-instruct-q4_k_m.gguf'
else:  # FORGE
    model_path = '/models/ember/forge/qwen2.5-coder-3b-instruct'
```

## 2. Create model switcher
Script to hot-swap models when hardware changes (phone→laptop→serval)

## 3. LoRA compatibility matrix
Test which rank-192 LoRAs work with each model size
Plan: All new LoRAs at rank-16 for universal compatibility

## 4. MycelialRouter integration
Connect to EmberVerse chat for depth-N conversations

## 5. Fractal training pipeline
Implement Romanesco growth algorithm
