import turtle
import pandas

screen = turtle.Screen()
screen.title("US State Guess")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States", prompt="Guess a state:").title()
    if answer_state == "Exit":
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(data[data.state == answer_state].x), int(data[data.state == answer_state].y))
        t.write(answer_state)

states_to_learn = [state for state in all_states if state not in guessed_states]
new_data = pandas.DataFrame(states_to_learn)
new_data.to_csv("states_to_learn.csv")
