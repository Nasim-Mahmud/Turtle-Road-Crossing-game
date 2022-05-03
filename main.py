from turtle import Screen
from player import Player
from transports import Transport
import time

screen = Screen()
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
transports1 = Transport()
transports2 = Transport()

screen.listen()
screen.onkey(player.Up, "Up")
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    if transports1.xcor() < 250 or transports2.xcor() < 250:
        transports1 = Transport()
        transports2 = Transport()

    transports1.auto_move()
    transports2.auto_move()
    screen.update()

screen.exitonclick()
