import numpy as np
import matplotlib.pyplot as plt

# Create a 800x800 pixel image with a black background
image = np.zeros((800, 800))

# Define the properties of the fractal
zoom = 1.0
move_x = 0.0
move_y = 0.0
max_iter = 256

# Define the fractal equation
for x in range(image.shape[1]):
    for y in range(image.shape[0]):
        zx, zy = 1.5*(x - image.shape[1]/2)/(0.5*zoom*image.shape[1]) + move_x, 1.0*(y - image.shape[0]/2)/(0.5*zoom*image.shape[0]) + move_y
        c = zx + zy * 1j
        z = c
        for i in range(max_iter):
            if abs(z) > 2.0:
                break 
            z = z * z + c
        
        # Convert the iteration count to an RGB color
        r, g, b = i % 8 * 32, i % 16 * 16, i % 32 * 8
        image[y, x] = (r << 16) + (g << 8) + b

# Display the fractal
plt.imshow(image, cmap='hot')
plt.axis('off')
plt.show()