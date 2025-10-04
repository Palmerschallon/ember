# Cursor Rules

## Development Guidelines

### Code Style
- Python: PEP 8 compliant
- JavaScript: ES6+ with semicolons
- 4 spaces for indentation

### Project Structure
- Backend code in `/backend`
- Frontend code in `/frontend`
- Shared utilities in `/Shared`

### Configuration
- Use environment variables for all configurable paths
- Never hardcode paths outside of .env
- All data paths relative to BASE_PATH from .env

### Testing
- Test all API endpoints
- Test camera controls
- Test universe generation determinism

### Memory/Logging
- Chat interactions logged to JSONL format
- Events streamed and logged for replay
- All logs under /memory hierarchy
