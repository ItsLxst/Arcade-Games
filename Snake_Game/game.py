from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

MOVE_DELAY = 0.1
WALL_LIMIT = 280
FOOD_COLLISION_DISTANCE = 15
TAIL_COLLISION_DISTANCE = 10

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(MOVE_DELAY)
    snake.move()

    head = snake.head

    # Eat food
    if head.distance(food) < FOOD_COLLISION_DISTANCE:
        food.refresh()
        snake.extend()
        scoreboard.increase()

    # Hit wall - GAME END
    if (
        head.xcor() > WALL_LIMIT
        or head.xcor() < -WALL_LIMIT
        or head.ycor() > WALL_LIMIT
        or head.ycor() < -WALL_LIMIT
    ):
        scoreboard.reset()
        snake.reset_snake()

    # Hit tail - GAME END
    for body in snake.snake_body[1:]:
        if head.distance(body) < TAIL_COLLISION_DISTANCE:
            scoreboard.reset()
            snake.reset_snake()

screen.exitonclick()
