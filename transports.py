import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "black", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Transport(Turtle):
    def __init__(self):
        all_cars = []

    def create_cars(self):
        new_car = Turtle("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.color(random.choice(COLORS))
        random_y = random.randint(-250, 250)
