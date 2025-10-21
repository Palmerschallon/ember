from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app=FastAPI(title='Forge v6')
@app.get('/')
def home(): return HTMLResponse('<body style=background:#0a0b0c;color:#cfd5df;font-family:system-ui>Forge v6 running</body>')
if __name__=='__main__':
 import uvicorn; uvicorn.run(app, host='127.0.0.1', port=7700)
