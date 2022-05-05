from turtle import Screen
from player import Player
from transports import Transport
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
transports = Transport()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(player.Up, "Up")
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    transports.create_car()
    transports.auto_move()

    # Detect if the player reaches the top side
    if player.finish_line_reached():
        player.goto_start()
        transports.level_up()

#     Detect collision with transport
    for cars in transports.all_cars:
        if cars.distance(player) < 20:
            game_is_on = False

screen.exitonclick()
