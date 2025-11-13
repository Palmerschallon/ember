import matplotlib.pyplot as plt
import numpy as np

# Create data
N = 500
x = np.random.rand(N)
y = np.random.rand(N)

# Generate colors
colors = np.random.rand(N)

# Generate area of each point (0 to 15 point radii)
area = (30 * np.random.rand(N))**2

plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.show()