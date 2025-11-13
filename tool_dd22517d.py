import numpy as np
import matplotlib.pyplot as plt

# Define the dimensions (resolution) of the fractal image
width, height = 800, 800

# Define the x and y coordinate arrays
x = np.linspace(-2.0, 2.0, width)
y = np.linspace(-2.0, 2.0, height)
X, Y = np.meshgrid(x, y)

# Define the iteration count
iteration_count = 1000

# Define the output array of the same size as the coordinate arrays
c = np.zeros_like(X + 1j * Y)

# Define the complex constant for the Julia set
c_constant = np.complex(-0.8, 0.156)

# Perform the iteration
for i in range(iteration_count):
    c = c * c + c_constant

# Create the fractal image
plt.imshow(np.angle(c))
plt.show()