""" TODO: create screen
    TODO: create and move paddle
    TODO: create another paddle
    TODO: create the ball and make it move
    TODO: detect collision with wall and bounce
    TODO: detect collision with paddle
    TODO: detect when paddle misses
    TODO: keep score
    """
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.title("Pong")
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
# Track key states
keys = {"Up": False, "Down": False, "w": False, "s": False}

def key_down(key):
    keys[key] = True

def key_up(key):
    keys[key] = False

# Bind key press/release
for key in keys.keys():
    screen.onkeypress(lambda k=key: key_down(k), key)
    screen.onkeyrelease(lambda k=key: key_up(k), key)

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Continuous paddle movement
    if keys["Up"]:
        r_paddle.go_up()
    if keys["Down"]:
        r_paddle.go_down()
    if keys["w"]:
        l_paddle.go_up()
    if keys["s"]:
        l_paddle.go_down()

    #detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #detect if ball out of bounds r-side
    if ball.xcor() > 380:
        ball.reset_position()
        ball.move()
        scoreboard.l_point()

    #detect if ball out of bounds l-side
    if ball.xcor() < -380:
        ball.reset_position()
        ball.move()
        scoreboard.r_point()


screen.exitonclick()