import matplotlib.pyplot as plt
import numpy as np

# Fibonacci numbers
fibonacci_numbers = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]

# Golden ratio
phi = (1 + np.sqrt(5)) / 2

# Create a list of theta values
theta = [i * np.pi / 2 for i in range(len(fibonacci_numbers))]

# Create a list of radii
radii = [fibonacci_numbers[i] / (phi ** i) for i in range(len(fibonacci_numbers))]

# Create a new figure and polar axes
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)

# Hide the grid and labels
ax.grid(False)
ax.set_xticklabels([])
ax.set_yticklabels([])

# Plot each radius
for i in range(len(radii)):
    ax.plot([theta[i], theta[i]], [0, radii[i]], color='gold', linewidth=2)
    if i < len(radii) - 1:
        ax.plot([theta[i], theta[i+1]], [radii[i], radii[i]], color='gold', linewidth=2)
    # Add Fibonacci number labels
    ax.text(theta[i], radii[i], str(fibonacci_numbers[i]), fontsize=12, ha='center')

# Save the figure
plt.savefig('/media/palmerschallon/ThePod1/golden_ratio_spiral.png')