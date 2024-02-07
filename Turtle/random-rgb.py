from turtle import Turtle, Screen
import random
import turtle as t

t.colormode(255)
timmy = Turtle()
timmy.shape("turtle")
timmy.width(2)
timmy.speed(0)

radius = 100


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        timmy.circle(radius)
        current_heading = timmy.heading()
        timmy.setheading(current_heading + size_of_gap)

draw_spirograph(5)
# Keep at the bottom
screen = Screen()
screen.exitonclick()
