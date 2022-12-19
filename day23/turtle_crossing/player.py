from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("red", "green")
        self.setposition(STARTING_POSITION)
        self.setheading(90)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def at_finish_line(self):
        if self.ycor() >= 280:
            return True
        else:
            return False

    def next_level(self):
        self.setposition(STARTING_POSITION)
