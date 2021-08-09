import time

from pong_field import PongField
from paddle import Paddle
from score import ScoreBoard
from ball import Ball

field = PongField().get_field()

score_board = ScoreBoard((-100, 180), (100, 180))
ball = Ball()

right_paddle = Paddle((350, 0))
field.onkeypress(right_paddle.move_up, "Up")
field.onkeypress(right_paddle.move_down, "Down")

left_paddle = Paddle((-350, 0))
field.onkeypress(left_paddle.move_up, "w")
field.onkeypress(left_paddle.move_down, "s")


game_is_on = True
while game_is_on:
    field.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 400:
        ball.reset_position()
        score_board.increase_right_board()

    if ball.xcor() < -400:
        ball.reset_position()
        score_board.increase_left_board()

    time.sleep(0.1)
field.exitonclick()

