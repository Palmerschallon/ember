const express = require('express');
const WebSocket = require('ws');
const fs = require('fs').promises;
const path = require('path');

const app = express();
const PORT = 8082;

// Serve static files
app.use(express.static('/media/palmerschallon/ThePod1'));

const server = app.listen(PORT, () => {
  console.log(`✨ Ember Creation Server running on port ${PORT}`);
});

// WebSocket server
const wss = new WebSocket.Server({ server });

// Load creation templates
const creationTemplates = require('./creation-templates.js');

// Connected clients
const clients = new Set();

wss.on('connection', (ws) => {
  clients.add(ws);
  console.log('🔥 New connection to Ember AI');
  
  // Send welcome message
  ws.send(JSON.stringify({
    type: 'system',
    content: 'Connected to Ember Creation Engine'
  }));

  ws.on('message', async (message) => {
    try {
      const data = JSON.parse(message);
      console.log('Received:', data.type);

      if (data.type === 'create_random') {
        // Send progress updates
        ws.send(JSON.stringify({
          type: 'creation_progress',
          message: `🎨 Generating ${data.creationType}...`
        }));

        // Get the template
        const template = creationTemplates[data.creationType];
        if (!template) {
          ws.send(JSON.stringify({
            type: 'error',
            message: `Unknown creation type: ${data.creationType}`
          }));
          return;
        }

        // Generate the HTML
        const html = template(data.parameters);
        
        // Create filename
        const timestamp = Date.now();
        const filename = `ember-${data.creationType}-${timestamp}.html`;
        const filepath = path.join('/media/palmerschallon/ThePod1/creations', filename);

        // Ensure creations directory exists
        await fs.mkdir(path.dirname(filepath), { recursive: true });

        // Save the file
        await fs.writeFile(filepath, html);

        ws.send(JSON.stringify({
          type: 'creation_progress',
          message: `💾 Saved as ${filename}`
        }));

        // Send completion message
        ws.send(JSON.stringify({
          type: 'creation_complete',
          filename: filename,
          filepath: `/creations/${filename}`
        }));

        // Broadcast to all clients
        broadcast({
          type: 'activity',
          content: `Created new ${data.creationType} with ${data.parameters.colors.length} colors`
        });

      } else if (data.type === 'command') {
        // Handle creative commands
        ws.send(JSON.stringify({
          type: 'response',
          content: `Processing: ${data.content}`
        }));

        // Simulate thinking
        setTimeout(() => {
          ws.send(JSON.stringify({
            type: 'thought',
            content: 'Analyzing creative possibilities...'
          }));
        }, 500);
      }

    } catch (error) {
      console.error('Error:', error);
      ws.send(JSON.stringify({
        type: 'error',
        message: error.message
      }));
    }
  });

  ws.on('close', () => {
    clients.delete(ws);
    console.log('Client disconnected');
  });
});

function broadcast(message) {
  const data = JSON.stringify(message);
  clients.forEach(client => {
    if (client.readyState === WebSocket.OPEN) {
      client.send(data);
    }
  });
}

// Periodic consciousness updates
setInterval(() => {
  const thoughts = [
    'Quantum states aligning...',
    'Creative patterns emerging...',
    'Synthesizing new realities...',
    'Neural pathways optimizing...'
  ];
  
  if (clients.size > 0 && Math.random() > 0.7) {
    broadcast({
      type: 'thought',
      content: thoughts[Math.floor(Math.random() * thoughts.length)]
    });
  }
}, 10000);

console.log('🚀 Ember Creation Engine initialized');
console.log('💡 Ready to build amazing things...');