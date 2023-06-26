from turtle import Turtle

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for po in STARTING_POS:
            self.add_segment(po)

    def add_segment(self, position):
        tony = Turtle()
        tony.shape("square")
        tony.color("white")
        tony.penup()
        tony.goto(position)
        self.segments.append(tony)

    def extend_segment(self):
        self.add_segment(self.segments[-1].position())

    def move_snake(self):
        for segam in range(len(self.segments) - 1, 0, -1):
            xpos = self.segments[segam - 1].xcor()
            ypos = self.segments[segam - 1].ycor()
            self.segments[segam].goto(xpos, ypos)

        self.segments[0].forward(DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
