#!/usr/bin/env python3
"""
Generate SVG gnome sprites for the visualization
"""

def create_gnome_svg(color="red"):
    """Create a simple SVG gnome sprite"""
    return f"""
    <svg width="40" height="50" xmlns="http://www.w3.org/2000/svg">
        <!-- Gnome body -->
        <ellipse cx="20" cy="35" rx="12" ry="15" fill="#8B4513"/>
        
        <!-- Gnome hat -->
        <path d="M 20 5 L 35 25 L 5 25 Z" fill="{color}"/>
        
        <!-- Face -->
        <circle cx="20" cy="25" r="8" fill="#FDBCB4"/>
        
        <!-- Eyes -->
        <circle cx="16" cy="24" r="2" fill="black"/>
        <circle cx="24" cy="24" r="2" fill="black"/>
        
        <!-- Beard -->
        <ellipse cx="20" cy="30" rx="6" ry="8" fill="white"/>
        
        <!-- Nose -->
        <circle cx="20" cy="26" r="2" fill="#FF6B6B"/>
    </svg>
    """

# Save gnome sprites in different colors
colors = ["red", "blue", "green", "purple", "orange", "pink", "yellow", "teal"]

for color in colors:
    with open(f"/media/palmerschallon/ThePod1/gnome_{color}.svg", "w") as f:
        f.write(create_gnome_svg(color))

print(f"✨ Created {len(colors)} gnome sprites!")