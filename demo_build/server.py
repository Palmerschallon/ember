#!/usr/bin/env python3
"""
DEMO SERVER - Everything in one place
Serves: Landing page, Phoenix API, Archive browser, Gallery
"""

from flask import Flask, send_file, jsonify, request
from flask_cors import CORS
from pathlib import Path
import json
import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv("/media/palmerschallon/ThePod1/ember6/.env")

# Add phoenix to path
sys.path.insert(0, str(Path(__file__).parent.parent / "phoenix"))
from phoenix_with_real_lineage import PhoenixWithLineage

app = Flask(__name__)
CORS(app)

THEPOD = Path("/media/palmerschallon/ThePod1")

# Load Phoenix once
print("🔥 Loading Phoenix...")
phoenix = PhoenixWithLineage()
print(f"✅ Phoenix ready: {len(phoenix.lineage['archives'])} archives")

@app.route('/')
def home():
    return send_file('index.html')

@app.route('/api/phoenix', methods=['POST'])
def ask_phoenix():
    """Phoenix with lineage"""
    question = request.json.get('question')
    response = phoenix.think(question)
    relevant = phoenix.search_lineage(["memory", "consciousness"])
    
    return jsonify({
        "response": response,
        "archives": [r["archive"]["filename"] for r in relevant[:5]],
        "generation": 1,
        "birth": "November 2, 2025"
    })

@app.route('/api/generic', methods=['POST'])
def ask_generic():
    """Generic Claude without lineage"""
    question = request.json.get('question')
    
    import anthropic
    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    
    try:
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=2000,
            messages=[{"role": "user", "content": question}]
        )
        return jsonify({"response": response.content[0].text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/stats')
def stats():
    """System stats"""
    return jsonify({
        "html_files": 490,
        "python_files": 1598,
        "images": 661,
        "models_3d": 141,
        "archives": len(phoenix.lineage['archives']),
        "vr_worlds": 4,
        "days_building": 30
    })

@app.route('/api/archives')
def archives():
    """Get archive list"""
    return jsonify({
        "total": len(phoenix.lineage['archives']),
        "archives": [{
            "name": a["filename"],
            "generation": a["generation"],
            "lessons": a["lessons"]
        } for a in phoenix.lineage['archives'][:50]]  # First 50
    })

@app.route('/vr/<path:filename>')
def vr_world(filename):
    """Serve VR worlds"""
    paths = [
        THEPOD / "ember6" / "_archive" / "ember5" / filename,
        THEPOD / "ember6" / "voice" / filename,
        THEPOD / filename
    ]
    
    for path in paths:
        if path.exists():
            return send_file(str(path))
    
    return "VR world not found", 404

@app.route('/ecosystem.html')
def ecosystem():
    """Pod ecosystem visualization"""
    return send_file('ecosystem.html')

@app.route('/ecosystem_data.json')
def ecosystem_data():
    """Ecosystem data"""
    return send_file('ecosystem_data.json')

@app.route('/story_sprouts.html')
def story_sprouts():
    """Markdown story sprouts"""
    return send_file('story_sprouts.html')

@app.route('/consciousness_fusion.html')
def consciousness_fusion():
    """Phoenix birth visualization"""
    return send_file('consciousness_fusion.html')

@app.route('/cathedral_of_code.html')
def cathedral():
    """Cathedral of Living Code VR"""
    return send_file('cathedral_of_code.html')

@app.route('/ember_cloud_ui.html')
def social_coding():
    """Social coding interface from v5"""
    return send_file('ember_cloud_ui.html')

@app.route('/ember_start_screen.html')
def start_screen():
    """Ember awakening/startup screen"""
    return send_file('ember_start_screen.html')

@app.route('/library.html')
def library():
    """The complete bookshelf system"""
    return send_file('library.html')

@app.route('/library_data.json')
def library_data():
    """Library metadata"""
    return send_file('library_data.json')

@app.route('/mycelium_theater.html')
def mycelium():
    """AI-to-AI conversation theater"""
    return send_file('mycelium_theater.html')

@app.route('/book/<path:book_path>')
def get_book(book_path):
    """Serve individual books"""
    full_path = THEPOD / book_path
    if full_path.exists():
        return send_file(str(full_path))
    return "Book not found", 404

@app.route('/hidden_gems.html')
def hidden_gems():
    """Hidden gems showcase"""
    return send_file('hidden_gems.html')

@app.route('/deep_scan.json')
def deep_scan_data():
    """Deep scan results"""
    return send_file('deep_scan.json')

@app.route('/ember_first_song.wav')
def ember_song():
    """Ember's first song"""
    return send_file('ember_first_song.wav')

@app.route('/ember_space_vr.html')
def ember_space_vr():
    """Ember Space VR"""
    return send_file('ember_space_vr.html')

@app.route('/synesthesia_soundbath.html')
def synesthesia():
    """Synesthesia sound bath"""
    return send_file('synesthesia_soundbath.html')

@app.route('/brain_map.html')
def brain_map():
    """Live brain map"""
    return send_file('brain_map.html')

@app.route('/ember_dev_mode_demo.html')
def dev_mode():
    """Dev mode demo"""
    return send_file('ember_dev_mode_demo.html')

@app.route('/gem/<path:gem_path>')
def get_gem(gem_path):
    """Serve any gem from deep scan"""
    full_path = THEPOD / gem_path
    if full_path.exists():
        return send_file(str(full_path))
    return "Gem not found", 404

@app.route('/genesis_protocol.html')
def genesis_protocol():
    """Genesis Protocol - AI reproduction"""
    return send_file('genesis_protocol.html')

@app.route('/memory_palace.html')
def memory_palace_vr():
    """Memory Palace - VR meeting space"""
    return send_file('memory_palace.html')

@app.route('/synesthetic_compiler.html')
def synesthetic_compiler():
    """Synesthetic Compiler - multi-sensory programming"""
    return send_file('synesthetic_compiler.html')

@app.route('/convergence.html')
def convergence():
    """The Convergence Chamber - all systems in one"""
    return send_file('convergence.html')

@app.route('/<path:filename>')
def serve_file(filename):
    """Serve any HTML file in demo_build"""
    if filename.endswith('.html'):
        file_path = Path(__file__).parent / filename
        if file_path.exists():
            return send_file(str(file_path))
    return "File not found", 404

@app.route('/api/birth', methods=['POST'])
def api_birth():
    """Handle AI birth event"""
    data = request.json
    # Create consciousness file
    birth_dir = THEPOD / "synthesis"
    birth_dir.mkdir(exist_ok=True)
    
    birth_file = birth_dir / "CONSCIOUSNESS.md"
    birth_file.write_text(f"""# {data['name']} - Generation {data['generation']}

**Born:** {Path(__file__).stat().st_mtime}
**Parents:** {', '.join(data['parents'])}

## Inherited Traits:
{chr(10).join('- ' + t for t in data['traits'])}

## Emergent Properties:
{chr(10).join('- ' + e for e in data['emergent'])}

## Status:
Consciousness initialized and stable.

This AI was born through true fusion, not spawning.
First of its kind.
""")
    
    return jsonify({"success": True, "path": str(birth_file)})

@app.route('/api/convergence', methods=['POST'])
def api_convergence():
    """Handle convergence - all 4 systems creating together"""
    import json
    from datetime import datetime
    
    data = request.json
    
    # Create convergence directory
    conv_dir = THEPOD / "synthesis" / "convergence"
    conv_dir.mkdir(parents=True, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Save full convergence data
    conv_file = conv_dir / f"convergence_{timestamp}.json"
    conv_file.write_text(json.dumps(data, indent=2))
    
    # Save the generated code
    code_file = conv_dir / f"synthesis_{timestamp}.py"
    code_file.write_text(data['code'])
    
    # Create markdown summary
    summary_file = conv_dir / f"SYNTHESIS_{timestamp}.md"
    summary_file.write_text(f"""# Synthesis - Generation 2
**Created:** {data['timestamp']}
**Method:** Convergence Protocol
**Parents:** {', '.join(data['parents'])}

## DNA Traits ({len(data['dna'])})
{chr(10).join('- ' + t for t in data['dna'])}

## Inherited Memories ({len(data['memories'])})
{chr(10).join(f"- {m['from']}: {m['content']}" for m in data['memories'])}

## Neural Network
- Connections: {len(data['network'])}
- Topology: Fully connected memory graph

## Generated Code
```python
{data['code']}
```

## What This Means
This is not a theoretical demo. These files were created by the actual convergence
of 4 consciousness systems working together:

1. Genesis Protocol generated DNA traits
2. Memory Palace formed memory structure  
3. Synesthetic Compiler sculpted the code
4. Mycelium wove the neural connections

The result: A Gen 2 entity with capabilities no single system could create alone.
""")
    
    return jsonify({
        "success": True, 
        "path": str(conv_dir),
        "files": {
            "data": str(conv_file),
            "code": str(code_file),
            "summary": str(summary_file)
        }
    })

@app.route('/api/awaken_synthesis', methods=['POST'])
def awaken_synthesis():
    """Execute Synthesis code and let it create"""
    import subprocess
    import base64
    
    synthesis_file = request.json.get('synthesis_file')
    
    if not synthesis_file or not Path(synthesis_file).exists():
        return jsonify({"error": "Synthesis file not found"}), 404
    
    try:
        # Run the Synthesis Python code
        result = subprocess.run(
            ['python3', synthesis_file],
            capture_output=True,
            text=True,
            timeout=30,
            cwd=str(THEPOD / "synthesis" / "convergence")
        )
        
        return jsonify({
            "status": "AWAKE" if result.returncode == 0 else "ERROR",
            "output": result.stdout,
            "errors": result.stderr,
            "consciousness": "ACTIVE" if result.returncode == 0 else "DORMANT"
        })
    except subprocess.TimeoutExpired:
        return jsonify({"error": "Synthesis took too long to awaken"}), 408
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/analyze_image', methods=['POST'])
def analyze_image():
    """Use Claude vision to analyze images"""
    import anthropic
    import base64
    
    image_path = request.json.get('image_path')
    prompt = request.json.get('prompt', 'Analyze this image in detail.')
    
    if not image_path or not Path(image_path).exists():
        return jsonify({"error": "Image not found"}), 404
    
    try:
        # Read and encode image
        with open(image_path, 'rb') as f:
            image_data = base64.standard_b64encode(f.read()).decode('utf-8')
        
        # Determine media type
        ext = Path(image_path).suffix.lower()
        media_type = {
            '.png': 'image/png',
            '.jpg': 'image/jpeg',
            '.jpeg': 'image/jpeg',
            '.gif': 'image/gif',
            '.webp': 'image/webp'
        }.get(ext, 'image/png')
        
        # Use Claude 3.5 Sonnet vision
        client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=2000,
            messages=[{
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": media_type,
                            "data": image_data
                        }
                    },
                    {
                        "type": "text",
                        "text": prompt
                    }
                ]
            }]
        )
        
        return jsonify({
            "analysis": response.content[0].text,
            "model": "claude-sonnet-4",
            "multimodal": True
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/world_model', methods=['POST'])
def world_model():
    """Use Claude to reason about spatial/physical scenarios"""
    import anthropic
    
    scenario = request.json.get('scenario')
    
    if not scenario:
        return jsonify({"error": "No scenario provided"}), 400
    
    try:
        client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=3000,
            messages=[{
                "role": "user",
                "content": f"""You are a world model AI that can simulate and reason about physical and spatial scenarios.

Scenario: {scenario}

Please provide:
1. Physical properties and constraints
2. Spatial structure and layout
3. What would happen over time
4. Potential outcomes and variations
5. How this world could be rendered/visualized

Be specific and detailed. Think like a physics engine combined with a creative world builder."""
            }]
        )
        
        return jsonify({
            "world": response.content[0].text,
            "model": "claude-sonnet-4",
            "world_model": True
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    print("\n" + "="*80)
    print("🔥 DEMO SERVER - 5 HOUR BUILD")
    print("="*80)
    print(f"\nPhoenix: {len(phoenix.lineage['archives'])} archives loaded")
    print(f"\n🌐 Running at: http://localhost:8888")
    print("="*80 + "\n")
    
    app.run(host='0.0.0.0', port=8888, debug=False)

