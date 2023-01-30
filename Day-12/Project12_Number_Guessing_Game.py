from Project12_art import logo
import random

print(logo)

# Global variable to set the difficulty turns
EASY_LEVEL=10
MEDIUM_LEVEL=7
HARD_LEVEL=5

def check_answer(guess,answer,turns):
    """Guess the number and keep tracting the number of turns"""
    if guess>answer:
        print("Too high")
        return turns-1
    elif guess<answer:
        print("Too low")
        return  turns-1
    else:
        print(f"You got it! The answer is {answer}")

def difficulty_level():
    choose_difficulty=input("Choose Difficulty Level.Type 'easy', 'medium' or hard': ")
    if choose_difficulty=="easy":
        return EASY_LEVEL
    elif choose_difficulty=="medium":
        return MEDIUM_LEVEL
    else:
        return HARD_LEVEL

    guess=int(input("Make a guess: "))

def game():
    print("Welcome To The Number Guessing Game.!")
    answer=random.randint(1,100)
    print("I'm Thinking About The Number Between 1 and 100")
    turns=difficulty_level()
    guess=0
    while guess!=answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess=int(input("Make a guess: "))
        turns=check_answer(guess,answer,turns)
        if turns==0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")

game()