import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=725, height=491)

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()
guessed_states = []

data = pd.read_csv("50_states.csv")
states = data.state.to_list()

location_x = data.x.to_list()
location_y = data.y.to_list()

if answer_state in states:
    location_index = states.index(answer_state)
    location_x_axis = location_x[location_index]
    location_y_axis = location_y[location_index]
    guessed_states.append(answer_state)
    print(f"Guessed {guessed_states}")
    print(f"Location: {location_x_axis}, {location_y_axis}")
    t = turtle.Turtle()
    t.color("black")
    t.penup()
    t.hideturtle()
    t.goto(location_x_axis, location_y_axis)
    t.write(answer_state, align="center", font=("Arial", 10, "normal"))


screen.exitonclick()

