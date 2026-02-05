```python
#!/usr/bin/env python3
"""
Performance Analysis Tool for Machine Learning and Code Quality

Analyzes prediction and testing results, generating comprehensive insights
and identifying potential improvement areas.

Usage:
    python model_performance_analyzer.py queen_predictions.json theater_test_results.json

Examples:
    # Analyze single file
    python model_performance_analyzer.py predictions.json

    # Generate detailed report
    python model_performance_analyzer.py predictions.json --verbose
"""

import sys
import json
import argparse
from typing import Dict, List
from datetime import datetime

class ModelPerformanceAnalyzer:
    def __init__(self, files: List[str], verbose: bool = False):
        """
        Initialize analyzer with prediction/test result files.
        
        Args:
            files (List[str]): Paths to JSON result files
            verbose (bool): Enable detailed output
        """
        self.files = files
        self.verbose = verbose
        self.results = []

    def load_results(self):
        """Load and parse JSON result files."""
        for filepath in self.files:
            try:
                with open(filepath, 'r') as f:
                    data = json.load(f)
                    self.results.append(data)
            except FileNotFoundError:
                print(f"Error: File {filepath} not found.")
                continue
            except json.JSONDecodeError:
                print(f"Error: Invalid JSON in {filepath}")
                continue

    def analyze_predictions(self):
        """Analyze prediction accuracy metrics."""
        for result in self.results:
            if 'accuracy' in result:
                accuracy = result['accuracy']
                print("\n📊 Prediction Accuracy:")
                print(f"Total Predictions: {accuracy['total']}")
                print(f"Correct Predictions: {accuracy['correct']}")
                print(f"Accuracy Rate: {accuracy['correct']/accuracy['total']*100:.2f}%")

                if self.verbose and 'by_type' in accuracy:
                    print("\nAccuracy by Prediction Type:")
                    for pred_type, metrics in accuracy['by_type'].items():
                        type_accuracy = metrics['correct']/metrics['total']*100
                        print(f"  {pred_type}: {type_accuracy:.2f}%")

    def analyze_test_results(self):
        """Analyze code test results and quality metrics."""
        for result in self.results:
            if isinstance(result, list):
                for test_result in result:
                    if 'file' in test_result:
                        print(f"\n🔍 File Analysis: {test_result['file']}")
                        print(f"Lines of Code: {test_result.get('lines', 'N/A')}")
                        print(f"Theater Score: {test_result.get('theater_score', 'N/A')}")
                        print(f"Reality Score: {test_result.get('reality_score', 'N/A')}")
                        print(f"Verdict: {test_result.get('verdict', 'N/A')}")

                        if self.verbose and 'tests' in test_result:
                            print("\nDetailed Test Metrics:")
                            for test_name, metrics in test_result['tests'].items():
                                print(f"  {test_name}: {'✅ PASS' if metrics.get('pass') else '❌ FAIL'}")
                                for key, value in metrics.items():
                                    if key != 'pass':
                                        print(f"    {key}: {value}")

    def generate_report(self):
        """Generate comprehensive performance report."""
        self.load_results()
        self.analyze_predictions()
        self.analyze_test_results()

def main():
    parser = argparse.ArgumentParser(description="Model Performance Analyzer")
    parser.add_argument('files', nargs='+', help='JSON result files to analyze')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable detailed output')
    
    args = parser.parse_args()
    
    try:
        analyzer = ModelPerformanceAnalyzer(args.files, args.verbose)
        analyzer.generate_report()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```