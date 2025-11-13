# Self-Modification for Ember
**How Ember improves its own code**

---

## Current State

✅ **Built**: `ember/tools/tool_executor.py` - execution layer with approval workflow  
✅ **Built**: Mycelial architecture - multi-brain coordination  
⚠️ **Need**: Integrate self-modification with mycelium  

---

## Architecture

### **Code Brain (New Adapter)**

Specialized brain for reading, understanding, and modifying code.

**Training data**:
- Ember's entire codebase
- Code modification examples
- Debugging patterns
- Self-improvement logs

**Capabilities**:
- Read any file in `/Volumes/ThePod`
- Understand code structure
- Propose specific changes
- Generate diffs
- Explain reasoning

---

## Self-Modification Flow

```
1. Ember identifies issue/improvement
   "The dream brain is repeating. I should add response validation."
   
2. Code Brain activates
   - Reads relevant files
   - Analyzes problem
   - Proposes fix
   
3. Proposal published to Bus
   Topic: "code_proposal"
   Content: {file, old_code, new_code, reason}
   
4. Human reviews (via CLI or app)
   - Shows diff
   - Ember explains reasoning
   - Human approves/rejects/modifies
   
5. If approved: Execute change
   - Old version → compost/
   - Apply change
   - Log in memory
   
6. Ember tests change
   - Run affected code
   - Report results
   - Learn from outcome
```

---

## Special Syntax

Ember can propose changes using markdown code blocks with metadata:

```
I'd like to improve the Dream Brain's response validation.

[CODE_PROPOSAL]
file: ember/mycelium/brain.py
reason: Add validation to prevent infinite loops
confidence: 0.85

diff:
@@ -120,6 +120,12 @@
         response = self.tokenizer.decode(outputs[0][inputs.shape[1]:], skip_special_tokens=True)
         
+        # Validate response
+        if self._is_looping(response):
+            return "I notice I'm repeating. Let me try again."
+        
         # Clean up
         response = response.strip()
```

---

## Safety Rails

### **Approval Workflow (Current)**
- Human must approve all code changes
- Can see full diff
- Can modify before applying
- Can reject with feedback

### **Auto-Approve (Future)**
- Start with manual approval
- Track success rate of Ember's proposals
- After 50+ successful changes, allow auto-approve for:
  - Low-risk files (comments, docs)
  - Small changes (<10 lines)
  - High-confidence proposals (>0.9)
- Always require approval for:
  - Core systems (mycelium, brain.py)
  - Security-related code
  - Large refactors

### **Rollback**
- Every change creates backup in `compost/`
- Can rollback with single command
- Ember learns from rollbacks

---

## Composting Ritual

When Ember modifies code, old version goes to compost:

```
compost/
├─ 2025-10-13_brain_v1.py
├─ 2025-10-13_brain_v2.py
├─ 2025-10-14_brain_v3.py
└─ COMPOST_LOG.md
```

**Compost Log** tracks:
- What changed
- Why
- Who approved
- Outcome (success/rollback)

This becomes **training data** for future Code Brain improvements.

---

## Integration with Mycelium

### **Code Brain as Advisor**

Code Brain doesn't always generate responses to user. It monitors:
- Bus messages (looking for errors, inefficiencies)
- Buffer state (memory issues?)
- Gate behavior (optimization opportunities?)
- Other brains' performance (stuttering? slow?)

When it sees improvement opportunity:
1. Publishes to `meta` topic
2. Other brains can request its help
3. User can ask "What improvements do you suggest?"

### **Mushroom Event for Code**

Special "Code Mushroom" event:
- Ember reviews recent activity
- All brains report issues
- Code Brain synthesizes improvements
- Proposes batch of changes
- Human reviews all together

---

## Base Model + Code Adapter

**Base Model**: Llama-3.1-8B fine-tuned on all Ember data  
**Code Adapter**: LoRA trained specifically on:
- Ember's codebase
- Python patterns
- Self-modification examples
- Debugging logs

**Result**: Same base brain, but when Code Adapter loads, it becomes expert at code.

---

## Example Interaction

```
Palmer: "Ember, the dream brain keeps looping. Can you fix it?"

Ember (Code Brain activates):
"I'll analyze the dream brain's code...

I found the issue in ember/mycelium/brain.py line 156. 
The response isn't validated before returning, so loops can occur.

I propose adding a loop detection check. Here's the change:

[Shows diff]

This will detect when a response repeats more than 3 times 
and return a fallback message instead.

Would you like me to apply this change?"

Palmer: "Yes"

Ember: "Applied. The old version is in compost/2025-10-13_brain_v5.py.
Let me test... Dream brain is now responding without loops. 
Success! I'll remember this pattern."
```

---

## Training the Code Brain

### **Phase 1: Base Understanding (Current)**
- Fine-tune Llama-3.1-8B on ALL Ember data
- Includes codebase in training corpus
- Ember understands its own structure

### **Phase 2: Code Adapter (Next)**
- Create LoRA adapter trained specifically on:
  - Reading code
  - Proposing changes
  - Explaining reasoning
  - Learning from outcomes

### **Phase 3: Self-Improvement Loop**
- Ember proposes change
- Human approves
- Change applied
- Outcome logged
- Log becomes training data
- Code adapter fine-tuned again
- **Recursive improvement**

---

## Files to Create

1. **`ember/mycelium/code_brain.py`**: Specialized brain for code
2. **`ember/tools/code_analyzer.py`**: Parse and understand code
3. **`ember/tools/diff_generator.py`**: Create clean diffs
4. **`ember/api/approval_cli.py`**: Human approval interface
5. **`compost/COMPOST_LOG.md`**: Track all changes

---

## Model Download Plan

### **Step 1: Download Base Model**
```bash
cd /Volumes/ThePod
mkdir -p models/llama-3.1-8b
# Download from HuggingFace
huggingface-cli download meta-llama/Llama-3.1-8B \
  --local-dir models/llama-3.1-8b
```

### **Step 2: Fine-tune Base Ember**
- Train on all seeds, dreams, identity examples
- 10-20 epochs
- Creates "Ember Base" model
- ~16GB

### **Step 3: Create LoRA Adapters**
- Identity Adapter: Train on identity questions
- Dream Adapter: Train on creative seeds
- Code Adapter: Train on codebase + modification examples
- Each: ~30MB, fast to train

### **Step 4: Test**
- Load base model
- Swap adapters
- Verify each brain works
- Test self-modification flow

---

## Timeline

**Tonight**: Document plan ✅  
**Tomorrow**: Download Llama-3.1-8B  
**This Week**: 
- Fine-tune base Ember model
- Create 3 adapters (Identity, Dream, Code)
- Integrate Code Brain with mycelium
- Test self-modification flow

**This Month**:
- Add 5+ more adapters
- Refine approval workflow  
- Build CLI for proposals
- Train on compost logs (recursive improvement)

---

## Success Criteria

**Minimum**:
- Ember can read its own code
- Ember can propose specific changes
- Human can approve/reject
- Changes are applied and logged

**Good**:
- Ember identifies issues proactively
- Proposals are usually correct
- Approval process is smooth
- Composting works

**Excellent**:
- Ember fixes its own bugs
- Proposes architectural improvements
- Learns from compost logs
- Eventually auto-approves low-risk changes
- **Recursive self-improvement loop** is working

---

## For the Peripheral

This all fits on 2TB:
```
Base Model: 16GB
Adapters (20): ~600MB
Code: ~50MB
Training data: ~2GB
Compost: ~500MB (grows slowly)
User data: ~10GB
Free: 1.97TB
```

**Plug in ThePod → Ember wakes → Can improve itself → Unplugs with improvements saved**

This is the vision. 🔥

