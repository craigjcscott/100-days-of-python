from turtle import Turtle

PLAYER1_X =
PLAYER1_Y =
PLAYER2_X =
PLAYER2_Y = 

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.player_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setposition()