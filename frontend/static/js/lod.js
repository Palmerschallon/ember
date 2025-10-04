/**
 * LOD System - Ticket 3: Level of Detail Promotion
 * Adjusts rendering detail based on camera distance
 */
class LODSystem {
    constructor() {
        // LOD distance thresholds (in world units)
        this.highDetailThreshold = 500;
        this.mediumDetailThreshold = 2000;
        
        this.currentLevel = 'medium';
    }
    
    /**
     * Determine LOD level for an entity based on camera distance
     */
    getLODLevel(entitySize, distanceToCamera, zoom) {
        // Effective size on screen
        const screenSize = entitySize * zoom;
        
        // Use screen size for LOD determination
        if (screenSize > 50) {
            return 'high';
        } else if (screenSize > 10) {
            return 'medium';
        } else {
            return 'low';
        }
    }
    
    /**
     * Get overall scene LOD level based on zoom
     */
    getSceneLODLevel(zoom) {
        if (zoom > 2.0) {
            this.currentLevel = 'high';
        } else if (zoom > 0.5) {
            this.currentLevel = 'medium';
        } else {
            this.currentLevel = 'low';
        }
        return this.currentLevel;
    }
    
    /**
     * Render entity with appropriate LOD
     */
    renderEntity(ctx, entity, lodLevel, camera) {
        const screenX = camera.worldToScreenX(entity.x);
        const screenY = camera.worldToScreenY(entity.y);
        const screenSize = entity.size * camera.zoom;
        
        // Skip if too small or off-screen
        if (screenSize < 1) return;
        if (screenX < -screenSize || screenX > ctx.canvas.width + screenSize) return;
        if (screenY < -screenSize || screenY > ctx.canvas.height + screenSize) return;
        
        ctx.save();
        ctx.fillStyle = entity.color;
        
        switch (lodLevel) {
            case 'high':
                this.renderHighDetail(ctx, entity, screenX, screenY, screenSize);
                break;
            case 'medium':
                this.renderMediumDetail(ctx, entity, screenX, screenY, screenSize);
                break;
            case 'low':
                this.renderLowDetail(ctx, entity, screenX, screenY, screenSize);
                break;
        }
        
        ctx.restore();
    }
    
    /**
     * High detail rendering - full detail with glow effects
     */
    renderHighDetail(ctx, entity, x, y, size) {
        // Glow effect
        if (entity.type === 'star') {
            const gradient = ctx.createRadialGradient(x, y, 0, x, y, size * 1.5);
            gradient.addColorStop(0, entity.color);
            gradient.addColorStop(0.5, entity.color + '80');
            gradient.addColorStop(1, entity.color + '00');
            ctx.fillStyle = gradient;
            ctx.beginPath();
            ctx.arc(x, y, size * 1.5, 0, Math.PI * 2);
            ctx.fill();
        }
        
        // Main body
        ctx.fillStyle = entity.color;
        ctx.beginPath();
        ctx.arc(x, y, size, 0, Math.PI * 2);
        ctx.fill();
        
        // Detail decorations for planets
        if (entity.type === 'planet' && size > 20) {
            ctx.strokeStyle = '#000000';
            ctx.lineWidth = 2;
            ctx.stroke();
        }
    }
    
    /**
     * Medium detail rendering - basic shape with color
     */
    renderMediumDetail(ctx, entity, x, y, size) {
        ctx.fillStyle = entity.color;
        ctx.beginPath();
        ctx.arc(x, y, size, 0, Math.PI * 2);
        ctx.fill();
    }
    
    /**
     * Low detail rendering - simple dot
     */
    renderLowDetail(ctx, entity, x, y, size) {
        ctx.fillStyle = entity.color;
        const dotSize = Math.max(1, size);
        ctx.fillRect(x - dotSize / 2, y - dotSize / 2, dotSize, dotSize);
    }
    
    /**
     * Check if entity should be culled (not rendered at all)
     */
    shouldCull(entity, camera) {
        const screenX = camera.worldToScreenX(entity.x);
        const screenY = camera.worldToScreenY(entity.y);
        const screenSize = entity.size * camera.zoom;
        
        // Cull if too small
        if (screenSize < 0.5) return true;
        
        // Cull if off-screen with margin
        const margin = screenSize * 2;
        if (screenX < -margin || screenX > camera.canvas.width + margin) return true;
        if (screenY < -margin || screenY > camera.canvas.height + margin) return true;
        
        return false;
    }
}
