from turtle import Screen
from snake import Snake
from snakeFood import SnakeFood
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
game_is_on = True

# Create our snake object
snake = Snake()
# Create our snake food object
snake_food = SnakeFood()
# Create our scoreboard object
scoreboard = Scoreboard()
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)


while game_is_on:

    screen.update()
    time.sleep(0.1)

    snake.move_snake_body()

    # Detect collision with the snake food

    if snake.snake_head.distance(snake_food) < 15:
        snake_food.refresh()
        snake.extend_the_snake_body()
        scoreboard.increase_score()

    # Detect collision with the wall
    if (snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280) or (snake.snake_head.ycor() > 280 or snake.snake_head.ycor() < -280):
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with the tail
    for snake_body_part in snake.snake_body[1:]:
        if snake.snake_head.distance(snake_body_part) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
