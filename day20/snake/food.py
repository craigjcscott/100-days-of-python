from turtle import Turtle
import random

class Food:
    def __init__(self):
        self.xcor = 0
        self.ycor = 0
        self.create_food()

    def create_food(self):
        self.xcor = random.choice(range(-280, 280, 20))
        self.ycor = random.choice(range(-280, 280, 20))
        new_food = Turtle()
        new_food.penup()
        new_food.color("green")
        new_food.shape("circle")
        new_food.setposition(self.xcor, self.ycor)
