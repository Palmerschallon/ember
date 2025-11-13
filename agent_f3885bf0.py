import math

# Define the dimensions of the pattern
width, height = 80, 24

# Create a two-dimensional array of characters
grid = [[' ' for x in range(width)] for y in range(height)]

# Draw a sinusoidal pattern
for y in range(height):
    for x in range(width):
        # Compute the distance to the center of the pattern
        dx = x - width / 2
        dy = y - height / 2
        distance = math.sqrt(dx * dx + dy * dy)

        # Compute the sinusoidal pattern
        value = (1.0 + math.sin(distance / 3.0)) / 2.0

        # Choose a character based on the computed value
        if value > 0.7:
            char = '*'
        elif value > 0.3:
            char = '+'
        else:
            char = '.'

        grid[y][x] = char

# Print the grid
for row in grid:
    print(''.join(row))