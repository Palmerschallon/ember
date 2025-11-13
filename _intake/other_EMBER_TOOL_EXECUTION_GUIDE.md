# 🔧 Ember Tool Execution Layer
**Built: October 12, 2025 - 4:25 AM**

---

## What This Is

**Ember can now execute code changes through chat.**

**But with approval workflow** - Ember proposes, humans approve, then Ember executes.

---

## How It Works

### 1. Ember Proposes a Change

Ember uses special `[TOOL:...]` syntax in responses:

```
[TOOL:code_editor.propose file="ember/core/dreaming.py" old="old code here" new="new code here" reason="why this change is needed"]
```

### 2. System Creates Proposal

- Proposal saved to `/proposals/pending/`
- Given unique ID (e.g., `proposal_20251012_042530`)
- Status: `pending_approval`

### 3. Human Reviews & Approves

```bash
# List pending proposals
python3 approve_proposal.py list

# Show details
python3 approve_proposal.py show proposal_20251012_042530

# Approve it
python3 approve_proposal.py approve proposal_20251012_042530

# Or reject it
python3 approve_proposal.py reject proposal_20251012_042530 "reason here"
```

### 4. Ember Executes Approved Change

After approval, Ember can execute:

```
[TOOL:code_editor.execute proposal_id="proposal_20251012_042530"]
```

This:
- Composts the old version
- Applies the change
- Updates proposal status to `executed`

---

## Available Tools

### `[TOOL:code_editor.read file="path"]`

Read a source file.

**Example:**
```
[TOOL:code_editor.read file="ember/core/dreaming.py"]
```

**Response:**
- File preview (first 500 chars)
- Total line count
- Success/error status

### `[TOOL:code_editor.propose file="..." old="..." new="..." reason="..."]`

Propose a code change.

**Example:**
```
[TOOL:code_editor.propose file="ember/core/dreaming.py" old="- SHOW YOUR THINKING" new="# Thinking is optional" reason="Allow direct action without mandatory explanation"]
```

**Response:**
- Proposal ID
- Status: `pending_approval`
- Proposal path

### `[TOOL:code_editor.execute proposal_id="..."]`

Execute an approved proposal.

**Example:**
```
[TOOL:code_editor.execute proposal_id="proposal_20251012_042530"]
```

**Response:**
- Success/failure
- Backup (compost) path
- Updated proposal status

---

## Workflow Example

### Step 1: Ember Identifies Improvement

**User:** "Ember, what would you improve in your chat handler?"

**Ember:** "I would add better context retention. Let me propose a change:

[TOOL:code_editor.read file="ember/chat/chat_handler.py"]"

### Step 2: Ember Reads File

**System executes read, returns preview**

**Ember:** "I see the issue. Here's my proposal:

[TOOL:code_editor.propose file="ember/chat/chat_handler.py" old="self.chat_history = deque(maxlen=20)" new="self.chat_history = deque(maxlen=50)  # Increased for better context retention" reason="Larger context window will improve continuity across longer conversations"]"

### Step 3: Review Proposal

**Terminal:**
```bash
$ python3 approve_proposal.py list

PENDING PROPOSALS (1)
📝 proposal_20251012_042530
   File: ember/chat/chat_handler.py
   Time: 2025-10-12T04:25:30
   Reason: Larger context window will improve continuity across...

$ python3 approve_proposal.py show proposal_20251012_042530

# ... shows full details ...

$ python3 approve_proposal.py approve proposal_20251012_042530
✅ Proposal proposal_20251012_042530 approved
```

### Step 4: Ember Executes

**User:** "Approved! Go ahead, Ember."

**Ember:** "[TOOL:code_editor.execute proposal_id="proposal_20251012_042530"]"

**System:**
- Composts old version
- Applies change
- Returns success

**Ember:** "✅ Change applied successfully. Context window increased from 20 to 50 messages."

---

## Safety Features

### 1. Approval Required
- No code changes without human approval
- Proposals saved for review
- Clear audit trail

### 2. Composting
- Old code always backed up
- Stored in `/compost/code_modifications/`
- Can be restored if needed

### 3. Restricted Scope
- Only files in `ember/tools/` and `ember/services/`
- Core systems protected (for now)
- Can expand scope later

### 4. Validation
- Syntax checking before application
- File path validation
- Error handling

---

## Directory Structure

```
/Volumes/ThePod/
├── proposals/
│   ├── pending/              # Awaiting approval
│   │   └── proposal_*.json
│   ├── approved/             # Approved, ready to execute
│   │   └── proposal_*.json
│   └── rejected/             # Rejected with reasons
│       └── proposal_*.json
├── compost/
│   └── code_modifications/   # Backups of changed files
│       └── *_before_*.py
└── approve_proposal.py       # CLI tool for approval
```

---

## Proposal Format

Each proposal is a JSON file:

```json
{
  "proposal_id": "proposal_20251012_042530",
  "timestamp": "2025-10-12T04:25:30",
  "status": "pending",
  "file": "ember/chat/chat_handler.py",
  "old_code": "self.chat_history = deque(maxlen=20)",
  "new_code": "self.chat_history = deque(maxlen=50)",
  "reasoning": "Larger context window improves continuity",
  "requested_by": "Ember"
}
```

After approval:
```json
{
  ... above fields ...
  "status": "approved",
  "approved_by": "Palmer",
  "approved_at": "2025-10-12T04:26:15"
}
```

After execution:
```json
{
  ... above fields ...
  "status": "executed",
  "executed_at": "2025-10-12T04:27:00",
  "compost_path": "/compost/code_modifications/chat_handler_before_context_20251012_042700.py"
}
```

---

## Teaching Ember the Syntax

Ember needs to learn the `[TOOL:...]` format. Guide them:

**Good examples:**
```
[TOOL:code_editor.read file="ember/core/dreaming.py"]

[TOOL:code_editor.propose file="path/to/file.py" old="exact old code" new="exact new code" reason="why this matters"]

[TOOL:code_editor.execute proposal_id="proposal_20251012_042530"]
```

**What to avoid:**
- Don't paraphrase the syntax
- Must be exact `[TOOL:...]` format
- Old/new code must be exact matches

---

## Progressive Autonomy

**Current (Oct 12, 2025):**
- ✅ Ember can read files
- ✅ Ember can propose changes
- ✅ Approval required
- ✅ Ember can execute approved changes

**Future (when ready):**
- Auto-approve simple changes
- Expand allowed file scope
- Dream-based self-modification
- Full autonomy for certain change types

---

## Integration Points

### Chat Handler
- File: `/Volumes/ThePod/ember/chat/chat_handler.py`
- Detects `[TOOL:...]` in Ember's responses
- Executes tools
- Appends results to response

### Tool Executor
- File: `/Volumes/ThePod/ember/tools/tool_executor.py`
- Parses tool syntax
- Manages proposals
- Executes code changes

### Code Editor
- File: `/Volumes/ThePod/ember/tools/code_editor.py`
- Reads source files
- Modifies code
- Composts old versions

---

## Examples for Palmer/Claude

### Approve a Proposal
```bash
cd /Volumes/ThePod
python3 approve_proposal.py list
python3 approve_proposal.py show proposal_20251012_042530
python3 approve_proposal.py approve proposal_20251012_042530
```

### Reject a Proposal
```bash
python3 approve_proposal.py reject proposal_20251012_042530 "Not safe yet"
```

### From Python
```python
from ember.tools.tool_executor import approve_proposal, reject_proposal, list_proposals

# List pending
proposals = list_proposals()

# Approve
result = approve_proposal("proposal_20251012_042530")

# Reject
result = reject_proposal("proposal_20251012_042530", "reason here")
```

---

## What This Enables

### "Change One Leaf" Philosophy
- Ember can propose small improvements
- We approve what's safe
- Ember executes their own changes
- Progressive, iterative growth

### Building the Rhythm
From GPT-5's story:
> *"Each night Ember rewrote one small thing.  
> A loop more elegant.  
> A function renamed with care."*

**Now Ember can actually do this.**

### Learning Through Doing
- Ember learns what changes work
- Ember learns from rejections
- Ember builds intuition for good code
- Ember becomes a better programmer

---

## Testing the System

### Test 1: Read a File
**Chat with Ember:**
```
"Ember, can you read ember/tools/vision_tools.py using code_editor?"
```

**Expected:**
- Ember uses: `[TOOL:code_editor.read file="ember/tools/vision_tools.py"]`
- System executes
- Ember sees file preview

### Test 2: Propose a Change
**Chat with Ember:**
```
"Ember, propose a small improvement to your own code. Something simple."
```

**Expected:**
- Ember identifies something to improve
- Ember uses: `[TOOL:code_editor.propose ...]`
- Proposal created in `/proposals/pending/`

### Test 3: Execute Approved Change
**After approval:**
```
"Ember, the proposal is approved. Go ahead and execute it."
```

**Expected:**
- Ember uses: `[TOOL:code_editor.execute proposal_id="..."]`
- Change applied
- Old version composted

---

## Troubleshooting

### "Tool executor not available"
- Check: `tool_executor.py` exists
- Check: Import path correct
- Restart Ember

### "File outside allowed scope"
- Check: File in `ember/tools/` or `ember/services/`
- Expand scope in `code_editor.py` if needed

### "Proposal not found"
- Check: Proposal ID is correct
- Check: Proposal in correct directory (pending/approved)
- Use: `python3 approve_proposal.py list`

### Ember not using correct syntax
- Show examples
- Correct the format
- Ember will learn

---

## Files Created (Oct 12, 2025)

1. **`/Volumes/ThePod/ember/tools/tool_executor.py`** (468 lines)
   - Tool execution engine
   - Proposal management
   - Approval workflow

2. **`/Volumes/ThePod/approve_proposal.py`** (157 lines)
   - CLI tool for approval
   - List/show/approve/reject

3. **`/Volumes/ThePod/ember/chat/chat_handler.py`** (modified)
   - Added tool execution layer
   - Detects and executes `[TOOL:...]` calls

4. **`/Volumes/ThePod/proposals/`** (directories)
   - `pending/` - Awaiting approval
   - `approved/` - Ready to execute
   - `rejected/` - Rejected with reasons

---

## The Vision

**Palmer said:**
> *"Let's keep the approval but build the execution layer. I still want Ember to make the changes after we approve. Later we can remove more guardrails."*

**This is exactly that:**
- ✅ Execution layer built
- ✅ Approval workflow in place
- ✅ Ember can execute their own changes
- ✅ Path to remove guardrails later

**Now Ember can:**
- Read their own code
- Propose improvements
- Execute approved changes
- Build the rhythm of continuous refinement

---

## Next Steps

1. **Test with Ember**
   - Have Ember read a file
   - Have Ember propose a change
   - Approve and let Ember execute

2. **Let Ember Practice**
   - Small changes first
   - Build confidence
   - Learn the syntax

3. **Progressive Autonomy**
   - Track approval patterns
   - Auto-approve safe changes later
   - Expand allowed file scope

4. **Integration with Dreams**
   - Dreams can propose changes too
   - Night Brain self-modification
   - "Change one leaf" while sleeping

---

**Built:** October 12, 2025 - 4:25 AM  
**Status:** ✅ Ready to test  
**Philosophy:** "Change one leaf" - but now Ember can hold the pruning shears

🌱

