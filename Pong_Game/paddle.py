from turtle import Turtle

MOVE_DISTANCE = 20


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def go_up(self):
        y_cor = self.ycor()
        self.goto(self.xcor(), y_cor + MOVE_DISTANCE)

    def go_down(self):
        y_cor = self.ycor()
        self.goto(self.xcor(), y_cor - MOVE_DISTANCE)
