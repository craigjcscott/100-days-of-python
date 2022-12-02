from turtle import Turtle

PLAYER1_X = -50
PLAYER2_X = 50


class Scoreboard(Turtle):

    def __init__(self, player):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.player = player
        if self.player == 1:
            self.setposition(PLAYER1_X, 250)
        else:
            self.setposition(PLAYER2_X, 250)
        self.write(self.score, align="center", font=("Arial", 24, "normal"))

    def goal_scored(self):
        self.clear()
        self.score += 1
        self.write(self.score, align="center", font=("Arial", 24, "normal"))

