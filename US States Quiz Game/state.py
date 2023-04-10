from turtle import Turtle

# Constants for our write operation
ALIGN = "center"
MOVE = False
FONT = ('Arial', 12, 'normal')


class State(Turtle):

    def __init__(self, x, y, country_name):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.color("black")
        self.goto(x=x, y=y)
        self.write(arg=f"{country_name}",
                   move=MOVE, align=ALIGN, font=FONT)
