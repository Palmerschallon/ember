import matplotlib.pyplot as plt
import numpy as np

# Golden ratio
phi = (1 + np.sqrt(5)) / 2

# Spiral parameters
spiral_rotations = 8
theta = np.linspace(0, 2.0*np.pi*spiral_rotations, 1000)

# Radius grows by the golden ratio for each full rotation
radius = np.power(phi, theta / (2.0*np.pi))

# Convert to cartesian coordinates
x = radius * np.cos(theta)
y = radius * np.sin(theta)

# Fibonacci numbers for labelling
fibonacci_numbers = [0, 1]
for i in range(spiral_rotations):
    fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])

# Create a new figure
fig = plt.figure(figsize=(6, 6))

# Add the spiral
plt.plot(x, y, color='goldenrod')

# Add Fibonacci labels
for i in range(spiral_rotations):
    label_radius = np.power(phi, i)
    label_x = label_radius * np.cos(i * 2.0 * np.pi)
    label_y = label_radius * np.sin(i * 2.0 * np.pi)
    plt.text(label_x, label_y, str(fibonacci_numbers[i]), fontsize=12, ha='center')

# Set up plot appearance
plt.axis('off')
plt.axis('equal')

# Save the plot
plt.savefig('/media/palmerschallon/ThePod1/golden_ratio_spiral.png')