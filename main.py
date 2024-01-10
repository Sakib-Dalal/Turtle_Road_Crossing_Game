import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle 🐢 Road 🛣️ Crossing 🚷 Game 🚧🚗 ")
screen.tracer(0)
screen.listen()

player = Player()
car = CarManager()
level = Scoreboard()

screen.onkey(key="Up", fun=player.move)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # generate a car and move car
    car.create_car()
    car.move()

    for cars in car.all_cars:
        if cars.distance(player) < 20:
            level.game_over()
            game_is_on = False

    # reset if player at finish line
    if player.player_at_finish():
        player.start_pos()
        level.level_ref()
        car.level_up()


screen.exitonclick()
