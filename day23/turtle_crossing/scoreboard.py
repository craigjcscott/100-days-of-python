from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.setposition(-275, 250)
        self.write(f"Level: {self.level}", align='left', font=FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align='left', font=FONT)

    def game_over(self):
        self.setposition(0,0)
        self.write("GAME OVER", align='center', font=FONT)