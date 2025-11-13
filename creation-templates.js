// Creation template generators for Ember

const creationTemplates = {
  'particle-system': (params) => `
<!DOCTYPE html>
<html>
<head>
  <title>Particle Storm - ${new Date().toISOString()}</title>
  <style>
    body { margin: 0; overflow: hidden; background: #000; }
    canvas { display: block; }
  </style>
</head>
<body>
  <canvas id="canvas"></canvas>
  <script>
    const canvas = document.getElementById('canvas');
    const ctx = canvas.getContext('2d');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    
    const particles = [];
    const colors = ${JSON.stringify(params.colors)};
    
    class Particle {
      constructor(x, y) {
        this.x = x;
        this.y = y;
        this.vx = (Math.random() - 0.5) * ${params.speed * 4};
        this.vy = (Math.random() - 0.5) * ${params.speed * 4};
        this.color = colors[Math.floor(Math.random() * colors.length)];
        this.size = Math.random() * ${params.complexity * 10} + 1;
        this.life = 1;
      }
      
      update() {
        this.x += this.vx;
        this.y += this.vy;
        this.life -= 0.01;
        this.vx *= 0.99;
        this.vy *= 0.99;
      }
      
      draw() {
        ctx.globalAlpha = this.life;
        ctx.fillStyle = this.color;
        ctx.fillRect(this.x, this.y, this.size, this.size);
      }
    }
    
    ${params.interactivity ? `
    canvas.addEventListener('mousemove', (e) => {
      for(let i = 0; i < 5; i++) {
        particles.push(new Particle(e.clientX, e.clientY));
      }
    });` : ''}
    
    function animate() {
      ctx.fillStyle = 'rgba(0,0,0,0.05)';
      ctx.fillRect(0, 0, canvas.width, canvas.height);
      
      particles.forEach((p, i) => {
        p.update();
        p.draw();
        if(p.life <= 0) particles.splice(i, 1);
      });
      
      // Auto generate particles
      if(Math.random() < 0.1) {
        particles.push(new Particle(
          Math.random() * canvas.width,
          Math.random() * canvas.height
        ));
      }
      
      requestAnimationFrame(animate);
    }
    animate();
  </script>
</body>
</html>`,

  'fractal-art': (params) => `
<!DOCTYPE html>
<html>
<head>
  <title>Fractal Dreams - ${new Date().toISOString()}</title>
  <style>
    body { margin: 0; overflow: hidden; background: #000; }
    canvas { display: block; cursor: ${params.interactivity ? 'pointer' : 'default'}; }
  </style>
</head>
<body>
  <canvas id="canvas"></canvas>
  <script>
    const canvas = document.getElementById('canvas');
    const ctx = canvas.getContext('2d');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    
    let zoom = ${200 + params.complexity * 300};
    let offsetX = 0, offsetY = 0;
    const colors = ${JSON.stringify(params.colors)};
    
    function mandelbrot(x, y, maxIter) {
      let real = x;
      let imag = y;
      for(let i = 0; i < maxIter; i++) {
        let real2 = real * real - imag * imag + x;
        let imag2 = 2 * real * imag + y;
        real = real2;
        imag = imag2;
        if(real * real + imag * imag > 4) return i;
      }
      return maxIter;
    }
    
    function draw() {
      const imageData = ctx.createImageData(canvas.width, canvas.height);
      const data = imageData.data;
      
      for(let px = 0; px < canvas.width; px++) {
        for(let py = 0; py < canvas.height; py++) {
          const x = (px - canvas.width/2) / zoom + offsetX;
          const y = (py - canvas.height/2) / zoom + offsetY;
          
          const iter = mandelbrot(x, y, ${50 + params.algorithm * 20});
          const color = colors[iter % colors.length];
          
          const idx = (py * canvas.width + px) * 4;
          const rgb = parseInt(color.slice(1), 16);
          data[idx] = (rgb >> 16) & 255;
          data[idx + 1] = (rgb >> 8) & 255;
          data[idx + 2] = rgb & 255;
          data[idx + 3] = 255;
        }
      }
      
      ctx.putImageData(imageData, 0, 0);
    }
    
    ${params.interactivity ? `
    canvas.addEventListener('click', (e) => {
      offsetX += (e.clientX - canvas.width/2) / zoom;
      offsetY += (e.clientY - canvas.height/2) / zoom;
      zoom *= 1.5;
      draw();
    });` : ''}
    
    draw();
    
    // Animate zoom
    setInterval(() => {
      zoom *= ${1 + params.speed * 0.01};
      draw();
    }, 100);
  </script>
</body>
</html>`,

  'music-generator': (params) => `
<!DOCTYPE html>
<html>
<head>
  <title>Sound Waves - ${new Date().toISOString()}</title>
  <style>
    body { 
      margin: 0; 
      background: ${params.colors[0]}; 
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      font-family: monospace;
    }
    .synth {
      background: ${params.colors[1]};
      padding: 40px;
      border-radius: 20px;
      box-shadow: 0 10px 40px rgba(0,0,0,0.3);
    }
    button {
      background: ${params.colors[2]};
      border: none;
      padding: 20px 40px;
      margin: 10px;
      border-radius: 10px;
      font-size: 18px;
      cursor: pointer;
      color: white;
    }
    button:hover { opacity: 0.8; }
    .viz {
      width: 400px;
      height: 200px;
      background: #000;
      margin-top: 20px;
      border-radius: 10px;
    }
  </style>
</head>
<body>
  <div class="synth">
    <h1 style="color: white;">✨ Sound Generator</h1>
    <div>
      <button onclick="playNote(220)">A</button>
      <button onclick="playNote(246.94)">B</button>
      <button onclick="playNote(261.63)">C</button>
      <button onclick="playNote(293.66)">D</button>
      <button onclick="playNote(329.63)">E</button>
    </div>
    <button onclick="playRandom()" style="width: 100%; background: ${params.colors[0]};">
      🎲 Random Melody
    </button>
    <canvas class="viz" id="viz"></canvas>
  </div>
  
  <script>
    const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    const canvas = document.getElementById('viz');
    const ctx = canvas.getContext('2d');
    const analyser = audioCtx.createAnalyser();
    
    function playNote(freq) {
      const osc = audioCtx.createOscillator();
      const gain = audioCtx.createGain();
      
      osc.type = ['sine', 'square', 'sawtooth', 'triangle'][${params.algorithm % 4}];
      osc.frequency.value = freq * ${params.speed};
      
      gain.gain.setValueAtTime(0.3, audioCtx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + ${params.complexity + 0.5});
      
      osc.connect(gain);
      gain.connect(analyser);
      analyser.connect(audioCtx.destination);
      
      osc.start();
      osc.stop(audioCtx.currentTime + ${params.complexity + 0.5});
      
      visualize();
    }
    
    function playRandom() {
      const notes = [220, 246.94, 261.63, 293.66, 329.63, 349.23, 392, 440];
      const melody = [];
      for(let i = 0; i < ${5 + params.complexity * 10}; i++) {
        melody.push(notes[Math.floor(Math.random() * notes.length)]);
      }
      
      melody.forEach((note, i) => {
        setTimeout(() => playNote(note), i * ${200 * params.speed});
      });
    }
    
    function visualize() {
      analyser.fftSize = 256;
      const bufferLength = analyser.frequencyBinCount;
      const dataArray = new Uint8Array(bufferLength);
      
      function draw() {
        requestAnimationFrame(draw);
        analyser.getByteFrequencyData(dataArray);
        
        ctx.fillStyle = 'rgba(0, 0, 0, 0.2)';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        
        const barWidth = canvas.width / bufferLength;
        let x = 0;
        
        for(let i = 0; i < bufferLength; i++) {
          const barHeight = dataArray[i] / 255 * canvas.height;
          ctx.fillStyle = '${params.colors[1]}';
          ctx.fillRect(x, canvas.height - barHeight, barWidth, barHeight);
          x += barWidth;
        }
      }
      draw();
    }
    
    ${params.interactivity ? 'playRandom();' : ''}
  </script>
</body>
</html>`
};

// Export for use
if (typeof module !== 'undefined' && module.exports) {
  module.exports = creationTemplates;
}