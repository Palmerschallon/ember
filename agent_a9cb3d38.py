import matplotlib.pyplot as plt
import numpy as np

# Create a range of x values from -2pi to 2pi
x = np.linspace(-2*np.pi, 2*np.pi, 1000)

# Create y values using the sine function
y = np.sin(x)

# Plot x against y
plt.plot(x, y)

# Display the plot
plt.show()