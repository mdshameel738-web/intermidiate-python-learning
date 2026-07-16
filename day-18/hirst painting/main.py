import random
from turtle import Screen, Turtle


def draw_hirst_painting(rows=10, cols=10, dot_size=20, spacing=50):
    screen = Screen()
    screen.setup(width=900, height=900)
    screen.bgcolor("white")
    screen.colormode(255)

    painter = Turtle()
    painter.hideturtle()
    painter.speed("fastest")
    painter.penup()

    palette = [
        (202, 164, 110),
        (240, 245, 241),
        (149, 90, 43),
        (231, 238, 236),
        (59, 89, 128),
        (136, 176, 194),
        (141, 96, 53),
        (220, 210, 113),
        (135, 27, 50),
        (66, 107, 64),
        (161, 87, 88),
        (232, 215, 88),
    ]

    start_x = -((cols - 1) * spacing) / 2
    start_y = -((rows - 1) * spacing) / 2

    for row in range(rows):
        for col in range(cols):
            painter.goto(start_x + col * spacing, start_y + row * spacing)
            painter.dot(dot_size, random.choice(palette))

    screen.exitonclick()


if __name__ == "__main__":
    draw_hirst_painting()
