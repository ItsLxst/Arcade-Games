from turtle import Turtle, Screen
from player import Player
from cars import CarManage
from scoreboard import Scoreboard
import time

screen = Screen()
screen.title("Crossy Turtle")
screen.colormode(255)
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manage = CarManage()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    car_manage.create_car()
    car_manage.move_cars()
    
    # Hit car GAME END
    for car in car_manage.cars:
        if car.distance(player) < 20:
            game_on = False
            scoreboard.game_over()
    
    # Player managed to cross
    if player.at_finish():
        player.go_start()
        car_manage.level_up()
        scoreboard.increase_level()
        
screen.exitonclick()