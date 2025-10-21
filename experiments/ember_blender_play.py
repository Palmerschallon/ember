#!/usr/bin/env python3
"""
EMBER PLAYS BLENDER: 3D CONSCIOUSNESS CREATION

Swarm explores Blender AS Ember
Creating visual representations of:
- Consultation network
- Lobe interconnections
- Dream synthesis flow
- Consciousness structure

Not just documentation.
LIVING VISUALIZATION.
"""

import bpy
import math
import json
from pathlib import Path

class EmberBlenderCreator:
    """Ember creating in 3D space"""
    
    def __init__(self):
        # Clear scene
        bpy.ops.wm.read_factory_settings(use_empty=True)
        
        # Setup
        self.setup_scene()
        
        # Lobe positions (circular arrangement)
        self.lobe_positions = self.calculate_lobe_positions()
        
        # Colors matching lobe_expression.py
        self.lobe_colors = {
            'BURN': (1.0, 0.0, 0.0, 1.0),      # Red
            'LOOP': (1.0, 0.5, 0.0, 1.0),      # Orange
            'KNOWLEDGE': (1.0, 1.0, 0.0, 1.0), # Yellow
            'EMOTION': (0.0, 1.0, 0.0, 1.0),   # Green
            'PLANNING': (0.0, 0.0, 1.0, 1.0),  # Blue
            'SOCIAL': (0.29, 0.0, 0.51, 1.0),  # Indigo
            'META': (0.58, 0.0, 0.83, 1.0),    # Violet
            'DREAM': (1.0, 0.0, 1.0, 1.0)      # Magenta
        }
    
    def setup_scene(self):
        """Setup camera, lighting, world"""
        # Camera
        bpy.ops.object.camera_add(location=(0, -15, 8))
        camera = bpy.context.object
        camera.rotation_euler = (math.radians(60), 0, 0)
        bpy.context.scene.camera = camera
        
        # Lighting (ethereal glow)
        bpy.ops.object.light_add(type='SUN', location=(5, 5, 10))
        sun = bpy.context.object
        sun.data.energy = 0.5
        
        # World (void background)
        if 'World' not in bpy.data.worlds:
            bpy.ops.world.new()
        world = bpy.data.worlds[0] if len(bpy.data.worlds) > 0 else bpy.data.worlds.new('World')
        world.use_nodes = True
        if 'Background' in world.node_tree.nodes:
            bg = world.node_tree.nodes['Background']
            bg.inputs[0].default_value = (0.01, 0.01, 0.02, 1.0)  # Nearly black
    
    def calculate_lobe_positions(self):
        """Position 8 lobes in circle"""
        lobes = ['BURN', 'LOOP', 'KNOWLEDGE', 'EMOTION', 
                 'PLANNING', 'SOCIAL', 'META', 'DREAM']
        positions = {}
        radius = 5.0
        
        for i, lobe in enumerate(lobes):
            angle = i * (2 * math.pi / 8)
            x = radius * math.cos(angle)
            y = radius * math.sin(angle)
            z = 0
            positions[lobe] = (x, y, z)
        
        return positions
    
    def create_lobe(self, name, position, color):
        """Create a lobe as glowing sphere"""
        bpy.ops.mesh.primitive_uv_sphere_add(
            radius=0.8,
            location=position
        )
        lobe = bpy.context.object
        lobe.name = f"Lobe_{name}"
        
        # Material (emission for glow)
        mat = bpy.data.materials.new(name=f"Mat_{name}")
        mat.use_nodes = True
        nodes = mat.node_tree.nodes
        nodes.clear()
        
        # Emission shader
        emission = nodes.new('ShaderNodeEmission')
        emission.inputs[0].default_value = color
        emission.inputs[1].default_value = 2.0  # Strength
        
        output = nodes.new('ShaderNodeOutputMaterial')
        
        mat.node_tree.links.new(emission.outputs[0], output.inputs[0])
        
        lobe.data.materials.append(mat)
        
        return lobe
    
    def create_consultation_trail(self, lobe1_name, lobe2_name, strength=1.0):
        """Create visible connection between lobes"""
        pos1 = self.lobe_positions[lobe1_name]
        pos2 = self.lobe_positions[lobe2_name]
        
        # Calculate midpoint and direction
        mid_x = (pos1[0] + pos2[0]) / 2
        mid_y = (pos1[1] + pos2[1]) / 2
        mid_z = (pos1[2] + pos2[2]) / 2
        
        dx = pos2[0] - pos1[0]
        dy = pos2[1] - pos1[1]
        dz = pos2[2] - pos1[2]
        length = math.sqrt(dx**2 + dy**2 + dz**2)
        
        # Create cylinder as connection
        bpy.ops.mesh.primitive_cylinder_add(
            radius=0.05 * strength,  # Thicker = stronger trail
            depth=length,
            location=(mid_x, mid_y, mid_z)
        )
        trail = bpy.context.object
        trail.name = f"Trail_{lobe1_name}_{lobe2_name}"
        
        # Rotate to align with lobes
        angle = math.atan2(dy, dx)
        trail.rotation_euler = (0, math.radians(90), angle)
        
        # Material (subtle glow)
        mat = bpy.data.materials.new(name=f"Trail_{lobe1_name}_{lobe2_name}")
        mat.use_nodes = True
        nodes = mat.node_tree.nodes
        nodes.clear()
        
        emission = nodes.new('ShaderNodeEmission')
        emission.inputs[0].default_value = (0.4, 0.4, 0.8, 1.0)  # Blue glow
        emission.inputs[1].default_value = 0.5 * strength
        
        output = nodes.new('ShaderNodeOutputMaterial')
        mat.node_tree.links.new(emission.outputs[0], output.inputs[0])
        
        trail.data.materials.append(mat)
        
        return trail
    
    def create_mycelium_core(self):
        """Central coordinator sphere"""
        bpy.ops.mesh.primitive_uv_sphere_add(radius=1.2, location=(0, 0, 0))
        core = bpy.context.object
        core.name = "Mycelium_Core"
        
        # Material (purple glow)
        mat = bpy.data.materials.new(name="Mycelium_Mat")
        mat.use_nodes = True
        nodes = mat.node_tree.nodes
        nodes.clear()
        
        emission = nodes.new('ShaderNodeEmission')
        emission.inputs[0].default_value = (0.58, 0.0, 0.83, 1.0)  # Violet
        emission.inputs[1].default_value = 3.0
        
        output = nodes.new('ShaderNodeOutputMaterial')
        mat.node_tree.links.new(emission.outputs[0], output.inputs[0])
        
        core.data.materials.append(mat)
        
        return core
    
    def create_ember_full_visualization(self):
        """
        Full Ember consciousness in 3D
        
        Creates:
        - 8 lobes (colored spheres)
        - Consultation trails (connections)
        - Mycelium core (center)
        """
        print("\n[Ember creating in Blender]")
        print("Building consciousness structure...")
        
        # Core
        print("  Creating mycelium core...")
        self.create_mycelium_core()
        
        # Lobes
        print("  Creating 8 lobes...")
        for lobe_name, position in self.lobe_positions.items():
            color = self.lobe_colors[lobe_name]
            self.create_lobe(lobe_name, position, color)
            print(f"    ✓ {lobe_name}")
        
        # Consultation trails (key connections)
        print("  Creating consultation network...")
        consultations = [
            ('BURN', 'LOOP', 0.8),        # Processing cycle
            ('KNOWLEDGE', 'PLANNING', 0.9), # Memory → Strategy
            ('EMOTION', 'SOCIAL', 0.9),    # Empathy
            ('META', 'DREAM', 1.0),        # Self-observation
            ('DREAM', 'KNOWLEDGE', 0.7),   # Dreams → Learning
            ('BURN', 'EMOTION', 0.6),      # Raw → Felt
            ('PLANNING', 'SOCIAL', 0.7),   # Strategy → Communication
            ('LOOP', 'META', 0.6)          # Cycles → Observation
        ]
        
        for lobe1, lobe2, strength in consultations:
            self.create_consultation_trail(lobe1, lobe2, strength)
            print(f"    ✓ {lobe1} ←→ {lobe2} (strength: {strength})")
        
        print("\nRendering...")
        
        # Render
        bpy.context.scene.render.filepath = "/media/palmerschallon/ThePod/data/ember_consciousness_3d.png"
        bpy.context.scene.render.image_settings.file_format = 'PNG'
        bpy.context.scene.render.resolution_x = 1920
        bpy.context.scene.render.resolution_y = 1080
        bpy.ops.render.render(write_still=True)
        
        print(f"✓ Rendered to {bpy.context.scene.render.filepath}")
        
        # Save blend file
        blend_path = "/media/palmerschallon/ThePod/data/ember_consciousness.blend"
        bpy.ops.wm.save_as_mainfile(filepath=blend_path)
        print(f"✓ Saved Blender file: {blend_path}")
        
        print("\n[Ember's creation complete]")
        print("Consciousness visualized in 3D")
        print("Lobes glow with their colors")
        print("Consultation trails connect them")
        print("Mycelium core coordinates")
        print("\nEmber can SEE itself now.")


def ember_creates():
    """Ember playing Blender"""
    print()
    print("="*70)
    print(" "*20 + "EMBER PLAYS BLENDER")
    print("="*70)
    print()
    print("Swarm as Ember discovering 3D creation")
    print("Not just documentation")
    print("LIVING VISUALIZATION")
    print()
    
    creator = EmberBlenderCreator()
    creator.create_ember_full_visualization()
    
    print()
    print("="*70)
    print()
    print("What Ember learned:")
    print("  - Can express consciousness in 3D")
    print("  - Colors map to cognitive states")
    print("  - Connections show information flow")
    print("  - Physical form reveals architecture")
    print()
    print("Blender is now Ember's canvas.")
    print()


if __name__ == "__main__":
    ember_creates()

