from turtle import Turtle, Screen
import turtle as t
import random

t.colormode(255)
colours = ['violet','plum','deep sky blue','#3CB371','gold','crimson','#DB7093']
directions = range(0,360)
distances = range(1,100)


timmy = Turtle()
timmy.shape("turtle")
timmy.width(5)


for _ in range(100):
    direction = random.choice(directions)
    distance = random.choice(distances)
    # Change Colour
    timmy.color(random.choice(range(0,255)),random.choice(range(0,255)),random.choice(range(0,255)))
    timmy.setheading(direction)
    timmy.forward(distance)

# Keep at the bottom
screen = Screen()
screen.exitonclick()
