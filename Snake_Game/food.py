from turtle import Turtle
import random

FOOD_BOUNDARY = 280

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("cornflowerblue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-FOOD_BOUNDARY, FOOD_BOUNDARY)
        random_y = random.randint(-FOOD_BOUNDARY, FOOD_BOUNDARY)
        self.goto(random_x, random_y)
