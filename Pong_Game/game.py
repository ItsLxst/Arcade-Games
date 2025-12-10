from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
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
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    # Paddle collision + bounce
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.x_bounce()

    # Right paddle miss + Game reset
    if ball.xcor() > 380:
        ball.reset_pos()
        scoreboard.l_point()

    # Left paddle miss + Game reset
    if ball.xcor() < -380:
        ball.reset_pos()
        scoreboard.r_point()

screen.exitonclick()