import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()

keys = {"Up": False, "Left": False, "Right": False}

def key_down(key):
    keys[key] = True

def key_up(key):
    keys[key] = False

for key in keys.keys():
    screen.onkeypress(lambda k = key:key_down(k), key)
    screen.onkeyrelease(lambda k = key:key_up(k), key)


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if keys["Up"]:
        player.go_up()

    if keys["Left"]:
        player.go_left()

    if keys["Right"]:
        player.go_right()

    cars.create_car()
    cars.move_cars()

    #Detect collision of player to car
    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    #Detect success in crossing
    if player.is_at_finish():
        player.go_to_start()
        cars.level_up()
        scoreboard.next_level()

screen.exitonclick()
