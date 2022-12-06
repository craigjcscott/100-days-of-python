from turtle import Screen
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
import time

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
TOP_RIGHT_CORNER = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
BALL_SPEED = 0.05

screen = Screen()
screen.setup(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

p1_scoreboard = Scoreboard(player=1)
p2_scoreboard = Scoreboard(player=2)

p1_paddle = Paddle(player=1)
p2_paddle = Paddle(player=2)

screen.listen()
screen.onkey(key="w", fun=p1_paddle.up)
screen.onkey(key="s", fun=p1_paddle.down)
screen.onkey(key="Up", fun=p2_paddle.up)
screen.onkey(key="Down", fun=p2_paddle.down)

ball = Ball()


def play_game():

    game_running = True
    while game_running:
        screen.update()
        time.sleep(BALL_SPEED)
        ball.move()

        if ball.distance(p2_paddle.pos()) < 50 and abs(ball.xcor() > 330) \
                or ball.distance(p1_paddle.pos()) < 50 and abs(ball.xcor()) > 330:
            ball.bounce_paddle()

        if abs(ball.ycor()) >= 280:
            ball.bounce_wall()

        if ball.score_goal(WINDOW_WIDTH / 2):
            game_running = False
            p1_scoreboard.goal_scored()

        if ball.score_goal(-1 * WINDOW_WIDTH / 2):
            game_running = False
            p2_scoreboard.goal_scored()

        if not game_running:
            p1_paddle.reset_position(player=1)
            p2_paddle.reset_position(player=2)
            ball.reset()
            time.sleep(1)


match_running = True
while match_running:
    if p1_scoreboard.score > 4:
        match_running = False
        print("The winner is Player 1!")
    elif p2_scoreboard.score > 4:
        match_running = False
        print("The winner is Player 2!")
    else:
        play_game()



screen.exitonclick()