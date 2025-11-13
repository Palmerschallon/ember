import matplotlib.pyplot as plt
import numpy as np

# Create a time array
T = np.linspace(0, 2 * np.pi, 1000)

# Create a figure and a set of subplots
fig, ax = plt.subplots()

# Plot a sine wave
ax.plot(T, np.sin(T))

# Show the plot
plt.title('Sine Wave')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid(True)
plt.savefig('/media/palmerschallon/ThePod1/sine_wave.png')
plt.show()