# Try this code in the Reeborg's World website
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

# Hurdle 1
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

# Calling the function 6 times to achieve the goal
jump()
jump()
jump()
jump()
jump()
jump()  

# Another way to code more shorter and readable instead of calling the function 6 times
for step in range(0,6):
    jump()