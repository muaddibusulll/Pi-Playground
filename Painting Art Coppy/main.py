import colorgram
import turtle as t
import random


def draw_line(x, y):
    for _ in range(11):
        my_turtle.dot(20, random.choice(rgb_colors))
        my_turtle.forward(50)
        my_turtle.dot(20, random.choice(rgb_colors))

    my_turtle.setx(x)
    my_turtle.sety(y + 50)


rgb_colors = []
colors = colorgram.extract(
    '/home/iosif/python/python_bootcamp_Udemy/day-18/painting/image.jpg', 30)
for color in colors:
    rgb_colors.append(color.rgb)

my_turtle = t.Turtle()

my_turtle.penup()
my_turtle.hideturtle()
my_turtle.sety(-300)
my_turtle.setx(-300)

t.colormode(255)

print(my_turtle.xcor())

for i in range(10):

    draw_line(x=my_turtle.xcor(), y=my_turtle.ycor())


screen = t.Screen()
screen.exitonclick()
