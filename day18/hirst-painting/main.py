import colorgram
import turtle as t
import random

timmy = t.Turtle()
t.colormode(255)

extracted_colors = colorgram.extract('image.jpg', 20)

extracted_color_tuples = []

for color in extracted_colors:
    r = color.rgb.r
    b = color.rgb.b
    g = color.rgb.g
    temp_tuple = (r, b, g)
    extracted_color_tuples.append(temp_tuple)


def draw_dot(dot_size, dot_colors, rand_color=True):
    dot_color = random.choice(dot_colors)
    timmy.dot(dot_size, dot_color)


draw_dot(10, extracted_color_tuples)










screen = t.Screen()
screen.exitonclick()





