/**
 * Camera System - Ticket 1: Zoom-to-Cursor
 * Handles camera transformations with zoom targeting cursor position
 */
class Camera {
    constructor(canvas) {
        this.canvas = canvas;
        this.x = 0;
        this.y = 0;
        this.zoom = 1.0;
        this.minZoom = 0.1;
        this.maxZoom = 10.0;
        
        // Pan state
        this.isPanning = false;
        this.panStartX = 0;
        this.panStartY = 0;
        this.panStartCameraX = 0;
        this.panStartCameraY = 0;
    }
    
    /**
     * Zoom camera toward cursor position (Ticket 1 implementation)
     * This keeps the world point under the cursor stationary during zoom
     */
    zoomTowardsCursor(delta, mouseX, mouseY) {
        // Calculate world position under cursor BEFORE zoom
        const worldXBefore = this.screenToWorldX(mouseX);
        const worldYBefore = this.screenToWorldY(mouseY);
        
        // Apply zoom
        const zoomFactor = delta > 0 ? 1.1 : 0.9;
        const newZoom = this.zoom * zoomFactor;
        
        // Clamp zoom
        if (newZoom < this.minZoom || newZoom > this.maxZoom) {
            return;
        }
        
        this.zoom = newZoom;
        
        // Calculate world position under cursor AFTER zoom
        const worldXAfter = this.screenToWorldX(mouseX);
        const worldYAfter = this.screenToWorldY(mouseY);
        
        // Adjust camera position to keep the point under cursor stationary
        this.x += (worldXAfter - worldXBefore);
        this.y += (worldYAfter - worldYBefore);
    }
    
    /**
     * Convert screen coordinates to world coordinates
     */
    screenToWorldX(screenX) {
        const canvasX = screenX - this.canvas.width / 2;
        return this.x + canvasX / this.zoom;
    }
    
    screenToWorldY(screenY) {
        const canvasY = screenY - this.canvas.height / 2;
        return this.y + canvasY / this.zoom;
    }
    
    /**
     * Convert world coordinates to screen coordinates
     */
    worldToScreenX(worldX) {
        return (worldX - this.x) * this.zoom + this.canvas.width / 2;
    }
    
    worldToScreenY(worldY) {
        return (worldY - this.y) * this.zoom + this.canvas.height / 2;
    }
    
    /**
     * Start panning
     */
    startPan(screenX, screenY) {
        this.isPanning = true;
        this.panStartX = screenX;
        this.panStartY = screenY;
        this.panStartCameraX = this.x;
        this.panStartCameraY = this.y;
    }
    
    /**
     * Update pan
     */
    updatePan(screenX, screenY) {
        if (!this.isPanning) return;
        
        const deltaX = screenX - this.panStartX;
        const deltaY = screenY - this.panStartY;
        
        this.x = this.panStartCameraX - deltaX / this.zoom;
        this.y = this.panStartCameraY - deltaY / this.zoom;
    }
    
    /**
     * Stop panning
     */
    stopPan() {
        this.isPanning = false;
    }
    
    /**
     * Reset camera to initial state
     */
    reset() {
        this.x = 0;
        this.y = 0;
        this.zoom = 1.0;
    }
    
    /**
     * Apply camera transformation to canvas context
     */
    applyTransform(ctx) {
        ctx.setTransform(1, 0, 0, 1, 0, 0);
        ctx.translate(this.canvas.width / 2, this.canvas.height / 2);
        ctx.scale(this.zoom, this.zoom);
        ctx.translate(-this.x, -this.y);
    }
}
