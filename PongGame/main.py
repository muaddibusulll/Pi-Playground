from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

RIGHT_PUDDLE_POSITION = [350, 0]
LEFT_PUDDLE_POSITION = [-350, 0]

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("PongGame")
screen.tracer(0)
screen.listen(0)

scoreboard = Scoreboard()

game_is_on = True

ball = Ball()


right_paddle = Paddle(RIGHT_PUDDLE_POSITION)
left_paddle = Paddle(LEFT_PUDDLE_POSITION)

screen.listen()

# Right puddle moving
screen.onkey(key="Up", fun=right_paddle.up)
screen.onkey(key="Down", fun=right_paddle.down)
# Left puddle moving
screen.onkey(key="w", fun=left_paddle.up)
screen.onkey(key="s", fun=left_paddle.down)


while game_is_on:

    screen.update()
    time.sleep(0.1)
    ball.ball_moving()

    # Ball detect collision with the up wall
    if (ball.ycor() > 280 or ball.ycor() < -280):
        ball.collision_with_wall()

    # Ball detect collision with the puddles
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or (ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        ball.collision_with_the_puddle()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.increase_score("puddle_1")
    elif ball.xcor() < -380:
        ball.reset_position()
        scoreboard.increase_score("puddle_2")


screen.exitonclick()
