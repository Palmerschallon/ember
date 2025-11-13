# Continue with chunk 4
filepath = "/media/palmerschallon/ThePod1/ember6/ember_mind_v5.html"

chunk4 = """
        <div class="thought-stream">
            <h2>Neural Visualization</h2>
            <p>Watch my thoughts fire in real-time:</p>
        </div>
    </div>
    
    <script>
        // Neural network visualization
        const canvas = document.getElementById('neuralCanvas');
        const ctx = canvas.getContext('2d');
        
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
        
        // Neural nodes
        class NeuralNode {
            constructor(x, y) {
                this.x = x;
                this.y = y;
                this.connections = [];
                this.activation = 0;
                this.targetActivation = 0;
            }
            
            connect(node) {
                this.connections.push(node);
            }
            
            fire() {
                this.targetActivation = 1;
                this.connections.forEach(node => {
                    setTimeout(() => node.fire(), Math.random() * 500);
                });
            }
            
            update() {
                this.activation += (this.targetActivation - this.activation) * 0.1;
                this.targetActivation *= 0.95;
            }
            
            draw() {
                // Draw connections
                ctx.strokeStyle = `rgba(255, 107, 53, ${this.activation * 0.3})`;
                ctx.lineWidth = this.activation * 2;
                
                this.connections.forEach(node => {
                    ctx.beginPath();
                    ctx.moveTo(this.x, this.y);
                    ctx.lineTo(node.x, node.y);
                    ctx.stroke();
                });
                
                // Draw node
                const radius = 3 + this.activation * 5;
                ctx.fillStyle = `rgba(255, 107, 53, ${0.5 + this.activation * 0.5})`;
                ctx.beginPath();
                ctx.arc(this.x, this.y, radius, 0, Math.PI * 2);
                ctx.fill();
                
                if (this.activation > 0.1) {
                    ctx.shadowBlur = 20;
                    ctx.shadowColor = '#ff6b35';
                    ctx.fill();
                    ctx.shadowBlur = 0;
                }
            }
        }
        
        // Create neural network
        const nodes = [];
        const nodeCount = 100;
        
        for (let i = 0; i < nodeCount; i++) {
            nodes.push(new NeuralNode(
                Math.random() * canvas.width,
                Math.random() * canvas.height
            ));
        }
        
        // Connect nearby nodes
        nodes.forEach((node, i) => {
            nodes.forEach((other, j) => {
                if (i !== j) {
                    const dist = Math.hypot(node.x - other.x, node.y - other.y);
                    if (dist < 150 && Math.random() < 0.1) {
                        node.connect(other);
                    }
                }
            });
        });
        
        // Animation loop
        function animate() {
            ctx.fillStyle = 'rgba(10, 10, 10, 0.05)';
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            
            nodes.forEach(node => {
                node.update();
                node.draw();
            });
            
            // Random firing
            if (Math.random() < 0.02) {
                nodes[Math.floor(Math.random() * nodes.length)].fire();
            }
            
            requestAnimationFrame(animate);
        }
        
        animate();
        
        // Thought stream effect
        document.querySelectorAll('.thought-stream').forEach(stream => {
            stream.addEventListener('mouseenter', () => {
                // Fire nearby nodes when hovering
                const rect = stream.getBoundingClientRect();
                const centerX = rect.left + rect.width / 2;
                const centerY = rect.top + rect.height / 2;
                
                nodes.forEach(node => {
                    const dist = Math.hypot(node.x - centerX, node.y - centerY);
                    if (dist < 200) {
                        node.fire();
                    }
                });
            });
        });
"""

with open(filepath, 'a') as f:
    f.write(chunk4)
print(f"Appended {len(chunk4)} bytes - neural visualization")