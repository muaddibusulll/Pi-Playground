from turtle import Turtle, Screen
import random

FOOD = "food.jpg"


class SnakeFood(Turtle):

    def __init__(self):
        super().__init__()
        # self.food_screen = Screen()
        # self.food_screen.addshape(FOOD)
        self.shape("circle")
        # self.shape(FOOD)
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.goto(x=random.randint(-250, 250), y=random.randint(-250, 250))
