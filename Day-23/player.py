from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

'''Create a turtle player that starts at the bottom of the screen and listen for the "Up" keypress to move the turtle 
north.'''


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("slateblue")
        self.penup()
        self.setheading(90)
        self.go_to_start()

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True