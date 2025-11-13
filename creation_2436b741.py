import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Set the seed for reproducibility
random.seed(42)

# Create the figure and a 3D axis
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

# Generate the coordinates for the spheres
num_spheres = 50
x = np.random.uniform(-5, 5, num_spheres)
y = np.random.uniform(-5, 5, num_spheres)
z = np.random.uniform(-5, 5, num_spheres)

# Generate random sizes and colors for the spheres
sizes = np.random.uniform(20, 100, num_spheres)
colors = np.random.uniform(0, 1, (num_spheres, 3))

# Plot each sphere
for (xi, yi, zi, si, ci) in zip(x, y, z, sizes, colors):
    ax.scatter(xi, yi, zi, s=si, c=[ci], alpha=0.6, edgecolors='w')

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Remix of Interactive 3D Spheres')

# Save the figure
plt.savefig('/media/palmerschallon/ThePod1/3d_spheres_remix.png')