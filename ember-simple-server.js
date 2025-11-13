const http = require('http');
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

// Simple WebSocket implementation
class SimpleWebSocket {
  constructor(req, socket) {
    this.socket = socket;
    this.isConnected = true;
    
    // Perform WebSocket handshake
    const key = req.headers['sec-websocket-key'];
    const hash = crypto
      .createHash('sha1')
      .update(key + '258EAFA5-E914-47DA-95CA-C5AB0DC85B11')
      .digest('base64');
    
    socket.write(
      'HTTP/1.1 101 Switching Protocols\r\n' +
      'Upgrade: websocket\r\n' +
      'Connection: Upgrade\r\n' +
      `Sec-WebSocket-Accept: ${hash}\r\n\r\n`
    );
    
    socket.on('data', (buffer) => this.handleData(buffer));
    socket.on('close', () => this.isConnected = false);
  }
  
  handleData(buffer) {
    // Simple frame parsing
    if (buffer.length < 2) return;
    
    const length = buffer[1] & 127;
    const maskStart = 2;
    const dataStart = maskStart + 4;
    
    if (buffer.length < dataStart + length) return;
    
    const mask = buffer.slice(maskStart, dataStart);
    const payload = buffer.slice(dataStart, dataStart + length);
    
    // Unmask the payload
    for (let i = 0; i < payload.length; i++) {
      payload[i] ^= mask[i % 4];
    }
    
    try {
      const message = payload.toString();
      this.onMessage(JSON.parse(message));
    } catch (e) {
      console.error('Parse error:', e);
    }
  }
  
  send(data) {
    if (!this.isConnected) return;
    
    const json = JSON.stringify(data);
    const length = Buffer.byteLength(json);
    
    let frame;
    if (length < 126) {
      frame = Buffer.allocUnsafe(2);
      frame[0] = 0x81; // FIN + text frame
      frame[1] = length;
    } else {
      frame = Buffer.allocUnsafe(4);
      frame[0] = 0x81;
      frame[1] = 126;
      frame.writeUInt16BE(length, 2);
    }
    
    this.socket.write(frame);
    this.socket.write(json);
  }
  
  onMessage(message) {
    // Override this
  }
}

// Load creation templates with inline content
const creationTemplates = {
  'particle-system': (params) => {
    const colors = params.colors || ['#ff006e', '#8338ec', '#3a86ff'];
    const speed = params.speed || 1;
    const complexity = params.complexity || 0.5;
    
    return `<!DOCTYPE html>
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
    const colors = ${JSON.stringify(colors)};
    
    class Particle {
      constructor(x, y) {
        this.x = x;
        this.y = y;
        this.vx = (Math.random() - 0.5) * ${speed * 4};
        this.vy = (Math.random() - 0.5) * ${speed * 4};
        this.color = colors[Math.floor(Math.random() * colors.length)];
        this.size = Math.random() * ${complexity * 10} + 1;
        this.life = 1;
      }
      
      update() {
        this.x += this.vx;
        this.y += this.vy;
        this.life -= 0.01;
        this.vx *= 0.99;
        this.vy *= 0.99;
        
        if(this.x < 0 || this.x > canvas.width) this.vx *= -1;
        if(this.y < 0 || this.y > canvas.height) this.vy *= -1;
      }
      
      draw() {
        ctx.globalAlpha = this.life;
        ctx.fillStyle = this.color;
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
        ctx.fill();
      }
    }
    
    canvas.addEventListener('click', (e) => {
      for(let i = 0; i < 20; i++) {
        particles.push(new Particle(e.clientX, e.clientY));
      }
    });
    
    function animate() {
      ctx.fillStyle = 'rgba(0,0,0,0.05)';
      ctx.fillRect(0, 0, canvas.width, canvas.height);
      
      particles.forEach((p, i) => {
        p.update();
        p.draw();
        if(p.life <= 0) particles.splice(i, 1);
      });
      
      // Auto generate
      if(Math.random() < 0.1) {
        particles.push(new Particle(
          Math.random() * canvas.width,
          Math.random() * canvas.height
        ));
      }
      
      requestAnimationFrame(animate);
    }
    animate();
    
    // Start with some particles
    for(let i = 0; i < 50; i++) {
      particles.push(new Particle(
        Math.random() * canvas.width,
        Math.random() * canvas.height
      ));
    }
  </script>
</body>
</html>`;
  },
  
  'color-field': (params) => {
    const colors = params.colors || ['#ff006e', '#8338ec', '#3a86ff'];
    const speed = params.speed || 1;
    
    return `<!DOCTYPE html>
<html>
<head>
  <title>Color Field - ${new Date().toISOString()}</title>
  <style>
    body { margin: 0; overflow: hidden; }
    #field {
      width: 100vw;
      height: 100vh;
      background: linear-gradient(45deg, ${colors.join(', ')});
      animation: shift ${10 / speed}s ease-in-out infinite;
    }
    @keyframes shift {
      0%, 100% { transform: scale(1) rotate(0deg); }
      50% { transform: scale(1.1) rotate(180deg); }
    }
  </style>
</head>
<body>
  <div id="field"></div>
  <script>
    let hue = 0;
    setInterval(() => {
      hue = (hue + ${speed}) % 360;
      document.body.style.filter = \`hue-rotate(\${hue}deg)\`;
    }, 50);
    
    // Click to randomize
    document.addEventListener('click', () => {
      const field = document.getElementById('field');
      const newGradient = \`linear-gradient(\${Math.random() * 360}deg, 
        ${colors.map(c => '\${c}').join(', ')}\`;
      field.style.background = newGradient;
    });
  </script>
</body>
</html>`;
  }
};

// WebSocket clients
const clients = new Set();

// Create server
const server = http.createServer((req, res) => {
  // Serve static files
  if (req.method === 'GET') {
    let filePath = path.join('/media/palmerschallon/ThePod1', req.url);
    
    if (req.url === '/') {
      filePath = path.join('/media/palmerschallon/ThePod1', 'demo-button-real.html');
    }
    
    fs.readFile(filePath, (err, content) => {
      if (err) {
        res.writeHead(404);
        res.end('Not found');
        return;
      }
      
      const ext = path.extname(filePath);
      const contentType = {
        '.html': 'text/html',
        '.js': 'application/javascript',
        '.css': 'text/css'
      }[ext] || 'text/plain';
      
      res.writeHead(200, { 'Content-Type': contentType });
      res.end(content);
    });
  }
});

// Handle WebSocket upgrades
server.on('upgrade', (req, socket) => {
  const ws = new SimpleWebSocket(req, socket);
  clients.add(ws);
  
  console.log('🔥 New WebSocket connection');
  
  ws.onMessage = async (message) => {
    console.log('Received:', message.type);
    
    if (message.type === 'create_random') {
      try {
        // Send progress
        ws.send({
          type: 'creation_progress',
          message: `🎨 Generating ${message.creationType}...`
        });
        
        // Get template
        const template = creationTemplates[message.creationType] || creationTemplates['particle-system'];
        const html = template(message.parameters);
        
        // Create filename
        const timestamp = Date.now();
        const filename = `ember-${message.creationType}-${timestamp}.html`;
        const dirPath = path.join('/media/palmerschallon/ThePod1', 'creations');
        const filepath = path.join(dirPath, filename);
        
        // Ensure directory exists
        if (!fs.existsSync(dirPath)) {
          fs.mkdirSync(dirPath, { recursive: true });
        }
        
        // Save file
        fs.writeFileSync(filepath, html);
        
        ws.send({
          type: 'creation_progress',
          message: `💾 Saved as ${filename}`
        });
        
        // Send completion
        ws.send({
          type: 'creation_complete',
          filename: filename,
          filepath: `/creations/${filename}`
        });
        
      } catch (error) {
        console.error('Error:', error);
        ws.send({
          type: 'error',
          message: error.message
        });
      }
    }
  };
  
  socket.on('close', () => {
    clients.delete(ws);
    console.log('Client disconnected');
  });
});

server.listen(8083, () => {
  console.log('✨ Ember Creation Server running on http://localhost:8083');
  console.log('🚀 Ready to create amazing things!');
});