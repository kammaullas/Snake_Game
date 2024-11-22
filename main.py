from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard
scoreboard=Scoreboard()
screen = Screen()
screen.listen()
screen.setup(width=600,height=600)
screen.title("My snake Game")
screen.bgcolor("white")
screen.tracer(0)
snake = Snake()
food = Food()
game_is_on = True
screen.onkey(snake.left, "Left")
screen.onkey(snake.up, "x")
screen.onkey(snake.dn, "d")
screen.onkey(snake.right, "Right")
while game_is_on:
    time.sleep(0.1)
    snake.move()
    screen.update()
    if snake.head.distance(food)<15 :
        food.refresh()
        snake.extend()
        scoreboard.increse_score()
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280 :
        scoreboard.reset_score()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            game_is_on=False
            scoreboard.reset_score()
screen.exitonclick()

