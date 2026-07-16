from turtle import Turtle
import random

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

START_X = 300
MIN_Y = -250
MAX_Y = 250


class CarManage:

    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def random_color(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return (r, g, b)

    def create_car(self):
        rand_chance = random.randint(1, 6)

        if rand_chance == 1:
            car = Turtle(shape="square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(self.random_color())

            random_y = random.randint(MIN_Y, MAX_Y)
            car.goto(START_X, random_y)

            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
