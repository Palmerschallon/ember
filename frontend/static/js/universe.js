/**
 * Universe Manager - Handles universe data from backend (Ticket 2)
 */
class Universe {
    constructor() {
        this.entities = [];
        this.seed = 42;
        this.bounds = {
            min_x: -10000,
            max_x: 10000,
            min_y: -10000,
            max_y: 10000
        };
    }
    
    /**
     * Load universe from backend
     */
    async load(seed = null) {
        if (seed !== null) {
            this.seed = seed;
        }
        
        try {
            const response = await fetch(`/api/universe?seed=${this.seed}&entities=100`);
            const data = await response.json();
            
            this.entities = data.entities;
            this.bounds = data.bounds;
            this.seed = data.seed;
            
            return data;
        } catch (error) {
            console.error('Failed to load universe:', error);
            return null;
        }
    }
    
    /**
     * Get entities in view frustum (for optimization)
     */
    getVisibleEntities(camera) {
        // Simple bounds check
        const left = camera.screenToWorldX(0);
        const right = camera.screenToWorldX(camera.canvas.width);
        const top = camera.screenToWorldY(0);
        const bottom = camera.screenToWorldY(camera.canvas.height);
        
        // Add margin for smooth appearance/disappearance
        const margin = 1000 / camera.zoom;
        
        return this.entities.filter(entity => {
            return entity.x >= left - margin &&
                   entity.x <= right + margin &&
                   entity.y >= top - margin &&
                   entity.y <= bottom + margin;
        });
    }
    
    /**
     * Get entity at screen position
     */
    getEntityAtPosition(worldX, worldY) {
        for (const entity of this.entities) {
            const dx = entity.x - worldX;
            const dy = entity.y - worldY;
            const distance = Math.sqrt(dx * dx + dy * dy);
            
            if (distance <= entity.size) {
                return entity;
            }
        }
        return null;
    }
}
