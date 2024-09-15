import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    attempts = 100  # Limit attempts to avoid potential infinite loop
    while '-' in word or ' ' in word:
        word = random.choice(words)
        attempts -= 1
        if attempts == 0:
            raise ValueError("No valid word found after multiple attempts.")
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)    # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()    # to keep track of what user has guessed

    lives = 5

    print(f"The word has {len(word)} letters.")

    while len(word_letters) > 0 and lives > 0:
        print(f'You have {lives} lives left and you have used these letters: ', ' '.join(used_letters))

        # What current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()  # getting user input
        if len(user_letter) != 1:
            print('\nPlease enter only a single letter.')
        elif user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print(f'Good job! {user_letter} is in the word.')

            else:
                lives -= 1
                print(f'\nYour letter {user_letter} is not in the word.')

        elif user_letter in used_letters:
            print('\nYou have already used that letter. Please try again.')

        else:
            print('\nInvalid character. Please try again.')

    if lives == 0:
        print(f'You died, sorry. The word was {word}')
    else:
        print(f'Yay! You guessed the word {word}!!')

    play_again = input('Do you want to play again? (Y/N): ').upper()
    if play_again == 'Y':
        hangman()

if __name__ == '__main__':
    hangman()
