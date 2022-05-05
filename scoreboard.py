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
        self.write(f"Level: {self.level}", align="Left", font=FONT)

    def upgrade_level(self):
        self.level += 1