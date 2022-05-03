import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "black", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Transport(Turtle):
    def __init__(self):
        super().__init__()
        self.color(random.choice(COLORS))
        self.shape("square")
        # self.left(90)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        # self.random_pos()
        self.auto_move(self.random_pos())

    def random_pos(self):
        rand_pos = random.randint(-270, 270)
        return rand_pos

    def auto_move(self, pos):
        self.goto(pos)
        self.backward(STARTING_MOVE_DISTANCE)
