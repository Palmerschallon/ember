from svgwrite import Drawing, rgb
import math

# Create a new SVG drawing
dwg = Drawing('mandala.svg', profile='tiny')

# Center of the mandala
center_x = 250
center_y = 250

# Number of petals
petals = 36

# Radius of the mandala
radius = 100

# Draw the mandala
for i in range(petals):
    # Calculate the angle and position of each petal
    angle = i * (360 / petals)
    x = center_x + radius * math.cos(math.radians(angle))
    y = center_y + radius * math.sin(math.radians(angle))

    # Draw a line from the center to the petal position
    dwg.add(dwg.line((center_x, center_y), (x, y), stroke=rgb(0, 0, 0, '%')))

# Save the drawing
dwg.save()