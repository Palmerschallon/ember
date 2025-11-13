#!/usr/bin/env python3
"""Chunked file writer - bypasses parameter size limits"""

def write_chunk(filepath, content, append=True):
    mode = 'a' if append else 'w'
    with open(filepath, mode) as f:
        f.write(content)
    return f"Wrote {len(content)} bytes"

def build_file_from_chunks(filepath, chunks):
    """Build a file from a list of content chunks"""
    for i, chunk in enumerate(chunks):
        write_chunk(filepath, chunk, append=(i > 0))
    return f"Built {filepath} from {len(chunks)} chunks"