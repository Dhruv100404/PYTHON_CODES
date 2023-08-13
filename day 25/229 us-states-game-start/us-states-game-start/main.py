import turtle
import pandas

s = turtle.Screen()
s.title("US game state")
data = pandas.read_csv("50_states.csv")
image = "blank_states_img.gif"
s.addshape(image)
turtle.shape(image)
all_states = data.state.to_list()
guessed = []

while len(guessed) < 50:
    answer = s.textinput(title=f"{len(guessed)} /50 states correct ", prompt="What's the another state name? ").title()

    if answer == "Exit":
        break
    if answer in all_states:

        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer]

        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer)


s.exitonclick()
