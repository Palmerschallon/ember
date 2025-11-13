
# Anchor Suite Smoke Test Checklist

Goal: confirm that Anchor is alive, integrated, and visible from both human + agent sides.

---

## 1. CLI / Ledger Basics

- [ ] From the `anchor/` directory, install in editable mode:

  ```bash
  cd anchor
  pip install -e .
  ```

- [ ] Run:

  ```bash
  anchor add "Smoke test: first anchor."
  ```

  Expect:
  - "Anchored entry" message
  - Timestamp and ID printed

- [ ] Run:

  ```bash
  anchor list
  ```

  Expect:
  - At least one entry visible with the text preview.

- [ ] Run:

  ```bash
  anchor verify "Smoke test: first anchor."
  ```

  Expect:
  - "Verified entries" with matching timestamp/id/hash.

- [ ] Confirm the ledger file exists:

  - `~/.anchor/ledger.sqlite3` (or overridden via `ANCHOR_HOME`)

---

## 2. HTTP API

- [ ] Start the server:

  ```bash
  anchor serve --port 7171
  ```

- [ ] In another shell, check health:

  ```bash
  curl http://127.0.0.1:7171/health
  ```

  Expect:
  - `{"status":"ok"}`

- [ ] Add an entry via API:

  ```bash
  curl -X POST http://127.0.0.1:7171/entries \
    -H "Content-Type: application/json" \
    -d '{"text": "Smoke test via API", "meta": {"source":"curl","type":"note"}}'
  ```

- [ ] List entries:

  ```bash
  curl "http://127.0.0.1:7171/entries?limit=5"
  ```

  Expect:
  - JSON array including the API-created entry.

- [ ] Verify via API:

  ```bash
  curl -X POST http://127.0.0.1:7171/verify \
    -H "Content-Type: application/json" \
    -d '{"text":"Smoke test via API"}'
  ```

  Expect:
  - JSON array with matching entry.

---

## 3. Ember Integration

- [ ] Ensure `anchor/anchor_client.py` and `anchor/ember_memory_adapter.py` are importable in Ember’s environment.

- [ ] In an Ember context (Python REPL or agent code), run:

  ```python
  from anchor_client import AnchorClient
  from ember_memory_adapter import EmberMemory

  client = AnchorClient("http://127.0.0.1:7171")
  mem = EmberMemory(client)

  print("Health:", mem.is_available())
  e = mem.remember(
      "Smoke test from Ember.",
      project="ember",
      kind="note",
      importance=0.9,
  )
  print(e)
  ```

  Expect:
  - Health is `True`.
  - New AnchorEntry printed with id, ts_utc, text, meta.

- [ ] Confirm the new entry appears in:

  ```bash
  anchor list
  ```

  and via:

  ```bash
  curl "http://127.0.0.1:7171/entries?limit=10"
  ```

---

## 4. Pod UI / Anchor Panel

- [ ] Ensure `AnchorPanel.tsx` and `anchorClient.ts` are included in your frontend build.

- [ ] Embed `AnchorPanel` in your Pod shell (e.g. `PodShell.tsx`) and load the UI.

- [ ] With `anchor serve` running, open the Pod UI in the browser.

  Expect:
  - Panel header shows “Anchor”.
  - Status indicator: `Local · Online` (or equivalent).
  - If ledger has entries, recent anchors are listed.

- [ ] In the input box “Anchor a moment…”, type:

  > `Smoke test via UI.`

  and click the button / press enter.

  Expect:
  - New card appears in the list.
  - The entry also shows up in:
    - `anchor list`
    - `GET /entries`

---

## 5. Symmetry Check

- [ ] Confirm that a single entry added through any of:
  - CLI (`anchor add`)
  - API (`POST /entries`)
  - Ember (`EmberMemory.remember`)
  - UI (`AnchorPanel`)

  …is visible from all of:
  - `anchor list`
  - `GET /entries`
  - `EmberMemory.recent()`
  - AnchorPanel UI

If all checks pass, the spine is alive, the Pod sees it, Ember uses it, and the organism is coherent enough to iterate on.
