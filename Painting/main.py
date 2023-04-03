from turtle import Turtle, Screen

my_turtle = Turtle()
screen = Screen()


def forward():
    my_turtle.forward(10)


def backwards():
    my_turtle.backward(10)


def counter_clockwise():
    my_turtle.left(10)


def clockwise():
    my_turtle.right(10)


screen.listen()

screen.onkey(fun=forward, key="w")
screen.onkey(fun=backwards, key="s")
screen.onkey(fun=counter_clockwise, key="a")
screen.onkey(fun=clockwise, key="d")
screen.onkey(fun=screen.reset, key="c")

screen.exitonclick()
