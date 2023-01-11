import random
name=input("Tell me your name..? ")
print("     Welcome "+name+" to the word guessing game..!!")
words=["java","python","javascript","css","programming","google","youtube","chatgpt","default","void","integer",
       "artificial intelligence","data science","machine learning","web development","blockchain development"]
word=random.choice(words)
print("Guess the Characters")
guesses=''
turn=20
while turn>0:
    failed=0
    for character in word:
        if character in guesses:
            print(character,end=" ")
        else:
            print("_")
            failed+=1
    if failed==0:
        print("\nCongrats!You Win the game")
        print("The word is: ",word)
        break
    print()
    guess=input("Guess a character: ")
    guesses=guesses+guess

    if guess not in word:
        turn-=1
        print("Worng guess")
        print("Now you've only ",+ turn," more turns left.")
        if turn==0:
            print("You lost the game.")
            print("The correct word is: ", word)