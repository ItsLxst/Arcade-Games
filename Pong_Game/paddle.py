from turtle import Turtle

class Paddle(Turtle):

    def __init__(self,coordinat):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(coordinat)

    def go_up(self):
        y_cor = self.ycor()
        self.goto(self.xcor(), y_cor + 20)

    def go_down(self):
        y_cor = self.ycor()
        self.goto(self.xcor(), y_cor - 20)