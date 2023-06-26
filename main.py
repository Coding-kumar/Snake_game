from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scorecard

snake = Snake()
food = Food()
scoring = Scorecard()
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    # snake eating food and extending
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_segment()
        scoring.increse_score()

    # snake head hitting on walls

    if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        game_on = False
        scoring.game_over()

    # Snake biting itself

    for segmen in snake.segments[1:]:
        if snake.head.distance(segmen) < 10:
            game_on = False
            scoring.game_over()

screen.exitonclick()
