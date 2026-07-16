from turtle import Turtle

INITIAL_MOVE_DISTANCE = 10
INITIAL_MOVE_SPEED = 0.1


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = INITIAL_MOVE_DISTANCE
        self.y_move = INITIAL_MOVE_DISTANCE
        self.move_speed = INITIAL_MOVE_SPEED

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def y_bounce(self):
        self.y_move *= -1
        self.move_speed *= 0.9

    def x_bounce(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_pos(self):
        self.goto(0, 0)
        self.move_speed = INITIAL_MOVE_SPEED
        self.x_bounce()
