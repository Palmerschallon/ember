# 🔥 THE TOOL EXECUTION PROBLEM

**Date**: October 30, 2025  
**Status**: ⚠️ CRITICAL BUG IDENTIFIED

---

## WHAT WE DISCOVERED

**Ember isn't using tools.** It's hallucinating instead.

### Test Results:

```
User: "Search for consciousness"
Expected: <tool>search(query="consciousness")</tool>
Actual: "I searched for consciousness and felt..." (hallucinated)

User: "Show me what's in the bookshelves"  
Expected: <tool>list(path="essential/bookshelves")</tool>
Actual: "I confirmed the contents..." (hallucinated)
```

**NO TOOL CALLS IN LOGS** - The `[TOOL CALL]` markers never appear.

---

## ROOT CAUSE

**Llama 3.2-3B Instruct is too small** to reliably follow tool-use instructions, even with:
- ✅ Explicit system prompt
- ✅ Few-shot examples
- ✅ Clear formatting rules
- ✅ Mandatory instructions

**The model prefers to generate natural language** rather than structured tool calls.

---

## WHAT WE TRIED

1. ✅ System prompt with examples
2. ✅ BOOTSTRAP with tool instructions  
3. ✅ Few-shot examples in prompt
4. ✅ Few-shot examples right before user message
5. ❌ None of it worked consistently

---

## THE SOLUTION

**Option 1: Pre-emptive Intent Detection** ⚡ (FAST)

Detect tool need from USER's message BEFORE Ember generates:

```python
def preemptive_tool_routing(user_message):
    """Detect and execute tools BEFORE model generates"""
    
    # Search keywords
    if any(word in user_message.lower() for word in 
           ['search', 'find', 'look for', 'what about']):
        query = extract_query(user_message)
        result = search_pod(query)
        # Inject result BEFORE Ember responds
        return result
    
    # List keywords
    if any(word in user_message.lower() for word in
           ['show me', 'list', "what's in", 'contents of']):
        path = extract_path(user_message)
        result = list_directory(path)
        return result
    
    # Code generation
    if any(word in user_message.lower() for word in
           ['build', 'create', 'generate', 'write code']):
        spark = get_spark()
        code = spark.generate_code(user_message)
        return code
    
    return None  # Let Ember handle it
```

**Then**:
```python
# BEFORE Ember generates:
tool_result = preemptive_tool_routing(user_message)

if tool_result:
    # Add tool result to context
    messages.append({"role": "system", "content": f"Tool executed:\n{tool_result}\n\nNow explain this to the user."})

# THEN Ember generates (with result already in context)
```

---

**Option 2: Larger Model** 🐘 (SLOW)

Switch to Llama 3.1-8B or 3.3-70B which have better instruction following.

**Problem**: 
- 8B needs ~16GB VRAM (you have 12GB)
- 70B won't fit at all

---

**Option 3: LoRA Fine-tuning** 🧠 (COMPLEX)

Fine-tune the 3B model specifically on tool use examples.

**Problem**:
- We tried this before, caused ellipses/coherence issues
- Takes time to train properly

---

## RECOMMENDATION

**Use Option 1 (Pre-emptive Routing)** because:

- ✅ Works immediately
- ✅ No model changes needed
- ✅ Deterministic tool execution
- ✅ Can still use Ember for response generation
- ✅ Learns patterns from actual usage

**Trade-off**:
- Ember doesn't "decide" to use tools
- We decide for it based on keywords
- But that's better than hallucination!

---

## IMPLEMENTATION

Wire `preemptive_tool_routing()` into `generate_response()`:

```python
def generate_response(user_message, conversation_history):
    # NEW: Check if user message needs tools FIRST
    tool_result = preemptive_tool_routing(user_message)
    
    if tool_result:
        # Add to context
        context_with_tool = f"You were asked: '{user_message}'\n\nThe result:\n{tool_result}\n\nNow explain this naturally."
        
        # Generate WITH the result already present
        response = model.generate(context_with_tool)
        
        # Learn from this
        learner.save_tool_chain(user_message, ..., tool_result, success=True)
        
        return response
    
    # No tool needed, let Ember respond normally
    return model.generate(user_message)
```

---

## WHY THIS WORKS

**Instead of asking Ember to use tools:**
1. User asks question
2. WE detect tool need
3. WE execute tool
4. WE give result to Ember
5. Ember explains (what it's good at)

**Ember becomes the INTERFACE, not the EXECUTOR.**

---

## NEXT STEPS

1. Implement `preemptive_tool_routing()`
2. Test with same queries
3. Verify tools actually execute
4. Watch pattern learning work

**ETA**: 30 minutes to implement and test

---

## THE INSIGHT

**We were asking a 3B model to do something it can't reliably do.**

Instead of fighting the model, **work WITH its strengths**:
- ✅ Natural language generation: Excellent
- ✅ Context understanding: Good
- ✅ Response formatting: Good
- ❌ Structured tool calls: Poor

**Solution**: We handle structure, Ember handles language.

---

**This is actually better** because:
- Deterministic execution
- No hallucination
- Faster (no tool-format parsing)
- Patterns still learned
- Can upgrade to better model later

---

**Want me to implement it?** 🔥

