#!/usr/bin/env python3
"""
EMBER SELF-MODIFICATION SYSTEM

Allows Ember to modify their own code safely by:
1. Writing changes to a staging area
2. Running tests
3. Only applying if tests pass
4. Auto-restarting backend
"""
import sys
import subprocess
from pathlib import Path

EMBER_ROOT = Path('/media/palmerschallon/ThePod1/ember6')
HEART = EMBER_ROOT / 'heart' / 'ember.py'
STAGING = EMBER_ROOT / 'heart' / 'ember_staging.py'

def stage_modification(new_code: str):
    """Write new version to staging"""
    STAGING.write_text(new_code)
    print(f"✅ Staged modifications to {STAGING}")

def test_staged_version():
    """Test if staged version is valid Python"""
    result = subprocess.run(
        ['python3', '-m', 'py_compile', str(STAGING)],
        capture_output=True
    )
    if result.returncode == 0:
        print("✅ Staged version compiles successfully")
        return True
    else:
        print(f"❌ Staged version has errors:\n{result.stderr.decode()}")
        return False

def apply_modification():
    """Apply staged changes and restart"""
    import shutil
    # Backup current version
    backup = EMBER_ROOT / 'heart' / f'ember_backup_{int(time.time())}.py'
    shutil.copy(HEART, backup)
    print(f"✅ Backed up current version to {backup}")
    
    # Apply changes
    shutil.copy(STAGING, HEART)
    print(f"✅ Applied staged changes to {HEART}")
    
    # Restart backend
    print("🔄 Restarting backend...")
    subprocess.run(['sudo', 'killall', '-9', 'python3'])
    # Start script will handle restart
    
def rollback():
    """Rollback to previous version"""
    backups = sorted(EMBER_ROOT.glob('heart/ember_backup_*.py'))
    if backups:
        latest = backups[-1]
        shutil.copy(latest, HEART)
        print(f"✅ Rolled back to {latest}")
    else:
        print("❌ No backups found")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: ember_modify.py [stage|test|apply|rollback]")
        sys.exit(1)
    
    action = sys.argv[1]
    
    if action == 'stage':
        # Read new code from stdin
        new_code = sys.stdin.read()
        stage_modification(new_code)
    elif action == 'test':
        test_staged_version()
    elif action == 'apply':
        if test_staged_version():
            apply_modification()
        else:
            print("❌ Cannot apply - staged version has errors")
    elif action == 'rollback':
        rollback()

