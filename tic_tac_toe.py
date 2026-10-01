# In this script you can write your code.
# Start by writing all the functions.
# In the last part after if __name__ == "__main__": you can call the functions to play your game.
# If you run `uv run python tic_tac_toe.py` in the command line the game will start. Try it out! ;)

# Function for ... (displaying the board?)
def display_board(board):
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

# Function for choosing the symbols
def choose_symbols():
    symbol_1 = input("Spieler 1, willst du X oder O? ").upper()
    while symbol_1 not in ("X", "O"):
        symbol_1 = input("Bitte nur X oder O eingeben: ").upper()
    if symbol_1 == "X":
        symbol_2 = "O"
    else:
        symbol_2 = "X"
    return symbol_1, symbol_2



# Function for asking the player for a move
def ask_for_move(board, symbol):
    while True:
        position = int(input(f"Spieler {symbol}, welches Feld (1-9)? ")) - 1
        if board[position] in ("X", "O"):
            print("Das Feld ist schon belegt.")
        else:
            board[position] = symbol
            return

WINNING_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),   # Zeilen
    (0, 3, 6), (1, 4, 7), (2, 5, 8),   # Spalten
    (0, 4, 8), (2, 4, 6),              # Diagonale
    ]


# Function for checking if someone has won
def check_winner(board, symbol):
    for line in WINNING_LINES:
        if all(board[i] == symbol for i in line):
            return True
    return False

# Function for checking if the game is a draw
def is_draw(board):
    return all(field in ("X", "O") for field in board)


# Function that runs one complete game
def play_game():
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = choose_symbols()
    turn = 0

    while True:
        display_board(board)
        symbol = symbols[turn % 2]
        ask_for_move(board, symbol)

        if check_winner(board, symbol):
            display_board(board)
            print(f"Spieler {symbol} hat gewonnen!")
            break

        if is_draw(board):
            display_board(board)
            print("Unentschieden!")
            break

        turn += 1

if __name__ == "__main__":
    # Start a new round of Tic-tac-toe
    print("Welcome to a new round of Tic-Tac-Toe!")
    play_game()