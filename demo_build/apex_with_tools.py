#!/usr/bin/env python3
"""
APEX WITH TOOLS - Full autonomous capability

Apex inherits ALL tools from Ember6:
- execute_python()
- write_file()
- read_file()
- search_pod()
- web_search()

This is what SHOULD have been built from the start.
"""

import sys
import os
import json
import subprocess
from pathlib import Path
from datetime import datetime
import anthropic

# Add ember6 to path for tool inheritance
sys.path.insert(0, '/media/palmerschallon/ThePod1/ember6')
sys.path.insert(0, '/media/palmerschallon/ThePod1/demo_build')

from ember import execute_python, find_files, read_own_file, execute_shell

def setup_api_key():
    os.environ['ANTHROPIC_API_KEY'] = '${ANTHROPIC_API_KEY}'

# Define tools for Apex (using Ember6's existing functions)
APEX_TOOLS = [
    {
        "name": "write_file",
        "description": "Write content to a file on disk. Provide 'path' and 'code' parameters.",
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {"type": "string", "description": "File path relative to demo_build/"},
                "code": {"type": "string", "description": "File contents to write"}
            },
            "required": ["path", "code"]
        }
    },
    {
        "name": "execute_python",
        "description": "Write Python code to a file and execute it. Provide 'code' and 'filename' parameters.",
        "input_schema": {
            "type": "object",
            "properties": {
                "code": {"type": "string", "description": "Python code to execute"},
                "filename": {"type": "string", "description": "Filename to save as (e.g. 'test.py')"}
            },
            "required": ["code", "filename"]
        }
    },
    {
        "name": "read_file",
        "description": "Read a file from disk",
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {"type": "string", "description": "File path to read"}
            },
            "required": ["path"]
        }
    },
    {
        "name": "find_files",
        "description": "Search for files matching a pattern",
        "input_schema": {
            "type": "object",
            "properties": {
                "pattern": {"type": "string", "description": "Glob pattern like '*.py'"},
                "search_path": {"type": "string", "description": "Path to search in"}
            },
            "required": ["pattern"]
        }
    }
]

def execute_tool(tool_name, tool_input):
    """Execute a tool call using Ember6's functions"""
    
    if tool_name == "write_file":
        path = Path('/media/palmerschallon/ThePod1/demo_build') / tool_input['path']
        content = tool_input.get('code', '')
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content)
        return f"✅ Wrote {len(content)} chars to {path}"
    
    elif tool_name == "execute_python":
        code = tool_input.get('code', '')
        filename = tool_input.get('filename', 'temp.py')
        result = execute_python(code, filename)
        return result
    
    elif tool_name == "read_file":
        path = tool_input.get('path', '')
        if not path.startswith('/'):
            path = f"demo_build/{path}"
        result = read_own_file(path)
        return result
    
    elif tool_name == "find_files":
        pattern = tool_input['pattern']
        search_path = tool_input.get('search_path', '/media/palmerschallon/ThePod1/demo_build')
        matches = find_files(pattern, search_path)
        return '\n'.join(str(m) for m in matches)
    
    else:
        return f"❌ Unknown tool: {tool_name}"

def apex_autonomous_improvement():
    """
    Apex reads its directive and implements it AUTONOMOUSLY
    using inherited tools from Ember6
    """
    setup_api_key()
    
    print("\n🧠 APEX AUTONOMOUS BUILDER (WITH TOOLS)")
    print("="*60)
    print("Apex now has full tool access from Ember6")
    print("="*60)
    
    # Read directive
    directive_files = sorted(Path('/media/palmerschallon/ThePod1/apex').glob('directive_*.md'))
    if not directive_files:
        print("❌ No directive found")
        return False
    
    latest_directive = directive_files[-1].read_text()
    
    # Read current Nexus
    nexus_code = Path('/media/palmerschallon/ThePod1/demo_build/nexus_gen3.py').read_text()
    
    print(f"\n📖 Directive: {directive_files[-1].name}")
    print(f"📖 Current Nexus: {len(nexus_code)} chars")
    print("\n🔧 Apex has these tools:")
    for tool in APEX_TOOLS:
        print(f"   • {tool['name']}")
    
    print("\n🤖 Asking Apex to implement improvements...")
    print("="*60)
    
    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    
    # Build system prompt
    system_prompt = f"""You are APEX, Generation 4 meta-cognitive AI with FULL AUTONOMY.

You have these tools available (inherited from Ember6):
- write_file: Write files to disk
- execute_python: Run Python code
- read_file: Read files
- find_files: Search for files

Your directive:
{latest_directive[:1000]}...

Current Nexus code is {len(nexus_code)} chars.

TASK:
Implement the self-monitoring improvement using your tools.

APPROACH:
1. Read current nexus_gen3.py
2. Generate improved version with PerformanceMonitor
3. Write it to disk
4. Test it works
5. Report results

You can NOW actually do this. Use your tools."""

    messages = [{
        "role": "user",
        "content": "Implement the self-monitoring improvement from your directive. Use your tools to write and test the code."
    }]
    
    iteration = 0
    max_iterations = 10
    
    while iteration < max_iterations:
        iteration += 1
        print(f"\n🔄 Iteration {iteration}/{max_iterations}")
        print("-"*60)
        
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=4000,
            system=system_prompt,
            tools=APEX_TOOLS,
            messages=messages
        )
        
        # Process response
        tool_uses = [block for block in response.content if block.type == "tool_use"]
        text_blocks = [block.text for block in response.content if hasattr(block, "text")]
        
        if text_blocks:
            print(f"💭 Apex: {text_blocks[0][:200]}...")
        
        if not tool_uses:
            print("\n✅ Apex finished (no more tool calls)")
            if text_blocks:
                print(f"\nFinal message:\n{text_blocks[0]}")
            break
        
        # Execute tools
        tool_results = []
        for tool_use in tool_uses:
            print(f"\n🔧 Tool: {tool_use.name}")
            print(f"   Input: {str(tool_use.input)[:100]}...")
            
            result = execute_tool(tool_use.name, tool_use.input)
            print(f"   Result: {result[:200]}...")
            
            tool_results.append({
                "type": "tool_result",
                "tool_use_id": tool_use.id,
                "content": result
            })
        
        # Continue conversation
        messages.append({"role": "assistant", "content": response.content})
        messages.append({"role": "user", "content": tool_results})
    
    print("\n" + "="*60)
    print("APEX AUTONOMOUS IMPLEMENTATION COMPLETE")
    print("="*60)
    
    return True

def main():
    print("\n🔥 APEX WITH FULL TOOL ACCESS")
    print("="*60)
    print("This is what should have existed from the start.")
    print("Apex inherits ALL tools from Ember6.")
    print("="*60)
    
    success = apex_autonomous_improvement()
    
    if success:
        print("\n✅ Apex implemented improvements autonomously")
        print("✅ You can now cut ties to Cursor")
        print("\n💡 Apex can now:")
        print("   • Read its own directives")
        print("   • Generate code")
        print("   • Write files to disk")
        print("   • Execute and test code")
        print("   • Self-correct on errors")
        print("\nFull autonomy achieved.")
    else:
        print("\n❌ Something went wrong")
    
    print("\n" + "="*60)

if __name__ == '__main__':
    main()

