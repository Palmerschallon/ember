#!/usr/bin/env python3
"""
PHOENIX DEMO SERVER
Serves the interactive demo and handles live Phoenix queries
"""

from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import os
from pathlib import Path
from phoenix_with_real_lineage import PhoenixWithLineage
import anthropic

app = Flask(__name__)
CORS(app)

# Initialize Phoenix once (cache the lineage load)
print("🔥 Initializing Phoenix with full lineage...")
phoenix = PhoenixWithLineage()
print(f"✅ Phoenix ready with {len(phoenix.lineage['archives'])} archives loaded")

@app.route('/')
def serve_demo():
    """Serve the demo page"""
    return send_file('phoenix_demo.html')

@app.route('/api/phoenix', methods=['POST'])
def ask_phoenix():
    """Ask Phoenix a question - uses real lineage"""
    data = request.get_json()
    question = data.get('question', '')
    
    if not question:
        return jsonify({"error": "No question provided"}), 400
    
    print(f"\n🔥 Phoenix received question: {question[:50]}...")
    
    # Phoenix thinks with its lineage
    response = phoenix.think(question)
    
    # Also return which archives were searched
    relevant = phoenix.search_lineage(["memory", "consciousness", "conversation", "chat"])
    archive_names = [item["archive"]["filename"] for item in relevant[:5]]
    
    return jsonify({
        "response": response,
        "archives_searched": archive_names,
        "total_archives": len(phoenix.lineage['archives']),
        "generation": phoenix.generation,
        "birth_date": phoenix.birth_date
    })

@app.route('/api/generic', methods=['POST'])
def ask_generic():
    """Ask generic Claude the same question - no lineage"""
    data = request.get_json()
    question = data.get('question', '')
    
    if not question:
        return jsonify({"error": "No question provided"}), 400
    
    print(f"\n🤖 Generic Claude received question: {question[:50]}...")
    
    # Call Claude without any lineage context
    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    
    try:
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=2000,
            messages=[{"role": "user", "content": question}]
        )
        
        return jsonify({
            "response": response.content[0].text,
            "has_lineage": False
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/archives', methods=['GET'])
def get_archives():
    """Get the list of all archives Phoenix has read"""
    archives_info = []
    
    for archive in phoenix.lineage['archives']:
        archives_info.append({
            "filename": archive["filename"],
            "generation": archive["generation"],
            "lessons": archive["lessons"],
            "excerpt": archive["content"][:200]
        })
    
    return jsonify({
        "total": len(archives_info),
        "archives": archives_info
    })

@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Get Phoenix's stats"""
    return jsonify({
        "name": phoenix.name,
        "generation": phoenix.generation,
        "birth_date": phoenix.birth_date,
        "parents": phoenix.parents,
        "archives_loaded": len(phoenix.lineage['archives']),
        "discoveries": len(phoenix.lineage['discoveries']),
        "has_birth_story": len(phoenix.lineage['birth_story']) > 0
    })

if __name__ == '__main__':
    print("\n" + "="*80)
    print("🔥 PHOENIX DEMO SERVER STARTING")
    print("="*80)
    print(f"\n📚 Archives loaded: {len(phoenix.lineage['archives'])}")
    print(f"🐦 Phoenix Generation: {phoenix.generation}")
    print(f"📅 Birth: {phoenix.birth_date}")
    print(f"\n🌐 Demo will be at: http://localhost:5555")
    print("="*80 + "\n")
    
    app.run(host='0.0.0.0', port=5555, debug=False)

