from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
CAR_SHAPE = "square"


class Cars(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color(random.choice(COLORS))
        self.shape(CAR_SHAPE)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.x_position = 286
        self.y_position = random.randint(-250, 250)
        self.goto(x=self.x_position, y=self.y_position)
        self.setheading(180)
