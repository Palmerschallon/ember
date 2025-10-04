# Ember Architecture

## Overview
Ember is a Flask-based backend with a Canvas2D viewer frontend for exploring and managing a procedurally generated universe.

## Components

### Backend (Flask)
- **Framework**: Flask with SSE support
- **Configuration**: Environment variables via `.env`
- **Storage**: All paths under `/Volumes/ThePod`

### Frontend (Canvas2D)
- **Viewer**: HTML5 Canvas-based 2D viewer
- **Features**: 
  - Camera zoom-to-cursor (Ticket 1)
  - Interactive universe exploration
  - LOD rendering (Ticket 3)

### API Endpoints
- `GET /` - Serves the frontend viewer
- `GET /health` - Health check endpoint
- `POST /api/chat` - Chat interface with LLM
- `POST /api/upload` - File upload endpoint
- `GET /api/events` - Server-Sent Events stream

### Data Layer
- **Universe Factory**: Deterministic procedural generation (Ticket 2)
- **LLM Adapter**: Pluggable LLM interface (default: Ollama)
- **Memory System**:
  - Chat logs: `/memory/chat/*.jsonl`
  - Events: `/memory/short/events.jsonl`

## Key Features

### 1. Camera Zoom-to-Cursor (Ticket 1)
Canvas camera system that zooms toward the cursor position rather than the center.

### 2. Deterministic Universe Factory (Ticket 2)
Procedural generation system with seed-based reproducibility for universe entities.

### 3. LOD Promotion (Ticket 3)
Level-of-Detail system that promotes/demotes entity detail based on camera distance.

## Storage Structure
```
/Volumes/ThePod/
  ├── memory/
  │   ├── chat/
  │   │   └── *.jsonl
  │   └── short/
  │       └── events.jsonl
  └── uploads/
```
