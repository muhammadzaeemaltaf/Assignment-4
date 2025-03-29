from random import choice
from words import words
import string

def get_valid_word(words):
    word = choice(words)  
    while '-' in word or ' ' in word:
        word = choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 6

    while len(word_letters) > 0 and lives > 0:

        print("You have", lives, "lives left and you have used these letters: ", ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", ' '.join(word_list))

        user_input = input("Guess a letter: ").upper()

        if user_input in alphabet - used_letters:
            used_letters.add(user_input)
            if user_input in word_letters:
                word_letters.remove(user_input)
            else:
                lives -= 1
                print("Letter is not in the word. You have lost a life.")

        elif user_input in used_letters:
            print("You have already used that letter. Please try again.")
        else:
            print("Invalid character. Please try again.")
        
    
    if lives == 0:
        print("You have lost. The word was", word)
    else:
        print("Congratulations! You have guessed the word", word)

hangman()