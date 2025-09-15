#this game is about guessing the letters of a secret word
#a game loop an infinte while loop
#a random word is selected from an existing list 
#the user is given a hint the amount of letters 
#the user inputs the their guess the computer chacks if the letter exist in the program
#if it exist tell the user and make them guess the next letter
#if the user gets it wrong penalty them for wrong guess and let em try again until their chances are zero 
import random 



print("welcome to the hangman game ")


while True:
    word_list = ["python", "programming", "developer", "keyboard"]
    magic_word = random.choice(word_list)
    length = len(magic_word)

    word_display = []

    for _ in range(len(secret_word)):
        word_display.append("_")
        print(word_display)
        continue



    user_guess = input("guess").lower()

    #compare the user input and the guessed word 
    if user_guess in magic_word:
        print("you got s guess right")
    else:
        print("your guess is wrong you loose one chance ")
    print(f)