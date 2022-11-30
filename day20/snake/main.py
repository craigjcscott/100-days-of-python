from turtle import Screen
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()

while abs(snake.snake_body[0].xcor()) <= 280 and abs(snake.snake_body[0].ycor()) <= 280:
    screen.listen()
    screen.onkey(key="Up", fun=snake.up)
    screen.onkey(key="Down", fun=snake.down)
    screen.onkey(key="Left", fun=snake.left)
    screen.onkey(key="Right", fun=snake.right)

    screen.update()
    time.sleep(snake.speed)
    snake.move()

    if (round(snake.snake_body[0].xcor()) == food.xcor) and (round(snake.snake_body[0].ycor()) == food.ycor):
        print('hello')

screen.exitonclick()
