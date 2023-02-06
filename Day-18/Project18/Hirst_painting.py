# import colorgram
#
# colors = colorgram.extract('Spot-paintings.jpg', 400)
# rgb_color = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_color.append(new_color)
# print(rgb_color)

import turtle as turtle_module
import random

timmy = turtle_module.Turtle()
color_list = [(244, 232, 220), (212, 150, 96), (245, 227, 234), (220, 232, 240), (228, 242, 235), (55, 105, 134), (149, 86, 57), (125, 162, 186), (140, 69, 94), (199, 133, 155), (213, 88, 64), (165, 151, 49), (55, 121, 88), (124, 178, 153), (195, 88, 117), (26, 50, 76), (226, 201, 121), (76, 158, 121), (55, 43, 29), (41, 56, 106), (235, 163, 184), (57, 35, 49), (118, 36, 57), (53, 158, 175), (103, 120, 167), (28, 53, 41), (241, 169, 157), (12, 99, 73), (157, 211, 189), (114, 43, 34), (147, 211, 221), (181, 184, 214), (16, 89, 102), (76, 75, 35), (238, 198, 9)]
turtle_module.colormode(255)
timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()

timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
num_of_dots = 100

for dot_count in range(1, num_of_dots + 1):
    timmy.dot(20, random.choice(color_list))
    timmy.forward(50)
    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)

my_screen = turtle_module.Screen()
my_screen.exitonclick()
