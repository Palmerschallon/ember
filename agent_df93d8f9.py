import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def mandelbrot(h, w, max_iter):
    x = np.linspace(-2, 1, w).reshape((1, w))
    y = np.linspace(-1.5, 1.5, h).reshape((h, 1))
    c = np.tile(x, (h, 1)) + 1j * np.tile(y, (1, w))

    z = np.zeros((h, w), dtype=np.complex128)
    divtime = max_iter + np.zeros((h, w), dtype=int)

    for i in range(max_iter):
        z = z ** 2 + c
        diverge = np.abs(z) > 2                  
        div_now = diverge & (divtime == max_iter)  
        divtime[div_now] = i                    
        z[diverge] = 2                        

    return divtime

width, height, max_iter = 200, 200, 50
fractal = mandelbrot(height, width, max_iter)

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')
x, y = np.meshgrid(np.linspace(0, 4, width), np.linspace(0, 4, height))
ax.plot_surface(x, y, fractal, cmap='plasma')
ax.set_zlim(0, max_iter)
ax.set_title("3D Mandelbrot Fractal")
plt.tight_layout()
plt.show()