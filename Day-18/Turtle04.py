import turtle as t
import random

timmy = t.Turtle()
directions = [0, 90, 180, 270]
timmy.pensize(10)
timmy.speed("fast")

# Random color
t.colormode(255)


def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    color = (red, green, blue)
    return color

# Draw a Random Walk


for _ in range(200):
    timmy.color(random_color())
    timmy.forward(30)
    timmy.setheading(random.choice(directions))

my_screen = t.Screen()
my_screen.exitonclick()