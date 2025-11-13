# Why Tools Aren't Working - ROOT CAUSE FOUND

## Discovery Process

### Test 1: No examples in prompt
**Result**: Model doesn't use `<tool>` format at all. Just hallucinates file list directly.

```
User: List files
Model: > list()
  file1.txt
  file2.txt
  ...
```

### Test 2: Explicit instructions only
**Result**: Model still doesn't use tool format.

### Test 3: Few-shot examples
**Result**: ✓✓✓ Model USES tools correctly!

```
System: 
  Example:
  User: List files
  Assistant: <tool>list()</tool>

User: List the files
Model: <tool>list()</tool>   ✓ WORKS!

User: Read config.txt
Model: <tool>read(path="config.txt")</tool>   ✓ WORKS!

User: Search for neural networks  
Model: <tool>search(query="neural networks")</tool>   ✓ WORKS!
```

### Test 4: Does it hallucinate after </tool>?
**Result**: NO! With few-shot examples, model stops cleanly at `</tool>`.

## THE ROOT CAUSE

**Llama 3.2 3B base model was NOT trained on tool use.**

Without examples, it doesn't know the pattern. 

**WITH few-shot examples in the system prompt, it works perfectly.**

## The Fix

Our system prompt needs few-shot examples:

```python
system_prompt = f"""You are Ember.

Examples of tool use:
User: List files
Assistant: <tool>list()</tool>

User: Read test.txt
Assistant: <tool>read(path="test.txt")</tool>

User: Search for embeddings
Assistant: <tool>search(query="embeddings")</tool>

Your identity:
{identity}

Available tools:
- <tool>list(directory=".")</tool>
- <tool>read(path="filename")</tool>
- <tool>write(path="filename", content="text")</tool>
- <tool>search(query="term")</tool>

Use tools as shown in examples. After using a tool, wait for results.
"""
```

## Why Previous Versions Failed

1. **`ember_chat.py` with LoRA**: LoRA probably wasn't trained well enough OR wasn't trained with the right format
2. **`ember.py`**: No few-shot examples in prompt → model doesn't know the pattern
3. **`ember_with_universal_tools.py`**: Same issue - no examples

## The Solution Is Simple

Add few-shot examples to the system prompt. Model already knows how to follow patterns - we just need to show it the pattern.

## Next Step

Update `ember_with_universal_tools.py` with proper few-shot prompt.

