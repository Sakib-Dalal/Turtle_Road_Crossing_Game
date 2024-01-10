import turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.start_pos()

    def start_pos(self):
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move(self):
        self.forward(10)

    def player_at_finish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
