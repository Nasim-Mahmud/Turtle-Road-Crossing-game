import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "black", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Transport(Turtle):
    def __init__(self):
        super().__init__()
        self.spawn()

    def random_pos(self):
        self.goto(random.randint(270, 350), random.randint(-250, 260))

    # def auto_move(self):
    #     self.backward(STARTING_MOVE_DISTANCE)

    def spawn(self):
        self.color(random.choice(COLORS))
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.random_pos()
        self.backward(STARTING_MOVE_DISTANCE)
