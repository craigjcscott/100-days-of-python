from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.move_x = 10
        self.move_y = 10

    def move(self):
        self.goto(self.xcor() + self.move_x, self.ycor() + self.move_y)

    def bounce_wall(self):
        self.move_y *= -1
        # if self.heading() < 180:
        #     self.setheading(self.heading() + 180)
        # else:
        #     self.setheading(self.heading() - 180)

    def out_of_bounds(self, x_boundry):
        if round(abs(self.xcor())) > x_boundry:
            return True

    def bounce_paddle(self):
        if self.heading() < 180:
            self.setheading(self.heading() + 180)
        else:
            self.setheading(360 - self.heading())