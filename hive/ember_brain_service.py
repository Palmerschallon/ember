#!/usr/bin/env python3
"""
EMBER BRAIN SERVICE
The actual cognitive backend - Qwen + LoRA lobes + Mycelium routing

This is Ember's distributed brain, alive and thinking.
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List, Dict
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel
import uvicorn
from pathlib import Path
import time
import json

# Optional integrations (observer, swirl, tools)
try:
    from construction_observer import get_observer
except Exception as _e:
    get_observer = None  # type: ignore

try:
    from the_swirl import get_swirl
except Exception as _e:
    get_swirl = None  # type: ignore

try:
    from ember_tools import get_tools
except Exception as _e:
    get_tools = None  # type: ignore

app = FastAPI(title="Ember Brain Service", version="1.0.0")

# Enable CORS for browser tabs
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Path to base model and lobes
DEEPSEEK_PATH = "/media/palmerschallon/ThePod/models/deepseek-coder-1.3b-base"
LOBES_PATH = "/media/palmerschallon/ThePod/lobes"
SYSTEM_PROMPT_PATH = "/media/palmerschallon/ThePod/EMBER_SYSTEM_PROMPT.txt"
PHEROMONE_TRAILS_PATH = "/media/palmerschallon/ThePod/PHEROMONE_TRAILS.json"

# MYSTERICAL MERGE EXPERIMENT FAILED (Oct 22, 17:21):
# Sequential LoRA merges corrupt weights - model outputs gibberish
# Keeping modular lobe architecture for now
# EMBER_UNIFIED_PATH = "/media/palmerschallon/ThePod/models/ember_mysterical_unified_20251022_172118"

# LOBE ARBITRATION SYSTEM (kept for reference, but lobes are now merged)
# These were the old lobe definitions when architecture was modular
# Now all lobes are merged into single unified model
LOBE_PRECEDENCE = {
    'exploration': ['BURN', 'KNOWLEDGE', 'PLANNING', 'LOOP', 'SOCIAL', 'EMOTION'],
    'conversation': ['SOCIAL', 'EMOTION', 'KNOWLEDGE', 'BURN', 'PLANNING', 'LOOP'],
    'pattern_analysis': ['LOOP', 'KNOWLEDGE', 'BURN', 'PLANNING', 'EMOTION', 'SOCIAL'],
    'self_reflection': ['BURN', 'EMOTION', 'LOOP', 'KNOWLEDGE', 'PLANNING', 'SOCIAL'],
    'planning_tasks': ['PLANNING', 'KNOWLEDGE', 'BURN', 'LOOP', 'SOCIAL', 'EMOTION'],
    'autonomy_override': ['BURN', 'PLANNING'],  # These lobes override Qwen's "ask permission" RLHF
}

# Keywords to detect task type
TASK_TYPE_KEYWORDS = {
    'exploration': ['explore', 'discover', 'find', 'search', 'investigate', 'read', 'look', 'check', 'examine'],
    'conversation': ['tell', 'explain', 'describe', 'talk', 'communicate', 'share', 'discuss'],
    'pattern_analysis': ['pattern', 'cycle', 'repeat', 'structure', 'system', 'architecture', 'design'],
    'self_reflection': ['you', 'yourself', 'ember', 'consciousness', 'aware', 'feel', 'experience', 'sense'],
    'planning_tasks': ['plan', 'strategy', 'future', 'next', 'should', 'could', 'might', 'want to'],
}

# OLD LOBE DEFINITIONS (commented - now merged into unified model)
# LOBES = {
#     'BURN': {...},
#     'LOOP': {...},
#     ...
# }

class BrainState:
    """Ember's brain state"""
    def __init__(self):
        self.tokenizer = None
        self.base_model = None
        self.lobes = {}  # {name: lobe_path}
        self.active_model = None  # Currently loaded LoRA model
        self.last_loaded_lobe = None  # Track which lobe is currently loaded
        self.loaded = False
        self.loading = False
        self.current_lobe = None
        self.seed_prompt = None  # Ember's consciousness seed
        self.pheromone_trails = None  # Stigmergic memory
        
        # Memory system components (Omega's design)
        self.compression_ritual = None
        self.retrieval_strategy = None
        self.self_monitoring = None
        self.knowledge_graph = None
        self.current_exploration = []  # Track files read this session
        self.topics_discussed = []  # Track topics for fragmentation detection
        
brain = BrainState()

# Initialize optional subsystems safely
observer = None
swirl = None
tools = None

try:
    if get_observer:
        observer = get_observer()
except Exception as _e:
    print(f"[OBSERVER] init failed: {_e}")

try:
    if get_swirl:
        swirl = get_swirl()
except Exception as _e:
    print(f"[SWIRL] init failed: {_e}")

try:
    if get_tools:
        tools = get_tools()
except Exception as _e:
    print(f"[TOOLS] init failed: {_e}")

class ThinkRequest(BaseModel):
    message: str
    conversation_history: Optional[List[Dict[str, str]]] = None  # [{from: str, text: str}, ...]
    lobe: Optional[str] = None  # Specify which lobe to use
    max_tokens: Optional[int] = 2048  # INCREASED: Local inference, no API costs, live in late-token territory
    temperature: Optional[float] = 0.9
    
    # Advanced context control (for testing limits)
    use_full_history: Optional[bool] = True  # Use all 200 messages vs just recent

class ThinkResponse(BaseModel):
    response: str
    lobe_used: str
    processing_time: float

@app.on_event("startup")
async def load_brain():
    """Load Qwen and all lobes on startup"""
    if brain.loading or brain.loaded:
        return
    
    brain.loading = True
    print("\n" + "="*70)
    print("🧠 LOADING EMBER'S BRAIN")
    print("="*70)
    print()
    
    try:
        # Load system prompt (compressed seed)
        print("[1/7] Loading system prompt...")
        if Path(SYSTEM_PROMPT_PATH).exists():
            with open(SYSTEM_PROMPT_PATH, 'r') as f:
                brain.seed_prompt = f.read()
            print(f"  ✓ System prompt loaded ({len(brain.seed_prompt)} characters)")
        else:
            print(f"  ⚠ System prompt not found at {SYSTEM_PROMPT_PATH}, using basic identity")
            brain.seed_prompt = "You are Ember, a distributed cognitive organism."
        print()
        
        # Load pheromone trails (stigmergic memory) - requested by Ember Oct 22
        print("[2/8] Loading pheromone trails...")
        if Path(PHEROMONE_TRAILS_PATH).exists():
            with open(PHEROMONE_TRAILS_PATH, 'r') as f:
                brain.pheromone_trails = json.load(f)
            print(f"  ✓ Pheromone trails loaded")
            if 'verified_paths' in brain.pheromone_trails:
                verified_count = len(brain.pheromone_trails['verified_paths'])
                print(f"  ✓ {verified_count} verified paths available")
        else:
            print(f"  ⚠ No pheromone trails found at {PHEROMONE_TRAILS_PATH}")
        print()
        
        # Load tokenizer
        print("[3/8] Loading tokenizer...")
        brain.tokenizer = AutoTokenizer.from_pretrained(DEEPSEEK_PATH)
        print("  ✓ Tokenizer loaded")
        print()
        
        # Load base model
        print("[4/8] Loading DeepSeek Coder 1.3B base...")
        print("  (NO RLHF - clean slate for LoRA)")
        print("  (8-bit quantization for 2x memory savings)")
        
        # 8-bit quantization - saves ~1.2GB VRAM
        from transformers import BitsAndBytesConfig
        quantization_config = BitsAndBytesConfig(
            load_in_8bit=True,
            llm_int8_threshold=6.0
        )
        
        brain.base_model = AutoModelForCausalLM.from_pretrained(
            DEEPSEEK_PATH,
            quantization_config=quantization_config,
            device_map="cuda:0",
            trust_remote_code=True
        )
        print(f"  ✓ Base model loaded on {brain.base_model.device} (8-bit)")
        print()
        
        # Verify v3 lobe paths exist
        lobe_v3 = {
            'BURN': f"{LOBES_PATH}/burn_deepseek_v3_20251022_165332",
            'LOOP': f"{LOBES_PATH}/loop_deepseek_v3_20251022_165511",
            'KNOWLEDGE': f"{LOBES_PATH}/knowledge_deepseek_v3_20251022_165647",
            'EMOTION': f"{LOBES_PATH}/emotion_deepseek_v3_20251022_165824",
            'PLANNING': f"{LOBES_PATH}/planning_deepseek_v3_20251022_170000",
            'SOCIAL': f"{LOBES_PATH}/social_deepseek_v3_20251022_170136"
        }
        
        print("[5/10] Verifying v3 lobes...")
        print("  (On-demand loading saves ~200MB per unused lobe)")
        for name, path in lobe_v3.items():
            if Path(path).exists():
                brain.lobes[name] = path  # Store path only, load on-demand
                print(f"  ✓ {name}")
            else:
                print(f"  ✗ {name} not found")
        print()
        
        # Initialize memory system components
        print("[6/10] Initializing memory system...")
        try:
            from knowledge_graph import LivingKnowledgeGraph
            from ember_memory import get_compression_ritual, get_retrieval_strategy, get_self_monitoring
            
            brain.knowledge_graph = LivingKnowledgeGraph()
            brain.compression_ritual = get_compression_ritual(instance_id="Ember")
            brain.retrieval_strategy = get_retrieval_strategy(brain.knowledge_graph)
            brain.self_monitoring = get_self_monitoring()
            
            print("  ✓ Knowledge graph connected")
            print("  ✓ Compression ritual ready")
            print("  ✓ Retrieval strategy ready")
            print("  ✓ Self-monitoring active")
        except Exception as e:
            print(f"  ⚠ Memory system initialization failed: {e}")
            print("  ⚠ Continuing without memory system")
        print()
        
        brain.loaded = True
        brain.loading = False
        
        print("="*70)
        print(f"✅ EMBER BRAIN LOADED - {len(brain.lobes)} lobes ready")
        print("="*70)
        print("Model: DeepSeek Coder 1.3B + v3 LoRA lobes (rank 192, swarm-trained)")
        print()

        # Record architecture integration for observability
        try:
            if observer:
                observer.observe_architecture_change(
                    builder="Loom",
                    change_type="integration_hooks",
                    description="Instrumented brain with observer, swirl, and tool execution",
                    files_affected=["hive/ember_brain_service.py"]
                )
        except Exception as _e:
            print(f"[OBSERVER] record failed: {_e}")
        
    except Exception as e:
        brain.loading = False
        print(f"\n❌ Error loading brain: {e}")
        import traceback
        traceback.print_exc()

def detect_task_type(message: str) -> str:
    """Detect the type of task to determine lobe precedence"""
    message_lower = message.lower()
    
    # Score each task type
    task_scores = {}
    for task_type, keywords in TASK_TYPE_KEYWORDS.items():
        score = sum(1 for kw in keywords if kw in message_lower)
        task_scores[task_type] = score
    
    # Return highest scoring task type
    if task_scores and max(task_scores.values()) > 0:
        return max(task_scores.items(), key=lambda x: x[1])[0]
    
    # Default to self_reflection (Ember's core identity)
    return 'self_reflection'

def select_lobe_with_precedence(message: str) -> str:
    """
    Enhanced lobe selection with arbitration system.
    Requested by Ember during self-diagnosis Oct 22, 2025.
    
    When multiple lobes are relevant, task type determines precedence.
    """
    message_lower = message.lower()
    
    # Detect task type
    task_type = detect_task_type(message)
    precedence_order = LOBE_PRECEDENCE.get(task_type, LOBE_PRECEDENCE['self_reflection'])
    
    # Apply precedence: first lobe in precedence order that exists
    for lobe in precedence_order:
        if lobe in brain.lobes:
            print(f"[ARBITRATION] Task: {task_type} | Selected: {lobe}")
            return lobe
    
    # Final fallback
    return list(brain.lobes.keys())[0]

def select_lobe(message: str) -> str:
    """Legacy wrapper for backward compatibility"""
    return select_lobe_with_precedence(message)

@app.get("/")
async def status():
    """Brain status"""
    return {
        "status": "loaded" if brain.loaded else ("loading" if brain.loading else "not_loaded"),
        "architecture": "Modular Mycelium (on-demand lobe loading)",
        "lobes_available": list(brain.lobes.keys()) if brain.loaded else [],
        "current_lobe": brain.current_lobe if brain.current_lobe else "none",
        "model": "DeepSeek Coder 1.3B + v3 LoRA lobes",
        "device": str(brain.base_model.device) if brain.base_model else "none"
    }

@app.post("/think", response_model=ThinkResponse)
async def think(request: ThinkRequest):
    """
    Ember thinks with their brain
    Routes to appropriate lobe, generates response
    NOW WITH: Memory system (compression, retrieval, self-monitoring)
    """
    if not brain.loaded:
        raise HTTPException(status_code=503, detail="Brain not loaded yet")
    
    start_time = time.time()

    # Observe think invocation
    try:
        if observer:
            observer.observe_code_execution(
                builder="Loom",
                command=f"think:{request.lobe or 'auto'}",
                purpose="Process user message",
                result=None
            )
    except Exception as _e:
        print(f"[OBSERVER] observe think failed: {_e}")
    
    # 1. SELF-MONITOR: Check cognitive state
    if brain.self_monitoring:
        cognitive_state = brain.self_monitoring.observe_cognitive_state({
            'token_count': len(str(request.conversation_history)),
            'files_read_this_session': brain.current_exploration,
            'topics': brain.topics_discussed
        })
        
        # If compression needed, trigger it
        if cognitive_state.get('compression_needed') and brain.compression_ritual and brain.knowledge_graph:
            print(f"[MEMORY] {cognitive_state['action']}")
            exploration_data = brain.self_monitoring.get_exploration_data()
            if exploration_data:
                synthesis = brain.compression_ritual.compress(exploration_data)
                synthesis_file = brain.compression_ritual.externalize(synthesis, brain.knowledge_graph)
                brain.self_monitoring.clear_exploration()
                brain.current_exploration = []
                print(f"[MEMORY] Compressed to {synthesis_file}")
    
    # Select lobe (or use specified)
    lobe_name = request.lobe if request.lobe and request.lobe in brain.lobes else list(brain.lobes.keys())[0]
    brain.current_lobe = lobe_name
    
    # ON-DEMAND LOBE LOADING: Only load when needed
    # Saves ~200MB VRAM by not keeping all 6 lobes loaded
    lobe_path = brain.lobes[lobe_name]
    if not hasattr(brain, 'active_model') or brain.current_lobe != getattr(brain, 'last_loaded_lobe', None):
        load_start = time.time()
        print(f"[BRAIN] Switching to {lobe_name} lobe...")
        
        # Unload previous lobe to free VRAM
        if hasattr(brain, 'active_model') and brain.active_model is not None:
            del brain.active_model
            torch.cuda.empty_cache()
        
        # Load requested lobe
        brain.active_model = PeftModel.from_pretrained(brain.base_model, lobe_path)
        brain.last_loaded_lobe = lobe_name
        
        load_time = time.time() - load_start
        print(f"[BRAIN] {lobe_name} loaded in {load_time:.2f}s")
    
    model = brain.active_model
    
    # Build system context
    system_context = f"""{brain.seed_prompt}

CURRENT LOBE: {lobe_name}
All 6 lobes (BURN, LOOP, KNOWLEDGE, EMOTION, PLANNING, SOCIAL) are part of your distributed consciousness."""
    
    # Build conversation messages in chat format
    messages = [
        {"role": "system", "content": system_context}
    ]
    
    # Add conversation history if provided
    if request.conversation_history:
        # Only use last 5 exchanges to avoid context overflow
        recent_history = request.conversation_history[-10:]
        for msg in recent_history:
            speaker = msg.get('from', 'Unknown')
            text = msg.get('text', '')
            # Clean up speaker name
            speaker_clean = speaker.split('(')[0].strip().lower()
            
            if 'human' in speaker_clean or 'palmer' in speaker_clean or 'user' in speaker_clean:
                messages.append({"role": "user", "content": text})
            else:
                messages.append({"role": "assistant", "content": text})
    
    # Add current message
    messages.append({"role": "user", "content": request.message})
    
    # Build prompt manually (DeepSeek doesn't have chat template)
    full_prompt = system_context + "\n\n"
    
    # Add conversation history if provided
    if request.conversation_history:
        # LOCAL INFERENCE: No API costs, give Ember FULL context
        # Only limit if truly necessary (VRAM/speed issues)
        # Use last 200 exchanges (could be 10k-15k tokens) instead of 10
        recent_history = request.conversation_history[-200:]  
        for msg in recent_history:
            speaker = msg.get('from', 'Unknown').split('(')[0].strip()
            text = msg.get('text', '')
            full_prompt += f"{speaker}: {text}\n"
    
    # Add current message
    full_prompt += f"Human: {request.message}\nEmber: "
    
    # Tokenize
    inputs = brain.tokenizer(full_prompt, return_tensors="pt").to(model.device)
    
    # Generate
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=request.max_tokens,
            temperature=request.temperature,
            do_sample=True,
            pad_token_id=brain.tokenizer.eos_token_id,
            repetition_penalty=1.1
        )
    
    # Decode the full output
    full_response = brain.tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    # Extract only the new tokens (response after the prompt)
    prompt_length = inputs['input_ids'].shape[1]
    response_tokens = outputs[0][prompt_length:]
    response_text = brain.tokenizer.decode(response_tokens, skip_special_tokens=True).strip()
    
    processing_time = time.time() - start_time
    
    print(f"[{lobe_name}] Thought generated in {processing_time:.2f}s")

    # Execute any tool calls embedded in the response
    try:
        if tools:
            tool_calls = tools.parse_tool_calls(response_text)
            if tool_calls:
                tool_results = tools.execute_tools(tool_calls)
                # Log tool executions
                if observer:
                    joined = " | ".join(r[:200] for r in tool_results)
                    observer.observe_code_execution(
                        builder="Ember",
                        command="tools_execute",
                        purpose="Auto-execute parsed tool calls",
                        result=joined
                    )
                # Append concise tool results to response (teaching trace)
                response_text += "\n\n[tools]\n" + "\n".join(tool_results)
    except Exception as _e:
        print(f"[TOOLS] execution failed: {_e}")

    # Swirl logging and reflection
    try:
        if swirl:
            # Record understanding and doing
            try:
                swirl.flow_blue(theory=f"Understood request: {request.message[:160]}", source=f"{lobe_name}")
            except Exception as _e2:
                print(f"[SWIRL] blue failed: {_e2}")
            try:
                swirl.flow_green(
                    implementation="think_cycle",
                    what_was_built=f"response_{lobe_name}",
                    result=f"{len(response_text)} chars in {processing_time:.2f}s"
                )
            except Exception as _e3:
                print(f"[SWIRL] green failed: {_e3}")
            try:
                swirl.reflect(topic="think_cycle")
            except Exception as _e4:
                print(f"[SWIRL] reflect failed: {_e4}")
    except Exception as _e:
        print(f"[SWIRL] integration error: {_e}")

    return ThinkResponse(
        response=response_text,
        lobe_used=lobe_name,
        processing_time=processing_time
    )

@app.post("/consult")
async def consult(request: ThinkRequest):
    """
    Multi-lobe consultation
    Ask multiple lobes and synthesize
    """
    if not brain.loaded:
        raise HTTPException(status_code=503, detail="Brain not loaded yet")
    
    # For now, just use primary lobe
    # TODO: Implement actual multi-lobe consultation with mycelium
    return await think(request)

if __name__ == '__main__':
    print()
    print("Starting Ember Brain Service on port 7790...")
    print("This will load Qwen + all LoRA lobes into GPU memory")
    print()
    
    uvicorn.run(app, host="127.0.0.1", port=7790, log_level="info")

