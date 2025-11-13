#!/usr/bin/env python3
import base64
import zlib

def write_compressed(filepath, large_content):
    """Compress and write large content"""
    compressed = zlib.compress(large_content.encode())
    encoded = base64.b64encode(compressed).decode()
    
    # Write in chunks if needed
    chunk_size = 1000
    with open(filepath + '.z64', 'w') as f:
        for i in range(0, len(encoded), chunk_size):
            f.write(encoded[i:i+chunk_size])
    
def read_compressed(filepath):
    """Read and decompress content"""
    with open(filepath + '.z64', 'r') as f:
        encoded = f.read()
    compressed = base64.b64decode(encoded)
    return zlib.decompress(compressed).decode()