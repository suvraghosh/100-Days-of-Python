import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images=[rock,paper,scissors]

user_choice=int(input(".→_→ Enter 0 for rock, 1 for paper, 2 for scissors ←_←. \n"))

if user_choice>=3:
    print("You enter the invalid number.You lose")
else:
    print(f"User choice: {game_images[user_choice]}")

    comp_choice=random.randint(0,2)
    print(f"Computer choice: {game_images[comp_choice]}")

    if comp_choice==0 and user_choice==1:
        print("You win!")
    elif comp_choice==1 and user_choice==0:
        print("You lose")
    elif comp_choice==0 and user_choice==2:
        print("You lose")
    elif comp_choice==2 and user_choice==0:
        print("You Win!")
    elif comp_choice==2 and user_choice==1:
        print("You lose")
    elif comp_choice==1 and user_choice==2:
        print("You Win!")
    elif comp_choice==user_choice:
        print("Game Draw.")
