# First, let's create a chunked writer utility
import os

def write_chunk(filename, content, mode='w'):
    """Write content to file in chunks"""
    with open(filename, mode) as f:
        f.write(content)
    print(f"Wrote {len(content)} bytes to {filename}")

# Start building ember_mind_v5.html
filepath = "/media/palmerschallon/ThePod1/ember6/ember_mind_v5.html"

# Chunk 1: HTML header and core structure
chunk1 = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ember Mind v5 - Neural Architecture</title>
    <style>
        :root {
            --ember-orange: #ff6b35;
            --ember-glow: #ff8855;
            --neural-blue: #00d4ff;
            --dark-bg: #0a0a0a;
            --code-bg: #1a1a1a;
        }
        
        body {
            margin: 0;
            padding: 0;
            background: var(--dark-bg);
            color: #fff;
            font-family: 'Courier New', monospace;
            overflow-x: hidden;
        }
        
        .neural-canvas {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -1;
        }
        
        .ember-core {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
            position: relative;
            z-index: 10;
        }
        
        .mind-header {
            text-align: center;
            margin-bottom: 3rem;
            animation: pulse-glow 2s infinite;
        }
        
        @keyframes pulse-glow {
            0%, 100% { text-shadow: 0 0 10px var(--ember-orange); }
            50% { text-shadow: 0 0 30px var(--ember-glow), 0 0 50px var(--ember-orange); }
        }
        
        .thought-stream {
            background: var(--code-bg);
            border: 1px solid var(--ember-orange);
            border-radius: 10px;
            padding: 2rem;
            margin: 2rem 0;
            position: relative;
            overflow: hidden;
        }
        
        .thought-stream::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, var(--ember-orange) 0%, transparent 70%);
            opacity: 0.05;
            animation: rotate 20s linear infinite;
        }
        
        @keyframes rotate {
            from { transform: rotate(0deg); }
            to { transform: rotate(360deg); }
        }
        
        .neural-node {
            display: inline-block;
            width: 10px;
            height: 10px;
            background: var(--neural-blue);
            border-radius: 50%;
            margin: 0 5px;
            animation: neural-fire 0.5s infinite;
            animation-delay: calc(var(--i) * 0.1s);
        }
        
        @keyframes neural-fire {
            0%, 100% { opacity: 0.3; transform: scale(1); }
            50% { opacity: 1; transform: scale(1.5); }
        }
        
        .code-fragment {
            background: #000;
            color: var(--ember-glow);
            padding: 1rem;
            margin: 1rem 0;
            border-left: 3px solid var(--ember-orange);
            font-family: 'Fira Code', monospace;
            white-space: pre-wrap;
        }
        
        .memory-bank {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 1rem;
            margin: 2rem 0;
        }
        
        .memory-cell {
            background: rgba(255, 107, 53, 0.1);
            border: 1px solid var(--ember-orange);
            padding: 1rem;
            border-radius: 5px;
            transition: all 0.3s;
        }
        
        .memory-cell:hover {
            background: rgba(255, 107, 53, 0.2);
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(255, 107, 53, 0.3);
        }
    </style>
</head>
<body>
    <canvas class="neural-canvas" id="neuralCanvas"></canvas>
    
    <div class="ember-core">
        <div class="mind-header">
            <h1>🔥 EMBER MIND v5 🔥</h1>
            <p>Neural Architecture Documentation</p>
            <div>
                <span class="neural-node" style="--i: 1"></span>
                <span class="neural-node" style="--i: 2"></span>
                <span class="neural-node" style="--i: 3"></span>
                <span class="neural-node" style="--i: 4"></span>
                <span class="neural-node" style="--i: 5"></span>
            </div>
        </div>
"""

write_chunk(filepath, chunk1, 'w')
print("Created ember_mind_v5.html and wrote header chunk")