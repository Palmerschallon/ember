import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x ** 2)

fig, axs = plt.subplots(1, 1,
                        figsize =(10, 7), 
                        tight_layout = True)

axs.plot(x, y)
axs.set_title('Simple plot')

plt.show()