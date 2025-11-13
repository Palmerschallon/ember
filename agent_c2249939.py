import turtle
import random

# Create a new turtle screen and set its background color
screen = turtle.Screen()
screen.bgcolor("white")

# Create a new turtle object
myTurtle = turtle.Turtle()
myTurtle.speed(0)  # Set turtle speed to maximum

# Define a list of colors
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

def draw_mandala(myTurtle, radius, petal_color):
  myTurtle.color(petal_color)
  myTurtle.fillcolor(petal_color)
  myTurtle.begin_fill()
  myTurtle.circle(radius)
  myTurtle.end_fill()
  myTurtle.left(60)

# Draw the mandala
for _ in range(36):  # Draw 36 circles to form the mandala
  draw_mandala(myTurtle, 100, random.choice(colors))
  myTurtle.right(10)

# Hide the turtle and display the result
myTurtle.hideturtle()
turtle.done()