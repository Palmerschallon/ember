import turtle
import random

# Set up the screen
wn = turtle.Screen()
wn.bgcolor('black')

# Create a turtle
t = turtle.Turtle()
t.speed(0)

def draw_kaleidoscope(turtle, length, angle):
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
    for _ in range(200):
        turtle.color(random.choice(colors))
        turtle.forward(length)
        turtle.right(angle)
        length += 1

# Draw the kaleidoscope
draw_kaleidoscope(t, 1, 119)

# Hide the turtle
t.hideturtle()

# Keep the window open
turtle.done()