/**
 * Main Application Entry Point
 * Initializes all systems and sets up event handlers
 */

// Initialize components
let canvas, camera, universe, lodSystem, renderer, chatInterface;
let eventSource;

function init() {
    // Get canvas element
    canvas = document.getElementById('universe-canvas');
    
    // Initialize systems
    camera = new Camera(canvas);
    universe = new Universe();
    lodSystem = new LODSystem();
    renderer = new Renderer(canvas, camera, universe, lodSystem);
    chatInterface = new ChatInterface();
    
    // Setup event listeners
    setupCanvasEvents();
    setupControlEvents();
    setupSSE();
    
    // Load initial universe
    loadUniverse();
    
    // Start rendering
    renderer.start();
    
    // Update info display
    setInterval(updateInfo, 100);
}

/**
 * Setup canvas event listeners (pan, zoom)
 */
function setupCanvasEvents() {
    // Mouse wheel zoom (Ticket 1: zoom-to-cursor)
    canvas.addEventListener('wheel', (e) => {
        e.preventDefault();
        
        const rect = canvas.getBoundingClientRect();
        const mouseX = e.clientX - rect.left;
        const mouseY = e.clientY - rect.top;
        
        camera.zoomTowardsCursor(-e.deltaY, mouseX, mouseY);
    });
    
    // Mouse pan
    canvas.addEventListener('mousedown', (e) => {
        const rect = canvas.getBoundingClientRect();
        const mouseX = e.clientX - rect.left;
        const mouseY = e.clientY - rect.top;
        
        camera.startPan(mouseX, mouseY);
    });
    
    canvas.addEventListener('mousemove', (e) => {
        const rect = canvas.getBoundingClientRect();
        const mouseX = e.clientX - rect.left;
        const mouseY = e.clientY - rect.top;
        
        camera.updatePan(mouseX, mouseY);
    });
    
    canvas.addEventListener('mouseup', () => {
        camera.stopPan();
    });
    
    canvas.addEventListener('mouseleave', () => {
        camera.stopPan();
    });
}

/**
 * Setup control button events
 */
function setupControlEvents() {
    // Reset view
    document.getElementById('reset-view').addEventListener('click', () => {
        camera.reset();
    });
    
    // Regenerate universe
    document.getElementById('regenerate').addEventListener('click', () => {
        loadUniverse(universe.seed);
    });
    
    // Set seed
    document.getElementById('set-seed').addEventListener('click', () => {
        const seed = parseInt(document.getElementById('seed-input').value);
        if (!isNaN(seed)) {
            loadUniverse(seed);
        }
    });
}

/**
 * Setup Server-Sent Events
 */
function setupSSE() {
    eventSource = new EventSource('/api/events');
    
    eventSource.onmessage = (event) => {
        const data = JSON.parse(event.data);
        console.log('SSE Event:', data);
    };
    
    eventSource.onerror = (error) => {
        console.error('SSE Error:', error);
    };
}

/**
 * Load universe from backend
 */
async function loadUniverse(seed = null) {
    const data = await universe.load(seed);
    if (data) {
        document.getElementById('seed-display').textContent = data.seed;
        document.getElementById('seed-input').value = data.seed;
        document.getElementById('entity-count').textContent = data.entities.length;
    }
}

/**
 * Update info display
 */
function updateInfo() {
    document.getElementById('zoom-level').textContent = camera.zoom.toFixed(2);
    document.getElementById('pos-x').textContent = Math.round(camera.x);
    document.getElementById('pos-y').textContent = Math.round(camera.y);
    document.getElementById('lod-level').textContent = lodSystem.currentLevel;
}

// Initialize when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
} else {
    init();
}
