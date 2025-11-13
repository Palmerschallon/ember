import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Create the x, y, and z coordinate arrays
y,x = np.mgrid[-7:7:0.1, -7:7:0.1]
z = np.sin(np.sqrt(x**2 + y**2))

# Create a 3D surface plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
plt.show()