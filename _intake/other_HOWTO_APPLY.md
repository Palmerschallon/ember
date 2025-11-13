# How to apply the core fixes

## 1) Add two drop-in modules
Copy `ember/eventbus.py` and `ember/routes_viewers.py` into your project.

## 2) Wire them in `app.py` (minimal edits)
```python
from ember.eventbus import EventBus
from ember.routes_viewers import bp_viewers
from flask import Flask, request, jsonify
import time

app = Flask(__name__)
BUS = EventBus(maxlen=5000)
app.register_blueprint(bp_viewers)

@app.get("/health")
def health():
    return jsonify({"ok": True, "ts": time.time()})

@app.get("/api/events")
def api_events():
    cursor = int(request.args.get("cursor", "0"))
    items = BUS.since(cursor)
    return jsonify({"ok": True, "events": items, "cursor": BUS.last_id()})
```

Emit events in your handlers:
```python
BUS.emit("swarm:attractor", params=payload)
```

## 3) Serve the viewers
Ensure `.env` contains:
```
VIEWERS_DIR=/Volumes/ThePod/viewers
```

## 4) Avoid duplicate endpoints
Make sure each `@app.route` is defined once and each function name is unique.

## 5) Free a busy port
```bash
bash scripts/kill_ember_port.sh 7777
```

## 6) Client polling
```js
let cursor = 0;
async function pull(){
  const r = await fetch(`/api/events?cursor=${cursor}`);
  const j = await r.json();
  j.events.forEach(handle);
  cursor = j.cursor;
}
setInterval(pull, 1000);
```
