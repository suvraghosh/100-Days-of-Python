'''Reeborg was exploring a dark maze and the battery in its flashlight ran out.
Write a program using an if/elif/else statement so Reeborg can find the exit. The secret is to have Reeborg follow along the right edge of the maze, turning right if it can, going straight ahead if it can’t turn right, or turning left as a last resort.

Try this code in the Reeborg's World website
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json'''

# Lost in a maze

def turn_right():
    turn_left()
    turn_left()
    turn_left()
# This codition help us to prevent from the infinite loop at some of the cases.
while front_is_clear():
    move()
turn_left()

while not at_goal():
     if right_is_clear():
        turn_right()
        move()
     elif front_is_clear():
        move()
     else:
        turn_left()