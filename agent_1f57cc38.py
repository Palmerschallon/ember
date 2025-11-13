import matplotlib.pyplot as plt
import numpy as np

# Initial setup
x, y = np.meshgrid(np.linspace(-2,2,1000), np.linspace(-2,2,1000))
c = x + 1j*y
z = c
for i in range(100):
    z = z*z + c

# Function to render with infinite zoom
def render_with_infinite_zoom():
    plt.figure(figsize=(10,10))
    plt.imshow(np.abs(z)<1000, cmap='hot', interpolation='none', extent=[-2,2,-2,2])
    for i in range(100):
        xlim = plt.gca().get_xlim()
        ylim = plt.gca().get_ylim()
        plt.gca().set_xlim(xlim[0]*0.9, xlim[1]*0.9)
        plt.gca().set_ylim(ylim[0]*0.9, ylim[1]*0.9)
        plt.draw()
        plt.pause(0.01)

render_with_infinite_zoom()