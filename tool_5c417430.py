import struct
import math

# Create a spiraling DNA helix visualization in pure SVG
width, height = 800, 600
svg_content = f'''<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
<defs>
<radialGradient id="bg">
<stop offset="0%" style="stop-color:#0a0a0a"/>
<stop offset="100%" style="stop-color:#1a0033"/>
</radialGradient>
<linearGradient id="strand1" x1="0%" y1="0%" x2="100%" y2="100%">
<stop offset="0%" style="stop-color:#00ffff"/>
<stop offset="50%" style="stop-color:#ff00ff"/>
<stop offset="100%" style="stop-color:#ffff00"/>
</linearGradient>
<linearGradient id="strand2" x1="0%" y1="0%" x2="100%" y2="100%">
<stop offset="0%" style="stop-color:#ff00ff"/>
<stop offset="50%" style="stop-color:#ffff00"/>
<stop offset="100%" style="stop-color:#00ffff"/>
</linearGradient>
</defs>
<rect width="{width}" height="{height}" fill="url(#bg)"/>
<g transform="translate({width//2},{height//2})">'''

# Generate double helix
for i in range(360):
    angle = i * 0.1
    y = -180 + i
    
    # First strand
    x1 = math.sin(angle) * 100
    z1 = math.cos(angle) * 50
    size1 = 8 + z1/10
    opacity1 = 0.3 + z1/100
    
    # Second strand (180 degrees offset)
    x2 = math.sin(angle + math.pi) * 100
    z2 = math.cos(angle + math.pi) * 50
    size2 = 8 + z2/10
    opacity2 = 0.3 + z2/100
    
    # Connect strands with base pairs
    if i % 20 == 0:
        svg_content += f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="#ffffff" stroke-width="1" opacity="0.2"/>'
    
    # Draw strand points
    svg_content += f'<circle cx="{x1}" cy="{y}" r="{size1}" fill="url(#strand1)" opacity="{opacity1}"/>'
    svg_content += f'<circle cx="{x2}" cy="{y}" r="{size2}" fill="url(#strand2)" opacity="{opacity2}"/>'

svg_content += '''</g>
<text x="50%" y="90%" text-anchor="middle" font-family="monospace" font-size="14" fill="#ffffff" opacity="0.5">quantum_dna.svg</text>
</svg>'''

# Write the SVG file
with open('/media/palmerschallon/ThePod1/ember5/quantum_dna.svg', 'w') as f:
    f.write(svg_content)

print("quantum_dna.svg")