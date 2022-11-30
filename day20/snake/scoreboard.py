from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.sety(270)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def add_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def game_over(self):
        self.sety(0)
        self.write("Game Over", align="center", font=("Arial", 24, "normal"))
