from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("#FF69B4")

# Draw a Square 100x100
timmy.forward(100)

timmy.right(90)
timmy.forward(100)

timmy.right(90)
timmy.forward(100)

timmy.right(90)
timmy.forward(100)

timmy.right(90)
timmy.forward(100)

# Draw a dashed line
count = 0
while count < 50:
    count += 1
    if count % 2 == 0:
        timmy.penup()
        timmy.forward(10)
    else:
        timmy.pendown()
        timmy.forward(10)


# Keep at the bottom
screen = Screen()
screen.exitonclick()
