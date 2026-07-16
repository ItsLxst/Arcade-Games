from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

WALL_LIMIT = 280
PADDLE_COLLISION_DISTANCE = 50
PADDLE_COLLISION_X = 320
BALL_OUT_X = 380

screen = Screen()
screen.bgcolor("black")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)
screen.title("Pong Game")

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(right_paddle.go_up, "Up")
screen.onkeypress(right_paddle.go_down, "Down")
screen.onkeypress(left_paddle.go_up, "w")
screen.onkeypress(left_paddle.go_down, "s")

game_on = True
while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Wall collision + bounce
    if ball.ycor() > WALL_LIMIT or ball.ycor() < -WALL_LIMIT:
        ball.y_bounce()

    # Paddle collision + bounce
    if (
        ball.distance(right_paddle) < PADDLE_COLLISION_DISTANCE
        and ball.xcor() > PADDLE_COLLISION_X
    ) or (
        ball.distance(left_paddle) < PADDLE_COLLISION_DISTANCE
        and ball.xcor() < -PADDLE_COLLISION_X
    ):
        ball.x_bounce()

    # Right paddle miss + score update
    if ball.xcor() > BALL_OUT_X:
        ball.reset_pos()
        scoreboard.l_point()

    # Left paddle miss + score update
    if ball.xcor() < -BALL_OUT_X:
        ball.reset_pos()
        scoreboard.r_point()

screen.exitonclick()
