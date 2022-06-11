#Step 5
from replit import clear

import random
from hangman_words import word_list
# Update the word list to use the 'word_list' from hangman_words.py
#random choice word_list
chosen_word = random.choice(word_list)
#getting the length of chosen_word
word_length = len(chosen_word)
#established end_of_game as false for the while loop to keep going
end_of_game = False
#lives of hangman established
lives = 6


#Import the logo from hangman_art.py and print it at the start of the game.
from hangman_art import logo, stages
print(logo)

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
#establishing space for the letters to go
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
#clear sentences each time after each input
    clear()

    # If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You have already guessed {guess}.")

    #Check guessed letter...position is turned into an integer to find the postion in the word
    for position in range(word_length):
        letter = chosen_word[position]
#replacing right letter with position of where it goes
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
    #If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"You guessed {guess} which is not in the word. You lose a life.")
    #established the number of lives to be lost if guess is wrong
        lives -= 1
    #when lives = 0 end_of_game will equal true
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    print(stages[lives])

