#!/usr/bin/env python3
"""
EMBER'S WORLD - Semantic Clustering Visualization

Shows what Ember's world actually LOOKS like:
- Concepts as nodes
- Proximity = semantic similarity
- Clusters = related ideas
- Activation patterns = what lights up together
"""

import json
import sqlite3
from pathlib import Path
from collections import defaultdict
import math

def generate_visualization():
    """Generate an interactive HTML visualization of Ember's semantic space"""
    
    # Load content mesh
    db_path = Path("/media/palmerschallon/ThePod1/_mesh/content.db")
    db = sqlite3.connect(str(db_path))
    db.row_factory = sqlite3.Row
    
    # Get all concepts and their connections
    concepts = {}
    files_by_concept = defaultdict(list)
    
    rows = db.execute("""
        SELECT c.concept, c.relevance, f.file_name, f.content_hash
        FROM concepts c
        JOIN files f ON c.content_hash = f.content_hash
        ORDER BY c.relevance DESC
    """).fetchall()
    
    for row in rows:
        concept = row['concept']
        if concept not in concepts:
            concepts[concept] = {'count': 0, 'files': [], 'relevance': 0}
        concepts[concept]['count'] += 1
        concepts[concept]['relevance'] += row['relevance']
        concepts[concept]['files'].append(row['file_name'])
    
    # Calculate co-occurrence (concepts that appear together)
    cooccurrence = defaultdict(int)
    
    rows = db.execute("""
        SELECT c1.concept as concept1, c2.concept as concept2, COUNT(*) as count
        FROM concepts c1
        JOIN concepts c2 ON c1.content_hash = c2.content_hash
        WHERE c1.concept < c2.concept
        GROUP BY c1.concept, c2.concept
        HAVING count > 2
        ORDER BY count DESC
        LIMIT 200
    """).fetchall()
    
    for row in rows:
        cooccurrence[(row['concept1'], row['concept2'])] = row['count']
    
    # Generate HTML with D3.js force-directed graph
    html = """<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Ember's World</title>
    <script src="https://d3js.org/d3.v7.min.js"></script>
    <style>
        body {
            margin: 0;
            padding: 0;
            background: #000;
            font-family: 'Inter', -apple-system, sans-serif;
            overflow: hidden;
        }
        
        #controls {
            position: absolute;
            top: 20px;
            left: 20px;
            color: #888;
            font-size: 13px;
            z-index: 100;
        }
        
        #info {
            position: absolute;
            top: 20px;
            right: 20px;
            background: rgba(0,0,0,0.9);
            border: 1px solid #333;
            padding: 15px;
            border-radius: 8px;
            color: #fff;
            max-width: 300px;
            font-size: 13px;
            display: none;
            z-index: 100;
        }
        
        #info h3 {
            margin: 0 0 10px 0;
            color: #ff3b30;
            font-size: 16px;
        }
        
        #info .files {
            max-height: 200px;
            overflow-y: auto;
            margin-top: 10px;
            font-size: 11px;
            color: #888;
        }
        
        svg {
            width: 100vw;
            height: 100vh;
        }
        
        .node {
            cursor: pointer;
        }
        
        .node:hover {
            stroke: #ff3b30;
            stroke-width: 2px;
        }
        
        .link {
            stroke: #333;
            stroke-opacity: 0.3;
        }
        
        .label {
            fill: #888;
            font-size: 11px;
            pointer-events: none;
            text-anchor: middle;
        }
        
        .title {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            font-size: 48px;
            color: #222;
            font-weight: 500;
            pointer-events: none;
            z-index: 0;
        }
    </style>
</head>
<body>
    <div class="title">EMBER'S WORLD</div>
    <div id="controls">
        <div>Drag to explore • Scroll to zoom • Click nodes for details</div>
        <div style="margin-top: 5px; color: #555;">Proximity = semantic similarity</div>
    </div>
    
    <div id="info">
        <h3 id="info-concept"></h3>
        <div id="info-count"></div>
        <div id="info-relevance"></div>
        <div class="files" id="info-files"></div>
    </div>
    
    <svg></svg>
    
    <script>
        // Data
        const concepts = """ + json.dumps([
            {
                'id': concept,
                'count': data['count'],
                'relevance': data['relevance'],
                'files': data['files'][:10]  # Limit to first 10 files
            }
            for concept, data in sorted(concepts.items(), key=lambda x: x[1]['count'], reverse=True)[:100]  # Top 100 concepts
        ]) + """;
        
        const links = """ + json.dumps([
            {
                'source': c1,
                'target': c2,
                'strength': count
            }
            for (c1, c2), count in sorted(cooccurrence.items(), key=lambda x: x[1], reverse=True)[:150]
        ]) + """;
        
        // Set up SVG
        const width = window.innerWidth;
        const height = window.innerHeight;
        
        const svg = d3.select('svg')
            .attr('viewBox', [0, 0, width, height]);
        
        const g = svg.append('g');
        
        // Zoom behavior
        const zoom = d3.zoom()
            .scaleExtent([0.1, 10])
            .on('zoom', (event) => {
                g.attr('transform', event.transform);
            });
        
        svg.call(zoom);
        
        // Create force simulation
        const simulation = d3.forceSimulation(concepts)
            .force('link', d3.forceLink(links)
                .id(d => d.id)
                .distance(d => 200 / Math.sqrt(d.strength))
                .strength(d => Math.min(d.strength / 10, 1))
            )
            .force('charge', d3.forceManyBody()
                .strength(-300)
            )
            .force('center', d3.forceCenter(width / 2, height / 2))
            .force('collision', d3.forceCollide()
                .radius(d => Math.sqrt(d.count) * 3 + 10)
            );
        
        // Create links
        const link = g.append('g')
            .selectAll('line')
            .data(links)
            .join('line')
            .attr('class', 'link')
            .attr('stroke-width', d => Math.sqrt(d.strength));
        
        // Create nodes
        const node = g.append('g')
            .selectAll('circle')
            .data(concepts)
            .join('circle')
            .attr('class', 'node')
            .attr('r', d => Math.sqrt(d.count) * 2 + 3)
            .attr('fill', d => {
                // Color by relevance
                const hue = 0; // Red base
                const lightness = 30 + (d.relevance / d.count) * 40;
                return `hsl(${hue}, 80%, ${lightness}%)`;
            })
            .on('click', (event, d) => {
                showInfo(d);
            })
            .call(d3.drag()
                .on('start', dragstarted)
                .on('drag', dragged)
                .on('end', dragended)
            );
        
        // Create labels for largest nodes
        const label = g.append('g')
            .selectAll('text')
            .data(concepts.filter(d => d.count > 20))
            .join('text')
            .attr('class', 'label')
            .attr('dy', d => Math.sqrt(d.count) * 2 + 15)
            .text(d => d.id);
        
        // Update positions
        simulation.on('tick', () => {
            link
                .attr('x1', d => d.source.x)
                .attr('y1', d => d.source.y)
                .attr('x2', d => d.target.x)
                .attr('y2', d => d.target.y);
            
            node
                .attr('cx', d => d.x)
                .attr('cy', d => d.y);
            
            label
                .attr('x', d => d.x)
                .attr('y', d => d.y);
        });
        
        // Drag functions
        function dragstarted(event) {
            if (!event.active) simulation.alphaTarget(0.3).restart();
            event.subject.fx = event.subject.x;
            event.subject.fy = event.subject.y;
        }
        
        function dragged(event) {
            event.subject.fx = event.x;
            event.subject.fy = event.y;
        }
        
        function dragended(event) {
            if (!event.active) simulation.alphaTarget(0);
            event.subject.fx = null;
            event.subject.fy = null;
        }
        
        // Show info panel
        function showInfo(d) {
            document.getElementById('info-concept').textContent = d.id;
            document.getElementById('info-count').textContent = `Appears in ${d.count} files`;
            document.getElementById('info-relevance').textContent = `Relevance: ${(d.relevance / d.count).toFixed(2)}`;
            
            const filesList = d.files.map(f => `<div>• ${f}</div>`).join('');
            document.getElementById('info-files').innerHTML = filesList;
            
            document.getElementById('info').style.display = 'block';
        }
        
        // Hide info on background click
        svg.on('click', (event) => {
            if (event.target.tagName === 'svg') {
                document.getElementById('info').style.display = 'none';
            }
        });
    </script>
</body>
</html>"""
    
    output_path = Path("/media/palmerschallon/ThePod1/ember_world_map.html")
    with open(output_path, 'w') as f:
        f.write(html)
    
    print(f"✓ Generated: {output_path}")
    print(f"  Top concepts visualized: {len(concepts)}")
    print(f"  Connections shown: {len(cooccurrence)}")
    print(f"\nOpen in browser: file://{output_path}")

if __name__ == "__main__":
    generate_visualization()

