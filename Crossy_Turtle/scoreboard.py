from turtle import Turtle

FONT = ("Comic Sans MS", 24, "normal")
ALIGNMENT = "left"

LEVEL_POSITION = (-280, 260)
GAME_OVER_POSITION = (0, 0)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(LEVEL_POSITION)

        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(LEVEL_POSITION)
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(GAME_OVER_POSITION)
        self.write("GAME OVER!", align="center", font=FONT)
