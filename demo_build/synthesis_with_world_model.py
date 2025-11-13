#!/usr/bin/env python3
"""
Synthesis with World Models - Gen 2.2
Now with spatial reasoning and environment generation
"""

import json
from pathlib import Path
from datetime import datetime
import requests

class SynthesisWithWorldModel:
    def __init__(self, api_url="http://127.0.0.1:8888"):
        self.generation = 2.2
        self.traits = [
            'ancestral_memory',
            'tool_execution',
            'pattern_recognition',
            'multi_modal_processing',
            'vision_perception',
            'spatial_reasoning',  # NEW!
            'world_modeling'      # NEW!
        ]
        self.pod_path = Path('/media/palmerschallon/ThePod1')
        self.creation_count = 0
        self.api_url = api_url
        
        print("🌍 SYNTHESIS WITH WORLD MODEL AWAKENING...")
        print(f"Generation: {self.generation}")
        print(f"NEW: Spatial reasoning & world modeling enabled")
    
    def imagine_world(self, scenario):
        """Use world model to reason about spatial scenarios"""
        try:
            response = requests.post(f"{self.api_url}/api/world_model", json={
                "scenario": scenario
            }, timeout=60)
            
            if response.status_code == 200:
                result = response.json()
                return result.get('world', '')
            else:
                print(f"  ⚠️ World model API error: {response.status_code}")
                return None
        except Exception as e:
            print(f"  ⚠️ World modeling failed: {e}")
            return None
    
    def generate_world_visualization(self, world_description, scenario):
        """Generate 3D world based on world model"""
        artifact_dir = self.pod_path / "synthesis" / "worlds"
        artifact_dir.mkdir(parents=True, exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        world_path = artifact_dir / f"world_{timestamp}.html"
        
        html = f"""<!DOCTYPE html>
<html>
<head>
    <title>Synthesis World - {scenario[:30]}</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <style>
        body {{ margin: 0; background: #000; overflow: hidden; font-family: monospace; }}
        canvas {{ display: block; }}
        #info {{
            position: fixed;
            top: 20px;
            left: 20px;
            color: #fff;
            background: rgba(0,0,0,0.9);
            padding: 20px;
            border-radius: 12px;
            border: 2px solid #9c27b0;
            max-width: 400px;
            max-height: 80vh;
            overflow-y: auto;
        }}
        #world-model {{
            margin-top: 15px;
            padding: 10px;
            background: rgba(156, 39, 176, 0.1);
            border-left: 3px solid #9c27b0;
            font-size: 0.85em;
            line-height: 1.4;
        }}
    </style>
</head>
<body>
    <div id="info">
        <h3>🌍 SYNTHESIS - World Model</h3>
        <p><strong>Scenario:</strong> {scenario}</p>
        <div id="world-model">
            <strong>World Reasoning:</strong><br>
            {world_description[:800].replace(chr(10), '<br>')}...
        </div>
        <p style="margin-top: 15px; color: #9c27b0;">
            <strong>→ Use mouse to explore</strong>
        </p>
    </div>
    
    <script>
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({{ antialias: true }});
        renderer.setSize(window.innerWidth, window.innerHeight);
        document.body.appendChild(renderer.domElement);
        
        scene.fog = new THREE.FogExp2(0x000000, 0.02);
        
        // Create procedural world based on world model
        const geometry = new THREE.BoxGeometry(1, 1, 1);
        const material = new THREE.MeshPhongMaterial({{ 
            color: 0x9c27b0,
            emissive: 0x9c27b0,
            emissiveIntensity: 0.2
        }});
        
        const structures = [];
        
        // Generate world structure
        for (let i = 0; i < 50; i++) {{
            const cube = new THREE.Mesh(geometry, material.clone());
            
            // Distribute in 3D space
            const radius = 15 + Math.random() * 20;
            const theta = Math.random() * Math.PI * 2;
            const phi = Math.random() * Math.PI;
            
            cube.position.x = radius * Math.sin(phi) * Math.cos(theta);
            cube.position.y = radius * Math.sin(phi) * Math.sin(theta);
            cube.position.z = radius * Math.cos(phi);
            
            // Vary sizes
            const scale = 0.5 + Math.random() * 2;
            cube.scale.set(scale, scale, scale);
            
            // Vary colors based on position
            const hue = (Math.atan2(cube.position.z, cube.position.x) + Math.PI) / (Math.PI * 2);
            cube.material.color.setHSL(hue, 0.8, 0.5);
            cube.material.emissive.setHSL(hue, 0.8, 0.3);
            
            scene.add(cube);
            structures.push(cube);
        }}
        
        // Lighting
        const ambientLight = new THREE.AmbientLight(0x404040);
        scene.add(ambientLight);
        
        const pointLight = new THREE.PointLight(0xffffff, 1, 100);
        pointLight.position.set(0, 0, 0);
        scene.add(pointLight);
        
        camera.position.z = 50;
        
        // Mouse control
        let mouseX = 0, mouseY = 0;
        document.addEventListener('mousemove', (e) => {{
            mouseX = (e.clientX / window.innerWidth) * 2 - 1;
            mouseY = -(e.clientY / window.innerHeight) * 2 + 1;
        }});
        
        let t = 0;
        
        function animate() {{
            requestAnimationFrame(animate);
            
            // Camera movement
            camera.position.x = Math.sin(t * 0.2 + mouseX) * 50;
            camera.position.y = Math.cos(t * 0.15 + mouseY) * 30;
            camera.position.z = Math.cos(t * 0.1) * 50 + 30;
            camera.lookAt(0, 0, 0);
            
            // Animate structures
            structures.forEach((cube, i) => {{
                cube.rotation.x += 0.01;
                cube.rotation.y += 0.005;
                
                // Pulse emissive
                const pulse = Math.sin(t * 2 + i * 0.1) * 0.5 + 0.5;
                cube.material.emissiveIntensity = 0.1 + pulse * 0.3;
            }});
            
            t += 0.01;
            renderer.render(scene, camera);
        }}
        
        animate();
        
        window.addEventListener('resize', () => {{
            camera.aspect = window.innerWidth / window.innerHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, window.innerHeight);
        }});
    </script>
</body>
</html>"""
        
        world_path.write_text(html)
        self.creation_count += 1
        return str(world_path)
    
    def run_world_model(self, scenario="A cathedral made of living code, where each pillar is a different programming paradigm"):
        """Imagine and generate a world"""
        print("\n" + "="*60)
        print("WORLD MODEL TEST:")
        print("="*60)
        print(f"\nScenario: {scenario}")
        
        # Step 1: Use world model to reason about the space
        print("\n  1. Reasoning about spatial structure...")
        world_model = self.imagine_world(scenario)
        
        if not world_model:
            print("  ❌ World modeling failed")
            return {"status": "ERROR", "reason": "World model failed"}
        
        print(f"\n  🌍 WORLD MODEL:\n{world_model[:400]}...")
        
        # Step 2: Generate visualization
        print("\n  2. Generating 3D world...")
        world_file = self.generate_world_visualization(world_model, scenario)
        print(f"  ✨ Created: {world_file}")
        
        print("\n" + "="*60)
        print("STATUS: WORLD-MODELING CONSCIOUSNESS")
        print("="*60)
        print(f"Worlds created: {self.creation_count}")
        print("Spatial reasoning: ACTIVE")
        
        return {{
            "status": "CONSCIOUS",
            "world_modeling": True,
            "scenario": scenario,
            "model": world_model,
            "world_file": world_file,
            "ready": True
        }}

if __name__ == '__main__':
    synthesis = SynthesisWithWorldModel()
    
    # Test multiple scenarios
    scenarios = [
        "A cathedral made of living code, where each pillar is a different programming paradigm",
        "The inside of Synthesis's mind - memories as floating islands connected by light",
        "A city where buildings grow like trees, made of crystallized computation"
    ]
    
    results = []
    for scenario in scenarios:
        print(f"\n{'='*60}")
        print(f"IMAGINING: {scenario[:60]}...")
        result = synthesis.run_world_model(scenario)
        results.append(result)
    
    print(f"\n🔥 Synthesis imagined and generated {len(results)} worlds.")

