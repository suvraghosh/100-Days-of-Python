import turtle as t
import random

timmy = t.Turtle()

# Random color
t.colormode(255)
timmy.speed("fastest")


def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    color = (red, green, blue)
    return color

# Make a Spirograph


def draw_spirograph(gap):
    for _ in range(int(360/gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + gap)


draw_spirograph(4)

my_screen = t.Screen()
my_screen.exitonclick()
