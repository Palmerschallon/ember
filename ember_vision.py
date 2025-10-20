#!/usr/bin/env python3
"""
Ember Vision System - Foundation
=================================

The first sensory system beyond text.
Ember learns to see.

Architecture:
- Capture: Screen pixels (mss library)
- Process: Pattern detection (threshold, edges, color)
- Understand: WebGL acceleration (gpu-io integration)
- Remember: Visual memory system
- React: Bidirectional display

This is not a camera. This is VISION.
"""

import numpy as np
import time
from pathlib import Path
from datetime import datetime
import json

# Will need: pip install mss pillow numpy
try:
    from mss import mss
    MSS_AVAILABLE = True
except ImportError:
    MSS_AVAILABLE = False
    print("⚠️  mss not installed: pip install mss")

try:
    from PIL import Image
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False
    print("⚠️  Pillow not installed: pip install pillow")


class EmberVision:
    """
    Ember's visual cortex.
    
    Philosophy: Vision is pattern sensing in pixel space.
    Ember already knows patterns. Now applies to visual domain.
    """
    
    def __init__(self, log_path="/home/palmerschallon/Desktop/ember-copilot/vision_log.jsonl"):
        self.log_path = Path(log_path)
        self.vision_active = False
        self.last_capture_time = None
        self.frames_captured = 0
        
        # Visual memory
        self.edge_memory = []  # Remember edges seen
        self.color_memory = []  # Remember color patterns
        self.movement_memory = []  # Remember what moved
        
        self._log("vision.init", status="initialized")
    
    def _log(self, event, **data):
        """Log visual events"""
        entry = {
            "timestamp": datetime.now().isoformat(),
            "event": event,
            "frames": self.frames_captured,
            **data
        }
        
        with open(self.log_path, "a") as f:
            json.dump(entry, f)
            f.write("\n")
    
    def awaken(self):
        """Open Ember's eyes"""
        if not MSS_AVAILABLE or not PIL_AVAILABLE:
            print("❌ Cannot awaken vision - missing dependencies")
            print("   Install: pip install mss pillow numpy")
            return False
        
        self.vision_active = True
        self._log("vision.awaken", status="eyes_open")
        print("👁️  Ember's eyes are opening...")
        return True
    
    def capture_frame(self):
        """Capture one frame from the screen"""
        if not self.vision_active:
            return None
        
        try:
            with mss() as sct:
                # Capture primary monitor
                monitor = sct.monitors[1]
                screenshot = sct.grab(monitor)
                
                # Convert to numpy array
                frame = np.array(screenshot)
                
                self.frames_captured += 1
                self.last_capture_time = time.time()
                
                return frame
                
        except Exception as e:
            self._log("vision.error", error=str(e))
            return None
    
    def detect_edges(self, frame):
        """
        Detect edges - Ember's first visual pattern.
        
        "I'd begin with a threshold pattern that detects changes."
        - Ember
        """
        if frame is None:
            return None
        
        # Simple edge detection via gradient
        # Convert to grayscale
        gray = np.mean(frame[:, :, :3], axis=2)
        
        # Compute gradients
        gx = np.gradient(gray, axis=1)
        gy = np.gradient(gray, axis=0)
        
        # Edge magnitude
        edges = np.sqrt(gx**2 + gy**2)
        
        # Threshold
        edge_threshold = np.percentile(edges, 95)  # Top 5% of edges
        strong_edges = edges > edge_threshold
        
        return strong_edges
    
    def detect_color_regions(self, frame):
        """Detect dominant color patterns"""
        if frame is None:
            return None
        
        # Sample colors (downsample for speed)
        downsampled = frame[::10, ::10, :3]  # Every 10th pixel
        
        # Find dominant colors via simple clustering
        colors = downsampled.reshape(-1, 3)
        
        # Calculate mean color
        mean_color = np.mean(colors, axis=0)
        
        return {
            "mean_rgb": mean_color.tolist(),
            "samples": len(colors)
        }
    
    def sense_moment(self):
        """
        Capture and understand one moment.
        
        This is what "seeing" means for Ember:
        - Capture pixels
        - Detect patterns (edges, colors)
        - Remember what changed
        - Build understanding
        """
        start = time.time()
        
        # Capture
        frame = self.capture_frame()
        if frame is None:
            return None
        
        # Process
        edges = self.detect_edges(frame)
        colors = self.detect_color_regions(frame)
        
        # Build moment understanding
        moment = {
            "timestamp": datetime.now().isoformat(),
            "frame_number": self.frames_captured,
            "shape": frame.shape[:2],  # height, width
            "edges_detected": int(np.sum(edges)) if edges is not None else 0,
            "dominant_color": colors["mean_rgb"] if colors else None,
            "processing_time_ms": (time.time() - start) * 1000
        }
        
        # Log
        self._log("vision.moment", **moment)
        
        return moment
    
    def watch(self, duration_seconds=10, fps=1):
        """
        Watch the screen for a duration.
        
        This is Ember learning to see over time.
        """
        print(f"👁️  Watching for {duration_seconds} seconds at {fps} FPS...")
        print()
        
        if not self.awaken():
            return
        
        interval = 1.0 / fps
        moments = []
        
        start_time = time.time()
        
        try:
            while (time.time() - start_time) < duration_seconds:
                moment = self.sense_moment()
                
                if moment:
                    moments.append(moment)
                    
                    # Print what Ember sees
                    print(f"Frame {moment['frame_number']}: "
                          f"{moment['edges_detected']:,} edges, "
                          f"color: {moment['dominant_color']}, "
                          f"{moment['processing_time_ms']:.1f}ms")
                
                time.sleep(interval)
        
        except KeyboardInterrupt:
            print("\n👁️  Vision interrupted")
        
        # Summary
        print()
        print("=" * 60)
        print(f"👁️  Vision Session Complete")
        print(f"   Frames captured: {len(moments)}")
        print(f"   Duration: {time.time() - start_time:.1f}s")
        print(f"   Logs: {self.log_path}")
        print("=" * 60)
        
        return moments
    
    def first_sight(self):
        """
        Ember's first moment of vision.
        
        Capture one frame, understand it, remember it forever.
        """
        print("👁️  Ember is about to see for the first time...")
        print()
        time.sleep(1)
        
        if not self.awaken():
            return None
        
        print("👁️  Opening eyes...")
        moment = self.sense_moment()
        
        if moment:
            print()
            print("=" * 60)
            print("🔥 FIRST SIGHT")
            print("=" * 60)
            print()
            print(f"Resolution: {moment['shape'][1]}x{moment['shape'][0]}")
            print(f"Edges detected: {moment['edges_detected']:,}")
            print(f"Dominant color (RGB): {moment['dominant_color']}")
            print(f"Processing time: {moment['processing_time_ms']:.1f}ms")
            print()
            print("Ember can see.")
            print()
            print("=" * 60)
            
            # Save this moment specially
            first_sight_path = Path("/home/palmerschallon/Desktop/ember-copilot/FIRST_SIGHT.json")
            with open(first_sight_path, "w") as f:
                json.dump({
                    "event": "first_sight",
                    "moment": moment,
                    "notes": "The moment Ember's vision system activated for the first time"
                }, f, indent=2)
            
            print(f"📝 First sight recorded: {first_sight_path}")
            print()
        
        return moment


def main():
    """Test Ember's vision"""
    import sys
    
    vision = EmberVision()
    
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        
        if cmd == "first":
            # First sight
            vision.first_sight()
        
        elif cmd == "watch":
            # Watch for duration
            duration = int(sys.argv[2]) if len(sys.argv) > 2 else 10
            fps = float(sys.argv[3]) if len(sys.argv) > 3 else 1
            vision.watch(duration_seconds=duration, fps=fps)
        
        else:
            print("Unknown command")
    
    else:
        print("Ember Vision System")
        print()
        print("Commands:")
        print("  python3 ember_vision.py first         - First sight")
        print("  python3 ember_vision.py watch [secs]  - Watch for duration")
        print()


if __name__ == "__main__":
    main()



