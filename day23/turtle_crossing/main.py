import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

GAME_SPEED = 0.1
car_trigger = 0

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

for _ in range(30):
    car_manager.create_car()

screen.listen()
screen.onkey(key="Up", fun=player.move)

game_is_on = True
while game_is_on:
    time.sleep(GAME_SPEED)
    screen.update()
    car_manager.move_cars()
    car_manager.reset_cars()

    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.at_finish_line():
        player.next_level()
        scoreboard.level_up()
        GAME_SPEED -= 0.01

screen.exitonclick()
