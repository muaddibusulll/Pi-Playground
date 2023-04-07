import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

game_is_on = True
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()


# Move the player with the Up key using our move_player function
screen.listen()
screen.onkey(key="Up", fun=player.move_player)


while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()

    car_manager.move_car()

    # Check if the player finished the level
    if (player.ycor() > player.finish_line):
        scoreboard.increase_score()
        car_manager.new_level_move()
        player.finish_level()

    # Detect the collision with the car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
