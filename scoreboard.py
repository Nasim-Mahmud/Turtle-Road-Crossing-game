from turtle import Turtle

FONT = ("Courier", 16, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.ht()
        self.penup()
        self.goto(-280, 270)
        self.write(f"Level: {self.level}", align="Left", font=FONT)
