# You are going to write a program that tests the compatibility between two people.

name1=input("What is your name:\n")
name1=input("What is their name:\n")

combined_name=name1+name2
lowerCase=combined_name.lower()
t=lowerCase.count("t")
r=lowerCase.count("r")
u=lowerCase.count("u")
e=lowerCase.count("e")

true=t+r+u+e

l=lowerCase.count("l")
o=lowerCase.count("o")
v=lowerCase.count("v")
e=lowerCase.count("e")

love=l+o+v+e

love_score=int(str(true) +str(love))
if (love_score<10) or (love_score>90):
    print(f"Your score is {love_score}%, you go together like coke and mentos.")
elif (love_score>=40) and (love_score<=50):
    print(f"Your score is {love_score}%,you are alright together.")
else:
    print(f"Your score is {love_score}%")