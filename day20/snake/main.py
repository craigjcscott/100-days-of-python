from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
MAX_X = WINDOW_WIDTH / 2 - 20
MAX_Y = WINDOW_HEIGHT / 2 - 20

screen = Screen()
screen.setup(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_running = True
while game_running:
    screen.update()
    time.sleep(snake.speed)
    snake.move()

    if food.distance(snake.head) < 1:
        scoreboard.add_score()
        food.move_food()
        snake.grow_snake()

    if snake.out_of_bounds(x_boundry=MAX_X, y_boundry=MAX_Y) or snake.head_touch_body() :
        game_running = False
        print("Game Over")
        scoreboard.game_over()

screen.exitonclick()
