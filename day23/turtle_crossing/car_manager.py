from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
SCREEN_Y = 600
LANES = range(round(SCREEN_Y / 20 - 2))
SCREEN_X = 600


class CarManager():
    def __init__(self):
        self.n_cars = 1
        self.cars = []

    def create_car(self):
        new_car = Turtle()
        new_car.penup()
        new_car.shape("square")
        new_car.shapesize(stretch_len=2)
        new_car.color(random.choice(COLORS))
        new_car.setposition(300, random.randint(-280,280))
        new_car.setheading(180)
        self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.forward(MOVE_INCREMENT)

    def delete_cars(self):
        for car in self.cars:
            if car.xcor() < -300:
                car.clear()
