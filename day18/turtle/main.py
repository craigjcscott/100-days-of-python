import turtle as t
import random

timmy = t.Turtle()
timmy.shape("turtle")
timmy.color("red", "green")
t.colormode(255)

hirst_colors = [(245, 238, 243), (246, 244, 242), (202, 110, 164), (240, 241, 245), (236, 243, 239), (149, 50, 75),
                (222, 136, 201), (53, 123, 93), (170, 41, 154), (138, 20, 31), (134, 184, 163), (197, 73, 92),
                (47, 86, 121), (73, 35, 43), (145, 149, 178), (14, 70, 98), (232, 165, 176), (160, 158, 142),
                (54, 50, 45), (101, 77, 75), (183, 171, 205), (36, 74, 60), (19, 89, 86), (82, 129, 148), (147, 19, 17),
                (27, 102, 68), (12, 64, 70), (107, 153, 127), (176, 208, 192), (168, 102, 99), (66, 60, 64),
                (219, 183, 178), (178, 202, 198), (112, 141, 139), (254, 0, 194)]


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


def draw_dot(dot_size, dot_colors, rand_color=True):
    if rand_color:
        dot_color = random.choice(dot_colors)
        timmy.dot(dot_size, dot_color)
    else:
        timmy.dot(dot_size)


def draw_hirst(dot_size, n_dots_x, n_dots_y, color_palette):
    # canvas_size_x = dot_size * (n_dots_x + 1) * 2
    # canvas_size_y = dot_size * (n_dots_x + 1) * 2
    # screen.screensize(canvas_size_x, canvas_size_y)
    timmy.penup()
    timmy.speed("fastest")
    timmy.setheading(225)
    timmy.forward(450)
    timmy.setheading(0)
    for i in range(n_dots_y):
        for ii in range(n_dots_x):
            draw_dot(dot_size=dot_size, dot_colors=color_palette, rand_color=True)
            timmy.forward(2 * dot_size)
        timmy.setheading(90)
        timmy.forward(2 * dot_size)
        timmy.setheading(180)
        timmy.forward(2 * dot_size * n_dots_x)
        timmy.setheading(0)


# dashed_line(100,10)

# draw_a_square()

# for _ in range(3, 11):
#     draw_shape(n_sides=_, side_length=100, rand_color=True)

# random_walk(n_steps=200, step_length=25, rand_color=True)

# spirograph(n_circles=100, radius=100, rand_color=True)

draw_hirst(dot_size=25, n_dots_x=15, n_dots_y=14, color_palette=hirst_colors)

screen = t.Screen()
screen.exitonclick()

print(screen.screensize())
