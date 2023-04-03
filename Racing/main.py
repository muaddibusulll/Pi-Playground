from turtle import Turtle, Screen
import random


def create_turtles(colors, racing_turtles):
    x = -235
    y = -135

    for color in colors:
        turtle = Turtle(shape="turtle")
        turtle.penup()
        turtle.color(color)
        turtle.goto(x=x, y=y)
        racing_turtles.append(turtle)
        y = y + 40

    return racing_turtles


screen = Screen()
screen.setup(width=500, height=400)
race_is_up = False


user_bet = screen.textinput(
    title="Bet", prompt="Witch turtle will gonna be win?")

colors = ["red", "green", "orange", "yellow", "blue", "purple"]
turtles = []

turtles = create_turtles(colors, turtles)

if user_bet:
    race_is_up = True

while race_is_up:

    for race_turtle in turtles:
        if race_turtle.xcor() > 230:
            race_is_up = False
            winner = race_turtle.pencolor()
            if winner == user_bet:
                print("You win")
            else:
                print("You lose")
        else:
            race_turtle.forward(random.randint(2, 10))


# Turtle().forward(random.randint(2, 10))


screen.exitonclick()
