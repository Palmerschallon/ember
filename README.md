# Ember

A Flask-based universe explorer with Canvas2D visualization, featuring deterministic procedural generation and intelligent camera controls.

## Features

### Implemented Tickets

#### ✅ Ticket 1: Camera Zoom-to-Cursor
- Mouse wheel zoom targets cursor position instead of viewport center
- Smooth zoom transitions that keep the point under cursor stationary
- No viewport jumping or jittering

#### ✅ Ticket 2: Deterministic Universe Factory
- Seed-based procedural generation of universes
- Same seed always produces identical universe
- Generates stars, planets, asteroids, and nebulae
- Reproducible and JSON-serializable

#### ✅ Ticket 3: LOD Promotion System
- Three detail levels: low, medium, high
- Automatic promotion/demotion based on screen size
- Distance-based culling for performance
- Smooth transitions between detail levels

### API Endpoints

- `GET /` - Serves the Canvas2D viewer interface
- `GET /health` - Health check endpoint
- `POST /api/chat` - Chat with LLM (via Ollama by default)
- `POST /api/upload` - Upload files
- `GET /api/events` - Server-Sent Events stream
- `GET /api/universe?seed=<int>&entities=<int>` - Generate/retrieve universe

### Architecture

- **Backend**: Flask with SSE support
- **Frontend**: HTML5 Canvas2D with vanilla JavaScript
- **LLM**: Pluggable adapter system (Ollama default)
- **Memory**: JSONL logging for chat and events
- **Storage**: Configurable via `.env` (default: `/Volumes/ThePod`)

## Setup

### Prerequisites

- Python 3.8+
- Ollama (optional, for chat functionality)

### Installation

1. Clone the repository:
```bash
cd /path/to/ember
```

2. Create a virtual environment and install dependencies:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Create `.env` file from example:
```bash
cp .env.example .env
```

4. Edit `.env` to configure paths:
```env
BASE_PATH=/Volumes/ThePod  # Or your preferred path
```

**Note**: For local testing without `/Volumes/ThePod`, you can use `/tmp/ember_data` or any other writable path.

5. (Optional) Install and start Ollama for chat functionality:
```bash
# Install Ollama from https://ollama.ai
ollama pull llama2
ollama serve
```

### Running

Start the Flask server:
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Testing

### Manual Test Steps

#### Test 1: Camera Zoom-to-Cursor (Ticket 1)
1. Open `http://localhost:5000` in browser
2. Wait for universe to load
3. Move mouse to a specific entity (e.g., a bright star)
4. Scroll mouse wheel to zoom in
5. **Expected**: The entity under cursor stays in place
6. Scroll to zoom out
7. **Expected**: Still tracks cursor position
8. Try zooming on different parts of the viewport
9. **Expected**: Each point zooms towards cursor, not center

#### Test 2: Deterministic Universe Factory (Ticket 2)
1. Note the current seed (displayed in controls, default: 42)
2. Click "Regenerate" button
3. **Expected**: Same universe appears (same positions, colors, types)
4. Change seed input to 123 and click "Set Seed"
5. **Expected**: Different universe appears
6. Change back to 42
7. **Expected**: Original universe reappears exactly

#### Test 3: LOD Promotion System (Ticket 3)
1. Start with default view (zoom 1.0)
2. Observe LOD level indicator (should show "medium")
3. Zoom in significantly (zoom > 2.0)
4. **Expected**: LOD changes to "high", entities show more detail
5. Zoom out significantly (zoom < 0.5)
6. **Expected**: LOD changes to "low", entities become simple dots
7. Observe rendering performance
8. **Expected**: Distant/small entities are culled, maintaining smooth FPS

#### Test 4: API Endpoints
```bash
# Health check
curl http://localhost:5000/health

# Get universe
curl http://localhost:5000/api/universe?seed=42&entities=50

# Chat (requires Ollama)
curl -X POST http://localhost:5000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello!"}'

# Upload file
curl -X POST http://localhost:5000/api/upload \
  -F "file=@test.txt"
```

#### Test 5: Memory/Logging
1. Send a chat message
2. Check logs:
```bash
# Chat logs (replace path with your BASE_PATH)
ls -la /Volumes/ThePod/memory/chat/
cat /Volumes/ThePod/memory/chat/chat_*.jsonl

# Event logs
cat /Volumes/ThePod/memory/short/events.jsonl
```
3. **Expected**: JSONL entries for chat interactions and events

### Automated Testing

Create a test file:
```python
# test_universe.py
from backend.universe_factory import UniverseFactory

def test_determinism():
    u1 = UniverseFactory.from_seed(42, 10)
    u2 = UniverseFactory.from_seed(42, 10)
    assert u1 == u2, "Same seed should produce same universe"
    
def test_different_seeds():
    u1 = UniverseFactory.from_seed(42, 10)
    u2 = UniverseFactory.from_seed(123, 10)
    assert u1 != u2, "Different seeds should produce different universes"

if __name__ == '__main__':
    test_determinism()
    test_different_seeds()
    print("All tests passed!")
```

Run:
```bash
python test_universe.py
```

## Project Structure

```
ember/
├── app.py                          # Main Flask application
├── backend/
│   ├── adapters/
│   │   └── llm_adapter.py         # LLM adapter (Ollama)
│   ├── universe_factory.py        # Ticket 2: Deterministic generation
│   └── memory_logger.py           # JSONL logging
├── frontend/
│   ├── index.html                 # Main HTML
│   └── static/
│       ├── css/
│       │   └── style.css          # Styles
│       └── js/
│           ├── camera.js          # Ticket 1: Zoom-to-cursor
│           ├── lod.js             # Ticket 3: LOD system
│           ├── universe.js        # Universe data management
│           ├── renderer.js        # Canvas rendering
│           ├── chat.js            # Chat interface
│           └── main.js            # App initialization
├── Shared/
│   ├── CURSOR_RULES.md            # Development guidelines
│   └── TICKETS.md                 # Ticket specifications
├── ARCHITECTURE.md                # Architecture documentation
├── requirements.txt               # Python dependencies
├── .env.example                   # Environment template
└── .gitignore                     # Git ignore rules
```

## Configuration

Edit `.env` file:

```env
# Base path for all data
BASE_PATH=/Volumes/ThePod

# Memory paths
MEMORY_CHAT_PATH=/Volumes/ThePod/memory/chat
MEMORY_EVENTS_PATH=/Volumes/ThePod/memory/short
UPLOADS_PATH=/Volumes/ThePod/uploads

# LLM Configuration
LLM_PROVIDER=ollama
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama2

# Flask Configuration
FLASK_ENV=development
FLASK_PORT=5000
FLASK_HOST=0.0.0.0
```

## Controls

- **Mouse Wheel**: Zoom in/out (zooms toward cursor)
- **Click + Drag**: Pan camera
- **Reset View**: Return to default view
- **Regenerate**: Regenerate current universe
- **Set Seed**: Generate universe from specific seed

## Memory Storage

All data stored under `BASE_PATH` (from `.env`):

```
/Volumes/ThePod/
├── memory/
│   ├── chat/
│   │   └── chat_YYYYMMDD.jsonl   # Daily chat logs
│   └── short/
│       └── events.jsonl           # Event stream log
└── uploads/                       # Uploaded files
```

## License

MIT