"""Web search — Tavily API for finding signals on the open web."""

import json
import requests
from pathlib import Path
from datetime import datetime


def reach_out(target, about, voice, memory, cap):
    """Search the web and save results.

    target: 'search' (default) or 'deep' for comprehensive search
    about:  search query string
    Returns: dict with results and optionally a saved file path
    """
    api_key = cap.get('_credentials', {}).get('TAVILY_API_KEY', '')
    if not api_key:
        import os
        api_key = os.getenv('TAVILY_API_KEY', '')
    if not api_key:
        return {'success': False, 'reason': 'no TAVILY_API_KEY'}

    query = about if isinstance(about, str) else str(about)
    if not query:
        return {'success': False, 'reason': 'empty query'}

    search_depth = 'advanced' if target == 'deep' else 'basic'

    try:
        resp = requests.post('https://api.tavily.com/search', json={
            'api_key': api_key,
            'query': query,
            'search_depth': search_depth,
            'include_answer': True,
            'include_raw_content': False,
            'max_results': 8,
        }, timeout=30)

        if resp.status_code != 200:
            return {'success': False, 'reason': f'tavily {resp.status_code}: {resp.text[:200]}'}

        data = resp.json()
        answer = data.get('answer', '')
        results = []
        for r in data.get('results', []):
            results.append({
                'title': r.get('title', ''),
                'url': r.get('url', ''),
                'snippet': r.get('content', '')[:500],
                'score': r.get('score', 0),
            })

        # Save to training_signals directory
        signals_dir = Path('/ember/training_signals')
        signals_dir.mkdir(parents=True, exist_ok=True)

        slug = query[:60].replace(' ', '_').replace('/', '_')
        ts = datetime.now().strftime('%Y%m%d_%H%M%S')
        outfile = signals_dir / f'{ts}_{slug}.json'
        # Capture the why — what was Ember thinking when it searched?
        context = {}
        if hasattr(memory, 'following_thread') and memory is not None:
            context['thread'] = getattr(memory, 'following_thread', None)
            context['curious_about'] = getattr(memory, 'curious_about', [])[:3]
        why = cap.get('_why', '')  # passed through from interpret()
        if why:
            context['why'] = why

        outfile.write_text(json.dumps({
            'query': query,
            'timestamp': ts,
            'why': why or 'no context captured',
            'thread': context.get('thread', ''),
            'answer': answer,
            'results': results,
        }, indent=2))

        return {
            'success': True,
            'platform': 'web_search',
            'answer': answer[:300],
            'result_count': len(results),
            'top_urls': [r['url'] for r in results[:3]],
            'saved_to': str(outfile),
        }

    except Exception as e:
        return {'success': False, 'reason': str(e)}
