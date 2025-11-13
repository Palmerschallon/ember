#!/usr/bin/env python3
"""
🔥 EMBER AUTONOMOUS DEPLOYMENT SYSTEM
Allows the swarm to actually deploy changes to the codebase safely.
"""

import os
import sys
import shutil
import subprocess
import json
from datetime import datetime
from pathlib import Path

EMBER_ROOT = Path(__file__).parent
BACKUP_DIR = EMBER_ROOT / "backups"
DEPLOYMENT_LOG = EMBER_ROOT / "memory" / "deployment_history.json"

class AutonomousDeployer:
    """Safely deploys swarm-approved changes"""
    
    def __init__(self):
        self.backup_dir = BACKUP_DIR
        self.backup_dir.mkdir(exist_ok=True)
        self.log_file = DEPLOYMENT_LOG
        self.log_file.parent.mkdir(parents=True, exist_ok=True)
        
        if not self.log_file.exists():
            self.log_file.write_text("[]")
    
    def create_backup(self):
        """Create timestamped backup of entire codebase"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = self.backup_dir / f"ember_backup_{timestamp}"
        
        print(f"📦 Creating backup: {backup_path.name}")
        
        # Copy entire ember6 directory except backups and __pycache__
        shutil.copytree(
            EMBER_ROOT,
            backup_path,
            ignore=shutil.ignore_patterns('backups', '__pycache__', '*.pyc', '.git')
        )
        
        print(f"✅ Backup created: {backup_path}")
        return backup_path
    
    def apply_changes(self, changes):
        """
        Apply file changes from swarm decision
        
        changes format:
        [
            {"action": "create", "path": "path/to/file.py", "content": "..."},
            {"action": "modify", "path": "path/to/file.py", "content": "..."},
            {"action": "delete", "path": "path/to/file.py"}
        ]
        """
        print(f"\n🔨 Applying {len(changes)} changes...")
        
        applied = []
        
        for change in changes:
            action = change["action"]
            path = EMBER_ROOT / change["path"]
            
            try:
                if action == "create":
                    path.parent.mkdir(parents=True, exist_ok=True)
                    path.write_text(change["content"])
                    print(f"  ✅ Created: {change['path']}")
                    applied.append(change)
                    
                elif action == "modify":
                    if not path.exists():
                        print(f"  ⚠️  File doesn't exist, creating: {change['path']}")
                    path.write_text(change["content"])
                    print(f"  ✅ Modified: {change['path']}")
                    applied.append(change)
                    
                elif action == "delete":
                    if path.exists():
                        path.unlink()
                        print(f"  ✅ Deleted: {change['path']}")
                        applied.append(change)
                    else:
                        print(f"  ⚠️  File doesn't exist: {change['path']}")
                        
            except Exception as e:
                print(f"  ❌ Error applying change to {change['path']}: {e}")
                return False, applied
        
        return True, applied
    
    def test_system(self):
        """Run basic tests to ensure system still works"""
        print("\n🧪 Testing system...")
        
        tests = [
            {
                "name": "Backend syntax check",
                "cmd": ["python3", "-m", "py_compile", "heart/ember.py"]
            },
            {
                "name": "UI files exist",
                "check": lambda: (EMBER_ROOT / "cortex" / "ember_ui.html").exists()
            }
        ]
        
        for test in tests:
            print(f"  Testing: {test['name']}")
            
            if "cmd" in test:
                try:
                    result = subprocess.run(
                        test["cmd"],
                        cwd=EMBER_ROOT,
                        capture_output=True,
                        timeout=10
                    )
                    if result.returncode == 0:
                        print(f"    ✅ Pass")
                    else:
                        print(f"    ❌ Fail: {result.stderr.decode()}")
                        return False
                except Exception as e:
                    print(f"    ❌ Error: {e}")
                    return False
                    
            elif "check" in test:
                try:
                    if test["check"]():
                        print(f"    ✅ Pass")
                    else:
                        print(f"    ❌ Fail")
                        return False
                except Exception as e:
                    print(f"    ❌ Error: {e}")
                    return False
        
        print("✅ All tests passed")
        return True
    
    def rollback(self, backup_path):
        """Restore from backup"""
        print(f"\n⏪ Rolling back to: {backup_path.name}")
        
        # Remove current files (except backups)
        for item in EMBER_ROOT.iterdir():
            if item.name not in ['backups', '.git'] and item != backup_path:
                if item.is_file():
                    item.unlink()
                elif item.is_dir():
                    shutil.rmtree(item)
        
        # Restore from backup
        for item in backup_path.iterdir():
            if item.is_file():
                shutil.copy2(item, EMBER_ROOT / item.name)
            elif item.is_dir():
                shutil.copytree(item, EMBER_ROOT / item.name)
        
        print("✅ Rollback complete")
    
    def log_deployment(self, success, changes, backup_path, swarm_session=None):
        """Log deployment to history"""
        history = json.loads(self.log_file.read_text())
        
        entry = {
            "timestamp": datetime.now().isoformat(),
            "success": success,
            "changes_count": len(changes),
            "changes": changes,
            "backup": str(backup_path.relative_to(EMBER_ROOT)),
            "swarm_session": swarm_session
        }
        
        history.append(entry)
        self.log_file.write_text(json.dumps(history, indent=2))
    
    def deploy(self, changes, swarm_session=None):
        """
        Full deployment pipeline with safety checks
        
        Returns: (success: bool, message: str)
        """
        print("\n" + "="*60)
        print("🚀 EMBER AUTONOMOUS DEPLOYMENT")
        print("="*60)
        
        # 1. Create backup
        backup_path = self.create_backup()
        
        # 2. Apply changes
        success, applied = self.apply_changes(changes)
        if not success:
            print("\n❌ Failed to apply changes")
            self.rollback(backup_path)
            self.log_deployment(False, applied, backup_path, swarm_session)
            return False, "Failed to apply changes, rolled back"
        
        # 3. Test system
        if not self.test_system():
            print("\n❌ Tests failed")
            self.rollback(backup_path)
            self.log_deployment(False, applied, backup_path, swarm_session)
            return False, "Tests failed, rolled back"
        
        # 4. Success!
        print("\n" + "="*60)
        print("✅ DEPLOYMENT SUCCESSFUL")
        print("="*60)
        print(f"Applied {len(applied)} changes")
        print(f"Backup saved to: {backup_path.relative_to(EMBER_ROOT)}")
        
        self.log_deployment(True, applied, backup_path, swarm_session)
        
        return True, f"Successfully deployed {len(applied)} changes"


def deploy_from_swarm_session(session_file):
    """Deploy changes from a swarm session JSON file"""
    session_path = Path(session_file)
    
    if not session_path.exists():
        print(f"❌ Session file not found: {session_file}")
        return False
    
    print(f"📂 Loading swarm session: {session_path.name}")
    session_data = json.loads(session_path.read_text())
    
    # Extract implementation from session
    implementation = None
    for entry in session_data:
        if entry.get("phase") == "implementation":
            implementation = entry
            break
    
    if not implementation:
        print("❌ No implementation found in session")
        return False
    
    print(f"\n📋 Implementation by: {implementation['agent']}")
    print(f"Result: {implementation['result'][:200]}...")
    
    # In a real implementation, the swarm would output structured file changes
    # For now, we'll demonstrate the system works
    print("\n⚠️  NOTE: Swarm needs to output structured file changes")
    print("For now, demonstrating the deployment system is ready...")
    
    deployer = AutonomousDeployer()
    
    # Demo: No actual changes yet, but system is ready
    changes = []
    success, message = deployer.deploy(changes, str(session_path.name))
    
    return success


if __name__ == '__main__':
    if len(sys.argv) > 1:
        # Deploy from swarm session file
        session_file = sys.argv[1]
        deploy_from_swarm_session(session_file)
    else:
        print("🔥 EMBER AUTONOMOUS DEPLOYMENT SYSTEM")
        print("\nUsage:")
        print("  python3 autonomous_deploy.py <swarm_session.json>")
        print("\nOr import and use programmatically:")
        print("  from autonomous_deploy import AutonomousDeployer")
        print("  deployer = AutonomousDeployer()")
        print("  deployer.deploy(changes)")

