from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
COLOR = "black"
PLAYER_SHAPE = "turtle"


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape(PLAYER_SHAPE)
        self.goto(STARTING_POSITION)
        self.speed("fastest")
        self.color(COLOR)
        self.setheading(to_angle=90)
        self.finish_line = FINISH_LINE_Y

    def move_player(self):
        self.forward(MOVE_DISTANCE)

    def finish_level(self):

        self.clear()
        self.goto(STARTING_POSITION)
