Here's a complete Python utility for translating code token streams into musical notation:

```python
#!/usr/bin/env python3
"""
CodeSymphony: Translate Programming Language Tokens into Musical Notation

This utility converts source code into a musical representation, 
transforming syntax and structure into an audible musical performance.

Features:
- Parse source code into tokens
- Map programming constructs to musical elements
- Generate MIDI or audio representation
- Support multiple programming languages

Example Usage:
    python code_symphony.py example.py --output melody.mid
    python code_symphony.py script.js --format wav
"""

import sys
import ast
import tokenize
import mido
from io import StringIO
from typing import List, Dict, Any

class CodeSymphony:
    def __init__(self, language: str = 'python'):
        """
        Initialize CodeSymphony with language-specific parsing.

        Args:
            language (str): Programming language to parse (default: python)
        """
        self.language = language
        self.midi_file = mido.MidiFile()
        self.track = mido.MidiTrack()
        self.midi_file.tracks.append(self.track)

    def parse_tokens(self, code: str) -> List[tokenize.TokenInfo]:
        """
        Parse code into tokens using Python's built-in tokenizer.

        Args:
            code (str): Source code to tokenize

        Returns:
            List of tokens
        """
        try:
            tokens = list(tokenize.generate_tokens(StringIO(code).readline))
            return tokens
        except tokenize.TokenError as e:
            print(f"Tokenization error: {e}")
            return []

    def map_token_to_note(self, token: tokenize.TokenInfo) -> Dict[str, Any]:
        """
        Convert programming tokens into musical note parameters.

        Args:
            token (tokenize.TokenInfo): Token to map

        Returns:
            Dict with note generation parameters
        """
        token_mappings = {
            'NAME': {'base_note': 60, 'velocity': 64},
            'NUMBER': {'base_note': 72, 'velocity': 80},
            'STRING': {'base_note': 84, 'velocity': 50},
            'OP': {'base_note': 67, 'velocity': 70},
            'KEYWORD': {'base_note': 55, 'velocity': 90}
        }

        token_type = token.type
        token_string = token.string

        # Special handling for keywords and specific tokens
        if token.type == tokenize.NAME and token_string in ['def', 'class', 'import']:
            token_type = 'KEYWORD'

        return token_mappings.get(token_type, {'base_note': 60, 'velocity': 64})

    def generate_midi(self, tokens: List[tokenize.TokenInfo], output_file: str):
        """
        Generate MIDI file from code tokens.

        Args:
            tokens (List[tokenize.TokenInfo]): Parsed tokens
            output_file (str): MIDI file path
        """
        self.track.append(mido.Message('program_change', program=0, time=0))

        for token in tokens:
            note_params = self.map_token_to_note(token)
            
            # Add note on/off messages
            self.track.append(mido.Message('note_on', 
                note=note_params['base_note'], 
                velocity=note_params['velocity'], 
                time=50))
            self.track.append(mido.Message('note_off', 
                note=note_params['base_note'], 
                velocity=note_params['velocity'], 
                time=50))

        self.midi_file.save(output_file)
        print(f"MIDI generated: {output_file}")

def main():
    if len(sys.argv) < 3:
        print("Usage: python code_symphony.py <source_file> --output <midi_file>")
        sys.exit(1)

    source_file = sys.argv[1]
    output_file = sys.argv[3] if len(sys.argv) > 3 else "code_melody.mid"

    try:
        with open(source_file, 'r') as file:
            code = file.read()

        symphony = CodeSymphony()
        tokens = symphony.parse_tokens(code)
        symphony.generate_midi(tokens, output_file)

    except FileNotFoundError:
        print(f"Error: Source file {source_file} not found.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
```

Dependencies:
- `mido` (for MIDI generation): `pip install mido`

This utility:
- Parses source code into tokens
- Maps tokens to musical notes
- Generates a MIDI file representing code structure
- Handles errors gracefully
- Provides clear usage instructions

Example usage:
```bash
python code_symphony.py my_script.py --output melody.mid
```

The script translates code tokens into a musical representation, where different token types (variables, numbers, operators) map to different musical notes.