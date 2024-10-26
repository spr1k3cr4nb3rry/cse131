# Name: Izzie Vazquez
# Assignment Name: Lab 06: Sudoku Program
# Assignment Description: 
#   -  Extend the program from Lab 05 so it both plays the game of Sudoku and enforces the rules. To receive full credit, it must do the following:
#       1) Invalid input:Recognize if the user types something other than a coordinate or the letter 'Q' to quit
#       2) Reversed coordinates: Handle both "B2" and "2B" in the same way
#       3) Lowercase coordinates: Handle both "B2" and "b2" in the same way
#       4) Invalid number: Warn the user if an invalid number such as 0 or 11 is entered into the board
#       5) Square already filled: Warn the user if the selected square already has a number
#       6) Unique Row: Recognize if the user's number is already present on the selected row
#       7) Unique Column: Recognize if the user's number is already present on the selected column
#       8) Unique Inside Square: Recognize if the user's number is already present on the selected inside square
# Reflection:
#   - The hardest part of this for me was creating test cases, actually! I wasn't too sure which ones I should write down in my PDF, and which ones I should present in my video, so it took me a minute to finish my PDF!
# Time taken:
#   - Approximately 3 hours.

import json
import os

def load_board(filename):
    """Load a Sudoku board from a JSON file."""
    if not os.path.exists(filename):
        print("File not found. Please check the filename and try again.")
        return None
    with open(filename, 'r') as file:
        data = json.load(file)
    return data['board']

def save_board(filename, board):
    """Save a Sudoku board to a JSON file."""
    with open(filename, 'w') as file:
        json.dump({"board": board}, file, indent=4)

def display_board(board):
    """Display the Sudoku board with coordinates and formatted layout."""
    print("   A B C   D E F   G H I")
    for i, row in enumerate(board):
        row_display = []
        for j, num in enumerate(row):
            row_display.append("." if num == 0 else str(num))
            if j in [2, 5]:
                row_display.append("|")
        print(f"{i+1}  {' '.join(row_display)}")
        if i in [2, 5]:
            print("   -----+-----+-----")
    print()

def coordinate_to_index(coordinate):
    """Convert a board coordinate into row/column indices."""
    columns = "ABCDEFGHI"
    # Standardize input by making uppercase and handling both "B2" and "2B" formats
    coordinate = coordinate.upper().replace(" ", "")
    if len(coordinate) == 2:
        if coordinate[0] in columns and coordinate[1].isdigit():
            col = columns.index(coordinate[0])
            row = int(coordinate[1]) - 1
        elif coordinate[1] in columns and coordinate[0].isdigit():
            col = columns.index(coordinate[1])
            row = int(coordinate[0]) - 1
        else:
            print("Invalid coordinate format. Please enter a letter followed by a number (e.g., 'B2').")
            return None
        if 0 <= row <= 8 and 0 <= col <= 8:
            return row, col
    print("Invalid coordinate. Please enter a valid coordinate (e.g., 'B8').")
    return None

def get_player_move(board):
    """Get a valid player move in the form of a coordinate and number."""
    while True:
        coordinate = input("Specify a coordinate to edit or 'Q' to save and quit\n> ").strip().upper()
        if coordinate == 'Q':
            return 'Q', None, None, None
        index = coordinate_to_index(coordinate)
        if index:
            row, col = index
            # Check if square is already filled
            if board[row][col] != 0:
                print("Square already filled. Choose an empty square.")
                continue
            try:
                num = int(input(f"What number goes in {coordinate}? "))
                # Check if num is valid and within range
                if not (1 <= num <= 9):
                    print("Invalid number. Please enter a number between 1 and 9.")
                    continue
                # Check row, column, and square uniqueness
                if num in board[row]:
                    print("Number already exists in this row. Try a different number.")
                    continue
                if num in [board[r][col] for r in range(9)]:
                    print("Number already exists in this column. Try a different number.")
                    continue
                if num in get_subsquare(board, row, col):
                    print("Number already exists in this square. Try a different number.")
                    continue
                return 'M', row, col, num
            except ValueError:
                print("Invalid input. Please enter a valid number between 1 and 9.")

def get_subsquare(board, row, col):
    """Get all numbers in the 3x3 subsquare of the specified cell."""
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    return [board[r][c] for r in range(start_row, start_row + 3) for c in range(start_col, start_col + 3)]

def make_move(board, row, col, num):
    """Update the board with the player's move."""
    board[row][col] = num

def main():
    filename = input("Enter filename to load board: ")
    board = load_board(filename)
    if board is None:
        return
    print("\nWelcome to Sudoku! Here’s your board:")
    display_board(board)
    while True:
        move_type, row, col, num = get_player_move(board)
        if move_type == 'Q':
            save_filename = input("Enter filename to save board: ")
            save_board(save_filename, board)
            print("Board saved. See you later!")
            break
        elif move_type == 'M':
            make_move(board, row, col, num)
            display_board(board)

if __name__ == "__main__":
    main()
