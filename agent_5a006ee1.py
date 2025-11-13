import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import hsv_to_rgb

# Define the properties of the Mandelbrot set
WIDTH = 800
HEIGHT = 800
MAX_ITER = 1000

# Function to compute the color of each pixel
def mandelbrot(c):
    z = c
    n = 0
    while abs(z) <= 2 and n < MAX_ITER:
        z = z*z + c
        n += 1
    if n == MAX_ITER:
        return (0, 0, 0)
    else:
        return hsv_to_rgb((n % 256 / 256, 1, n / MAX_ITER))

# Generate the Mandelbrot set
mandelbrot_set = np.zeros((WIDTH, HEIGHT, 3), dtype=np.uint8)
for x in range(WIDTH):
    for y in range(HEIGHT):
        real = 3.5 * (x - WIDTH / 2) / (0.5 * WIDTH)
        imag = 2.5 * (y - HEIGHT / 2) / (0.5 * HEIGHT)
        mandelbrot_set[y, x] = mandelbrot(complex(real, imag)) * 255

plt.imshow(mandelbrot_set, origin='lower')
plt.show()