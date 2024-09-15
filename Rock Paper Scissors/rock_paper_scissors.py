import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors: ").lower()

    # Input validation
    if user not in ['r', 'p', 's']:
        return "Invalid choice! Please choose 'r', 'p', or 's'."

    computer = random.choice(['r', 'p', 's'])

    # Mapping choices to full words for clarity
    choices = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}

    # Output user and computer choices
    print(f"\nYou chose {choices[user]}, Computer chose {choices[computer]}.")

    if user == computer:
        return "It's a tie!"

    # Check if the user wins
    if is_win(user, computer):
        return "You Won!"

    return "You Lost!"

def is_win(player, opponent):
    # Return True if the player wins
    return (player == 'r' and opponent == 's') or \
        (player == 's' and opponent == 'p') or \
        (player == 'p' and opponent == 'r')

# Game loop
while True:
    result = play()
    print(result)

    play_again = input("\nDo you want to play again? (y/n): ").lower()
    if play_again != 'y':
        print("Thanks for playing!")
        break
