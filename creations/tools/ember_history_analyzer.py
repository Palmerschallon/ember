```python
#!/usr/bin/env python3
"""
EmberConvoAnalyzer: Advanced conversation history analysis tool

Provides deep insights into conversation patterns, tracking:
- Message frequency
- Topic transitions
- Sentiment evolution
- Interaction metrics

Usage:
    python ember_convo_analyzer.py <conversation_file.json>

Example:
    python ember_convo_analyzer.py recent_chats.json
"""

import json
import sys
import argparse
from collections import defaultdict
from typing import Dict, List, Any
from datetime import datetime
import statistics

class EmberConvoAnalyzer:
    def __init__(self, filepath: str):
        """Initialize analyzer with conversation data."""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                self.conversations = json.load(f)
        except FileNotFoundError:
            print(f"Error: File {filepath} not found.")
            sys.exit(1)
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON in {filepath}")
            sys.exit(1)

    def analyze_message_frequency(self) -> Dict[str, int]:
        """Calculate message count by sender."""
        frequency = defaultdict(int)
        for conv in self.conversations:
            for msg in conv.get('messages', []):
                frequency[msg.get('sender', 'Unknown')] += 1
        return dict(frequency)

    def track_topic_transitions(self) -> List[str]:
        """Detect and track conversation topic shifts."""
        topics = []
        for conv in self.conversations:
            conversation_topics = [msg.get('topic', 'Undefined') for msg in conv.get('messages', [])]
            topics.extend(conversation_topics)
        return topics

    def calculate_response_times(self) -> List[float]:
        """Measure time between messages in seconds."""
        response_times = []
        for conv in self.conversations:
            sorted_msgs = sorted(conv.get('messages', []), key=lambda x: x.get('timestamp', 0))
            for i in range(1, len(sorted_msgs)):
                prev_time = datetime.fromisoformat(sorted_msgs[i-1].get('timestamp', ''))
                curr_time = datetime.fromisoformat(sorted_msgs[i].get('timestamp', ''))
                response_times.append((curr_time - prev_time).total_seconds())
        return response_times

    def generate_report(self) -> Dict[str, Any]:
        """Compile comprehensive conversation analysis report."""
        return {
            'message_frequency': self.analyze_message_frequency(),
            'topic_transitions': self.track_topic_transitions(),
            'response_times': {
                'average': statistics.mean(self.calculate_response_times()) if self.calculate_response_times() else 0,
                'median': statistics.median(self.calculate_response_times()) if self.calculate_response_times() else 0
            }
        }

def main():
    parser = argparse.ArgumentParser(description='Ember Conversation Analyzer')
    parser.add_argument('filepath', help='Path to conversation history JSON')
    args = parser.parse_args()

    try:
        analyzer = EmberConvoAnalyzer(args.filepath)
        report = analyzer.generate_report()
        print(json.dumps(report, indent=2))
    except Exception as e:
        print(f"Analysis failed: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
```