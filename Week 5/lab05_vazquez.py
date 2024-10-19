# Name: Izzie Vazquez
# Assignment Name: Lab 05: Sudoku Draft
# Assignment Description: 
#   -  Write a Python program that plays the game of Sudoku but does not enforce the rules. In this draft of the program, a player can place any number he or she wants in a given square. The program will be interactive, read from a file, and save data to a file. 
# Reflection:
#   - The hardest part of this week's lab for me was getting to formatting for the board right. I ended up having to look into the enumerate() function and browsing the W3Schools Python documentation for help getting the display_board() function just right.
# Time taken:
#   - Approximately 2 hours.

import json

def load_board(filename):
    """Load a Sudoku board from a JSON file."""
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
            if num == 0:
                row_display.append(" ")
            else:
                row_display.append(str(num))

            if j in [2, 5]:
                row_display.append("|")
        
        print(f"{i+1}  {' '.join(row_display)}")

        if i in [2, 5]:
            print("   -----+-----+-----")
    print()

def coordinate_to_index(coordinate):
    """Convert a board coordinates into row/column indices."""
    columns = "ABCDEFGHI"
    if len(coordinate) == 2 and coordinate[0] in columns and coordinate[1].isdigit():
        col = columns.index(coordinate[0])
        row = int(coordinate[1]) - 1
        if 0 <= row <= 8 and 0 <= col <= 8:
            return row, col
    print("Invalid coordinate. Please enter a valid coordinate (e.g., 'B8').")
    return None

def get_player_move():
    """Get a valid player move in the form of a coordinate and number."""
    while True:
        coordinate = input("Specify a coordinate to edit or 'Q' to save and quit\n> ").upper()
        if coordinate == 'Q':
            return 'Q', None, None, None
        index = coordinate_to_index(coordinate)
        if index:
            row, col = index
            try:
                num = int(input(f"What number goes in {coordinate}? "))
                if 1 <= num <= 9:
                    return 'M', row, col, num
                else:
                    print("Invalid number. Please enter a number between 1 and 9.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    
def make_move(board, row, col, num):
    """Update the board with the player's move."""
    board[row][col] = num

def main():
    filename = input("Enter filename to load board: ")
    board = load_board(filename)
    
    display_board(board)

    while True:
        move_type, row, col, num = get_player_move()

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
