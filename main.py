from turtle import Screen
from player import Player
from transports import Transport
import time

screen = Screen()
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
transports = Transport()

screen.listen()
screen.onkey(player.Up, "Up")
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    transports.create_car()
    transports.auto_move()
    if player.ycor() > 270:
        player.reset_position()

screen.exitonclick()
