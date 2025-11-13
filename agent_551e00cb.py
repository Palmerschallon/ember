import numpy as np

u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)

x = 10 * np.outer(np.cos(u), np.sin(v))
y = 10 * np.outer(np.sin(u), np.sin(v))
z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))

with open("/media/palmerschallon/ThePod1/sphere.txt", "w") as f:
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            f.write(f"{x[i, j]}, {y[i, j]}, {z[i, j]}\n")