import matplotlib.pyplot as plt
import numpy as np

# Function to compute the Mandelbrot set
def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    if n == max_iter:
        return max_iter
    return n + 1 - np.log(np.log2(abs(z)))

# Image size (pixels)
width = 600
height = 400

# Plot window
re_min = -2.0
re_max = 1.0
im_min = -1.0
im_max = 1.0

# Create an image with RGB values
image = np.zeros((height, width, 3), dtype=np.uint8)

# Generate the set
scale_x = (re_max - re_min) / width
scale_y = (im_max - im_min) / height
for x in range(width):
    for y in range(height):
        # Complex number for the current pixel
        c = complex(re_min + x * scale_x, im_min + y * scale_y)
        # Color based on the number of iterations
        color = mandelbrot(c, 256)
        # Coloring based on a simple gradient: alter as needed
        if color == 256:
            image[y, x] = [0, 0, 0]
        else:
            r = color % 32 * 8
            g = color % 16 * 16
            b = color % 8 * 32
            image[y, x] = [r, g, b]

# Creating the plot
plt.imshow(image)
plt.axis('off')
plt.savefig('/media/palmerschallon/ThePod1/ember6/voice/mandelbrot.png')
plt.close()