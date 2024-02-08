from Snake import Snake
from turtle import Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0) # Tracer is off

out_of_bounds = (300 , -300)

# Create snake body

snake = Snake()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.left, "a")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")


#update the screen
screen.update()

# Movement of the snake
game_is_on = True
prev_x = 0
prev_y = 0
count = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    game_is_on = snake.move()



screen.exitonclick()
