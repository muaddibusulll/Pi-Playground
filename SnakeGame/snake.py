from turtle import Turtle

SNAKE_STEP = 20


class Snake:

    def __init__(self):
        self.snake_body = []
        self.snake_creation()
        self.snake_head = self.snake_body[0]

    def snake_creation(self):
        """This function helps to create our snake with tree initial pieces"""
        x = 0
        for body_part in range(3):
            turtle_body = Turtle("square")
            turtle_body.penup()
            turtle_body.color("white")
            turtle_body.goto(x=x, y=0)
            self.snake_body.append(turtle_body)
            x = x - 20

    def move_snake_body(self):
        """This function makes our snake body to move"""
        # start, stop, step
        for snake_part in range(len(self.snake_body)-1, 0, -1):
            after_x = self.snake_body[snake_part-1].xcor()
            after_y = self.snake_body[snake_part-1].ycor()
            self.snake_body[snake_part].goto(after_x, after_y)
        self.snake_head.forward(SNAKE_STEP)

    def up(self):
        if self.snake_head.heading() != 270:
            self.snake_head.setheading(90)

    def down(self):
        if self.snake_head.heading() != 90:
            self.snake_head.setheading(270)

    def left(self):
        if self.snake_head.heading() != 0:
            self.snake_head.setheading(180)

    def right(self):
        if self.snake_head.heading() != 180:
            self.snake_head.setheading(0)
