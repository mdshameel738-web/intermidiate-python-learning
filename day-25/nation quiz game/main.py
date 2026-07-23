import turtle 
import turtle
import os
import sys
import pandas
from pathlib import Path

file_path = Path(__file__).resolve().parent / "states_data.csv"
data = pandas.read_csv(file_path)
FONT = ("Courier", 20, "normal")
screen=turtle.Screen()
all_states = data.state.to_list()


screen = turtle.Screen()
screen.title("India State Game")
image = "India-state.gif"

# make image path absolute, based on this script's location
script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, image)
screen.addshape(image_path)
turtle.shape(image_path)
guessed_states= []


while len(guessed_states) <50:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="what's another state's name?").title()
    if answer_state == "Exit":
        missed_states= []
        for missed_state in all_states:
            if missed_state not in guessed_states:
                missed_states.append(missed_state)
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_row=data[data.state == answer_state]
        x_cor=state_row.x.item()
        y_cor=state_row.y.item()
        t.goto(x_cor,y_cor)
        t.write(answer_state)



df=pandas.DataFrame(missed_states)
df.to_csv("States_name_to_learn.csv")




  




screen.exitonclick()











