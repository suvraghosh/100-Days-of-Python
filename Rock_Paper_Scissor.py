
import random


def Game(comp, user):
    if comp == user:
        return None
    elif comp == 'r':
        if user == 's':
            return False
        elif user == 'p':
            return True
    elif comp == 'p':
        if user == 'r':
            return False
        elif user == 's':
            return True
    elif comp == 's':
        if user == 'p':
            return False
        elif user == 'r':
            return True


print("Comp turn:Choose Rock(r) or Paper(p) or Scissor(s)")
randNo = random.randint(1, 3)
if randNo == 1:
    comp= 'r'
elif randNo == 2:
    comp = 'p'
elif randNo == 3:
    comp = 's'

user = input("User Turn:Choose (r) or (p) or (s): ")
a = Game(comp, user)

print(f"Computer choose:{comp}")

if a == None:
    print("Game draw!")
elif a:
    print("You win!")
else:
    print("You loose")