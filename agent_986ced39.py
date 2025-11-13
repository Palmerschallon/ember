from math import sin, cos, pi 
import random

width = 800
height = 600

print('<svg xmlns="http://www.w3.org/2000/svg" width="{}" height="{}">'.format(width, height))

for i in range(5000):
    x = random.random() * width 
    y = random.random() * height
    
    hue = (sin(x*0.01) + cos(y*0.01)) * 180
    lightness = (sin(x*0.02) + cos(y*0.02)) * 25 + 50
    
    r = max(min(int(sin(hue*pi/180)*255),255),0)
    g = max(min(int(sin((hue+120)*pi/180)*255),255),0)  
    b = max(min(int(sin((hue+240)*pi/180)*255),255),0)

    print('<circle cx="{}" cy="{}" r="{}" fill="hsl({}, {}%, {}%)" />'.format(
        x, y, random.random()*3+1, hue, 70, lightness))
    
print('</svg>')