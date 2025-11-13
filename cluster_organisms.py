#!/usr/bin/env python3
"""
ORGANISM CLUSTERING & MERGING
Automatically groups similar organisms and suggests merges

Process:
1. Scan all organisms
2. Cluster by similarity (imports, functions, purpose)
3. Suggest merges (keep best, archive rest)
4. Handle garbage (move to _archive_merged/)
"""

import sys
from pathlib import Path
import json
import ast
from typing import Dict, List, Set, Tuple
from collections import defaultdict
import hashlib

POD_ROOT = Path("/media/palmerschallon/ThePod1")
ARCHIVE_MERGED = POD_ROOT / "_archive_merged"

class OrganismClusterer:
    """Groups organisms by similarity for merging"""
    
    def __init__(self):
        self.organisms = []
        self.clusters = defaultdict(list)
        
    def analyze_file(self, filepath: Path) -> Dict:
        """Extract features from Python file"""
        try:
            content = filepath.read_text()
            tree = ast.parse(content)
            
            # Extract features
            imports = set()
            functions = []
            classes = []
            
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        imports.add(alias.name.split('.')[0])
                elif isinstance(node, ast.ImportFrom):
                    if node.module:
                        imports.add(node.module.split('.')[0])
                elif isinstance(node, ast.FunctionDef):
                    functions.append(node.name)
                elif isinstance(node, ast.ClassDef):
                    classes.append(node.name)
            
            # Get content hash
            content_hash = hashlib.md5(content.encode()).hexdigest()
            
            return {
                'path': filepath,
                'imports': imports,
                'functions': functions,
                'classes': classes,
                'lines': len(content.split('\n')),
                'content_hash': content_hash,
                'name_stem': filepath.stem
            }
        except Exception as e:
            return None
    
    def similarity_score(self, org1: Dict, org2: Dict) -> float:
        """Calculate similarity between two organisms (0-1)"""
        score = 0.0
        
        # 1. Exact duplicates (content hash)
        if org1['content_hash'] == org2['content_hash']:
            return 1.0
        
        # 2. Name similarity
        name1 = org1['name_stem'].lower()
        name2 = org2['name_stem'].lower()
        if name1 in name2 or name2 in name1:
            score += 0.3
        
        # 3. Import overlap
        imports1 = org1['imports']
        imports2 = org2['imports']
        if imports1 and imports2:
            import_overlap = len(imports1 & imports2) / len(imports1 | imports2)
            score += import_overlap * 0.3
        
        # 4. Function overlap
        funcs1 = set(org1['functions'])
        funcs2 = set(org2['functions'])
        if funcs1 and funcs2:
            func_overlap = len(funcs1 & funcs2) / len(funcs1 | funcs2)
            score += func_overlap * 0.4
        
        return score
    
    def cluster_organisms(self, threshold: float = 0.6) -> Dict:
        """Group organisms by similarity"""
        print("🔍 Analyzing organisms for clustering...")
        
        # Load organism map
        with open(POD_ROOT / "ORGANISM_MAP.json") as f:
            data = json.load(f)
        
        # Analyze each file
        analyzed = []
        total = len(data['organisms'])
        for i, org in enumerate(data['organisms']):
            if i % 100 == 0:
                print(f"   Progress: {i}/{total} ({i/total*100:.0f}%)")
            
            filepath = POD_ROOT / org['file']
            if filepath.exists():
                analysis = self.analyze_file(filepath)
                if analysis:
                    analyzed.append(analysis)
        
        print(f"   Analyzed {len(analyzed)} organisms")
        
        # Find clusters
        clusters = []
        used = set()
        
        for i, org1 in enumerate(analyzed):
            if i in used:
                continue
            
            cluster = [org1]
            used.add(i)
            
            for j, org2 in enumerate(analyzed):
                if j <= i or j in used:
                    continue
                
                similarity = self.similarity_score(org1, org2)
                if similarity >= threshold:
                    cluster.append(org2)
                    used.add(j)
            
            if len(cluster) > 1:
                clusters.append(cluster)
        
        print(f"   Found {len(clusters)} clusters")
        
        return clusters
    
    def suggest_merges(self, clusters: List) -> List[Dict]:
        """Suggest which files to keep/merge/archive"""
        suggestions = []
        
        for i, cluster in enumerate(clusters):
            # Sort by: most recent, most lines, best location
            def score_organism(org):
                score = 0
                
                # Prefer non-backup locations
                path_str = str(org['path'])
                if '_archive' in path_str:
                    score -= 100
                if 'backup' in path_str.lower():
                    score -= 50
                if 'generated' in path_str.lower():
                    score -= 30
                
                # Prefer more complete (more lines)
                score += org['lines'] / 10
                
                # Prefer more capabilities
                score += len(org['functions']) * 2
                score += len(org['classes']) * 5
                
                return score
            
            cluster.sort(key=score_organism, reverse=True)
            
            keep = cluster[0]
            merge = cluster[1:]
            
            suggestion = {
                'cluster_id': i,
                'keep': str(keep['path'].relative_to(POD_ROOT)),
                'merge_from': [str(o['path'].relative_to(POD_ROOT)) for o in merge],
                'reason': self._get_cluster_reason(cluster),
                'unique_functions': self._get_unique_functions(cluster),
                'action': 'merge_and_archive'
            }
            
            suggestions.append(suggestion)
        
        return suggestions
    
    def _get_cluster_reason(self, cluster: List[Dict]) -> str:
        """Explain why these cluster together"""
        names = [o['name_stem'] for o in cluster]
        
        # Check for exact duplicates
        hashes = [o['content_hash'] for o in cluster]
        if len(set(hashes)) == 1:
            return "Exact duplicates (same content)"
        
        # Check for name similarity
        base_name = names[0]
        if all(base_name in n or n in base_name for n in names):
            return f"Name variations of '{base_name}'"
        
        # Check for function overlap
        all_funcs = set()
        for org in cluster:
            all_funcs.update(org['functions'])
        
        overlap_counts = []
        for org in cluster:
            org_funcs = set(org['functions'])
            overlap = len(org_funcs & all_funcs) / len(all_funcs) if all_funcs else 0
            overlap_counts.append(overlap)
        
        avg_overlap = sum(overlap_counts) / len(overlap_counts)
        if avg_overlap > 0.7:
            return f"High function overlap ({avg_overlap:.0%})"
        
        return "Similar imports and structure"
    
    def _get_unique_functions(self, cluster: List[Dict]) -> Dict:
        """Find unique functions in each file that might need merging"""
        all_funcs = defaultdict(set)
        
        for org in cluster:
            for func in org['functions']:
                all_funcs[func].add(str(org['path'].name))
        
        # Find functions only in some files
        unique = {}
        for func, files in all_funcs.items():
            if len(files) < len(cluster):
                unique[func] = list(files)
        
        return unique

def execute_merges(suggestions: List[Dict], dry_run: bool = True):
    """Execute the suggested merges"""
    
    ARCHIVE_MERGED.mkdir(exist_ok=True)
    
    print("\n" + "="*70)
    print("MERGE EXECUTION")
    print("="*70)
    print(f"Mode: {'DRY RUN' if dry_run else 'ACTUAL EXECUTION'}")
    print()
    
    for suggestion in suggestions:
        print(f"\nCluster {suggestion['cluster_id']}:")
        print(f"  Keep: {suggestion['keep']}")
        print(f"  Reason: {suggestion['reason']}")
        print(f"  Merge from {len(suggestion['merge_from'])} files:")
        
        for merge_file in suggestion['merge_from']:
            print(f"    • {merge_file}")
        
        if suggestion['unique_functions']:
            print(f"  ⚠️  Unique functions to preserve:")
            for func, files in suggestion['unique_functions'].items():
                print(f"    • {func} (in {', '.join(files)})")
        
        if not dry_run:
            # Move merged files to archive
            for merge_file in suggestion['merge_from']:
                source = POD_ROOT / merge_file
                dest = ARCHIVE_MERGED / merge_file
                dest.parent.mkdir(parents=True, exist_ok=True)
                
                if source.exists():
                    source.rename(dest)
                    print(f"    ✓ Archived: {merge_file}")

def generate_merge_report(suggestions: List[Dict]) -> str:
    """Generate markdown report of suggested merges"""
    
    report = "# ORGANISM MERGE SUGGESTIONS\n\n"
    report += f"**Generated**: {Path(__file__).stat().st_mtime}\n\n"
    report += f"**Clusters Found**: {len(suggestions)}\n\n"
    report += "---\n\n"
    
    for suggestion in suggestions:
        report += f"## Cluster {suggestion['cluster_id']}\n\n"
        report += f"**Reason**: {suggestion['reason']}\n\n"
        report += f"**Keep**: `{suggestion['keep']}`\n\n"
        report += f"**Archive** ({len(suggestion['merge_from'])} files):\n"
        for merge_file in suggestion['merge_from']:
            report += f"- `{merge_file}`\n"
        report += "\n"
        
        if suggestion['unique_functions']:
            report += "**⚠️ Unique Functions** (may need manual merge):\n"
            for func, files in suggestion['unique_functions'].items():
                report += f"- `{func}` in: {', '.join(f'`{f}`' for f in files)}\n"
            report += "\n"
        
        report += "---\n\n"
    
    return report

if __name__ == "__main__":
    import sys
    
    # Check for execution flag
    execute = '--execute' in sys.argv
    
    clusterer = OrganismClusterer()
    
    print("="*70)
    print("ORGANISM CLUSTERING & MERGE ANALYSIS")
    print("="*70)
    print()
    
    # Find clusters
    clusters = clusterer.cluster_organisms(threshold=0.6)
    
    if not clusters:
        print("✓ No significant clusters found")
        sys.exit(0)
    
    # Generate suggestions
    suggestions = clusterer.suggest_merges(clusters)
    
    # Save report
    report = generate_merge_report(suggestions)
    report_file = POD_ROOT / "MERGE_SUGGESTIONS.md"
    report_file.write_text(report)
    print(f"\n📝 Report saved to: {report_file.name}")
    
    # Estimate cleanup
    total_files = sum(len(s['merge_from']) for s in suggestions)
    print(f"\n📊 SUMMARY:")
    print(f"   • {len(suggestions)} clusters identified")
    print(f"   • {total_files} files can be archived")
    print(f"   • {len(suggestions)} files will remain")
    print(f"   • Reduction: {total_files} → {len(suggestions)} ({100 - len(suggestions)/total_files*100:.0f}% reduction)")
    
    if execute:
        print("\n⚠️  EXECUTING MERGE...")
        print("   Creating pre-merge backup...")
        
        # Create timestamped backup
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_dir = ARCHIVE_MERGED / "pre_merge_backup" / timestamp
        backup_dir.mkdir(parents=True, exist_ok=True)
        
        # Save suggestions to backup
        (backup_dir / "MERGE_MANIFEST.json").write_text(json.dumps(suggestions, indent=2))
        
        print(f"   Backup saved to: {backup_dir}")
        
        # Execute merges
        execute_merges(suggestions, dry_run=False)
        
        print("\n✅ MERGE COMPLETE")
        print(f"   Files archived: {total_files}")
        print(f"   Backup location: {backup_dir}")
        print(f"\n   To rollback:")
        print(f"   python3 cluster_organisms.py --rollback {timestamp}")
    else:
        print("\n💡 To execute merges:")
        print("   python3 cluster_organisms.py --execute")

