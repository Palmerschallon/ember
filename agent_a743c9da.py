import numpy as np
from stl import mesh

def mandelbulb(x, y, z, n):
    r = np.sqrt(x**2 + y**2 + z**2)
    phi = np.arctan2(y, x)
    theta = np.arctan2(np.sqrt(x**2 + y**2), z)
    
    x_new = r**n * np.sin(theta*n) * np.cos(phi*n)
    y_new = r**n * np.sin(theta*n) * np.sin(phi*n)
    z_new = r**n * np.cos(theta*n)
    
    return x_new, y_new, z_new

def generate_mandelbulb(n=8, size=200, max_iterations=10, power=8):
    vertices = []
    
    for i in range(size):
        for j in range(size):
            for k in range(size):
                x, y, z = (i/size - 0.5)*2, (j/size - 0.5)*2, (k/size - 0.5)*2
                x0, y0, z0 = x, y, z
                
                iteration = 0
                while iteration < max_iterations:
                    x, y, z = mandelbulb(x, y, z, power)
                    if (x**2 + y**2 + z**2) > 4:
                        break
                    iteration += 1
                    
                if iteration == max_iterations:
                    vertices.append([i/size - 0.5, j/size - 0.5, k/size - 0.5])

    fractal = mesh.Mesh(np.zeros(len(vertices), dtype=mesh.Mesh.dtype))
    for i, v in enumerate(vertices):
        fractal.vectors[i] = np.array(v)

    fractal.save('mandelbulb.stl')
    
generate_mandelbulb()
print("Generated beautiful 3D mandelbulb fractal and saved to mandelbulb.stl")