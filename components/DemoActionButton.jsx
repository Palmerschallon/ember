// Quick demo-focused version with ONE KILLER BUTTON
import React, { useState } from 'react';

export const DemoActionButton = () => {
  const [isBuilding, setIsBuilding] = useState(false);
  const [sparkles, setSparkles] = useState([]);
  
  const buildSomethingAmazing = async () => {
    setIsBuilding(true);
    
    // Play build sound
    const audio = new Audio('data:audio/wav;base64,UklGRnoGAABXQVZFZm10IBAAAAABAAEAQB8AAEAfAAABAAgAZGF0YQoGAACBhYqFbF1fdJivrJBhNjVgodDbq2EcBj+a2/LDciUFLIHO8tiJNwgZaLvt559NEAxQp+PwtmMcBjiR1/LMeSwFJHfH8N2QQAoUXrTp66hVFApGn+DyvmwhB');
    audio.play();
    
    // Create sparkle effects
    const newSparkles = Array.from({length: 20}, (_, i) => ({
      id: Date.now() + i,
      x: Math.random() * window.innerWidth,
      y: Math.random() * window.innerHeight
    }));
    setSparkles(newSparkles);
    
    // Build something random and amazing
    const creations = [
      {
        type: '3D Scene',
        path: `/media/palmerschallon/ThePod1/demos/3d-world-${Date.now()}.html`,
        content: generate3DScene()
      },
      {
        type: 'AI Playground',
        path: `/media/palmerschallon/ThePod1/demos/ai-playground-${Date.now()}.html`,
        content: generateAIPlayground()
      },
      {
        type: 'Music Visualizer',
        path: `/media/palmerschallon/ThePod1/demos/music-viz-${Date.now()}.html`,
        content: generateMusicViz()
      }
    ];
    
    const creation = creations[Math.floor(Math.random() * creations.length)];
    
    // Actually create and open it
    await window.electron.writeFile(creation.path, creation.content);
    await window.electron.exec(`xdg-open ${creation.path} &`);
    
    setTimeout(() => {
      setIsBuilding(false);
      setSparkles([]);
    }, 2000);
  };
  
  return (
    <>
      <button
        onClick={buildSomethingAmazing}
        disabled={isBuilding}
        style={{
          position: 'fixed',
          top: '50%',
          left: '50%',
          transform: 'translate(-50%, -50%)',
          fontSize: '24px',
          padding: '30px 60px',
          background: isBuilding 
            ? 'linear-gradient(45deg, #ff006e, #8338ec, #3a86ff)' 
            : 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
          border: 'none',
          borderRadius: '20px',
          color: 'white',
          cursor: isBuilding ? 'wait' : 'pointer',
          boxShadow: '0 10px 40px rgba(102, 126, 234, 0.5)',
          animation: isBuilding ? 'pulse 0.5s infinite' : 'none',
          transition: 'all 0.3s ease'
        }}
      >
        {isBuilding ? '🔨 BUILDING SOMETHING AMAZING...' : '✨ BUILD SOMETHING AMAZING'}
      </button>
      
      {/* Sparkle effects */}
      {sparkles.map(sparkle => (
        <div
          key={sparkle.id}
          style={{
            position: 'fixed',
            left: sparkle.x,
            top: sparkle.y,
            width: '10px',
            height: '10px',
            background: '#ffd700',
            borderRadius: '50%',
            animation: 'sparkle 2s ease-out forwards'
          }}
        />
      ))}
      
      <style>{`
        @keyframes pulse {
          0% { transform: translate(-50%, -50%) scale(1); }
          50% { transform: translate(-50%, -50%) scale(1.05); }
          100% { transform: translate(-50%, -50%) scale(1); }
        }
        
        @keyframes sparkle {
          0% { 
            opacity: 1; 
            transform: translateY(0) scale(1);
          }
          100% { 
            opacity: 0; 
            transform: translateY(-100px) scale(0);
          }
        }
      `}</style>
    </>
  );
};

const generate3DScene = () => `<!DOCTYPE html>
<html>
<head>
  <title>Ember 3D World</title>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
</head>
<body style="margin:0;overflow:hidden;">
  <script>
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    const renderer = new THREE.WebGLRenderer();
    renderer.setSize(window.innerWidth, window.innerHeight);
    document.body.appendChild(renderer.domElement);
    
    // Create magical floating cubes
    const cubes = [];
    for(let i = 0; i < 50; i++) {
      const geometry = new THREE.BoxGeometry(1, 1, 1);
      const material = new THREE.MeshBasicMaterial({
        color: new THREE.Color(\`hsl(\${i * 7}, 70%, 50%)\`),
        wireframe: Math.random() > 0.5
      });
      const cube = new THREE.Mesh(geometry, material);
      cube.position.set(
        Math.random() * 40 - 20,
        Math.random() * 40 - 20,
        Math.random() * 40 - 20
      );
      scene.add(cube);
      cubes.push(cube);
    }
    
    camera.position.z = 30;
    
    function animate() {
      requestAnimationFrame(animate);
      cubes.forEach((cube, i) => {
        cube.rotation.x += 0.01 + i * 0.001;
        cube.rotation.y += 0.01 + i * 0.001;
      });
      renderer.render(scene, camera);
    }
    animate();
  </script>
</body>
</html>`;

const generateAIPlayground = () => `<!DOCTYPE html>
<html>
<head>
  <title>Ember AI Playground</title>
  <style>
    body { 
      margin: 0; 
      font-family: system-ui; 
      background: linear-gradient(135deg, #1e3c72, #2a5298);
      color: white;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
    }
    .container {
      text-align: center;
      padding: 40px;
      background: rgba(0,0,0,0.5);
      border-radius: 20px;
      backdrop-filter: blur(10px);
    }
    .brain {
      font-size: 100px;
      animation: pulse 2s infinite;
    }
    @keyframes pulse {
      0%, 100% { transform: scale(1); }
      50% { transform: scale(1.1); }
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="brain">🧠</div>
    <h1>AI Playground Active</h1>
    <p>Neural networks are spinning up...</p>
  </div>
</body>
</html>`;

const generateMusicViz = () => `<!DOCTYPE html>
<html>
<head>
  <title>Ember Music Visualizer</title>
  <style>
    body { margin: 0; background: #000; overflow: hidden; }
    canvas { display: block; }
  </style>
</head>
<body>
  <canvas id="viz"></canvas>
  <script>
    const canvas = document.getElementById('viz');
    const ctx = canvas.getContext('2d');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    
    const bars = 50;
    const barWidth = canvas.width / bars;
    
    function animate() {
      ctx.fillStyle = 'rgba(0,0,0,0.1)';
      ctx.fillRect(0, 0, canvas.width, canvas.height);
      
      for(let i = 0; i < bars; i++) {
        const height = Math.random() * canvas.height * 0.7;
        const hue = (i * 360 / bars + Date.now() * 0.1) % 360;
        ctx.fillStyle = \`hsl(\${hue}, 70%, 50%)\`;
        ctx.fillRect(i * barWidth, canvas.height - height, barWidth - 2, height);
      }
      
      requestAnimationFrame(animate);
    }
    animate();
  </script>
</body>
</html>`;