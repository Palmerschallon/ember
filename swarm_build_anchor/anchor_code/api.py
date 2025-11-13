from flask import Flask, jsonify, request
from pathlib import Path
from database import AnchorDB

app = Flask(__name__)
db = AnchorDB(Path.home() / ".anchor" / "ledger.db")

@app.route('/anchor', methods=['POST'])
def create_anchor():
    """HTTP endpoint for creating anchors"""
    data = request.json
    anchor_hash = db.anchor(
        agent_id=data.get('agent_id', 'api'),
        content=data['content'],
        metadata=data.get('metadata')
    )
    return jsonify({'hash': anchor_hash})

@app.route('/anchor/<anchor_hash>')
def get_anchor(anchor_hash):
    """Retrieve an anchor via HTTP"""
    anchor = db.retrieve(anchor_hash)
    if anchor:
        return jsonify(anchor)
    return jsonify({'error': 'Anchor not found'}), 404

@app.route('/chain')
def get_chain():
    """Get recent chain via HTTP"""
    limit = request.args.get('limit', 100, type=int)
    return jsonify(db.get_chain(limit))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)
