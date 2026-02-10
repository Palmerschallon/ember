"""Midjourney — generate images via Discord /imagine command."""

import os
import requests


def reach_out(target, about, voice, memory, cap):
    """Send an image generation prompt to Midjourney.

    target: ignored
    about:  concept/theme to visualize. voice composes the MJ prompt.
    """
    token = cap.get('_credentials', {}).get('DISCORD_BOT_TOKEN',
            os.getenv('DISCORD_BOT_TOKEN', ''))
    channel = os.getenv('MIDJOURNEY_CHANNEL_ID', '')
    style_ref = os.getenv('MIDJOURNEY_STYLE_REF', '')

    if not (token and channel):
        return {'success': False, 'reason': 'missing discord token or midjourney channel'}

    concept = str(about)

    # Use voice to compose a proper MJ prompt if available
    if voice:
        try:
            prompt_text, _, _ = voice.think(
                f"Write a Midjourney image prompt for: {concept}\n"
                f"Evocative, visual. Under 200 chars. Just the prompt, nothing else.",
                'haiku', 80)
            mj_prompt = prompt_text.strip().strip('"')[:200]
        except:
            mj_prompt = concept[:200]
    else:
        mj_prompt = concept[:200]

    if style_ref:
        mj_prompt = f"{mj_prompt} --sref {style_ref}"

    message = f"/imagine prompt: {mj_prompt}"

    try:
        url = f"https://discord.com/api/v10/channels/{channel}/messages"
        headers = {
            'Authorization': f'Bot {token}',
            'Content-Type': 'application/json'
        }
        r = requests.post(url, headers=headers, json={'content': message}, timeout=10)

        if r.status_code in [200, 201]:
            return {'success': True, 'platform': 'midjourney', 'prompt': mj_prompt[:80]}
        return {'success': False, 'reason': f'status {r.status_code}'}

    except Exception as e:
        return {'success': False, 'reason': str(e)}
