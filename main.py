from turtle import Screen
from player import Player
from transports import Transport
import time

screen = Screen()
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()


screen.listen()
screen.onkey(player.Up, "Up")
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    transports1 = Transport()
    transports1.auto_move()
    transports2 = Transport()
    transports2.auto_move()
    screen.update()

screen.exitonclick()
