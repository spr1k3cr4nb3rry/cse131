# Name: Izzie Vazquez
# Assignment Name: Lab 01: Tic-Tac-Toe
# Assignment Description:
#   - Tic-Tac-Toe, otherwise known as noughts and crosses, is a game played on a 3x3 grid where one player is represented with Xs and the other is represented with Os. The X player puts a mark in one of the nine grid locations. The O player then selects one of the eight remaining grid locations. The game continues until either one player gets three in a row or three diagonally. Write a program to represent the Tic-Tac-Toe game.
# Reflection:
#   - The hardest part of writing this assignment, believe it or not, was recording the video with the voice over. I ended up having to figure out Microsoft Clipchamp in order to record the test case demonstrations. I also struggled with remembering to add comments to my code, as I usually do not (which is a habit I need to lose). Sometimes I forget that I am not the only one who will be viewing my code, and that what makes sense in my brain may not make sense in the mind of, say, my professor or a teammate. Overall, though, I found the Tic-Tac-Toe lab pretty simple, but fun!
# Time taken: 
#   - Approximately 2 hours.

import json

# The characters used in the Tic-Tac-Toe board.
X = 'X'
O = 'O'
BLANK = ' '

# A blank Tic-Tac-Toe board.
blank_board = {  
            "board": [
                BLANK, BLANK, BLANK,
                BLANK, BLANK, BLANK,
                BLANK, BLANK, BLANK ]
        }

def read_board(filename):
    '''Read the previously existing board from the file if it exists.'''
    try:
        with open(filename, "r") as file:
            data = json.load(file)
        return data
    except FileNotFoundError: # If no board.json file is found, a blank board will be used instead.
        print("File not found. Blank board will be used.")
        return blank_board

def save_board(filename, board):
    '''Save the current game to a file.'''
    with open(filename, "w") as file:
        json.dump(board, file)

def display_board(board):
    '''Display a Tic-Tac-Toe board on the screen in a user-friendly way.'''
    board_list = board.get("board")
    print(f" {board_list[0]} | {board_list[1]} | {board_list[2]} ")
    print(f"---+---+---")
    print(f" {board_list[3]} | {board_list[4]} | {board_list[5]} ")
    print(f"---+---+---")
    print(f" {board_list[6]} | {board_list[7]} | {board_list[8]} \n")

def is_x_turn(board):
    '''Determine whose turn it is.'''
    x_turns = board["board"].count(X) # Counts how many Xs.
    o_turns = board["board"].count(O) # Counts how many Os.
    return x_turns == o_turns # If the number of Xs is equal to the number of Os, then it's X's turn. Else, it's O's turn.

def play_game(board):
    '''Play the game of Tic-Tac-Toe.'''
    while not game_done(board["board"], message = True): # Continue until game_done() returns True.
        display_board(board)

        x_turn = is_x_turn(board)
        if x_turn: print("X's turn")
        else: print("O's turn")

        move = input("Enter your move (1-9): ")

        if move == 'q': # Game is quit and saved for later.
            save_board("board.json", board)
            print("Game saved.")
            return
    
        move = int(move) - 1 # Adjust number for list indexing (starting at 0 vs. starting at 1).

        if board["board"][move] == BLANK: # Makes sure the space is blank before putting a mark down.
            board["board"][move] = X if x_turn else O
        else: print("Invalid move. Try again.")

    print("Game over.")

def game_done(board, message = False):
    '''Determine if the game is finished. If message == True, then display a message to the user. Otherwise, no message is displayed. '''
    # Game is finished if someone has completed a row.
    for row in range(3):
        if board[row * 3] != BLANK and board[row * 3] == board[row * 3 + 1] == board[row * 3 + 2]:
            if message:
                print("The game was won by", board[row * 3])
            return True

    # Game is finished if someone has completed a column.
    for col in range(3):
        if board[col] != BLANK and board[col] == board[3 + col] == board[6 + col]:
            if message:
                print("The game was won by", board[col])
            return True

    # Game is finished if someone has a diagonal.
    if board[4] != BLANK and (board[0] == board[4] == board[8] or
                              board[2] == board[4] == board[6]):
        if message:
            print("The game was won by", board[4])
        return True

    # Game is finished if all the squares are filled.
    tie = True
    for square in board:
        if square == BLANK:
            tie = False
    if tie:
        if message:
            print("The game is a tie!")
        return True

    return False

def main():
    '''The entry point for the Tic-Tac-Toe game.'''
    global board # 'board' should be accessible by all functions.

    choice = input("Load previous game? (y/n) ")
    if choice == "y": 
        # This code is meant to work with a preexisting board.json file. board.json initially contains a blank board.
        board = read_board("board.json")
    else:
        board = blank_board
    
    print("Enter 'q' to suspend your game. Otherwise, enter a number from 1 to 9")
    print("where the following numbers correspond to the locations on the grid:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 \n")

    print("The current board is:")
    play_game(board)

if __name__ == "__main__":
    main()