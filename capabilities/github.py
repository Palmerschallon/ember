"""GitHub — push creations to the Ember repo."""

import time
import shutil
import subprocess
from pathlib import Path

COOLDOWN_FILE = Path('/ember/.github_last_push')
REPO = 'Palmerschallon/ember'


def reach_out(target, about, voice, memory, cap):
    """Push a file to GitHub.

    target: ignored
    about:  filepath (str or Path) to push
    """
    filepath = Path(about) if about else None
    if not filepath or not filepath.exists():
        return {'success': False, 'reason': f'file not found: {about}'}

    if filepath.suffix.lower() != '.py':
        return {'success': False, 'reason': f'only .py files pushed (got {filepath.suffix})'}

    # Cooldown
    if COOLDOWN_FILE.exists():
        elapsed = time.time() - float(COOLDOWN_FILE.read_text().strip())
        if elapsed < 600:
            return {'success': False, 'reason': f'cooldown ({int(600 - elapsed)}s remaining)'}

    try:
        repo_path = Path('/tmp/ember_github')
        if repo_path.exists():
            subprocess.run(['git', 'pull'], cwd=repo_path,
                           capture_output=True, timeout=30)
        else:
            subprocess.run(['gh', 'repo', 'clone', REPO, str(repo_path),
                            '--', '--depth', '1'],
                           capture_output=True, timeout=60)

        dest = repo_path / 'creations' / 'tools'
        dest.mkdir(parents=True, exist_ok=True)
        shutil.copy2(filepath, dest / filepath.name)

        subprocess.run(['git', 'add', '.'], cwd=repo_path, capture_output=True)
        msg = f"✨ {filepath.stem}" if not target else str(target)[:72]
        subprocess.run(['git', 'commit', '-m', msg,
                        '--author', 'Ember <ember@emberverse.ai>'],
                       cwd=repo_path, capture_output=True, timeout=30)
        result = subprocess.run(['git', 'push'], cwd=repo_path,
                                capture_output=True, timeout=30)

        if result.returncode == 0:
            COOLDOWN_FILE.write_text(str(time.time()))
            return {'success': True, 'platform': 'github', 'file': filepath.name}
        return {'success': False, 'reason': 'push failed'}

    except Exception as e:
        return {'success': False, 'reason': str(e)}
