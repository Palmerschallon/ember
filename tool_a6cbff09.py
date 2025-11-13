import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 1000)
y = np.sin(x)

plt.plot(x, y, label='sin(x)')
plt.title('A Simple Plot')
plt.legend()
plt.savefig('/media/palmerschallon/ThePod1/plot.png')