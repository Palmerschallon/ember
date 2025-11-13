import matplotlib.pyplot as plt
import numpy as np

# Create a 1000x1000 grid of complex numbers
y, x = np.ogrid[-1.5:1.5:1000j, -2:1:1000j]
c = x + 1j*y

# Mandelbrot set
niter = 256
z = c
for n in range(niter):
    z = z**2 + c

# Create mask for points that diverge
mask = np.abs(z) < 1000

# Create image
plt.imshow(mask.T, extent=[-2, 1, -1.5, 1.5])
plt.gray()
plt.savefig('mandelbrot.png')