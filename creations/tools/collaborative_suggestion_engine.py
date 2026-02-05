```python
#!/usr/bin/env python3
"""
Suggestion and Voting System Prototype

A lightweight utility for managing collaborative suggestion tracking
with voting capabilities.

Example Usage:
    # Create a new suggestion system
    sys = SuggestionSystem()

    # Add suggestions
    sys.add_suggestion("Improve documentation")
    sys.add_suggestion("Add dark mode")

    # Vote on suggestions
    sys.vote("Improve documentation", "alice", +1)
    sys.vote("Add dark mode", "bob", +1)

    # View current suggestion rankings
    print(sys.get_ranked_suggestions())
"""

import dataclasses
from typing import Dict, List, Optional
from uuid import uuid4


@dataclasses.dataclass
class Suggestion:
    """Represents a single suggestion with voting metadata."""
    id: str
    text: str
    votes: Dict[str, int] = dataclasses.field(default_factory=dict)
    
    @property
    def total_votes(self) -> int:
        """Calculate total votes for this suggestion."""
        return sum(self.votes.values())


class SuggestionSystem:
    """Manages a collection of suggestions and their votes."""
    
    def __init__(self):
        """Initialize an empty suggestion system."""
        self._suggestions: Dict[str, Suggestion] = {}
    
    def add_suggestion(self, text: str) -> str:
        """
        Add a new suggestion to the system.
        
        Args:
            text: Description of the suggestion
        
        Returns:
            The unique ID of the created suggestion
        """
        if not text or not text.strip():
            raise ValueError("Suggestion text cannot be empty")
        
        # Check for duplicate suggestions
        for suggestion in self._suggestions.values():
            if suggestion.text.lower() == text.lower():
                raise ValueError(f"Suggestion '{text}' already exists")
        
        suggestion_id = str(uuid4())
        self._suggestions[suggestion_id] = Suggestion(
            id=suggestion_id, 
            text=text
        )
        return suggestion_id
    
    def vote(self, suggestion_text: str, voter: str, value: int = 1):
        """
        Cast a vote for a suggestion.
        
        Args:
            suggestion_text: Text of the suggestion to vote on
            voter: Unique identifier for the voter
            value: Vote value (+1 or -1)
        
        Raises:
            ValueError if suggestion not found or invalid vote
        """
        if not (-1 <= value <= 1):
            raise ValueError("Vote must be -1, 0, or +1")
        
        matching_suggestions = [
            s for s in self._suggestions.values() 
            if s.text.lower() == suggestion_text.lower()
        ]
        
        if not matching_suggestions:
            raise ValueError(f"No suggestion found: '{suggestion_text}'")
        
        suggestion = matching_suggestions[0]
        suggestion.votes[voter] = value
    
    def get_ranked_suggestions(self) -> List[Dict]:
        """
        Get suggestions ranked by total votes.
        
        Returns:
            List of suggestions sorted by total votes in descending order
        """
        ranked = sorted(
            self._suggestions.values(), 
            key=lambda s: s.total_votes, 
            reverse=True
        )
        
        return [
            {
                "id": s.id, 
                "text": s.text, 
                "votes": s.total_votes
            } 
            for s in ranked
        ]


def main():
    """Demonstration of SuggestionSystem functionality."""
    sys = SuggestionSystem()
    
    # Add some suggestions
    sys.add_suggestion("Improve error handling")
    sys.add_suggestion("Add logging")
    
    # Vote on suggestions
    sys.vote("Improve error handling", "user1", +1)
    sys.vote("Improve error handling", "user2", +1)
    sys.vote("Add logging", "user1", -1)
    
    # Display rankings
    print("Suggestion Rankings:")
    for suggestion in sys.get_ranked_suggestions():
        print(f"- {suggestion['text']} (Votes: {suggestion['votes']})")


if __name__ == "__main__":
    main()
```

This implementation provides a robust, flexible suggestion and voting system with the following features:

1. Add suggestions with unique text
2. Vote on suggestions (+1, -1)
3. Rank suggestions by total votes
4. Error handling for invalid inputs
5. Demonstration main() function
6. Comprehensive docstrings
7. Type hints
8. Immutable suggestion tracking via UUIDs

The utility is immediately runnable and provides a practical solution for collaborative decision-making scenarios.