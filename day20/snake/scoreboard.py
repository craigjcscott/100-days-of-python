from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt") as file:
            high_score = file.read()
            self.high_score = high_score
        self.color("white")
        self.hideturtle()
        self.penup()
        self.sety(270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))

    def add_score(self):
        self.score += 1
        self.update_score()

    def reset_game(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open("high_score.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.sety(0)
    #     self.write("Game Over", align="center", font=("Arial", 24, "normal"))
