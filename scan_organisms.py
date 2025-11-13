#!/usr/bin/env python3
"""
ORGANISM SCANNER
Scans ThePod for Python files that could be organisms
Checks if they have manifests or provide capabilities
"""

import sys
from pathlib import Path
import json
import re
import ast

sys.path.insert(0, str(Path(__file__).parent / "_archive_old" / "hive"))
from medusa import get_medusa

POD_ROOT = Path("/media/palmerschallon/ThePod1")

def extract_manifest_from_file(filepath: Path) -> dict:
    """
    Try to extract a manifest from a Python file
    Looks for MANIFEST or MEDUSA_MANIFEST dicts
    """
    try:
        content = filepath.read_text()
        
        # Look for manifest definitions
        manifest_patterns = [
            r'MANIFEST\s*=\s*{',
            r'MEDUSA_MANIFEST\s*=\s*{',
            r'ORGANISM_MANIFEST\s*=\s*{'
        ]
        
        for pattern in manifest_patterns:
            if re.search(pattern, content):
                # Try to parse the Python file
                try:
                    tree = ast.parse(content)
                    for node in ast.walk(tree):
                        if isinstance(node, ast.Assign):
                            for target in node.targets:
                                if isinstance(target, ast.Name):
                                    if 'MANIFEST' in target.id:
                                        # Found a manifest!
                                        # Try to safely evaluate it
                                        try:
                                            manifest_code = ast.get_source_segment(content, node.value)
                                            if manifest_code:
                                                # This is safe because it's just a dict literal
                                                manifest = eval(manifest_code)
                                                return manifest
                                        except:
                                            pass
                except:
                    pass
        
        # If no explicit manifest, try to infer capabilities
        inferred = {
            'name': filepath.stem,
            'provides': {'capabilities': []},
            'version': 'unknown',
            'auto_discovered': True
        }
        
        # Look for function definitions
        if 'def ' in content:
            functions = re.findall(r'def (\w+)\(', content)
            inferred['provides']['capabilities'] = functions[:10]  # Top 10
        
        # Look for class definitions
        if 'class ' in content:
            classes = re.findall(r'class (\w+)', content)
            inferred['provides']['classes'] = classes[:5]
        
        # Look for FastAPI/Flask routes
        if '@app.' in content or '@router.' in content:
            inferred['provides']['http_server'] = True
        
        # Only return if we found something useful
        if inferred['provides']['capabilities'] or inferred['provides'].get('classes'):
            return inferred
            
    except Exception as e:
        pass
    
    return None

def scan_for_organisms():
    """
    Scan ThePod for potential organisms
    """
    print("🔍 SCANNING THEPOD FOR ORGANISMS...")
    print("="*70)
    
    medusa = get_medusa()
    
    discovered = []
    
    # Scan key directories
    scan_dirs = [
        POD_ROOT,
        POD_ROOT / "_archive_old" / "hive",
        POD_ROOT / "essential",
    ]
    
    for scan_dir in scan_dirs:
        if not scan_dir.exists():
            continue
        
        print(f"\n📂 Scanning: {scan_dir.relative_to(POD_ROOT)}")
        
        for pyfile in scan_dir.rglob("*.py"):
            # Skip __init__.py and test files
            if pyfile.name.startswith('__') or pyfile.name.startswith('test_'):
                continue
            
            # Skip this scanner itself
            if pyfile.name == Path(__file__).name:
                continue
            
            manifest = extract_manifest_from_file(pyfile)
            
            if manifest:
                discovered.append({
                    'file': str(pyfile.relative_to(POD_ROOT)),
                    'manifest': manifest
                })
                
                # Auto-register with Medusa if it has explicit manifest
                if not manifest.get('auto_discovered'):
                    name = manifest.get('name', pyfile.stem)
                    medusa.register_organism(name, manifest)
                    print(f"   ✅ {name} (explicit manifest)")
                else:
                    print(f"   ⚪ {manifest['name']} (inferred: {len(manifest['provides']['capabilities'])} functions)")
    
    return discovered

def save_organism_map(organisms):
    """Save discovered organisms to a map file"""
    output_file = POD_ROOT / "ORGANISM_MAP.json"
    
    data = {
        "scan_timestamp": str(Path(__file__).stat().st_mtime),
        "total_discovered": len(organisms),
        "organisms": organisms
    }
    
    output_file.write_text(json.dumps(data, indent=2))
    print(f"\n💾 Saved organism map to: {output_file.name}")
    print(f"   Total organisms discovered: {len(organisms)}")

if __name__ == "__main__":
    organisms = scan_for_organisms()
    save_organism_map(organisms)
    
    print("\n" + "="*70)
    print("SCAN COMPLETE")
    print("="*70)
    
    # Show Medusa's current state
    medusa = get_medusa()
    print(f"\n📊 Medusa now knows about {len(medusa.organisms)} organisms")
    
    if medusa.organisms:
        print("\nRegistered organisms:")
        for name, info in list(medusa.organisms.items())[:10]:
            capabilities = info.get('provides', {}).get('capabilities', [])
            cap_str = f"{len(capabilities)} capabilities" if capabilities else "unknown"
            print(f"  • {name}: {cap_str}")

