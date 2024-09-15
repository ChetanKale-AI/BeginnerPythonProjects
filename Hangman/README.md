# Hangman Game

A simple command-line implementation of the classic Hangman game written in Python. Players must guess the hidden word, letter by letter, before they run out of lives!

## Features
- Randomly selects a word from a word list.
- Displays current progress with correctly guessed letters.
- Tracks and displays letters that have already been used.
- Allows users to replay the game after each round.
- Simple and intuitive command-line interface.

## Usage  
When you start the game, a random word will be selected, and you will have 5 lives to guess the word by guessing individual letters. Each incorrect guess will cost one life, and the game ends when you either guess the word correctly or lose all your lives.  

**Example Gameplay**
```bash
The word has 4 letters.

You have 5 lives left and you have used these letters: 
Current word:  - - - -

Guess a letter: E

Your letter E is not in the word.
You have 4 lives left and you have used these letters: E
Current word:  - - - -

Guess a letter: A
Good job! A is in the word.

You have 4 lives left and you have used these letters: E A
Current word:  - A - -

Guess a letter: S

Your letter S is not in the word.
You have 3 lives left and you have used these letters: E A S
Current word:  - A - -

Guess a letter: R
Good job! R is in the word.

You have 3 lives left and you have used these letters: E A S R
Current word:  R A - -

Guess a letter: T

Good job! T is in the word.

You have 3 lives left and you have used these letters: E A S R T
Current word:  R A T -

Guess a letter: P
Good job! P is in the word.

You have 3 lives left and you have used these letters: E A S R T P
Current word:  R A T P

Yay! You guessed the word RATP!!

```

## Rules of the Game
1. You start with 5 lives.  
2. The word is hidden and displayed as dashes (-), with the number of dashes equal to the number of letters in the word.  
3. You can guess one letter at a time.  
4. If the guessed letter is in the word, it will be revealed in its correct position(s).  
5. If the guessed letter is not in the word, you will lose a life.  
6. If you guess all the letters correctly before running out of lives, you win!  
7. If you lose all your lives, the game is over, and the word will be revealed.  
8. After each game, you'll be given the option to play again.  


