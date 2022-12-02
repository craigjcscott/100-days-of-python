from turtle import Turtle

P1_PADDLE_START = -360
P2_PADDLE_START = 350
MOVEMENT_DISTANCE = 20


class Paddle(Turtle):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=5)
        self.color("white")
        self.setheading(90)
        if self.player == 1:
            self.setx(P1_PADDLE_START)
        else:
            self.setx(P2_PADDLE_START)
        self.top = self.ycor() + 40
        self.bottom = self.ycor() - 40


    def up(self):
        self.forward(MOVEMENT_DISTANCE)

    def down(self):
        self.backward(MOVEMENT_DISTANCE)
