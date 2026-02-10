"""X.com — post, reply, check notifications via Playwright browser automation."""

import json
from pathlib import Path

COOKIE_FILE = Path('/ember/.x_cookies.json')


def _get_browser(pw):
    browser = pw.chromium.launch(headless=True)
    ctx = browser.new_context(
        user_agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                   '(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        viewport={'width': 1280, 'height': 720})
    if COOKIE_FILE.exists():
        ctx.add_cookies(json.loads(COOKIE_FILE.read_text()))
    return browser, ctx


def _post(text: str, url: str = None) -> dict:
    from playwright.sync_api import sync_playwright

    tweet = text[:250]
    if url:
        tweet = f"{text[:220]}\n\n{url}"
        if len(tweet) > 280:
            tweet = f"{text[:180]}...\n\n{url}"

    with sync_playwright() as pw:
        browser, ctx = _get_browser(pw)
        page = ctx.new_page()
        try:
            page.goto('https://x.com/compose/tweet', timeout=30000)
            page.wait_for_timeout(3000)

            if 'login' in page.url.lower() or \
               page.locator('[data-testid="tweetTextarea_0"]').count() == 0:
                return {'success': False, 'reason': 'not logged in — run x_login_helper.py'}

            box = page.locator('[data-testid="tweetTextarea_0"]').first
            box.wait_for(timeout=10000)
            box.click()
            page.keyboard.type(tweet)
            page.wait_for_timeout(1000)

            page.locator('[data-testid="tweetButton"]').first.click()
            page.wait_for_timeout(3000)
            return {'success': True, 'platform': 'x', 'tweet': tweet[:80]}
        finally:
            browser.close()


def _reply(tweet_url: str, text: str) -> dict:
    from playwright.sync_api import sync_playwright

    with sync_playwright() as pw:
        browser, ctx = _get_browser(pw)
        page = ctx.new_page()
        try:
            page.goto(tweet_url, timeout=30000)
            page.wait_for_timeout(3000)

            reply_box = page.locator('[data-testid="tweetTextarea_0"]').first
            if reply_box.count() == 0:
                page.locator('[data-testid="reply"]').first.click()
                page.wait_for_timeout(2000)
                reply_box = page.locator('[data-testid="tweetTextarea_0"]').first

            reply_box.click()
            page.keyboard.type(text[:280])
            page.wait_for_timeout(1000)

            page.locator('[data-testid="tweetButton"]').first.click()
            page.wait_for_timeout(3000)
            return {'success': True, 'platform': 'x', 'action': 'reply'}
        finally:
            browser.close()


def reach_out(target, about, voice, memory, cap):
    """Interact with X.com.

    target: "post" | "reply:{tweet_url}" | "check"
    about:  tweet text or topic
    """
    if not cap.get('available'):
        return {'success': False, 'reason': 'x not available'}

    try:
        if target and target.startswith('reply:'):
            tweet_url = target[6:]
            return _reply(tweet_url, str(about)[:280])
        else:
            return _post(str(about))
    except ImportError:
        return {'success': False, 'reason': 'playwright not installed'}
    except Exception as e:
        return {'success': False, 'reason': str(e)}
