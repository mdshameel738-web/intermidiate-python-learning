import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player=Player()
car=CarManager()
scoreborad=Scoreboard()


screen.listen()
screen.onkey(player.move,"Up")






game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_cars()   

    #detect the colllision 
    for cars in car.all_cars:
        if cars.distance(player) < 20:
            game_is_on=False
            scoreborad.game_over()

    if player.is_at_finish_line():
        player.over()
        car.level_up()
        scoreborad.increse_level()


screen.exitonclick()