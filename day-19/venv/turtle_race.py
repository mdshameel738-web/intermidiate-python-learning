from turtle import Turtle,Screen
import random


screen=Screen()
screen.setup(width=500,height=400)
screen.bgcolor("lightgreen")
user_bet=screen.textinput(title="Make your bet", prompt="Which color will win the race? Enter a color: ")

colors=["red","orange","yellow","green","blue","purple"]

y=[-70,-38,-6,26,58,90]

turtle_list=[]

turtle_speed=6

for i in range(6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230,y=y[i])
    turtle_list.append(new_turtle)

is_race=False

if user_bet:
    is_race=True

while is_race:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            is_race=False
            winning_color=turtle.pencolor()
            if winning_color==user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        random_distance=random.randint(0,10)
        turtle.forward(random_distance)

def reset_race():
    for turtle in turtle_list:
        turtle.goto(x=-230,y=turtle.ycor())
    user_bet=screen.textinput(title="Make your bet", prompt="Which color will win the race? Enter a color: ")
    is_race=False
    if user_bet:
        is_race=True
    while is_race:
        for turtle in turtle_list:
            if turtle.xcor() > 230:
                is_race=False
                winning_color=turtle.pencolor()
                if winning_color==user_bet:
                    print(f"You've won! The {winning_color} turtle is the winner!")
                else:
                    print(f"You've lost! The {winning_color} turtle is the winner!")
            random_distance=random.randint(0,10)
            turtle.forward(random_distance)

screen.listen()
screen.onkey(key="r",fun=reset_race)

screen.exitonclick()