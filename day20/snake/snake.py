from turtle import Turtle
STARTING_POS_X = 0
STARTING_POS_Y = 0
STARTING_LENGTH = 3
STARTING_SPEED = 0.05
MOVEMENT_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:
    def __init__(self):
        self.speed = STARTING_SPEED
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for i in range(STARTING_LENGTH):
            new_square = Turtle()
            new_square.penup()
            new_square.color("white")
            new_square.shape("square")
            new_square.setposition(STARTING_POS_X - MOVEMENT_DISTANCE * i, STARTING_POS_Y)
            self.snake_body.append(new_square)

    # def grow_snake(self):
    #

    def move(self, distance=MOVEMENT_DISTANCE):
        for segment_index in range(len(self.snake_body) - 1, 0, -1):
            segment = self.snake_body[segment_index]
            leading_segment_position = self.snake_body[segment_index - 1].position()
            segment.goto(leading_segment_position)
        self.head.forward(distance)

    def up(self):
        current_heading = self.head.heading()
        if current_heading != DOWN:
            self.head.setheading(UP)

    def down(self):
        current_heading = self.head.heading()
        if current_heading != UP:
            self.head.setheading(DOWN)

    def left(self):
        current_heading = self.head.heading()
        if current_heading != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        current_heading = self.head.heading()
        if current_heading != LEFT:
            self.head.setheading(RIGHT)