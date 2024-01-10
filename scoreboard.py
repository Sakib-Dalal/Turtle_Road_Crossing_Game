import turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.level_ref()

    def level_ref(self):
        self.clear()
        self.penup()
        self.hideturtle()
        self.goto(-200, 250)
        self.write(f"Level🐢: {self.level} 🏁", align="center", font=FONT)
        self.level += 1

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.write("🐢 GAME ☠️ OVER 😭", align="center", font=("Courier", 30, "normal"))
