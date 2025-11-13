#!/usr/bin/env python3
"""
DREAM API - HTTP interface for the dream system

Allows Ember (or any process) to report successful executions,
and query the state of cognitive processes.
"""

from flask import Flask, request, jsonify
from dream_system import DreamSystem, BackgroundDreamer
from pathlib import Path

app = Flask(__name__)

# Initialize dream system
dream_system = DreamSystem()
dreamer = BackgroundDreamer(dream_system, interval=300)  # 5 minute cycles

@app.route('/health', methods=['GET'])
def health():
    """Health check"""
    return jsonify({"status": "ok", "system": "dream_api"})

@app.route('/status', methods=['GET'])
def status():
    """Get current dream system status"""
    processes = {
        pid: p.to_dict() 
        for pid, p in dream_system.processes.items()
    }
    return jsonify({
        "processes": processes,
        "trained_lobes": dream_system.trained_lobes,
        "process_count": len(dream_system.processes)
    })

@app.route('/record', methods=['POST'])
def record_experience():
    """
    Record a successful execution.
    
    POST /record
    {
        "process_type": "recursion",
        "description": "Successfully executed recursive function",
        "metadata": {...}
    }
    """
    data = request.json
    
    if not data or 'process_type' not in data or 'description' not in data:
        return jsonify({
            "error": "Missing required fields: process_type, description"
        }), 400
    
    process_type = data['process_type']
    description = data['description']
    
    dream_system.record_success(process_type, description)
    
    return jsonify({
        "status": "recorded",
        "process_type": process_type,
        "description": description
    })

@app.route('/dream_cycle', methods=['POST'])
def trigger_dream_cycle():
    """Manually trigger a dream cycle"""
    dream_system.dream_cycle()
    return jsonify({"status": "dream_cycle_complete"})

@app.route('/train/<process_id>', methods=['POST'])
def train_process(process_id):
    """Manually trigger LoRA training for a specific process"""
    success = dream_system.train_lora(process_id)
    
    if success:
        return jsonify({
            "status": "training_prepared",
            "process_id": process_id
        })
    else:
        return jsonify({
            "status": "training_failed",
            "process_id": process_id,
            "error": "Process not ready or doesn't exist"
        }), 400

@app.route('/process/<process_id>', methods=['GET'])
def get_process(process_id):
    """Get details about a specific process"""
    process = dream_system.processes.get(process_id)
    
    if not process:
        return jsonify({"error": "Process not found"}), 404
    
    return jsonify(process.to_dict())

if __name__ == '__main__':
    print("DREAM API - Starting...")
    print(f"Current state: {len(dream_system.processes)} processes")
    
    # Start background dreaming
    dreamer.start()
    
    print("\nDream API running on http://localhost:7793")
    print("Background dreaming active (5 min cycles)")
    
    try:
        app.run(host='0.0.0.0', port=7793, debug=False)
    finally:
        dreamer.stop()

