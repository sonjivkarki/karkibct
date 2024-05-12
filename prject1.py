def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    for row in board:
        if row.count(row[0]) == 3 and row[0] != ' ':
            return True

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return True

    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return True

    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return True

    return False

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print_board(board)

    player = 'X'
    while True:
        row = int(input(f"Player {player}, enter row (0, 1, 2): "))
        col = int(input(f"Player {player}, enter column (0, 1, 2): "))

        if board[row][col] == ' ':
            board[row][col] = player
        else:
            print("That position is already taken!")
            continue

        print_board(board)

        if check_winner(board):
            print(f"Player {player} wins!")
            break

        if all(board[i][j] != ' ' for i in range(3) for j in range(3)):
            print("It's a tie!")
            break

        player = 'O' if player == 'X' else 'X'

if __name__ == "__main__":
    tic_tac_toe()
