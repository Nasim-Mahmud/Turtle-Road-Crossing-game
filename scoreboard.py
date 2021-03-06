from turtle import Turtle

FONT = ("Courier", 16, "bold")
LEVEL = 1


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = LEVEL
        self.ht()
        self.penup()
        self.goto(-280, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="Left", font=FONT)

    def level_up(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align="center", font=FONT)
