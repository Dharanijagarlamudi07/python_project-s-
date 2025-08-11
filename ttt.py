# Tic Tac Toe Game

# Create a 3x3 board
board = [[" " for _ in range(3)] for _ in range(3)]

def print_board():
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner(player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]) or \
           all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def is_draw():
    return all([cell != " " for row in board for cell in row])

current_player = "X"

while True:
    print_board()
    print(f"Player {current_player}'s turn")
    row = int(input("Enter row (0-2): "))
    col = int(input("Enter column (0-2): "))

    if board[row][col] != " ":
        print("That spot is taken! Try again.")
        continue

    board[row][col] = current_player

    if check_winner(current_player):
        print_board()
        print(f"Player {current_player} wins!")
        break
    elif is_draw():
        print_board()
        print("It's a draw!")
        break

    # Switch players
    current_player = "O" if current_player == "X" else "X"