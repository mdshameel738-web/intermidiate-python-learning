from turtle import Turtle,Screen

tom=Turtle()
screen=Screen()

def movef():
    tom.forward(100)


screen.listen()
screen.onkey(key="a",fun=movef)

screen.exitonclick()