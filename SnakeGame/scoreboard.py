from turtle import Turtle

# Constants for our write operation
ALIGN = "center"
MOVE = False
FONT = ('Arial', 12, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.color("white")
        self.goto(x=0, y=280)

        self.score = 0

        self.scoreboard_display()

    def increase_score(self):
        self.score = self.score + 1
        self.clear()
        self.scoreboard_display()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg=f"GAME OVER!\nScore: {self.score}",
                   move=MOVE, align=ALIGN, font=FONT)

    def scoreboard_display(self):
        self.write(arg=f"Score: {self.score}",
                   move=MOVE, align=ALIGN, font=FONT)
