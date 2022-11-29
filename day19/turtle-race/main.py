from turtle import Turtle, Screen
import random

screen = Screen()
track_length = 750
screen.setup(width=track_length, height=350)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
lane_positions = list(range(-125, 175, 50))
turtles_list = []

for i in range(6):
    turtle = Turtle()
    # turtle.speed("fastest")
    turtle.penup()
    turtle.shape("turtle")
    turtle.color("black", colors[i])
    turtle.goto(-1 * (track_length / 2) + 20, lane_positions[i])
    turtles_list.append(turtle)

player_choice = screen.textinput("Choose a turtle to back:", "'red', 'orange', 'yellow', 'green', 'blue', or 'purple' ")

race_in_progress = True
while race_in_progress:
    for turtle in turtles_list:
        turtle.forward(random.randint(1, 25))
        if turtle.xcor() >= (track_length / 2 - 19):
            race_in_progress = False
            print(f"The race is over. The {turtle.fillcolor()} turtle wins!")
            if turtle.fillcolor() == player_choice:
                print("You win! Congratulations.")
            else:
                print("Sorry, you lose! Better luck next time.")
            break


screen.exitonclick()
