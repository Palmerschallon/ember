import matplotlib.pyplot as plt
import numpy as np

# Create a time array
T = np.linspace(0, 4 * np.pi, 1000)

# Create a figure and a set of subplots
fig, ax = plt.subplots()

# Plot a sine wave
ax.plot(T, np.sin(T), color='blue', label='Sine wave')

# Plot a cosine wave
ax.plot(T, np.cos(T), color='red', label='Cosine wave')

# Set the title and labels
ax.set_title('Sine and Cosine Waves')
ax.set_xlabel('Time (s)')
ax.set_ylabel('Amplitude')

# Enable the legend
ax.legend()

# Show the plot
plt.show()