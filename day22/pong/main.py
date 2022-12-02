from turtle import Screen
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
import time

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
TOP_RIGHT_CORNER = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)

screen = Screen()
screen.setup(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

p1_scoreboard = Scoreboard(player=1)
p2_scoreboard = Scoreboard(player=2)

p1_paddle = Paddle(player=1)
p2_paddle = Paddle(player=2)

ball = Ball()
ball.setheading(ball.towards(TOP_RIGHT_CORNER))

screen.listen()
screen.onkey(key="w", fun=p1_paddle.up)
screen.onkey(key="s", fun=p1_paddle.down)
screen.onkey(key="Up", fun=p2_paddle.up)
screen.onkey(key="Down", fun=p2_paddle.down)


game_running = True
while game_running:
    screen.update()
    time.sleep(.10)
    ball.move()

    if ball.distance(p2_paddle.pos()) < 20 or ball.distance(p1_paddle.pos()) < 20:
        ball.bounce_paddle()

    elif abs(ball.ycor()) >= 300:
        ball.bounce_wall()

    elif ball.out_of_bounds(WINDOW_WIDTH / 2):
        game_running = False





screen.exitonclick()