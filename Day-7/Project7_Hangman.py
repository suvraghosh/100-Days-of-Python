import random
from Hangman_word import word_list
from Hangman_art import stages,logo

# Import the logo from hangman_art.py and print it at the start of the game.
print(logo)

end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# If you want to know the chosen random word just uncomment this.
# print(f'Pssst, the solution is {chosen_word}.')

#Create a variable called 'lives' to keep track of the number of lives left.
lives = 6

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You already guessed {guess}")
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
       # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    '''If guess is not a letter in the chosen_word,Then reduce 'lives' by 1.
        If lives goes down to 0 then the game should stop and it should print You lose.'''
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose the Game.!")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("Congratulations!You win the Game.")

# Import the stages from hangman_art.py.
    print(stages[lives])