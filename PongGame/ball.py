from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("circle")
        self.ball_x_cor = + 10
        self.ball_y_cor = -  10

    def ball_moving(self):
        """With this function we move the ball"""

        # The new x and y coordinates of the ball are
        # 10 + the current ball x and y coordinates
        new_x_ball_cor = self.ball_x_cor + self.xcor()
        new_y_ball_cor = self.ball_y_cor + self.ycor()

        self.goto(x=new_x_ball_cor, y=new_y_ball_cor)

    def collision_with_wall(self):

        # In all situations the only coordinate we need to change
        # is y. Because for example if the ball goes to the
        # left-top we need to bounce the ball to left bottom
        # so from [+y, -x] (left-top) needs to change to
        # [-y, -x] (left-bottom). This is the idea for all directions
        #
        self.ball_y_cor = self.ball_y_cor * -1

    def collision_with_the_puddle(self):

        self.ball_x_cor = self.ball_x_cor * -1

    # TODO: the reset function so when the player loses the ball the ball will
    # reset to it's initial position in the center ot the screen
    def reset_position(self):

        self.goto()
