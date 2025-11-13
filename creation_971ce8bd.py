import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

def update(num):
    x = np.linspace(0, 2 * np.pi, 1000)
    y = np.sin(x)
    ax.clear()
    ax.plot(x, y)

fig, ax = plt.subplots()
ani = FuncAnimation(fig, update, interval=1000, blit=True)
plt.savefig('/media/palmerschallon/ThePod1/fractal.png')