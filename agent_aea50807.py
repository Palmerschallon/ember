import turtle

# setting the window
wn = turtle.Screen()
wn.bgcolor('black')

# Define a turtle to draw the design
flower = turtle.Turtle()
flower.speed(10)

# draw the design
for i in range(36):
    for colors in ['red', 'magenta', 'blue', 'cyan', 'green', 'yellow', 'white']:
        flower.color(colors)
        flower.forward(100)
        flower.left(59)
    flower.right(10)

# Hide the turtle
flower.hideturtle()

# keep the window open
turtle.done()