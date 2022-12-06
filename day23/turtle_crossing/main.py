import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

car_manager.create_car()

screen.listen()
screen.onkey(key="Up", fun=player.move)

game_is_on = True
while game_is_on:
    time.sleep(0.25)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    car_manager.delete_cars()

    if player.ycor() >= 280:
        player.reset()
        scoreboard.next_level()
