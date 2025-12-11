from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Comic Sans MS", 24, "normal")

with open("high_score.txt", "r") as file:
    highest_score = int(file.read())

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = int(highest_score)
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("high_score.txt", "w") as file:
                file.write(str(self.highscore))
        self.score = 0
        self.update_scoreboard()


    def increase(self):
        self.score += 1
        self.update_scoreboard()