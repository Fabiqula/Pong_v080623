from turtle import Screen
from paddle import Paddle
from field import Field
from ball import Ball
from scoreboard import Scoreboard

import time





screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=800)
screen.title("Pong game")
screen.tracer(0)

r_paddle = Paddle((380, 0))
l_paddle = Paddle((-385, 0))

upper_line = Field((0, 295), 0.1, 40)
lower_line = Field((0, -295), 0.1, 40)
middle_line = Field((0, 0), 29.2, 0.001)

ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.reset_position()

    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_wall()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 355:
        ball.bounce_paddle()
        ball.speed_up()

    if ball.distance(l_paddle) < 50 and ball.xcor() < -360:
        ball.bounce_paddle()
        ball.speed_up()

    if ball.xcor() > 385:
        score.left_scores()


    if ball.xcor() < - 385:
        score.right_scores()


    if r_paddle.ycor() == 240:
        r_paddle.stop_up()

    if r_paddle.ycor() == -240:
        r_paddle.stop_down()

    if l_paddle.ycor() == 240:
        l_paddle.stop_up()

    if l_paddle.ycor() == -240:
        l_paddle.stop_down()


screen.exitonclick()
