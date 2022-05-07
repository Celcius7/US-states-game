import turtle
import pandas as pd
screen = turtle.Screen()
image = "blank_states_img.gif"
screen.title("U.S. states Game")
screen.addshape(image)
turtle.shape(image)


# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
#
state_guessed = []
data = pd.read_csv("50_states.csv")
all_states = data['state'].to_list()
while(len(state_guessed)<51):
    answer_state = screen.textinput(title = f"{len(state_guessed)}/50 state guessed", prompt="What's another state's name? ").title()

    if answer_state == 'Exit':
        break

    if answer_state in all_states:
        state_guessed.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()

        state_data = data[data.state == answer_state]
        x = int(state_data.x)
        y = int(state_data.y)

        t.goto(x,y)
        t.write(answer_state)

missed_state = []
for item in data['state'].to_list():
    if item not in state_guessed:
        missed_state.append(item)

new_data = pd.DataFrame(missed_state)
missed_state.to_csv("states_missed.csv")