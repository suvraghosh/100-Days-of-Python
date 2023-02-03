from turtle import Turtle , Screen

# Turtle() is a class & jimmy is a variable to store the object
jimmy = Turtle()
print(jimmy)

# This all are a methods
jimmy.shape("turtle")
jimmy.color("cyan")
jimmy.forward(100)

# Screen() is also be a class and Subclass of TurtleScreen
my_screen= Screen()
print(my_screen.canvwidth)
my_screen.exitonclick()

# External module to create a table
from prettytable import PrettyTable


table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)
