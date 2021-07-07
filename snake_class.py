from turtle import Turtle

TURTLE_POSITION = [(0, 0), (-20, 0), (-40, 0)]
DOWN = 270
LEFT = 180
UP = 90
RIGHT = 0
DISTANCE = 20


class Snake:

    def __init__(self) -> None:
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self) -> None:
        for position in TURTLE_POSITION:
            self.add_segment(position)

    def add_segment(self, position) -> None:
        turtle = Turtle('square')
        turtle.color('white')
        turtle.penup()
        turtle.goto(position)
        self.segments.append(turtle)

    def extend(self) -> None:
        self.add_segment(self.segments[-1].position())

    def move_forward(self) -> None:
        for turtle in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[turtle - 1].xcor()
            new_y = self.segments[turtle - 1].ycor()
            self.segments[turtle].goto(new_x, new_y)
        self.segments[0].forward(DISTANCE)

    def up(self) -> None:
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self) -> None:
        if self.head.heading() != UP:
            self.head.setheading(270)

    def lef(self) -> None:
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self) -> None:
        if self.head.heading() != LEFT:
            self.head.setheading(0)
