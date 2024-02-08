import turtle as t
from turtle import Turtle
import time

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake:
    def __init__(self):
        self.length = 3
        self.y_pos = 0
        self.x_pos = 0
        self.prev_y = 0
        self.prev_x = 0
        self.snake = []
        for _ in range(self.length):
            segment = Turtle(shape="square")
            segment.color("white")
            segment.penup()
            segment.goto(self.x_pos, self.y_pos)
            self.x_pos -= 20
            self.snake.append(segment)

    def move(self):
        self.prev_y = 0
        self.prev_x = 0
        for index, segment in enumerate(self.snake):
            if index == 0:
                self.prev_y = segment.ycor()
                self.prev_x = segment.xcor()
                segment.forward(MOVE_DISTANCE)
            else:
                temp_y = segment.ycor()
                temp_x = segment.xcor()
                segment.goto(self.prev_x, self.prev_y)
                self.prev_y = temp_y
                self.prev_x = temp_x
            if segment.xcor() == 300 or segment.xcor() == -300 or segment.ycor() == 300 or segment.ycor() == -300:
                return False
        return True

    def up(self):
        if self.snake[0].setheading() != DOWN:
            self.snake[0].setheading(UP)

    def left(self):
        if self.snake[0].setheading() != RIGHT:
            self.snake[0].setheading(LEFT)

    def right(self):
        if self.snake[0].setheading() != LEFT:
            self.snake[0].setheading(RIGHT)

    def down(self):
        if self.snake[0].setheading() != UP:
            self.snake[0].setheading(DOWN)

