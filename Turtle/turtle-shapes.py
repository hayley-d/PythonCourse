from turtle import Turtle, Screen
import random

colours = ['violet','plum','deep sky blue','#3CB371','gold','crimson','#DB7093']

timmy = Turtle()
timmy.shape("turtle")

# Draw a triangle
side_length = 100
timmy.color(random.choice(colours))

for _ in range(3):
    timmy.forward(side_length)
    timmy.right(120)

# Move to new spot
timmy.penup()
timmy.left(90)
for _ in range(3):
    timmy.forward(100)
timmy.pendown()
timmy.right(90)

# Pentagon
side_length = 100
timmy.color(random.choice(colours))

for _ in range(5):
    timmy.forward(side_length)
    timmy.right(360 / 5)

# Move to new spot
timmy.penup()
for _ in range(4):
    timmy.backward(100)
timmy.pendown()

# Draw a hexagon
side_length = 100
timmy.color(random.choice(colours))
for _ in range(6):
    timmy.forward(side_length)
    timmy.right(360 / 6)

# Keep at the bottom
screen = Screen()
screen.exitonclick()