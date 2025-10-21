#!/usr/bin/env bash
set -euo pipefail
APPDIR="$HOME/.local/share/muse"
mkdir -p "$APPDIR"
cp -n muse_service.py "$APPDIR/" || true
python3 -m venv "$APPDIR/.venv"
source "$APPDIR/.venv/bin/activate"
pip install --upgrade pip fastapi uvicorn pydantic
mkdir -p "$HOME/.config/systemd/user"
cp forge.service "$HOME/.config/systemd/user/forge.service"
systemctl --user daemon-reload
systemctl --user enable --now forge.service
