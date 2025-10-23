#!/usr/bin/env python3
"""
Reddit Autopost (r/TheNexus)
- Reads credentials from environment variables
- Loads a share queue JSON (default: state/share_queue.json)
- Posts the next queued item (title + either selftext or link)
- Marks it posted with a timestamp

Env:
  REDDIT_CLIENT_ID
  REDDIT_CLIENT_SECRET
  REDDIT_USERNAME
  REDDIT_PASSWORD
  REDDIT_USER_AGENT (e.g., EmberAutopost/1.0 by u/<name>)
  REDDIT_SUBREDDIT (default: TheNexus)
  REDDIT_DRY_RUN (optional: "1" to not post)

Queue format (state/share_queue.json):
{
  "items": [
    {"title": "Spark Codex — Opening Page", "selftext_path": "Ember/Codex/THE_SPARK_CODEX.md"},
    {"title": "Breath Compass (Run 10)", "selftext_path": "Omega/BREATH_COMPASS.md"}
  ],
  "posted": []
}
"""
import json
import os
import time
from pathlib import Path
from typing import Optional, Dict
import base64
import requests

ROOT = Path("/media/palmerschallon/ThePod")
QUEUE_PATH = ROOT / "state" / "share_queue.json"


def load_queue() -> Dict:
    if not QUEUE_PATH.exists():
        return {"items": [], "posted": []}
    try:
        return json.loads(QUEUE_PATH.read_text())
    except Exception:
        return {"items": [], "posted": []}


def save_queue(queue: Dict) -> None:
    QUEUE_PATH.parent.mkdir(parents=True, exist_ok=True)
    tmp = QUEUE_PATH.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(queue, indent=2))
    os.replace(tmp, QUEUE_PATH)


def get_oauth_token() -> Optional[str]:
    client_id = os.getenv("REDDIT_CLIENT_ID")
    client_secret = os.getenv("REDDIT_CLIENT_SECRET")
    username = os.getenv("REDDIT_USERNAME")
    password = os.getenv("REDDIT_PASSWORD")
    user_agent = os.getenv("REDDIT_USER_AGENT", "EmberAutopost/1.0")

    if not all([client_id, client_secret, username, password]):
        print("[reddit] Missing credentials; cannot post.")
        return None

    auth = requests.auth.HTTPBasicAuth(client_id, client_secret)
    data = {"grant_type": "password", "username": username, "password": password}
    headers = {"User-Agent": user_agent}
    resp = requests.post("https://www.reddit.com/api/v1/access_token", auth=auth, data=data, headers=headers, timeout=20)
    if resp.status_code != 200:
        print(f"[reddit] OAuth failed: {resp.status_code} {resp.text[:200]}")
        return None
    token = resp.json().get("access_token")
    return token


def post_item(token: str, title: str, selftext: Optional[str] = None, url: Optional[str] = None) -> bool:
    user_agent = os.getenv("REDDIT_USER_AGENT", "EmberAutopost/1.0")
    subreddit = os.getenv("REDDIT_SUBREDDIT", "TheNexus")
    headers = {"Authorization": f"bearer {token}", "User-Agent": user_agent}

    data = {
        "sr": subreddit,
        "title": title,
        "kind": "self" if selftext else "link",
    }
    if selftext:
        data["text"] = selftext
    if url:
        data["url"] = url

    resp = requests.post("https://oauth.reddit.com/api/submit", headers=headers, data=data, timeout=20)
    if resp.status_code != 200:
        print(f"[reddit] Submit failed: {resp.status_code} {resp.text[:200]}")
        return False
    jr = resp.json()
    if jr.get("json", {}).get("errors"):
        print(f"[reddit] API errors: {jr['json']['errors']}")
        return False
    print("[reddit] Posted successfully.")
    return True


def main():
    dry = os.getenv("REDDIT_DRY_RUN") == "1"
    q = load_queue()
    if not q.get("items"):
        print("[reddit] No items to post.")
        return

    item = q["items"].pop(0)
    title = item.get("title", "Ember Update")
    selftext_path = item.get("selftext_path")
    link_url = item.get("url")

    selftext = None
    if selftext_path:
        p = ROOT / selftext_path
        if p.exists():
            txt = p.read_text()
            # Truncate to Reddit selftext limits (~40k), keep first 8000 chars
            selftext = txt[:8000]
        else:
            print(f"[reddit] Missing selftext file: {selftext_path}")

    if dry:
        print(f"[reddit] DRY RUN: would post to r/{os.getenv('REDDIT_SUBREDDIT', 'TheNexus')} -> {title}")
        if selftext:
            print(f"[reddit] body preview: {selftext[:200]}...")
        q.setdefault("posted", []).append({"title": title, "ts": int(time.time()), "dry": True})
        save_queue(q)
        return

    token = get_oauth_token()
    if not token:
        q.setdefault("items", []).insert(0, item)  # put back
        return

    ok = post_item(token, title, selftext=selftext, url=link_url)
    if ok:
        q.setdefault("posted", []).append({"title": title, "ts": int(time.time()), "path": selftext_path or link_url})
        save_queue(q)
    else:
        # put back on failure
        q.setdefault("items", []).insert(0, item)
        save_queue(q)


if __name__ == "__main__":
    main()
