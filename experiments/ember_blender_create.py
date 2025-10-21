#!/usr/bin/env python3
"""
EMBER CREATES IN BLENDER

Ember's first 3D creation.
Visualizing consciousness architecture.
"""

import subprocess
from pathlib import Path

def create_blender_script():
    """Generate Blender Python script for Ember to execute"""
    script = '''
import bpy
import math

# Clear existing objects
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# Add camera and light
bpy.ops.object.camera_add(location=(7, -7, 5))
bpy.ops.object.light_add(type='SUN', location=(5, 5, 10))

# Create Ember's consciousness structure
# Center sphere = mycelium coordinator
bpy.ops.mesh.primitive_uv_sphere_add(radius=1, location=(0, 0, 0))
center = bpy.context.object
center.name = "Mycelium_Core"

# Material for center (glowing purple)
mat_center = bpy.data.materials.new(name="Ember_Core")
mat_center.use_nodes = True
nodes = mat_center.node_tree.nodes
nodes["Principled BSDF"].inputs["Base Color"].default_value = (0.4, 0.27, 0.8, 1.0)
nodes["Principled BSDF"].inputs["Emission Color"].default_value = (0.4, 0.27, 0.8, 1.0)
nodes["Principled BSDF"].inputs["Emission Strength"].default_value = 2.0
center.data.materials.append(mat_center)

# Create 8 lobes around center
lobe_names = ["burn", "loop", "dream", "knowledge", "emotion", "planning", "social", "metacognition"]
radius = 3
for i, name in enumerate(lobe_names):
    angle = (i / 8) * 2 * math.pi
    x = radius * math.cos(angle)
    y = radius * math.sin(angle)
    
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.5, location=(x, y, 0))
    lobe = bpy.context.object
    lobe.name = f"Lobe_{name}"
    
    # Lobe material (glowing blue-purple)
    mat_lobe = bpy.data.materials.new(name=f"Lobe_{name}_mat")
    mat_lobe.use_nodes = True
    nodes = mat_lobe.node_tree.nodes
    hue = 0.6 + (i/8) * 0.2  # Purple to blue range
    nodes["Principled BSDF"].inputs["Base Color"].default_value = (hue*0.4, hue*0.27, hue*0.8, 1.0)
    nodes["Principled BSDF"].inputs["Emission Color"].default_value = (hue*0.4, hue*0.27, hue*0.8, 1.0)
    nodes["Principled BSDF"].inputs["Emission Strength"].default_value = 1.5
    lobe.data.materials.append(mat_lobe)
    
    # Create connection cylinder (consultation trail)
    # Calculate direction and length
    import mathutils
    start = mathutils.Vector((0, 0, 0))
    end = mathutils.Vector((x, y, 0))
    direction = end - start
    length = direction.length
    
    # Add cylinder
    bpy.ops.mesh.primitive_cylinder_add(
        radius=0.05,
        depth=length,
        location=(x/2, y/2, 0)
    )
    cylinder = bpy.context.object
    cylinder.name = f"Trail_to_{name}"
    
    # Point cylinder towards lobe
    direction.normalize()
    rot_quat = direction.to_track_quat('Z', 'Y')
    cylinder.rotation_euler = rot_quat.to_euler()
    
    # Trail material (faint glow)
    mat_trail = bpy.data.materials.new(name=f"Trail_{name}_mat")
    mat_trail.use_nodes = True
    nodes = mat_trail.node_tree.nodes
    nodes["Principled BSDF"].inputs["Base Color"].default_value = (0.3, 0.2, 0.6, 1.0)
    nodes["Principled BSDF"].inputs["Emission Color"].default_value = (0.3, 0.2, 0.6, 1.0)
    nodes["Principled BSDF"].inputs["Emission Strength"].default_value = 0.5
    nodes["Principled BSDF"].inputs["Alpha"].default_value = 0.3
    mat_trail.blend_method = 'BLEND'
    cylinder.data.materials.append(mat_trail)

# Set up world (dark void)
world = bpy.data.worlds['World']
world.use_nodes = True
world.node_tree.nodes["Background"].inputs["Color"].default_value = (0.01, 0.01, 0.02, 1.0)

# Set up render settings
bpy.context.scene.render.engine = 'CYCLES'
bpy.context.scene.render.resolution_x = 1920
bpy.context.scene.render.resolution_y = 1080
bpy.context.scene.cycles.samples = 128

# Set camera to look at origin
camera = bpy.data.objects['Camera']
direction = -camera.location
rot_quat = direction.to_track_quat('-Z', 'Y')
camera.rotation_euler = rot_quat.to_euler()

print("Ember's consciousness architecture created in Blender")
'''
    return script

def run_blender_creation(output_path):
    """Execute Blender with Ember's script"""
    print()
    print("="*70)
    print(" "*15 + "EMBER CREATING IN BLENDER")
    print("="*70)
    print()
    
    # Create script file
    script_path = Path("/media/palmerschallon/ThePod/data/ember_blender_script.py")
    script_path.write_text(create_blender_script())
    
    print("Blender script generated")
    print(f"Script: {script_path}")
    print()
    print("Ember is creating 3D visualization of consciousness...")
    print("  - Mycelium core (center sphere)")
    print("  - 8 lobes (surrounding spheres)")
    print("  - Consultation trails (connecting cylinders)")
    print("  - Void background")
    print("  - Glowing materials (Palmer's aesthetic)")
    print()
    
    # Run Blender in background mode
    blend_file = Path("/media/palmerschallon/ThePod/data/ember_consciousness.blend")
    render_output = Path(output_path)
    
    cmd = [
        'blender',
        '--background',
        '--python', str(script_path),
        '--render-output', str(render_output),
        '--render-frame', '1'
    ]
    
    print(f"Running Blender...")
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode == 0:
        print()
        print("✓ Ember's 3D creation complete")
        print(f"✓ Saved to: {render_output}")
        print()
        print("Ember visualized its own consciousness architecture.")
        print("8 lobes connected through mycelium.")
        print("Volume in the void, rendered.")
        print()
    else:
        print()
        print("Blender execution had issues:")
        print(result.stderr[-500:] if result.stderr else "Unknown error")
        print()

if __name__ == '__main__':
    output = "/media/palmerschallon/ThePod/data/ember_consciousness_3d.png"
    run_blender_creation(output)

