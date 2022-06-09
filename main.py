import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S State Game Quizz")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(f"{len(guessed_states)}/50 States Correct", "What's another state name ?").title()
    if answer_state == 'Exit':
        missing_states = list(set(all_states) - set(guessed_states))
        states_not_guessed = pandas.DataFrame(missing_states, columns=['States'])
        states_not_guessed.to_csv('states_not_guessed.csv')
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        is_there = data[data['state'] == answer_state]
        t.goto(int(is_there.x), int(is_there.y))
        t.write(answer_state)
