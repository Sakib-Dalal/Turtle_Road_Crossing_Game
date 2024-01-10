import turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_num = random.randint(1, 6)
        if random_num == 1:
            random_y = random.randint(-200, 200)
            car = turtle.Turtle()
            car.penup()
            car.shape("square")
            car.shapesize(1, 2)
            car.color(random.choice(COLORS))
            car.goto(300, random_y)
            self.all_cars.append(car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
