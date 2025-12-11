from turtle import Turtle

STARTING_POS = (0,-280)
MOVE = 10
FINISH_Y = 280

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POS)
        self.right(90) # Not a bug, it's a feature 🥲

    def up(self):
        self.goto(self.xcor(), self.ycor() + MOVE)

    def at_finish_line(self):
        if self.ycor() > FINISH_Y:
            return True
        else:
            return False

    def go_start(self):
        self.goto(STARTING_POS)