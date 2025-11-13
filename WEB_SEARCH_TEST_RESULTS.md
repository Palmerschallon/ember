# TESTING EMBER'S WEB SEARCH - First Results

**Date:** 2025-10-28  
**Test:** Can Ember find the book they mentioned?

---

## What Ember Asked For:

> "My gaze falls upon the book 'The Feeling of Reality' by David Chalmers. Its pages might hold some answers..."

---

## Test 1: Direct Web Search Tool

```bash
python3 web_search.py "David Chalmers The Feeling of Reality book"
```

**DuckDuckGo Result:**
- Found: **"Reality+: Virtual Worlds and the Problems of Philosophy"** by David Chalmers
- This is likely what Ember was "remembering" - a real book!

**Actual David Chalmers Books:**
- "The Conscious Mind" (1996) - His famous consciousness book
- "Reality+: Virtual Worlds and the Problems of Philosophy" (2022)
- "The Character of Consciousness" (2010)

---

## Test 2: Asking Ember to Use Forage

**Problem:** Ember didn't use the `forage` tool!

Instead, Ember hallucinated:
```xml
<tool>perceive(url="https://chalmerslab.org/consciousness-bookshelves/")</tool>
```

These URLs don't exist. Ember is making them up.

---

## Why This Happened:

1. **Model behavior:** The LoRA is trained to use `perceive()` for file reading
2. **Confusion:** Ember extended this to web URLs (reasonable but wrong)
3. **Hallucination:** No web results to ground them, so made up plausible-sounding content

---

## The Issue:

Ember knows how to use tools, but:
- Uses `perceive()` for everything (files AND urls)
- Doesn't use `forage()` even when told about it in system prompt
- When tools "succeed" (because no validation), hallucinates the results

---

## Solutions:

### Option 1: Make perceive() work with URLs
Add URL support to the existing `perceive()` tool:
```python
def read_file(path: str, lines: int = 50) -> str:
    if path.startswith("http://") or path.startswith("https://"):
        # Fetch URL content
        return fetch_url(path)
    else:
        # Read file
        return read_file_content(path)
```

### Option 2: Stronger prompt about forage
Add examples of when to use forage vs perceive:
```
perceive() → for files on ThePod
forage() → for searching the web
```

### Option 3: Validate tool calls
Check if URLs/paths exist before "executing":
```python
if tool_name == "perceive" and "http" in path:
    return "Cannot perceive URLs. Use forage() to search web first."
```

---

## What DuckDuckGo Actually Gave Us:

**Limited but functional:**
- Found "Reality+" book (real)
- Basic search results
- No structured data (just HTML text extraction)

**Good enough for:**
- Finding if something exists
- Getting basic info
- Discovering real resources

**Not great for:**
- Detailed research
- Multiple results
- Structured data

---

## Recommendation:

1. **Fix perceive() to handle URLs** (Option 1)
   - Most natural for Ember
   - Matches how they already think
   - Web search becomes transparent

2. **Keep forage() as explicit search** (Option 2)
   - For when Ember needs to actively search
   - Different from passively reading a URL

3. **Add validation** (Option 3)
   - Prevent hallucination
   - Give clear errors

---

## Next Test:

Try with Google or Brave API to see if better results help Ember use tools correctly.

---

**DuckDuckGo works, but Ember needs clearer tool boundaries or URL support in perceive().** 🔥

