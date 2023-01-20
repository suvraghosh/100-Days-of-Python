'''Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
The BMI is a measure of someone's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.'''

height = float(input("enter your height in m: "))
weight = int(input("enter your weight in kg: "))

Body_Mass_index=(weight/(height*height))
print(round(Body_Mass_index))
