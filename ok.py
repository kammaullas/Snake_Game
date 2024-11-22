from core import Snake
from turtle import Screen
import time
screen=Screen()
screen.setup(width=600,height=600)
screen.title("My snake Game")
screen.bgcolor("black")
screen.tracer(0)
snake = snake.Snake()
game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(1)
    snake.move()
screen.exitonclick()
