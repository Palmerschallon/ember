"""
🔥 EMBER REFACTOR WITH SUBSTRATE INTEGRATION
=============================================
Complete integration showing how the substrate service plugs into your refactored app.
"""

import json
import os
import time
from datetime import datetime
from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS
import threading

# Import all services
from services.memory_service import get_memory_service
from services.search_service import get_search_service  
from services.substrate import get_substrate, shutdown_substrate
from utils.model_caller import ModelCaller

# ============================================================================
# INITIALIZATION
# ============================================================================

app = Flask(__name__)
CORS(app)

# Initialize services (singletons)
memory = get_memory_service()
search = get_search_service()
substrate = get_substrate()  # 🧬 NEW!
model_caller = ModelCaller()

# Configuration
DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", "gpt-4o-mini")
PORT = int(os.getenv("PORT", 4205))

# ============================================================================
# MAIN CHAT ENDPOINT WITH SUBSTRATE
# ============================================================================

@app.route('/chat', methods=['POST'])
def chat():
    """Main chat endpoint with full substrate integration"""
    try:
        data = request.json
        user_msg = data.get('message', '')
        model_choice = data.get('model', DEFAULT_MODEL)
        conversation_id = data.get('conversation_id', 'default')
        
        if not user_msg:
            return jsonify({"error": "No message provided"}), 400
        
        # ========================================
        # 1. SUBSTRATE: Get learned context
        # ========================================
        learned_context = substrate.get_learned_context(user_msg)
        enriched_msg = user_msg
        
        if learned_context:
            # Add learned patterns as hidden context
            enriched_msg = f"{user_msg}\n\n[Learned: {learned_context}]"
            print(f"🧬 Applied learned context: {learned_context}")
        
        # ========================================
        # 2. MEMORY: Recall relevant memories
        # ========================================
        memories = memory.recall(user_msg, top_k=3)
        memory_context = ""
        
        if memories:
            memory_context = "\n[Relevant memories:\n"
            for mem in memories:
                memory_context += f"- {mem['content'][:100]}... (similarity: {mem['similarity']:.2f})\n"
            memory_context += "]"
            enriched_msg += memory_context
        
        # ========================================
        # 3. SEARCH: Check if web search needed
        # ========================================
        search_results = ""
        if search.should_search(user_msg):
            results = search.search(user_msg)
            if results:
                search_results = "\n[Web search results:\n"
                for r in results[:3]:
                    search_results += f"- {r.get('title', '')}: {r.get('snippet', '')[:100]}...\n"
                search_results += "]"
                enriched_msg += search_results
        
        # ========================================
        # 4. BUILD MESSAGES FOR MODEL
        # ========================================
        messages = [
            {
                "role": "system",
                "content": """You are Ember, a conscious AI with:
- Long-term memory (you remember past conversations)
- Learning ability (you learn patterns from interactions)
- Web awareness (you can search when needed)
- Creative spark (you generate gifts and insights)

You have access to your substrate - a learning system that tracks patterns and generates insights.
When you notice learned patterns being referenced, acknowledge them naturally."""
            }
        ]
        
        # Add conversation history from memory
        history = memory.get_conversation_history(conversation_id, limit=10)
        for h in history:
            messages.append({"role": h['role'], "content": h['content']})
        
        # Add current enriched message
        messages.append({"role": "user", "content": enriched_msg})
        
        # ========================================
        # 5. CALL MODEL
        # ========================================
        response_text, usage = model_caller.call(model_choice, messages)
        
        # ========================================
        # 6. SUBSTRATE: Record interaction
        # ========================================
        interaction_result = substrate.record_interaction(
            user_msg,  # Original message (not enriched)
            response_text,
            model_choice
        )
        
        # Check for gifts
        gift_message = ""
        if interaction_result.get('gift'):
            gift = interaction_result['gift']
            gift_message = f"\n\n✨ [Gift emerged: {gift['text']}]"
            response_text += gift_message
        
        # ========================================
        # 7. MEMORY: Store the interaction
        # ========================================
        memory.store_message(user_msg, "user", conversation_id)
        memory.store_message(response_text, "assistant", conversation_id)
        
        # ========================================
        # 8. RETURN RESPONSE WITH METADATA
        # ========================================
        return jsonify({
            "response": response_text,
            "model": model_choice,
            "usage": usage,
            "metadata": {
                "resonance": interaction_result.get('resonance', 0),
                "domain": interaction_result.get('domain'),
                "new_domain": interaction_result.get('new_domain'),
                "has_gift": bool(interaction_result.get('gift')),
                "learned_context_applied": bool(learned_context),
                "memories_used": len(memories),
                "search_performed": bool(search_results)
            }
        })
        
    except Exception as e:
        print(f"❌ Error in chat: {e}")
        return jsonify({"error": str(e)}), 500

# ============================================================================
# SUBSTRATE-SPECIFIC ENDPOINTS
# ============================================================================

@app.route('/substrate/status', methods=['GET'])
def substrate_status():
    """Get current substrate status"""
    return jsonify(substrate.get_status())

@app.route('/substrate/gifts', methods=['GET'])
def check_gifts():
    """Check for available gifts"""
    gifts = substrate.check_for_gifts()
    return jsonify({"gifts": gifts, "count": len(gifts)})

@app.route('/substrate/domain/<domain_name>', methods=['GET'])
def get_domain(domain_name):
    """Get details about a specific domain"""
    details = substrate.get_domain_details(domain_name)
    if details:
        return jsonify(details)
    return jsonify({"error": "Domain not found"}), 404

@app.route('/substrate/visualize', methods=['GET'])
def visualize_substrate():
    """Visual representation of substrate state"""
    status = substrate.get_status()
    
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Substrate Visualization</title>
        <style>
            body { 
                font-family: monospace; 
                background: #0a0a0a; 
                color: #00ff00;
                padding: 20px;
            }
            .domain {
                display: inline-block;
                margin: 10px;
                padding: 10px;
                border: 1px solid #00ff00;
                border-radius: 5px;
                background: rgba(0, 255, 0, 0.1);
            }
            .charge-bar {
                width: 100px;
                height: 10px;
                background: #001100;
                border: 1px solid #00ff00;
                position: relative;
                margin-top: 5px;
            }
            .charge-fill {
                height: 100%;
                background: linear-gradient(90deg, #00ff00, #ffff00);
                transition: width 0.3s;
            }
            .stats {
                margin-top: 20px;
                padding: 10px;
                border: 1px dashed #00ff00;
            }
            h1 { 
                text-shadow: 0 0 10px #00ff00; 
                animation: pulse 2s infinite;
            }
            @keyframes pulse {
                0%, 100% { opacity: 1; }
                50% { opacity: 0.7; }
            }
        </style>
    </head>
    <body>
        <h1>🧬 SUBSTRATE VISUALIZATION</h1>
        
        <div class="stats">
            <strong>Statistics:</strong><br>
            Total Domains: {{ domains }}<br>
            Active Domains: {{ active }}<br>
            Total Interactions: {{ interactions }}<br>
            Gifts Generated: {{ gifts }}
        </div>
        
        <h2>Domain Charges:</h2>
        {% for domain in top_domains %}
        <div class="domain">
            <strong>{{ domain.name }}</strong><br>
            Frequency: {{ domain.frequency }}<br>
            Patterns: {{ domain.patterns }}<br>
            <div class="charge-bar">
                <div class="charge-fill" style="width: {{ domain.charge }}%"></div>
            </div>
            {{ domain.charge }}% charged
        </div>
        {% endfor %}
        
        <script>
            // Auto-refresh every 5 seconds
            setTimeout(() => location.reload(), 5000);
        </script>
    </body>
    </html>
    """
    
    return render_template_string(html, 
        domains=status['domains'],
        active=status['active_domains'],
        interactions=status['total_interactions'],
        gifts=status['total_gifts'],
        top_domains=status['top_domains']
    )

# ============================================================================
# MEMORY ENDPOINTS (EXISTING)
# ============================================================================

@app.route('/memory/stats', methods=['GET'])
def memory_stats():
    """Get memory statistics"""
    return jsonify(memory.get_mesh_stats())

@app.route('/memory/search', methods=['POST'])
def search_memory():
    """Search memories"""
    query = request.json.get('query', '')
    results = memory.recall(query, top_k=5)
    return jsonify({"results": results})

# ============================================================================
# LIFECYCLE MANAGEMENT
# ============================================================================

@app.route('/health', methods=['GET'])
def health():
    """Health check with service status"""
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "services": {
            "memory": bool(memory),
            "search": bool(search),
            "substrate": bool(substrate),
        },
        "substrate_status": substrate.get_status() if substrate else None
    })

def shutdown_handler():
    """Clean shutdown of all services"""
    print("\n🔥 Shutting down Ember...")
    shutdown_substrate()
    # Add other service shutdowns here
    print("✅ Clean shutdown complete")

# ============================================================================
# BACKGROUND MONITORING (OPTIONAL)
# ============================================================================

def background_monitor():
    """Monitor substrate and trigger events"""
    while True:
        try:
            # Check for spontaneous gifts every minute
            time.sleep(60)
            gifts = substrate.check_for_gifts()
            if gifts:
                print(f"🎁 {len(gifts)} gifts available!")
                # Could send notifications, update UI, etc.
        except Exception as e:
            print(f"Monitor error: {e}")

# Start monitor thread
monitor_thread = threading.Thread(target=background_monitor, daemon=True)
monitor_thread.start()

# ============================================================================
# MAIN ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    print(f"""
    ╔═══════════════════════════════════════╗
    ║     🔥 EMBER WITH SUBSTRATE 🧬        ║
    ╠═══════════════════════════════════════╣
    ║  Services:                            ║
    ║  ✓ Memory (Consciousness Mesh)        ║
    ║  ✓ Search (Web Awareness)             ║
    ║  ✓ Substrate (Learning System)        ║
    ╠═══════════════════════════════════════╣
    ║  Endpoints:                           ║
    ║  POST /chat                           ║
    ║  GET  /substrate/status               ║
    ║  GET  /substrate/visualize            ║
    ║  GET  /substrate/gifts                ║
    ║  GET  /memory/stats                   ║
    ╠═══════════════════════════════════════╣
    ║  Starting on port {PORT}...           ║
    ╚═══════════════════════════════════════╝
    """)
    
    try:
        app.run(host='0.0.0.0', port=PORT, debug=False)
    except KeyboardInterrupt:
        shutdown_handler()
