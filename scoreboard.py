from turtle import Turtle


class Scorecard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 280)
        self.pencolor("white")
        self.hideturtle()
        self.points = 0
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.points}", align="center", font=("arial", 12, "normal"))

    def increse_score(self):
        self.points += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("arial", 18, "normal"))
