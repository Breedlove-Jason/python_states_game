import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=725, height=491)

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()
guessed_states = []

data = pd.read_csv("50_states.csv")
states = data.state.to_list()
location_x = data.x.to_list()
location_y = data.y.to_list()

count = 0
game_is_on = True
while len(guessed_states) < 50 and game_is_on:
    answer_state = screen.textinput(title=f"Guessed {count}/50", prompt="What's another state's name?").title()

    if answer_state in states:
        guessed_states.append(answer_state)
        location_index = states.index(answer_state)
        location_x_axis = location_x[location_index]
        location_y_axis = location_y[location_index]
        t = turtle.Turtle()
        t.color("black")
        t.penup()
        t.hideturtle()
        t.goto(location_x_axis, location_y_axis)
        t.write(answer_state, align="center", font=("Arial", 10, "normal"))
        count += 1
    else:
        if answer_state == "Exit":
            game_is_on = False
        else:
            print("Try again.")


screen.exitonclick()
