from turtle import Turtle

SNAKE_STEP = 20


class Snake:

    def __init__(self):
        self.snake_body = []
        self.snake_creation()
        self.snake_head = self.snake_body[0]
        self.draw_the_head()

    def snake_creation(self):
        """This function helps to create our snake with tree initial pieces"""
        x = 0
        y = 0
        for body_part in range(3):
            self.add_body_part(body_part, x, y)
            x = x - 20

    def move_snake_body(self):
        """This function makes our snake body to move"""
        # start, stop, step
        for snake_part in range(len(self.snake_body)-1, 0, -1):
            after_x = self.snake_body[snake_part-1].xcor()
            after_y = self.snake_body[snake_part-1].ycor()
            self.snake_body[snake_part].goto(after_x, after_y)
        self.snake_head.forward(SNAKE_STEP)

    def add_body_part(self, position, x, y):
        turtle_body = Turtle("square")
        turtle_body.penup()
        turtle_body.speed("fastest")
        turtle_body.color("white")
        turtle_body.goto(x=x, y=y)
        self.snake_body.append(turtle_body)

    def extend_the_snake_body(self):
        # add a new part to the snake
        last_part_x = self.snake_body[-1].xcor()
        last_part_y = self.snake_body[-1].ycor()
        self.add_body_part(
            self.snake_body[-1].position(), last_part_x, last_part_y)

    def draw_the_head(self):
        self.snake_head.color("green")

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
