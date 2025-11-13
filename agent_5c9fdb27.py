import matplotlib.pyplot as plt
import numpy as np

# Create a blank image
image = np.zeros((800, 800))

# Define the properties of the fractal
xmin, xmax, ymin, ymax = -2.0, 1.0, -1.5, 1.5
width, height = 800, 800
cx, cy = -0.7, 0.27015
max_iter = 256

# Generate the fractal
for x in range(width):
    for y in range(height):
        zx, zy = x * (xmax - xmin) / (width - 1) + xmin, y * (ymax - ymin) / (height - 1) + ymin
        c = zx + zy * 1j
        z = c
        for i in range(max_iter):
            if abs(z) > 2.0:
                break 
            z = z * z + c
        image[y, x] = i

# Display the fractal
plt.imshow(image, cmap='twilight_shifted')
plt.show()