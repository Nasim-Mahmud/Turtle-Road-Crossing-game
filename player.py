from turtle import Turtle

START_POS = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.left(90)
        self.goto_start()

    def Up(self):  # Setting up the key
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def reset_position(self):
        self.setposition(START_POS)

    def goto_start(self):
        self.goto(START_POS)

    def finish_line_reached(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False