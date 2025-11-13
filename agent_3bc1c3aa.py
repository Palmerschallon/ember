import numpy as np
from scipy.interpolate import griddata
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the function
f = lambda x, y: np.sin(np.sqrt(x ** 2 + y ** 2))

# Create a grid of points
x = np.linspace(-7, 7, 100)
y = np.linspace(-7, 7, 100)
X, Y = np.meshgrid(x, y)

# Calculate Z values (heights) for X and Y
Z = f(X, Y)

# Create 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')

# Return as a string representation as actual plot can't be displayed
str(fig)