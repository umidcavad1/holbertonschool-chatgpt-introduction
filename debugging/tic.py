def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # rows
    for row in board:
        if row[0] != " " and row.count(row[0]) == 3:
            return row[0]

    # columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    # diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    moves = 0

    while True:
        print_board(board)

        try:
            row = int(input(f"Enter row (0-2) for player {player}: "))
            col = int(input(f"Enter col (0-2) for player {player}: "))

            if row not in range(3) or col not in range(3):
                print("Invalid position! Try again.")
                continue

            if board[row][col] != " ":
                print("That spot is already taken! Try again.")
                continue

            board[row][col] = player
            moves += 1

            winner = check_winner(board)
            if winner:
                print_board(board)
                print(f"Player {winner} wins!")
                break

            if moves == 9:
                print_board(board)
                print("It's a draw!")
                break

            player = "O" if player == "X" else "X"

        except ValueError:
            print("Please enter numbers only.")

tic_tac_toe()
