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
    pass



# Function for asking the player for a move
def ask_for_move(board, symbol):
    pass


# Function for checking if someone has won
def check_winner(board, symbol):
    pass


# Function for checking if the game is a draw
def is_draw(board):
    pass


# Function that runs one complete game
def play_game():
    pass


if __name__ == "__main__":
    play_game()
if __name__ == "__main__":
    # Start a new round of Tic-tac-toe
    print("Welcome to a new round of Tic-Tac-Toe!")
