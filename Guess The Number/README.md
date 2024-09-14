# Number Guessing Game

This is a Python-based number guessing game that includes two different modes:

1) **User guesses the number:** The program selects a random number, and the user has to guess it.  
2) **Computer guesses the number:** The user thinks of a number, and the computer tries to guess it with feedback provided by the user.  

## How to Play  

You can either guess the random number selected by the program or have the computer guess the number you're thinking of. You will receive feedback based on how close you are to the correct answer.

**Game Modes**  

**1. User Guesses the Number**  

In this mode, the computer selects a random number between 1 and a specified number (default is 10), and the user has to guess the correct number. After each guess, the program will provide feedback:

- Too Low: The guessed number is smaller than the target number.
- Too High: The guessed number is larger than the target number.
- Correct, the game ends and a congratulatory message is shown.  

**2. Computer Guesses the Number**  

In this mode, the user selects a number, and the computer will try to guess it. The user will provide feedback:  

- L: The computer's guess is too low.  
- H: The computer's guess is too high.  
- C: The computer's guess is correct.
  
The game continues until the computer guesses the number correctly.  

  ## What We Did
- Random Number Generation: The random.randint() function is used to generate a random number in the specified range.  
- User Input: The input() function is used to get responses from the user.  
- Conditional Logic: The program uses if statements to provide feedback on whether the guess is too high, too low, or correct.
- Computer Guessing: The computer uses a binary search-like approach, narrowing down the range of possible numbers based on user feedback (H, L, C).  

```python
import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a random number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, guess again. Too Low.')
        elif guess > random_number:
            print('Sorry, guess again. Too High.')

    print(f'Congratulations! You guessed the {random_number} correctly.')
```
- The function guess(x) generates a random number between 1 and x.
- The user keeps guessing until the correct number is guessed, with feedback after each attempt.
- The function computer_guess(x) asks the user for feedback and adjusts the range of possible numbers based on user input.
- The computer uses feedback (H, L, C) to zero in on the correct number.

```python
import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # Only one possible number left
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)? ').lower()

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'Yay! The computer guessed your number, {guess}, correctly!')
```

## Example Gameplay:

**User Guesses the Number**  
If the user sets the range from 1 to 10 and the random number is 5:  

- User guesses 3: The program prints "Too Low."
- User guesses 7: The program prints "Too High."
- User guesses 5: The program prints "Congratulations! You guessed the 5 correctly."
```python
Guess a random number between 1 and 10: 5
Sorry, guess again. Too Low.
Guess a random number between 1 and 10: 8
Sorry, guess again. Too High.
Guess a random number between 1 and 10: 7
Congratulations! You guessed the 7 correctly.
```

**Computer Guesses the Number**  
If the user picks 7:  

- Computer guesses 5: The user responds with L (too low).
- Computer guesses 9: The user responds with H (too high).
- Computer guesses 7: The user responds with C (correct), and the game ends.
  
```python
Is 5 too high (H), too low (L), or correct (C)? L
Is 8 too high (H), too low (L), or correct (C)? H
Is 7 too high (H), too low (L), or correct (C)? C
Yay! The computer guessed your number, 7, correctly!
```

