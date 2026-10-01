# Tic-Tac-Toe for two players in the command line.
# Start with: uv run python tic_tac_toe.py

# The 8 ways to win: 3 rows, 3 columns, 2 diagonals (as list indices 0-8)
WIN_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6),
]


def create_board():
    """Return an empty board: a list with 9 empty fields."""
    board = []
    for i in range(9):
        board.append(" ")
    return board


def display_board(board):
    """Print the board. Empty fields show their number (1-9)."""
    for i in range(9):
        if board[i] == " ":
            print(i + 1, end=" ")
        else:
            print(board[i], end=" ")
        if i % 3 == 2:
            print()


def choose_symbols():
    """Let player 1 pick X or O. Return the symbols of player 1 and 2 as a list."""
    symbol = input("Player 1, choose X or O: ").upper()
    if symbol == "O":
        return ["O", "X"]
    else:
        return ["X", "O"]


def ask_move(board, player, symbol):
    """Ask the player for a free field (1-9). Return its index (0-8)."""
    while True:
        field = int(input(f"Player {player} ({symbol}), choose a field: ")) - 1
        if board[field] == " ":
            return field
        print("This field is taken, try again.")


def has_won(board, symbol):
    """Return True if the symbol has three in a row, otherwise False."""
    for a, b, c in WIN_LINES:
        if board[a] == symbol and board[b] == symbol and board[c] == symbol:
            return True
    return False


def is_draw(board):
    """Return True if all fields are filled, otherwise False."""
    if " " in board:
        return False
    else:
        return True


# Tic-tac-toe game
if __name__ == "__main__":
    print("Welcome to a new round of Tic-Tac-Toe!")
    board = create_board()
    symbols = choose_symbols()
    turn = 0

    while True:
        display_board(board)
        player = turn % 2
        symbol = symbols[player]
        field = ask_move(board, player + 1, symbol)
        board[field] = symbol

        if has_won(board, symbol):
            display_board(board)
            print(f"Player {player + 1} ({symbol}) wins!")
            break
        if is_draw(board):
            display_board(board)
            print("It's a draw!")
            break
        turn += 1
