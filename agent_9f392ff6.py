import matplotlib.pyplot as plt
import numpy as np

# Size of the image
width = 10
height = 10

# Creating a new plot
fig = plt.figure(figsize=(width, height))
ax = fig.add_subplot(111, projection='3d')

# Creating a fractal
x = np.linspace(-2.0, 1.0, width)
y = np.linspace(-1.5, 1.5, height)
X, Y = np.meshgrid(x, y)
c = X + 1j*Y
z = c

# Iterations
for i in range(100):
    if not (np.abs(z) > 1000).any():
        break
    z = z*z + c

# Creating the 3D plot
ax.scatter(X, Y, np.abs(z), c=np.angle(z), cmap='hsv')

# Saving the figure
plt.savefig('/media/palmerschallon/ThePod1/ember5/fractal.png')

'Fractal Created'