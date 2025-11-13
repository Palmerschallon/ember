import matplotlib.pyplot as plt
import numpy as np

def mandelbrot(h, w, max_iter):
    x = np.linspace(-2, 1, w).reshape((1, w))
    y = np.linspace(-1.5, 1.5, h).reshape((h, 1))
    c = x + 1j * y
    z = np.zeros((h, w), dtype=np.complex128)
    output = np.zeros((h, w), dtype=int)
    
    for i in range(max_iter):
        z = z ** 2 + c
        mask = (np.abs(z) > 2)
        z[mask] = 2
        output[mask & (output == 0)] = i
    
    return output

h, w, max_iter = 1000, 1000, 100
output = mandelbrot(h, w, max_iter)

plt.figure(figsize=(10, 10))
plt.imshow(output, cmap='plasma')
plt.axis('off')

plt.tight_layout()
plt.savefig('mandelbrot.png', bbox_inches='tight', pad_inches=0)
plt.close()

print("Successfully created Mandelbrot set fractal image: mandelbrot.png")