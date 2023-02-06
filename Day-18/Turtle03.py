from turtle import Screen,Turtle
import random

timmy = Turtle()
colors = ["dark blue", "dark slate gray", "indigo", "saddle brown", "gold", "dark green", "teal", "crimson", "hot pink",
          "pale violet red", "olive", "rosy brown"]
# Challenge-2 To draw a triangle,square,pentagon,hexagon,heptagon,octagon,nonagon and decagon.


def shape(num_sides):

    angle = 360 / num_sides
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)


for shape_side_n in range(3, 11):
    timmy.color(random.choices(colors))
    shape(shape_side_n)

my_screen = Screen()
my_screen.exitonclick()
