# Imports
from turtle import Screen
from ball import Ball
from blocks import Blocks
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Breakout')
screen.tracer(0)

paddle = Paddle()
ball = Ball()
blocks = Blocks()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle.go_right, 'Right')
screen.onkey(paddle.go_left, 'Left')

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()

    # Detect collision with side walls
    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.bounce_x()

    # Detect collision with top wall
    if ball.ycor() > 290:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(paddle) < 30 and ball.ycor() < -230:
        ball.bounce_y()

    # Detect collision with block
    if ball.ycor() > 30:
        for block in blocks.blocks:
            if ball.distance(block) < 30:
                ball.bounce_y()
                block.goto(1000, 1000)
                scoreboard.increase_score(block)

    # Detect miss
    if ball.ycor() < -290:
        ball.reset_position()
        paddle.reset_position()
        scoreboard.decrease_lives()

    # Detect game over
    if scoreboard.lives == 0:
        ball.stop()
        blocks.hide()
        scoreboard.game_over()


screen.exitonclick()
