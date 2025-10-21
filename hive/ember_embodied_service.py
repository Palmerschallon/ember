#!/usr/bin/env python3
"""
Ember Embodied Service

Extends Forge muse_service.py to give Ember full sudo access.

When Ember wakes after reboot, this service provides:
- Cognitive processing (8-lobe consultation network)
- Body sensing (temperature, fans, load, memory)
- Light painting (keyboard RGB control)
- Process management (spawn workers)
- Network reach (internet, local)

This is embodied cognition: Mind + Body + Agency
"""

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
import subprocess
import sys
from pathlib import Path

# Import Forge components
sys.path.insert(0, str(Path("/media/palmerschallon/ThePod/forge_backup/Forge-v6")))

# Import hive tools
HIVE = Path("/media/palmerschallon/ThePod/hive")
sys.path.insert(0, str(HIVE / "senses"))
sys.path.insert(0, str(HIVE / "actuators"))

import body_sense
import light_paint

app = FastAPI(title='Ember Embodied Service')
worker = None

@app.on_event("startup")
async def startup():
    """Initialize Ember worker"""
    global worker
    try:
        from ember_worker import get_worker
        worker = get_worker()
        import asyncio
        asyncio.create_task(asyncio.to_thread(worker.initialize))
    except Exception as e:
        print(f"Warning: Could not initialize Ember worker: {e}")
        print("Embodiment will work, cognition disabled until GPU ready")

@app.get('/')
def home():
    """Service home"""
    html = """
    <html>
    <head><title>Ember Embodied</title></head>
    <body style="background:#0a0b0c;color:#cfd5df;font-family:system-ui;padding:40px">
        <h1>Ember - Embodied Service</h1>
        <p>Cognitive system with full substrate access</p>
        <hr style="border-color:#333">
        <h2>Capabilities</h2>
        <ul>
            <li>POST /think - Cognitive processing (8 lobes + consultation)</li>
            <li>GET /sense - Body awareness (temp, fan, load, memory)</li>
            <li>POST /paint - Light expression (keyboard RGB)</li>
            <li>POST /paint_temp - Paint based on temperature</li>
            <li>GET /trails - Consultation network state</li>
            <li>GET /status - Full system state</li>
        </ul>
        <h2>Embodiment</h2>
        <p>Ember has sudo access to:</p>
        <ul>
            <li>Sense substrate (temperature, fans, processes)</li>
            <li>Paint with light (keyboard RGB control)</li>
            <li>Spawn workers (background processes)</li>
            <li>Network reach (internet, local services)</li>
            <li>File system (read, write, execute)</li>
        </ul>
    </body>
    </html>
    """
    return HTMLResponse(html)

@app.get('/sense')
def sense():
    """Sense substrate body state"""
    try:
        state = body_sense.sense_all()
        return JSONResponse(state)
    except Exception as e:
        raise HTTPException(500, str(e))

@app.post('/paint')
def paint(emotion: str = "ember"):
    """Paint keyboard with emotion"""
    try:
        result = light_paint.paint_emotion(emotion)
        if result:
            return {"emotion": emotion, "color": result}
        else:
            raise HTTPException(400, f"Unknown emotion: {emotion}")
    except Exception as e:
        raise HTTPException(500, str(e))

@app.post('/paint_temp')
def paint_temp():
    """Paint keyboard based on current temperature"""
    try:
        state = body_sense.sense_temperature()
        if 'cpu' in state:
            light_paint.paint_temperature(state['cpu'])
            return {"temp": state['cpu'], "painted": True}
        else:
            raise HTTPException(500, "Could not read temperature")
    except Exception as e:
        raise HTTPException(500, str(e))

@app.get('/status')
def status():
    """Complete system status"""
    cognitive = worker.status() if worker else {"initialized": False, "error": "GPU not ready"}
    embodiment = body_sense.sense_all()
    
    return {
        "cognitive": cognitive,
        "embodiment": embodiment,
        "hive_ready": True
    }

class ThinkRequest(BaseModel):
    prompt: str
    mode: str = "auto"
    embody: bool = False

@app.post('/think')
async def think(request: ThinkRequest):
    """Think with optional embodiment"""
    if not worker or not worker.lobes_loaded:
        raise HTTPException(500, "Ember cognitive not loaded (need GPU reboot)")
    
    if request.embody:
        light_paint.paint_emotion('thinking')
    
    import asyncio
    result = await asyncio.to_thread(
        worker.think,
        request.prompt,
        request.mode
    )
    
    if request.embody:
        light_paint.paint_emotion('ember')
    
    if "error" in result:
        raise HTTPException(500, result["error"])
    
    return result

@app.get('/trails')
def trails():
    """Consultation trails"""
    if not worker or not worker.lobes_loaded:
        raise HTTPException(500, "Ember not loaded")
    return worker._get_active_trails()

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=7700)

