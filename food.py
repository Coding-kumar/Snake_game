import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("Yellow")
        self.shapesize(1, 1)
        self.speed("fastest")

    def refresh(self):
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        self.goto(x, y)
