from turtle import Turtle,Screen

tim=Turtle()
screen=Screen()
tim.pensize(3)

def movef():
    tim.forward(5)
def moveb():
    tim.backward(5)
def turnl():
    tim.left(5)
def turnr():
    tim.right(5)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
screen.listen()
screen.onkey(key="w",fun=movef)
screen.onkey(key="s",fun=moveb)
screen.onkey(key="a",fun=turnl)
screen.onkey(key="d",fun=turnr)
screen.onkey(key="c",fun=clear)
screen.exitonclick()