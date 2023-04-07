from turtle import Turtle

FONT = ("Courier", 24, "normal")
SCOREBOARD_COLOR = "black"
SCOREBOARD_POSITION = (-230, 250)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color(SCOREBOARD_COLOR)
        self.speed("fastest")
        self.goto(SCOREBOARD_POSITION)
        self.score = 0
        self.scoreboard_display()

    def scoreboard_display(self):
        self.write(arg=f"Score {self.score}",
                   move=False, align="center", font=FONT)

    def increase_score(self):
        self.score = self.score + 1
        self.clear()
        self.scoreboard_display()

    def game_over(self):
        self.clear()
        self.goto(x=0, y=0)
        self.write(arg=f"Game over !!\nScore {self.score}",
                   move=False, align="center", font=FONT)
