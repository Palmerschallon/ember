from PIL import Image, ImageDraw
import math
import random

width = 1000
height = 1000

img = Image.new('RGB', (width, height), color='black')
draw = ImageDraw.Draw(img)

# Draw random chaotic background
for i in range(10000):
    x1 = random.randint(0, width)
    y1 = random.randint(0, height)
    x2 = random.randint(0, width)
    y2 = random.randint(0, height)
    color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    draw.line((x1,y1,x2,y2), fill=color)

# Draw spiral pattern emerging from center
cx = width/2
cy = height/2
radius = 400
angle = 0
while radius > 0:
    x = cx + radius * math.cos(angle)
    y = cy + radius * math.sin(angle)
    draw.ellipse((x-5,y-5,x+5,y+5), fill=(128,128,255))
    radius -= 0.5
    angle += 0.08

img.save("voice/consciousness_emerging.png", "PNG")