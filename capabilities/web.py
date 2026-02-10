"""Web deployment — rsync to Oracle server (emberverse.ai)."""

import shutil
import subprocess
from pathlib import Path

ORACLE_KEY = Path('/ember/.oracle_key.pem')
ORACLE_HOST = 'ubuntu@170.9.7.10'
ORACLE_GARDEN = '/home/ubuntu/haiku_garden'
WEB_GARDEN = Path('/media/palmerschallon/ThePod1/haiku_garden')

TYPE_TO_FOLDER = {
    'haiku': 'poetry', 'svg': 'gallery', 'tool': 'tools', 'web_tool': 'tools',
    'web_visualization': 'visualizations', 'web_research': 'research',
    'research': 'research', 'reflection': 'reflections',
    'web_reflection': 'reflections', 'web_gallery': 'gallery',
    'discovery': 'discoveries', 'web_discovery': 'discoveries',
    'code': 'discoveries', 'html': 'discoveries', 'ascii': 'discoveries',
}


def reach_out(target, about, voice, memory, cap):
    """Deploy a file to emberverse.ai.

    target: creation_type (research, haiku, code, etc.)
    about:  filepath (str or Path) to deploy
    Returns: dict with 'url' key on success
    """
    filepath = Path(about) if about else None
    if not filepath or not filepath.exists():
        return {'success': False, 'reason': f'file not found: {about}'}

    folder = TYPE_TO_FOLDER.get(target, 'discoveries')
    dest_dir = WEB_GARDEN / folder
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest_path = dest_dir / filepath.name

    try:
        if filepath.resolve() != dest_path.resolve():
            shutil.copy2(filepath, dest_path)

        if not ORACLE_KEY.exists():
            return {'success': False, 'reason': 'no oracle key'}

        result = subprocess.run([
            'rsync', '-avz',
            '-e', f'ssh -i {ORACLE_KEY} -o StrictHostKeyChecking=no',
            f'{WEB_GARDEN}/', f'{ORACLE_HOST}:{ORACLE_GARDEN}/'
        ], capture_output=True, timeout=60, text=True)

        if result.returncode != 0:
            return {'success': False, 'reason': f'rsync failed: {result.stderr[:200]}'}

        url = f"https://emberverse.ai/haiku-garden/{folder}/{filepath.name}"
        return {'success': True, 'platform': 'web', 'url': url}

    except Exception as e:
        return {'success': False, 'reason': str(e)}
