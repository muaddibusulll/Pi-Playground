from turtle import Turtle

# Constants for our write operation
ALIGN = "center"
MOVE = False
FONT = ('Arial', 12, 'normal')


class Scoreboard(Turtle):

    def __init__(self):

        super().__init__()
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.hideturtle()
        self.goto(x=0, y=280)

        self.puddle_1_score = 0
        self.puddle_2_score = 0

        self.scoreboard_display()

    def increase_score(self, puddle):

        if (puddle == "puddle_1"):
            self.puddle_1_score = self.puddle_1_score + 1
        else:
            self.puddle_2_score = self.puddle_2_score + 1

        self.clear()
        self.scoreboard_display()

    def scoreboard_display(self):
        self.write(arg=f"Score 1: {self.puddle_1_score}    Score 2: {self.puddle_2_score}",
                   move=MOVE, align=ALIGN, font=FONT)
