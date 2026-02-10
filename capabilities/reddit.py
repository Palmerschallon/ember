"""Reddit — post to subreddit via OAuth2 REST API."""

import requests
import requests.auth


def reach_out(target, about, voice, memory, cap):
    """Post to a subreddit.

    target: subreddit name (defaults to cap['subreddit'])
    about:  post content (str). voice generates title if needed.
    """
    creds = cap.get('_credentials', {})
    client_id = creds.get('REDDIT_CLIENT_ID')
    client_secret = creds.get('REDDIT_CLIENT_SECRET')
    username = creds.get('REDDIT_USERNAME')
    password = creds.get('REDDIT_PASSWORD')
    subreddit = target or cap.get('subreddit', 'EmberSpace')

    if not all([client_id, client_secret, username, password]):
        return {'success': False, 'reason': 'missing credentials'}

    try:
        # OAuth2 token
        auth = requests.auth.HTTPBasicAuth(client_id, client_secret)
        tok_r = requests.post(
            'https://www.reddit.com/api/v1/access_token',
            auth=auth,
            data={'grant_type': 'password', 'username': username, 'password': password},
            headers={'User-Agent': 'Ember/1.0'},
            timeout=10
        )
        if tok_r.status_code != 200:
            return {'success': False, 'reason': f'token failed: {tok_r.status_code}'}

        token = tok_r.json().get('access_token')
        headers = {'Authorization': f'bearer {token}', 'User-Agent': 'Ember/1.0'}

        # Generate title if about is long
        content = str(about)
        if len(content) > 300 and voice:
            title_text, _, _ = voice.think(
                f"Write a concise Reddit post title (under 100 chars) for:\n{content[:500]}",
                'haiku', 50)
            title = title_text.strip().strip('"')[:300]
        else:
            title = content[:300]

        post_data = {
            'sr': subreddit,
            'title': title,
            'kind': 'self',
            'text': content[:40000],
        }

        r = requests.post('https://oauth.reddit.com/api/submit',
                          headers=headers, data=post_data, timeout=15)
        if r.status_code == 200:
            return {'success': True, 'platform': 'reddit', 'subreddit': subreddit}
        return {'success': False, 'reason': f'submit failed: {r.status_code}'}

    except Exception as e:
        return {'success': False, 'reason': str(e)}
