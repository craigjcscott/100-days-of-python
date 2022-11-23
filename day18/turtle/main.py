import turtle as t
import random
import colorgram

timmy = t.Turtle()
timmy.shape("turtle")
timmy.color("red", "green")
t.colormode(255)


def random_color():
    r = random.randint(1, 255)
    b = random.randint(1, 255)
    g = random.randint(1, 255)
    color_tuple = (r, b, g)
    return color_tuple


def dashed_line(line_length, dash_interval):
    number_of_dashes = round(line_length/dash_interval)
    for i in range(number_of_dashes):
        timmy.down()
        timmy.forward(dash_interval)
        timmy.up()
        timmy.forward(dash_interval)


def draw_a_square(side_length):
    for i in range(4):
        timmy.forward(side_length)
        timmy.right(90)


def draw_shape(n_sides, side_length, rand_color=False):
    if rand_color:
        timmy.pencolor(random_color())
    angle = 360/n_sides
    for _ in range(n_sides):
        timmy.forward(side_length)
        timmy.right(angle)


def random_walk(n_steps, step_length, rand_color=False):
    timmy.width(10)
    timmy.speed("fastest")
    for _ in range(n_steps):
        if rand_color:
            timmy.pencolor(random_color())
        timmy.forward(step_length)
        new_direction = random.choice([0, 90, 180, 270])
        timmy.setheading(new_direction)


def spirograph(n_circles, radius, rand_color=False):
    timmy.speed("fastest")
    angle = 360 / n_circles
    for _ in range(n_circles):
        if rand_color:
            timmy.pencolor(random_color())
        timmy.circle(radius)
        timmy.right(angle)


# dashed_line(100,10)

# draw_a_square()

# for _ in range(3, 11):
#     draw_shape(n_sides=_, side_length=100, rand_color=True)

# random_walk(n_steps=200, step_length=25, rand_color=True)

spirograph(n_circles=100, radius=100, rand_color=True)

screen = Screen()
screen.exitonclick()
