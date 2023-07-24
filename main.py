# main.py
import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball   import Ball
from scoreboard import Scoreboard


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()



screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)

    if 330 > ball.xcor() > 320 and (r_paddle.ycor() + 50 > ball.ycor() > r_paddle.ycor() - 50):
        ball.bounce_x()
    elif -330 < ball.xcor() < -320 and (l_paddle.ycor() + 50 > ball.ycor() > l_paddle.ycor() - 50):
        ball.bounce_x()

    if ball.xcor() > 380:  # piłka minęła prawą paletkę
        ball.reset_position()
        scoreboard.l_point()
    elif ball.xcor() < -380:  # piłka minęła lewą paletkę
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
