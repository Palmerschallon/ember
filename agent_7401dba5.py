import numpy as np
import matplotlib.pyplot as plt
import imageio

# Parameters
num_frames = 100
size = 500

# Initialize arrays
frames = np.zeros((num_frames, size, size, 3), dtype=np.uint8)

# Create frames
for i in range(num_frames):
    # Create fractal pattern
    x = np.linspace(-1, 1, size) + (np.random.rand()-0.5)/10
    y = np.linspace(-1, 1, size) + (np.random.rand()-0.5)/10
    X, Y = np.meshgrid(x, y)
    Z = (X + 1j * Y) ** (i / num_frames * 8)

    # Color based on angle
    hue = np.angle(Z) / (2 * np.pi) + 0.5
    sat = np.abs(Z) / 2
    val = 1
    hsv = np.stack((hue, sat, val), axis=-1)

    # Convert to RGB
    frames[i] = (plt.cm.hsv(hsv) * 255).astype(np.uint8)

# Save as GIF
imageio.mimsave('/media/palmerschallon/ThePod1/fractal_animation.png', frames)
