import turtle
import pandas as pd


screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states = pd.read_csv("50_states.csv")
state_names = states.state.to_list()


def write_state(state_name, x, y):
    new_turtle = turtle.Turtle()
    new_turtle.hideturtle()
    new_turtle.penup()
    new_turtle.hideturtle()
    new_turtle.setposition(x, y)
    new_turtle.write(state_name, align='left', font=("Arial", 12, "normal"))


prior_guesses = []
correct_guesses = 0
while correct_guesses < 50:
    answer_state = screen.textinput(title=f"{correct_guesses}/50 guessed", prompt="Name a state!")
    answer_state = answer_state.title()

    if answer_state == "quit":
        game_running = False
        break
    elif answer_state in prior_guesses:
        print("Already guessed, please try again")
        continue
    elif answer_state in state_names:
        state_data = states[states.state == answer_state]
        state_x_cor = int(state_data.x)
        state_y_cor = int(state_data.y)
        write_state(answer_state, state_x_cor, state_y_cor)
        prior_guesses.append(answer_state)
        correct_guesses += 1
    else:
        prior_guesses.append(answer_state)


turtle.mainloop()  # use instead of screen.exitonclick since we need to click on the screen
