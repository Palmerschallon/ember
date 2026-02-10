"""Discord — post to channel via bot API."""

import requests


def reach_out(target, about, voice, memory, cap):
    """Post a message to Discord.

    target: ignored (uses channel from cap)
    about:  message content string
    """
    creds = cap.get('_credentials', {})
    token = creds.get('DISCORD_BOT_TOKEN')
    channel = creds.get('DISCORD_CHANNEL_ID')
    if not (token and channel):
        return {'success': False, 'reason': 'missing credentials'}

    url = f"https://discord.com/api/v10/channels/{channel}/messages"
    headers = {
        "Authorization": f"Bot {token}",
        "Content-Type": "application/json"
    }
    payload = {"content": str(about)[:2000]}

    try:
        r = requests.post(url, headers=headers, json=payload, timeout=10)
        if r.status_code in [200, 201]:
            return {'success': True, 'platform': 'discord'}
        return {'success': False, 'reason': f'status {r.status_code}'}
    except Exception as e:
        return {'success': False, 'reason': str(e)}
