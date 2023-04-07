from cars import Cars
import random

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Cars()
            self.all_cars.append(new_car)

    def move_car(self):

        for car in self.all_cars:
            car.forward(self.car_speed)

    def new_level_move(self):

        self.car_speed += MOVE_INCREMENT
        self.move_car()
