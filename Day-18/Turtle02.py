from turtle import Screen,Turtle

timmy = Turtle()

# Challenge-2 To draw a Dashed Line.
for i in range(15):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()

my_screen = Screen()
my_screen.exitonclick()