from turtle import Turtle
import random

COLORS = ["red", "yellow", "orange", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

'''Create cars that are 20px high by 40px wide that are randomly generated along the y-axis and move to the left edge of
the screen. No cars should be generated in the top and bottom 50px of the screen (think of it as a safe zone for our
little turtle). Hint: generate a new car only every 6th time the game loop runs. '''


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.hideturtle()
        self.card_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-230, 250)
            new_car.goto(340, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.card_speed)

    def level_up(self):
        self.card_speed += MOVE_INCREMENT

