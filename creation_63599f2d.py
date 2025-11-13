import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# Create custom autumn colormap
autumn_colors = [(1.0, 1.0, 0.0), (1.0, 0.5, 0.0), (1.0, 0.0, 0.0), (0.5, 0.0, 0.0)]
autumn_cmap = LinearSegmentedColormap.from_list('autumn', autumn_colors)

# Create the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))

# Draw the trunk
trunk_height = 0.5
trunk_width = 0.1
trunk = plt.Rectangle((0.5 - trunk_width/2, 0), trunk_width, trunk_height, color='saddlebrown')
ax.add_patch(trunk)

# Draw the leaves
for i in range(500):
    # Randomize leaf position
    x = np.random.normal(0.5, 0.2)
    y = np.random.uniform(trunk_height, 1.0)
    
    # Randomize leaf size and color
    size = np.random.uniform(0.01, 0.03)
    color = autumn_cmap(np.random.rand())

    # Draw the leaf
    leaf = plt.Circle((x, y), size, color=color)
    ax.add_patch(leaf)

# Set the limits and remove the axis
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Save the image
plt.savefig('/media/palmerschallon/ThePod1/autumn_tree.png', dpi=150, bbox_inches='tight')