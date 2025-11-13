import matplotlib.pyplot as plt
import numpy as np

# Create a time array
T = np.linspace(0, 2 * np.pi, 1000)

# Create a rainbow of lines with different frequencies
for i in range(1, 6):
    Y = np.sin(i * T)
    plt.plot(T, Y, label=f'frequency {i}')

plt.legend()
plt.show()