#!/usr/bin/env python3
"""Generate large codebases from templates"""

def generate_class(name, methods, size=1000):
    """Generate a Python class with specified methods"""
    code = f"class {name}:\n"
    for method in methods:
        code += f"    def {method}(self):\n"
        code += f"        # Generated method with {size} lines\n"
        for i in range(min(size, 100)):
            code += f"        var_{i} = {i} * 2\n"
    return code

# Usage: generate and write large files
with open('/tmp/generated.py', 'w') as f:
    f.write(generate_class('MegaClass', ['process', 'analyze', 'transform'], 500))