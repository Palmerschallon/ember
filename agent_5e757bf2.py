import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os

# Parameters
num_frames = 100
size = 500

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
    val = np.ones(Z.shape)

    # Convert HSV to RGB
    rgb = plt.cm.hsv_to_rgb(np.dstack([hue, sat, val]))
    rgb_255 = (rgb * 255).astype(np.uint8)
    print(f'rgb_255 shape: {rgb_255.shape}, dtype: {rgb_255.dtype}')

    # Save as PNG
    Image.fromarray(rgb_255, 'RGB').save(f'/media/palmerschallon/ThePod1/frame_{i:03d}.png')
