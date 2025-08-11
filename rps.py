import random

# Function to get the computer's choice
def get_computer_choice():
    return random.choice(['r', 'p', 's'])

# Function to determine the result
def get_result(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == 'r' and computer == 's') or \
         (player == 'p' and computer == 'r') or \
         (player == 's' and computer == 'p'):
        return "You win!"
    else:
        return "You lose!"

# Function to convert choice to emoji
def get_emoji(choice):
    emojis = {'r': '✊', 'p': '✋', 's': '✌'}
    return emojis[choice]

# Main game loop
def main():
    while True:
        player = input("Rock, paper, or scissors? (r/p/s): ").lower()
        if player not in ['r', 'p', 's']:
            print("Invalid input. Please try again.")
            continue

        computer = get_computer_choice()

        print(f"You chose {get_emoji(player)}")
        print(f"Computer chose {get_emoji(computer)}")

        print(get_result(player, computer))

        again = input("Continue? (y/n): ").lower()
        if again != 'y':
            break

# Start the game
if __name__ == "__main__":
    main()