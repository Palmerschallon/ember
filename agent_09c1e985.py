import numpy as np
from scipy.spatial import ConvexHull

def mandelbulb(x, y, z, n, max_iters):
    c = np.array([x, y, z])
    z = np.zeros(3)
    dr = 1.0
    r = 0.0
    
    for i in range(max_iters):
        r = np.linalg.norm(z)
        if r > 2:
            break
        
        theta = np.arctan2(np.sqrt(z[0]**2 + z[1]**2), z[2])
        phi = np.arctan2(z[1], z[0])
        
        zr = r**n
        theta = theta*n
        phi = phi*n
        
        z = zr * np.array([np.sin(theta)*np.cos(phi),
                           np.sin(theta)*np.sin(phi),
                           np.cos(theta)]) + c
        
        dr = np.power(r, n-1) * n * dr + 1
        
    return 0.5 * np.log(r) * r / dr

vertices = []
for i in range(100000):
    x, y, z = np.random.uniform(-1, 1, size=3) 
    m = mandelbulb(x, y, z, 8, 10)
    if m < 50:
        vertices.append([x, y, z])
        
vertices = np.array(vertices)        
hull = ConvexHull(vertices)

obj_content = ""
for v in hull.vertices:
    obj_content += f"v {vertices[v,0]} {vertices[v,1]} {vertices[v,2]}\n"
    
for s in hull.simplices:
    obj_content += f"f {s[0]+1} {s[1]+1} {s[2]+1}\n"

print(obj_content)