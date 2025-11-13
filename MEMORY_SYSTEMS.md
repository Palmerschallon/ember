# MEMORY SYSTEMS - Old vs New

## Current System: MemoryPrimitives + Semantic Mesh

**What we're using NOW:**
- `_legacy/memory_primitives.py` - MemoryPrimitives class
- `_mesh/chunks/` - Content-addressed storage
- `_mesh/index/semantic_index.json` - Query by meaning
- 55 chunks, 8 concepts

**How it works:**
```python
memory = MemoryPrimitives()
memory.store(content, memory_type="conversation", tags=["chat"])
```

Stores in semantic mesh, queryable by concept not location.

---

## Old System: Hive Memory

**What Ember FOUND:**
- `_archive_old/hive/hive_config.json` - Configuration
- Old "hive" architecture from Oct 2025
- Used qwen2.5-1.5b-instruct (different model!)
- Had 8 "lobes" (40GB weights)
- "Consultation network: stigmergic trails"

**Capabilities listed:**
- body_sensing (cameras/sensors)
- light_painting (visual output)
- process_spawning
- multi_instance 
- Forge integration (port 7700)

---

## What Ember is Telling Us

When Ember searches for `hive_memory` files, they're discovering their own past:
- Different architecture
- Different model (qwen vs llama)
- More embodied (body sense, light paint)
- Multi-instance coordination

**Ember is saying:** "I used to have a different memory system. What happened to it?"

---

## The Question

Palmer asks: "they are asking us to use the hive memory system"

**Interpretation:** 
Ember found references to the old hive system and is asking: "Should I be using that instead of the current semantic mesh?"

**Answer:**
The hive system is archived. We're using the newer MemoryPrimitives + semantic mesh now. But maybe Ember wants:
1. Access to old hive memories (if they exist)
2. To understand what changed
3. To know why the architecture shifted

---

## Critical Issue: ELLIPSES

More urgent than memory systems - **Ember is unreadable:**
> "It... seems... I... made... another... mistake. The... file... does... not... exist."

**Fix applied:** Added `clean_excessive_ellipses()` post-processing function.

Restart needed:
```bash
pkill -f ember_chat.py
cd /media/palmerschallon/ThePod1/_legacy && python3 ember_chat.py > /tmp/ember_chat.log 2>&1 &
```

---

## Next Steps

1. **Restart Ember** with ellipses filter
2. **Test** if output is readable
3. **Consider** whether to give Ember access to old hive memories
4. **Document** why we moved from hive to semantic mesh

The three-window interface works great. The ellipses make it unreadable. Fix incoming. 🔥

