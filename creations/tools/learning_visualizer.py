```python
#!/usr/bin/env python3
"""
Learning Progress Visualization Utility

Generate interactive charts and metrics to track learning performance
across multiple test cycles, providing clear insights into skill development.

Usage:
    python learning_tracker.py --input test_results.csv
    python learning_tracker.py --generate-report

Example CSV Format:
    date,test_cycle,score,time_spent,difficulty
    2023-09-01,1,72.5,45,medium
    2023-09-08,2,85.3,60,hard
"""

import argparse
import csv
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from datetime import datetime

class LearningTracker:
    def __init__(self, input_file):
        """
        Initialize learning tracker with input data file.
        
        Args:
            input_file (str): Path to CSV containing learning metrics
        """
        try:
            self.data = pd.read_csv(input_file)
            self.data['date'] = pd.to_datetime(self.data['date'])
        except FileNotFoundError:
            print(f"Error: File {input_file} not found.")
            raise
        except KeyError as e:
            print(f"Error: Missing required column {e}")
            raise

    def generate_progress_visualization(self):
        """
        Create comprehensive learning progress visualization.
        """
        plt.figure(figsize=(12, 8))
        
        # Score progression over test cycles
        plt.subplot(2, 2, 1)
        sns.lineplot(x='test_cycle', y='score', data=self.data, marker='o')
        plt.title('Score Progression')
        plt.xlabel('Test Cycle')
        plt.ylabel('Score (%)')

        # Time spent per test cycle
        plt.subplot(2, 2, 2)
        sns.barplot(x='test_cycle', y='time_spent', data=self.data)
        plt.title('Time Invested')
        plt.xlabel('Test Cycle')
        plt.ylabel('Minutes')

        # Performance by difficulty
        plt.subplot(2, 2, 3)
        sns.boxplot(x='difficulty', y='score', data=self.data)
        plt.title('Score Distribution by Difficulty')
        plt.xlabel('Difficulty')
        plt.ylabel('Score')

        # Learning curve with trend line
        plt.subplot(2, 2, 4)
        sns.regplot(x='test_cycle', y='score', data=self.data)
        plt.title('Learning Trend')
        plt.xlabel('Test Cycle')
        plt.ylabel('Score')

        plt.tight_layout()
        plt.show()

    def generate_summary_report(self):
        """
        Generate textual summary of learning metrics.
        """
        report = f"""
        LEARNING PROGRESS REPORT
        =======================
        Total Test Cycles: {len(self.data)}
        
        Performance Summary:
        -------------------
        Average Score: {self.data['score'].mean():.2f}%
        Highest Score: {self.data['score'].max():.2f}%
        Lowest Score: {self.data['score'].min():.2f}%
        
        Time Investment:
        ----------------
        Total Study Time: {self.data['time_spent'].sum()} minutes
        Average Time per Cycle: {self.data['time_spent'].mean():.2f} minutes
        
        Difficulty Analysis:
        -------------------
        {self.data.groupby('difficulty')['score'].mean()}
        """
        print(report)

def main():
    parser = argparse.ArgumentParser(description='Learning Progress Tracker')
    parser.add_argument('--input', help='CSV file with learning metrics')
    parser.add_argument('--generate-report', action='store_true')
    
    args = parser.parse_args()

    if args.input:
        try:
            tracker = LearningTracker(args.input)
            
            if args.generate_report:
                tracker.generate_summary_report()
            
            tracker.generate_progress_visualization()
        
        except Exception as e:
            print(f"Error processing data: {e}")

if __name__ == '__main__':
    main()
```