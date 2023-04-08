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

        with open("game_data.txt", mode="r") as game_score:
            self.high_score = int(game_score.read())

        self.scoreboard_display()

    def increase_score(self):

        self.score = self.score + 1
        self.scoreboard_display()

    def scoreboard_display(self):
        self.clear()
        self.write(arg=f"Score: {self.score}  Hight Score: {self.high_score}",
                   move=MOVE, align=ALIGN, font=FONT)

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("game_data.txt", mode="w") as game_score:
                game_score.write(f"{self.high_score}")
        self.score = 0
        self.scoreboard_display()

    # def game_over(self):
        #     self.goto(x=0, y=0)
        #     self.write(arg=f"GAME OVER!\nScore: {self.score}",
        #                move=MOVE, align=ALIGN, font=FONT)
