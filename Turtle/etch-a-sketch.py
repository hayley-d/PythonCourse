import turtle as t
from turtle import Turtle
from turtle import Screen

Timmy = Turtle()


def move_forward():
    Timmy.forward(10)


def move_left():
    Timmy.left(10)


def move_backward():
    Timmy.backward(10)


def move_right():
    Timmy.right(10)

def clear():
    Timmy.clear()
    Timmy.penup()
    Timmy.home()
    Timmy.pendown()

screen = Screen()
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
