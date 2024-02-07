# import colorgram
from turtle import Turtle
from turtle import Screen
import turtle as t
import random

# rgb_colours = []
# colours = colorgram.extract('art.jpg', 30)
#
# for colour in colours:
#     r = colour.rgb.r
#     g = colour.rgb.g
#     b = colour.rgb.b
#     colour_tuple = (r, g, b)
#     rgb_colours.append(colour_tuple)
#
# print(rgb_colours)

colour_list = [(239, 236, 238), (238, 237, 236), (237, 237, 241), (26, 108, 164), (193, 38, 81), (237, 161, 50), (234, 215, 86), (227, 237, 229), (223, 137, 176), (143, 108, 57), (103, 197, 219), (21, 57, 132), (205, 166, 30), (213, 74, 91), (238, 89, 49), (142, 208, 227), (119, 191, 139), (5, 185, 177), (106, 108, 198), (137, 29, 72), (4, 162, 86), (98, 51, 36), (24, 155, 210), (229, 168, 185), (173, 185, 221), (29, 90, 95), (233, 173, 162), (156, 212, 190), (87, 46, 33), (37, 45, 83)]

t.colormode(255)
timmy = Turtle()
timmy.shape("turtle")
timmy.penup()
timmy.speed(0)
timmy.setheading(225)
timmy.forward(250)
timmy.setheading(0)
timmy.hideturtle()

for _ in range(10):
    for _ in range(10):
        timmy.dot(20, random.choice(colour_list))
        timmy.forward(50)
    timmy.backward(500)
    timmy.left(90)
    timmy.forward(50)
    timmy.right(90)


# Keep at the bottom
screen = Screen()
screen.exitonclick()
