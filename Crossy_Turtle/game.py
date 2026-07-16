from turtle import Screen
from player import Player
from cars import CarManage
from scoreboard import Scoreboard
import time

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

MOVE_DELAY = 0.1
PLAYER_COLLISION_DISTANCE = 20

screen = Screen()
screen.title("Crossy Turtle")
screen.colormode(255)
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)

player = Player()
car_manage = CarManage()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")

game_on = True
while game_on:
    screen.update()
    time.sleep(MOVE_DELAY)

    car_manage.create_car()
    car_manage.move_cars()

    # Hit car - GAME OVER
    for car in car_manage.cars:
        if car.distance(player) < PLAYER_COLLISION_DISTANCE:
            game_on = False
            scoreboard.game_over()

    # Player reached the finish line
    if player.at_finish():
        player.go_start()
        car_manage.level_up()
        scoreboard.increase_level()

screen.exitonclick()
