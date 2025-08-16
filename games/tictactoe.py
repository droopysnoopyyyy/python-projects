def create_board():
    return [[" " for _ in range(3)] for _ in range(3)] #make 3 rows of lists with 3 empty spaces (nested)
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
def check_if_valid(board, row, col):
        return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " "
def check_wins(board):
     # Rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return True
    # Columns
    for c in range(3):
        if board[0][c] == board[1][c] == board[2][c] != " ":
            return True
    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True
    return False
def check_draws(board):
    for r in range(3):
        for c in range(3):
            if board[r][c] == " ":
                return False
    return True

def play_game():
    board = create_board()
    player = "X"

    while True:
        print_board(board)
        try:
            row = int(input(f"Player {player}, enter row (0-2): "))
            col = int(input(f"Player {player}, enter col (0-2): "))
        except ValueError:
            print("Invalid input. Please enter numbers 0, 1, or 2.")
            continue

        if not check_if_valid(board, row, col):
            print("Invalid move. Try again.")
            continue

        board[row][col] = player

        if check_wins(board):
            print_board(board)
            print(f"Player {player} wins!")
            break
        if check_draws(board):
            print_board(board)
            print("It's a draw!")
            break

        player = "O" if player == "X" else "X"
play_game()