import random
import turtle as t
from turtle import Turtle
from turtle import Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your Bet",
                            prompt="Which turtle will win the race? Enter a colour: Timmy(green), Zippy(blue), Ralph(purple), Daisy(yellow), Shelly(pink)\n")

names = ["Timmy", "Zippy", "Ralph", "Shelly", "Daisy"]
colours = ["green", "blue", "purple", "hot pink", "gold"]
y_pos = -100
x_pos = -230
index = 0
turtles = {}

for name in names:
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colours[index])
    index += 1
    new_turtle.goto(x=x_pos, y=y_pos)
    y_pos += 60
    turtles[name] = new_turtle

is_race_on = False

if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in turtles:
        turtles[turtle].forward(random.randint(0, 10))
        if turtles[turtle].xcor() > 230:
            winner = turtle
            is_race_on = False
            break
print(f"{winner} won the race!")

if user_bet.lower() == winner.lower():
    print("Congratulations! your bet is correct!")
else:
    print("Sorry, wrong bet")

screen.exitonclick()
