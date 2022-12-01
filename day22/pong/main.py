from turtle import Turtle, Screen

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 400

screen = Screen()
screen.setup(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

scoreboard = Scoreboard()

screen.exitonclick()