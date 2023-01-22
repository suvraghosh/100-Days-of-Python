# You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

import random

# Split string method
names=input("Give me the list of the names,Separated by comma: ")
names_split=names.split(",")
#Get the total number of items in list.
lenght_of_names=len(names_split)
random_choice=random.randint(0,lenght_of_names-1)
#Pick out random person from list of names using the random number.
who_will_pay=names_split[random_choice]
print(who_will_pay + " will pay the bill.")