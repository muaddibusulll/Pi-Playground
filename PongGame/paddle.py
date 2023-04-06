from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, puddle_position):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.shape("square")
        self.color("white")
        self.resizemode("user")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x=puddle_position[0], y=puddle_position[1])

    def up(self):
        new_y_position = self.ycor() + 20
        self.goto(x=self.xcor(), y=new_y_position)

    def down(self):
        new_y_position = self.ycor() - 20
        self.goto(x=self.xcor(), y=new_y_position)
