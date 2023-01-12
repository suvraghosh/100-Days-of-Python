import  random
import math

lower=int(input("Enter the lower bound: "))
upper=int(input("Enter the upper bound: "))

randomNumber=random.randint(lower,upper)
print("\n\tYou've only get",round(math.log(upper - lower +1,2)),"chances to guess the number..!\n")

count=0
while count< math.log(upper - lower+1,2):
    count+=1
    guess=int(input("Guess the number: "))
    if randomNumber==guess:
        print("Congrats!You win.")
        print("You did it in",count,"try")
        break

    elif guess<randomNumber:
        print(" The number is to small.\n")
    elif guess>randomNumber:
        print(" The number is to large.\n")

if count>= math.log(upper - lower+1,2):
    print("The correct number is: ",randomNumber)
    print("You loose..!")