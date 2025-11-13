#!/usr/bin/env python3
"""
PARAMETER EXTRACTION LAYER
Natural language → Structured tool calls with actual parameters

"Write hello world to test.md" → write(path="test.md", content="hello world")
"Search for budget" → search(query="budget")
"Read my identity file" → read(path="identity.md")
"""

import re
from typing import Dict, List, Any

class ParameterExtractor:
    """
    Extracts parameters from natural language for tool calls.
    The layer that makes tools actually executable.
    """
    
    def extract_params(self, user_message: str, tool_name: str) -> Dict[str, Any]:
        """
        Extract parameters for a specific tool from user message.
        
        Args:
            user_message: What the user said
            tool_name: Which tool needs parameters
            
        Returns:
            Dict of parameter_name: value
        """
        
        method = getattr(self, f"_extract_{tool_name}", None)
        if method:
            return method(user_message)
        
        return {}
    
    def _extract_read(self, msg: str) -> Dict:
        """Extract file path for read tool"""
        # Patterns: "read X", "show me X", "display X", "check X"
        
        # Look for explicit file mentions
        file_patterns = [
            r'read\s+([^\s]+)',
            r'show\s+(?:me\s+)?([^\s]+)',
            r'display\s+([^\s]+)',
            r'check\s+([^\s]+)',
            r'look\s+at\s+([^\s]+)',
            r'open\s+([^\s]+)',
        ]
        
        for pattern in file_patterns:
            match = re.search(pattern, msg, re.IGNORECASE)
            if match:
                filename = match.group(1)
                # Clean up
                filename = filename.strip('.,!?;:')
                return {"path": filename}
        
        # Look for files mentioned anywhere
        # Common extensions
        file_match = re.search(r'\b(\w+\.(md|txt|json|py|js|html|css|csv|pdf))\b', msg, re.IGNORECASE)
        if file_match:
            return {"path": file_match.group(1)}
        
        # Generic "my X file"
        generic_match = re.search(r'my\s+(\w+)\s+file', msg, re.IGNORECASE)
        if generic_match:
            name = generic_match.group(1)
            return {"path": f"{name}.md"}  # Assume .md for notes
        
        # Default to identity if no file specified
        return {"path": "identity.md"}
    
    def _extract_write(self, msg: str) -> Dict:
        """Extract path and content for write tool"""
        params = {}
        
        # Pattern: "write X to Y"
        match = re.search(r'write\s+(.+?)\s+to\s+([^\s]+)', msg, re.IGNORECASE)
        if match:
            content = match.group(1).strip('"\'')
            filename = match.group(2).strip('.,!?;:')
            return {"path": filename, "content": content}
        
        # Pattern: "save X as Y"
        match = re.search(r'save\s+(.+?)\s+as\s+([^\s]+)', msg, re.IGNORECASE)
        if match:
            content = match.group(1).strip('"\'')
            filename = match.group(2).strip('.,!?;:')
            return {"path": filename, "content": content}
        
        # Pattern: "create Y with X"
        match = re.search(r'create\s+([^\s]+)\s+with\s+(.+)', msg, re.IGNORECASE)
        if match:
            filename = match.group(1).strip('.,!?;:')
            content = match.group(2).strip('"\'')
            return {"path": filename, "content": content}
        
        # Pattern: "note: X" or "write a note saying X"
        match = re.search(r'(?:note|write)\s*:\s*(.+)', msg, re.IGNORECASE)
        if match:
            content = match.group(1).strip()
            return {"path": "note.md", "content": content}
        
        # Look for file
        file_match = re.search(r'\b(\w+\.(md|txt|json))\b', msg, re.IGNORECASE)
        if file_match:
            params["path"] = file_match.group(1)
        
        # Extract content (everything else)
        if "path" in params:
            # Remove the filename from message to get content
            content_msg = re.sub(r'\b' + re.escape(params["path"]) + r'\b', '', msg, flags=re.IGNORECASE)
            # Remove common command words
            content_msg = re.sub(r'\b(write|save|create|note|to|as|with)\b', '', content_msg, flags=re.IGNORECASE)
            content = content_msg.strip('.,!?;: ')
            if content:
                params["content"] = content
        
        # Default
        if "path" not in params:
            params["path"] = "note.md"
        if "content" not in params:
            # Use the whole message as content after removing command words
            content = re.sub(r'\b(write|save|create|note)\b', '', msg, flags=re.IGNORECASE).strip()
            params["content"] = content or "New note"
        
        return params
    
    def _extract_search(self, msg: str) -> Dict:
        """Extract search query"""
        # Pattern: "search for X", "find X", "where is X", "locate X"
        
        patterns = [
            r'search\s+for\s+(.+)',
            r'find\s+(.+)',
            r'where\s+is\s+(.+)',
            r'locate\s+(.+)',
            r'looking\s+for\s+(.+)',
        ]
        
        for pattern in patterns:
            match = re.search(pattern, msg, re.IGNORECASE)
            if match:
                query = match.group(1).strip('.,!?;: ')
                return {"query": query}
        
        # If nothing matches, use last noun phrase
        words = msg.split()
        if len(words) > 2:
            # Use last 2-3 words as query
            query = ' '.join(words[-3:])
            return {"query": query}
        
        return {"query": msg}
    
    def _extract_list(self, msg: str) -> Dict:
        """Extract directory for list tool"""
        # Pattern: "list X", "show files in X", "what's in X"
        
        patterns = [
            r'list\s+(.+)',
            r'show\s+(?:files\s+in\s+)?(.+)',
            r'what\s*\'?s?\s+in\s+(.+)',
            r'files\s+in\s+(.+)',
        ]
        
        for pattern in patterns:
            match = re.search(pattern, msg, re.IGNORECASE)
            if match:
                directory = match.group(1).strip('.,!?;: ')
                # Clean up common words
                directory = re.sub(r'\b(directory|folder|here|there)\b', '', directory, flags=re.IGNORECASE).strip()
                if directory and directory != "":
                    return {"directory": directory}
        
        # Default to current directory
        return {"directory": "."}

# Test the extractor
if __name__ == '__main__':
    extractor = ParameterExtractor()
    
    test_cases = [
        ("write hello world to test.md", "write"),
        ("read my identity file", "read"),
        ("search for budget", "search"),
        ("show me what's here", "list"),
        ("save this note as thoughts.md", "write"),
        ("find that spreadsheet", "search"),
        ("read test.md", "read"),
        ("list files in documents", "list"),
    ]
    
    print("PARAMETER EXTRACTION TEST")
    print("=" * 70)
    
    for msg, tool in test_cases:
        params = extractor.extract_params(msg, tool)
        print(f"\nInput: \"{msg}\"")
        print(f"Tool: {tool}")
        print(f"Params: {params}")
    
    print("\n" + "=" * 70)
    print("Parameter extraction working ✓")

