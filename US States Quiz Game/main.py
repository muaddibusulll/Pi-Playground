import turtle
import pandas
from state import State

IMAGE = "states_img.gif"

# ############ Our Graphical Properties ############

quiz_game_screen = turtle.Screen()
quiz_game_screen.title("U.S. Game Quiz")
# Add our image to the screen
quiz_game_screen.addshape(IMAGE)
# Make our turtle to have the "image shape"
turtle.shape(IMAGE)


# ############ End of Graphical Properties ############

def start_the_game_and_check_if_user_finds_the_state(score):
    correct_state = []
    while score < 50:

        user_answer = quiz_game_screen.textinput(title=f"Guess the State {score} / 50",
                                                 prompt="Enter the name of the state").title()

        if user_answer == "Exit":
            return correct_state
        if user_answer in states_data.state.unique():
            state = states_data[states_data.state == f"{user_answer}"]
            new_state = State(int(state["x"]), int(state["y"]), user_answer)
            score = score + 1
            correct_state.append(user_answer)


def complete_the_rest_of_the_map_and_returns_the_missing_states(user_found_states):
    missing_states = []
    for state in states_data.state.unique():
        if state not in user_found_states:
            not_found_state = states_data[states_data.state == f"{state}"]
            new_state = State(int(not_found_state["x"]), int(
                not_found_state["y"]), state)
            missing_states.append(state)
    return missing_states


def create_csv_file_with_missing_states(missing_states):
    new_data_with_missing_states = pandas.DataFrame(missing_states)
    new_data_with_missing_states.to_csv("missing_states.csv")


states_data = pandas.read_csv("50_states.csv")

score = 0

user_found_states = start_the_game_and_check_if_user_finds_the_state(
    score=score)

missing_states = complete_the_rest_of_the_map_and_returns_the_missing_states(
    user_found_states=user_found_states)

create_csv_file_with_missing_states(missing_states)

turtle.exitonclick()
