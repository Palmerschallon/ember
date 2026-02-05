```python
#!/usr/bin/env python3
"""
Pattern Discovery Utility

Analyzes and extracts unique patterns from JSON discovery logs.

Usage:
    python3 pattern_extractor.py <input_file>              # Print summary
    python3 pattern_extractor.py <input_file> --detailed   # Show detailed breakdown
    python3 pattern_extractor.py <input_file> --save       # Save extracted patterns

Examples:
    python3 pattern_extractor.py queen_discoveries.json
    python3 pattern_extractor.py queen_discoveries.json --detailed
"""

import sys
import json
from collections import defaultdict
from typing import List, Dict, Optional

class PatternAnalyzer:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.patterns = []
        self.load_patterns()

    def load_patterns(self) -> None:
        """Load JSON discovery patterns from file."""
        try:
            with open(self.file_path, 'r') as f:
                self.patterns = json.load(f)
        except FileNotFoundError:
            print(f"Error: File {self.file_path} not found.")
            sys.exit(1)
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON in {self.file_path}")
            sys.exit(1)

    def get_source_summary(self) -> Dict[str, int]:
        """Count pattern occurrences per source."""
        sources = defaultdict(int)
        for pattern in self.patterns:
            sources[pattern.get('source', 'Unknown')] += 1
        return dict(sources)

    def get_eigenpattern_summary(self) -> Dict[str, int]:
        """Count pattern occurrences per eigenpattern."""
        eigenpatterns = defaultdict(int)
        for pattern in self.patterns:
            eigenpatterns[pattern.get('eigenpattern', 'Unknown')] += 1
        return dict(eigenpatterns)

    def print_summary(self, detailed: bool = False) -> None:
        """Print summary of discovered patterns."""
        print(f"Total Patterns: {len(self.patterns)}")
        
        print("\nSources:")
        for source, count in self.get_source_summary().items():
            print(f"  {source}: {count} patterns")
        
        print("\nEigenpatterns:")
        for pattern, count in self.get_eigenpattern_summary().items():
            print(f"  {pattern}: {count} occurrences")
        
        if detailed:
            print("\nDetailed Patterns:")
            for pattern in self.patterns:
                print(f"  {pattern['pattern_name']} (Source: {pattern.get('source')}, "
                      f"Eigenpattern: {pattern.get('eigenpattern')})")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 pattern_extractor.py <input_file> [--detailed] [--save]")
        sys.exit(1)

    file_path = sys.argv[1]
    detailed = '--detailed' in sys.argv
    save = '--save' in sys.argv

    try:
        analyzer = PatternAnalyzer(file_path)
        analyzer.print_summary(detailed)

        if save:
            output_file = file_path.replace('.json', '_summary.json')
            summary = {
                'total_patterns': len(analyzer.patterns),
                'sources': analyzer.get_source_summary(),
                'eigenpatterns': analyzer.get_eigenpattern_summary()
            }
            with open(output_file, 'w') as f:
                json.dump(summary, f, indent=2)
            print(f"\nSummary saved to {output_file}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```

This utility:
- Reads JSON pattern discovery logs
- Provides summary of patterns by source and eigenpattern
- Supports detailed output
- Optional summary file saving
- Robust error handling
- Includes usage examples
- Clean, modular design with type hints

Can be run directly on the `queen_discoveries.json` file with various options.