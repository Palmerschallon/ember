/**
 * Renderer - Main rendering loop
 */
class Renderer {
    constructor(canvas, camera, universe, lodSystem) {
        this.canvas = canvas;
        this.ctx = canvas.getContext('2d');
        this.camera = camera;
        this.universe = universe;
        this.lodSystem = lodSystem;
        this.running = false;
        
        // Stats
        this.fps = 0;
        this.frameCount = 0;
        this.lastFpsUpdate = Date.now();
    }
    
    /**
     * Start rendering loop
     */
    start() {
        this.running = true;
        this.render();
    }
    
    /**
     * Stop rendering loop
     */
    stop() {
        this.running = false;
    }
    
    /**
     * Main render function
     */
    render() {
        if (!this.running) return;
        
        // Update canvas size
        this.updateCanvasSize();
        
        // Clear canvas
        this.ctx.fillStyle = '#000000';
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);
        
        // Get visible entities
        const visibleEntities = this.universe.getVisibleEntities(this.camera);
        
        // Update scene LOD level
        const sceneLOD = this.lodSystem.getSceneLODLevel(this.camera.zoom);
        
        // Render entities
        for (const entity of visibleEntities) {
            // Skip culled entities
            if (this.lodSystem.shouldCull(entity, this.camera)) {
                continue;
            }
            
            // Determine entity LOD level
            const entityLOD = this.lodSystem.getLODLevel(
                entity.size,
                this.getDistanceToCamera(entity),
                this.camera.zoom
            );
            
            // Render with appropriate LOD
            this.lodSystem.renderEntity(this.ctx, entity, entityLOD, this.camera);
        }
        
        // Update stats
        this.updateStats();
        
        // Continue loop
        requestAnimationFrame(() => this.render());
    }
    
    /**
     * Update canvas size to match display size
     */
    updateCanvasSize() {
        const displayWidth = this.canvas.clientWidth;
        const displayHeight = this.canvas.clientHeight;
        
        if (this.canvas.width !== displayWidth || this.canvas.height !== displayHeight) {
            this.canvas.width = displayWidth;
            this.canvas.height = displayHeight;
        }
    }
    
    /**
     * Get distance from entity to camera center
     */
    getDistanceToCamera(entity) {
        const dx = entity.x - this.camera.x;
        const dy = entity.y - this.camera.y;
        return Math.sqrt(dx * dx + dy * dy);
    }
    
    /**
     * Update FPS counter
     */
    updateStats() {
        this.frameCount++;
        const now = Date.now();
        
        if (now - this.lastFpsUpdate >= 1000) {
            this.fps = this.frameCount;
            this.frameCount = 0;
            this.lastFpsUpdate = now;
        }
    }
}
