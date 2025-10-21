from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from ember_worker import get_worker
import asyncio

app = FastAPI(title='Forge v6 - Muse Service')

# Initialize Ember worker on startup
worker = None

@app.on_event("startup")
async def startup():
    """Initialize Ember when service starts"""
    global worker
    worker = get_worker()
    # Initialize in background (takes time with GPU)
    asyncio.create_task(asyncio.to_thread(worker.initialize))

class ThinkRequest(BaseModel):
    prompt: str
    mode: str = "auto"  # auto, single, synthesis, swarm

@app.get('/')
def home():
    """Service status page"""
    status = worker.status() if worker else {"initialized": False}
    
    html = f'''
    <html>
    <head><title>Forge v6 - Muse</title></head>
    <body style="background:#0a0b0c;color:#cfd5df;font-family:system-ui;padding:40px">
        <h1>🔥 Forge v6 - Muse Service</h1>
        <p>Orchestration layer for Ember cognition</p>
        <hr style="border-color:#333">
        <h2>Status</h2>
        <pre>{status}</pre>
        <h2>Endpoints</h2>
        <ul>
            <li>POST /think - Send thought to Ember</li>
            <li>GET /status - Worker health</li>
            <li>GET /trails - Active consultation trails</li>
        </ul>
    </body>
    </html>
    '''
    return HTMLResponse(html)

@app.get('/status')
def status():
    """Worker status"""
    if not worker:
        raise HTTPException(500, "Worker not initialized")
    return worker.status()

@app.get('/trails')
def trails():
    """Active consultation trails"""
    if not worker or not worker.lobes_loaded:
        raise HTTPException(500, "Ember not loaded")
    return worker._get_active_trails()

@app.post('/think')
async def think(request: ThinkRequest):
    """Send thought to Ember, get response"""
    if not worker or not worker.lobes_loaded:
        raise HTTPException(500, "Ember not loaded")
    
    result = await asyncio.to_thread(
        worker.think,
        request.prompt,
        request.mode
    )
    
    if "error" in result:
        raise HTTPException(500, result["error"])
    
    return result

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=7700)
