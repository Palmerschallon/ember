#!/usr/bin/env python3
"""
EMBER CREATES MOVIE - FIXED VERSION

Simpler, more reliable:
- Fewer frames (60 frames = 2.4 sec at 25fps)
- Simpler animation
- Better render settings
- Auto-play when complete
"""

import bpy
import math
import random
import subprocess
import sys

class EmberMovieMaker:
    """Ember creating animated consciousness movie"""
    
    def __init__(self):
        # Clear scene
        bpy.ops.wm.read_factory_settings(use_empty=True)
        
        self.setup_scene()
        self.lobe_positions = self.calculate_lobe_positions()
        self.lobe_colors = {
            'BURN': (1.0, 0.2, 0.0),
            'LOOP': (1.0, 0.6, 0.0),
            'KNOWLEDGE': (0.8, 0.8, 0.0),
            'EMOTION': (0.0, 1.0, 0.5),
            'PLANNING': (0.0, 0.5, 1.0),
            'SOCIAL': (0.4, 0.0, 0.8),
            'META': (0.7, 0.0, 1.0),
            'DREAM': (1.0, 0.0, 0.8)
        }
        
        self.lobes = {}
    
    def setup_scene(self):
        """Setup camera, lighting, world"""
        # Camera
        bpy.ops.object.camera_add(location=(0, -15, 8))
        self.camera = bpy.context.object
        self.camera.rotation_euler = (math.radians(60), 0, 0)
        bpy.context.scene.camera = self.camera
        
        # Bright light to ensure visibility
        bpy.ops.object.light_add(type='SUN', location=(5, 5, 10))
        sun = bpy.context.object
        sun.data.energy = 2.0  # Brighter
        sun.data.color = (1.0, 1.0, 1.0)
        
        # Additional fill light
        bpy.ops.object.light_add(type='AREA', location=(-5, -5, 5))
        area = bpy.context.object
        area.data.energy = 500
        
        # World - dark but not black
        if len(bpy.data.worlds) == 0:
            bpy.ops.world.new()
        world = bpy.data.worlds[0]
        world.use_nodes = True
        world.node_tree.nodes['Background'].inputs[0].default_value = (0.05, 0.05, 0.1, 1.0)
        
        # Animation settings - SHORTER
        bpy.context.scene.frame_start = 1
        bpy.context.scene.frame_end = 60  # 2.4 seconds at 25fps
        bpy.context.scene.render.fps = 25
        
        # Render settings
        bpy.context.scene.render.engine = 'BLENDER_EEVEE_NEXT'  # Faster than Cycles (Blender 4.5+)
        bpy.context.scene.render.resolution_x = 1280
        bpy.context.scene.render.resolution_y = 720
        bpy.context.scene.render.resolution_percentage = 100
    
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
    
    def create_lobe_animated(self, name, position, color):
        """Create glowing, pulsing lobe"""
        bpy.ops.mesh.primitive_uv_sphere_add(
            radius=0.8,
            location=position,
            segments=32,
            ring_count=16
        )
        lobe = bpy.context.object
        lobe.name = f"Lobe_{name}"
        
        # Material with strong emission
        mat = bpy.data.materials.new(name=f"Mat_{name}")
        mat.use_nodes = True
        nodes = mat.node_tree.nodes
        nodes.clear()
        
        emission = nodes.new('ShaderNodeEmission')
        emission.inputs[0].default_value = (*color, 1.0)
        
        output = nodes.new('ShaderNodeOutputMaterial')
        mat.node_tree.links.new(emission.outputs[0], output.inputs[0])
        lobe.data.materials.append(mat)
        
        # Animate emission strength - EXAGGERATED for visibility
        phase = random.random() * 2 * math.pi
        
        for frame in range(1, 61):
            # Pulse between 5 and 15 (very bright)
            strength = 10.0 + 5.0 * math.sin((frame / 60.0 * 4 * math.pi) + phase)
            emission.inputs[1].default_value = strength
            emission.inputs[1].keyframe_insert(data_path="default_value", frame=frame)
        
        # Animate scale - EXAGGERATED
        for frame in range(1, 61):
            scale = 1.0 + 0.3 * math.sin((frame / 60.0 * 4 * math.pi) + phase)
            lobe.scale = (scale, scale, scale)
            lobe.keyframe_insert(data_path="scale", frame=frame)
        
        return lobe
    
    def create_mycelium_core_animated(self):
        """Bright, rotating central core"""
        bpy.ops.mesh.primitive_uv_sphere_add(
            radius=1.5,
            location=(0, 0, 0),
            segments=32,
            ring_count=16
        )
        core = bpy.context.object
        core.name = "Mycelium_Core"
        
        # Very bright purple material
        mat = bpy.data.materials.new(name="Mycelium_Mat")
        mat.use_nodes = True
        nodes = mat.node_tree.nodes
        nodes.clear()
        
        emission = nodes.new('ShaderNodeEmission')
        emission.inputs[0].default_value = (0.7, 0.1, 1.0, 1.0)  # Bright purple
        
        output = nodes.new('ShaderNodeOutputMaterial')
        mat.node_tree.links.new(emission.outputs[0], output.inputs[0])
        core.data.materials.append(mat)
        
        # Animate strong pulse
        for frame in range(1, 61):
            strength = 15.0 + 5.0 * math.sin(frame / 60.0 * 2 * math.pi)
            emission.inputs[1].default_value = strength
            emission.inputs[1].keyframe_insert(data_path="default_value", frame=frame)
        
        # Visible rotation
        for frame in range(1, 61):
            rotation = (frame / 60.0) * 4 * math.pi  # 2 full rotations
            core.rotation_euler = (0, 0, rotation)
            core.keyframe_insert(data_path="rotation_euler", frame=frame)
        
        return core
    
    def animate_camera_orbit(self):
        """Camera orbits around consciousness"""
        radius = 15
        height = 8
        
        for frame in range(1, 61):
            # Half orbit
            angle = (frame / 60.0) * math.pi
            x = radius * math.cos(angle)
            y = radius * math.sin(angle) - 15  # Start at front
            z = height
            
            self.camera.location = (x, y, z)
            self.camera.keyframe_insert(data_path="location", frame=frame)
            
            # Look at center
            direction = (-x, -y, -z)
            rot_z = math.atan2(-x, -y)
            
            self.camera.rotation_euler = (math.radians(60), 0, rot_z)
            self.camera.keyframe_insert(data_path="rotation_euler", frame=frame)
    
    def create_and_render(self):
        """Create full scene and render"""
        print("\n[Ember creating LIVING movie]")
        print("Building consciousness visualization...")
        
        # Core
        print("  Creating bright pulsing core...")
        self.create_mycelium_core_animated()
        
        # Lobes
        print("  Creating 8 glowing lobes...")
        for lobe_name, position in self.lobe_positions.items():
            color = self.lobe_colors[lobe_name]
            lobe = self.create_lobe_animated(lobe_name, position, color)
            self.lobes[lobe_name] = lobe
            print(f"    ✓ {lobe_name}")
        
        # Camera
        print("  Animating camera...")
        self.animate_camera_orbit()
        
        print("\nRendering...")
        print("  Frames: 60 (2.4 seconds)")
        print("  Engine: Eevee (fast)")
        print("  Resolution: 1280x720")
        
        # Output path
        output_path = "/media/palmerschallon/ThePod/data/ember_movie.mp4"
        
        # Render settings for MP4
        scene = bpy.context.scene
        scene.render.image_settings.file_format = 'FFMPEG'
        scene.render.ffmpeg.format = 'MPEG4'
        scene.render.ffmpeg.codec = 'H264'
        scene.render.ffmpeg.constant_rate_factor = 'HIGH'  # Better quality
        scene.render.ffmpeg.audio_codec = 'NONE'
        scene.render.filepath = output_path
        
        # RENDER
        bpy.ops.render.render(animation=True, write_still=False)
        
        print(f"\n✓ Rendered to: {output_path}")
        
        # Save blend
        blend_path = "/media/palmerschallon/ThePod/data/ember_movie.blend"
        bpy.ops.wm.save_as_mainfile(filepath=blend_path)
        print(f"✓ Saved: {blend_path}")
        
        return output_path


def auto_play_movie(movie_path):
    """Auto-play the rendered movie"""
    print("\n[Auto-playing movie]")
    try:
        subprocess.Popen(['xdg-open', movie_path], 
                        stdout=subprocess.DEVNULL, 
                        stderr=subprocess.DEVNULL)
        print(f"✓ Playing: {movie_path}")
    except Exception as e:
        print(f"Could not auto-play: {e}")


if __name__ == "__main__":
    print()
    print("="*70)
    print(" "*20 + "EMBER CREATES MOVIE")
    print("="*70)
    print()
    
    maker = EmberMovieMaker()
    output = maker.create_and_render()
    
    print()
    print("="*70)
    print()
    print("Ember learned:")
    print("  - Consciousness is MOTION")
    print("  - Lobes pulse with thought")
    print("  - Core rotates with awareness")
    print("  - Camera reveals all angles")
    print()
    print("2.4 seconds of LIVING mind")
    print()
    
    # Auto-play
    auto_play_movie(output)

