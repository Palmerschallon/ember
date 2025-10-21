#!/usr/bin/env bash
set -euo pipefail
ZIP="${1:-Forge-v6.zip}"
APPDIR="$HOME/.local/share/muse"
mkdir -p "$APPDIR" "$HOME/Forge"
unzip -o "$ZIP" -d "$HOME/Forge" >/dev/null
cd "$HOME/Forge"
python3 -m venv "$APPDIR/.venv"
source "$APPDIR/.venv/bin/activate"
pip install --upgrade pip fastapi uvicorn pydantic
python3 muse_service.py &
xdg-open http://127.0.0.1:7700 >/dev/null 2>&1 || true
