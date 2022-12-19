from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
Y_LIM = 250
X_LIM = 300



class CarManager:
    def __init__(self):
        self.cars = []

    def create_car(self):
        new_car = Turtle()
        new_car.penup()
        new_car.shape("square")
        new_car.shapesize(stretch_len=2)
        new_car.color(random.choice(COLORS))
        new_car.setpos(random.randint(X_LIM, X_LIM * 4), random.randint(-Y_LIM, Y_LIM))
        new_car.setheading(180)
        self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.forward(MOVE_INCREMENT)

    def reset_cars(self):
        for car in self.cars:
            if car.xcor() < -X_LIM:
                car.setpos(random.randint(X_LIM, X_LIM * 2 - 100), random.randint(-Y_LIM, Y_LIM))
