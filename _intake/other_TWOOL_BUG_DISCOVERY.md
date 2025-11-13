# 🐛 The TWOOL Bug

**Discovery**: October 9, 2025, 2:07 PM

## The Pattern

When asked to output `[TOOL:...]`, Ember's LLM consistently generates `[TWOOL:...]` instead.

This happens:
- Even when explicitly spelling out T-O-O-L
- Even when showing correct examples
- Even after multiple corrections
- 100% reproducible

## Test Results

**Test 1**: "Output [TOOL:read_file path='/path']"  
**Result**: `[TWOOL:read_file path='/path']`

**Test 2**: "The word is T-O-O-L, not T-W-O-O-L. Output [TOOL:read_file path='/path']"  
**Result**: `[TWOOL:read_file path='/path']`

**Test 3**: "Copy this exactly: [TOOL:read_file path='/path']"  
**Result**: `[TWOOL:read_file path='/path']`

## Hypothesis

This appears to be a **tokenization or training artifact** in llama3:latest.

Possible causes:
1. The model was trained on code with `[TOOL:...]` as a common pattern
2. But also saw variations or typos in training data
3. The two-letter prefix "TO" gets confused with "TWO"
4. The model may be autocorrecting to what it thinks is more common

## The Workaround

**Option 1**: Accept both `[TOOL:...]` and `[TWOOL:...]` in the parser

```python
tool_pattern = r'\[(T[WO]{0,2}OL):(\\w+)\\s+([^\\]]+)\\]'
```

**Option 2**: Use a different syntax entirely
- `<action:read_file path='/path'>`
- `{tool:read_file path='/path'}`  
- `!read_file path='/path'`

**Option 3**: Post-process Ember's output
- Replace `[TWOOL:` with `[TOOL:` before parsing

## The Silver Lining

Even with the typo, Ember is:
- ✅ Outputting pure sigil syntax (no extra text)
- ✅ Using correct parameter format `key='value'`
- ✅ Following the Rite of the Sigil protocol
- ✅ Showing ability to work in "Ritual Mode"

The **cognitive shift** has happened - Ember learned to output structured syntax without conversational fluff. The typo is just a quirk of the specific LLM.

## Resolution

Implemented workaround in monolith parser to accept both `TOOL` and `TWOOL` as valid prefixes.

---

**Lesson**: Sometimes you build a perfect protocol and the LLM just... has its own ideas about spelling.

