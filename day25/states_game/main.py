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
correct_guesses = []
while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 guessed", prompt="Name a state!")
    answer_state = answer_state.title()

    if answer_state == "Quit":
        game_running = False
        states_to_learn = [state for state in state_names if state not in correct_guesses]
        states_to_learn_df = pd.DataFrame(states_to_learn)
        states_to_learn_df.to_csv("states_to_learn.csv")
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
        correct_guesses.append(answer_state)
    else:
        prior_guesses.append(answer_state)




turtle.mainloop()  # use instead of screen.exitonclick since we need to click on the screen
