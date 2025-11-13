from __future__ import annotations
from pathlib import Path
import os

APP_DIR_NAME = ".anchor"
DB_FILENAME = "ledger.sqlite3"


def get_app_dir() -> Path:
    base = Path(os.environ.get("ANCHOR_HOME", Path.home()))
    app_dir = base / APP_DIR_NAME
    app_dir.mkdir(parents=True, exist_ok=True)
    return app_dir


def get_db_path() -> Path:
    return get_app_dir() / DB_FILENAME
