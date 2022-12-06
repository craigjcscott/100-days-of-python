from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.move_x = 10
        self.move_y = 10

    def move(self):
        self.goto(self.xcor() + self.move_x, self.ycor() + self.move_y)

    def bounce_wall(self):
        self.move_y *= -1

    def score_goal(self, goal_line):
        if 0 < goal_line < round(self.xcor()):
            return True
        elif round(self.xcor() < goal_line < 0):
            return True

    def bounce_paddle(self):
        self.move_x *= -1
        self.move_x *= 1.1
        self.move_y *= 1.1

    def reset(self):
        self.setposition(0, 0)
        random_x = random.choice([-1,1])
        random_y = random.choice([-1,1])
        self.move_x = 10 * random_x
        self.move_y = 10 * random_y
