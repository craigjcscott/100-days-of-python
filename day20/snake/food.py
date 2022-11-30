from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")
        self.penup()
        random_x = random.choice(range(-260, 260, 20))
        random_y = random.choice(range(-260, 260, 20))
        self.setposition(random_x, random_y)

    def move_food(self):
        new_random_x = random.choice(range(-260, 260, 20))
        new_random_y = random.choice(range(-260, 260, 20))
        self.setposition(new_random_x, new_random_y)
