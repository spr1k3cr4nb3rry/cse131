import json

# Load the Sudoku board from a file
def load_board(filename):
    with open(filename, 'r') as file:
        game_data = json.load(file)
        return game_data['board']

# Save the Sudoku board to a file
def save_board(board, filename):
    game_data = {'board': board}
    with open(filename, 'w') as file:
        json.dump(game_data, file)

# Display the current Sudoku board
def display_board(board):
    print("Current Sudoku Board:")
    for row in board:
        print(" ".join(str(num) if num != 0 else "." for num in row))
    print()

# Validate the user's move (check row, column, and 3x3 subgrid)
def validate_move(board, row, col, number):
    # Check if number is already in the row
    for i in range(9):
        if board[row][i] == number:
            return False
    
    # Check if number is already in the column
    for i in range(9):
        if board[i][col] == number:
            return False
    
    # Check if number is already in the 3x3 grid
    grid_row_start = (row // 3) * 3
    grid_col_start = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[grid_row_start + i][grid_col_start + j] == number:
                return False
    
    # If no conflicts, the move is valid
    return True

# Check if the game is finished (no empty squares left)
def check_game_finished(board):
    for row in board:
        if 0 in row:
            return False
    return True

# Main game loop to interact with the user
def main():
    # Prompt the user for the filename to load
    filename = input("Enter the filename of the saved Sudoku game (e.g., 'myGame.txt'): ")
    board = load_board(filename)
    
    while True:
        display_board(board)
        
        # Check if the game is finished
        if check_game_finished(board):
            print("Congratulations! You have completed the Sudoku puzzle!")
            break
        
        # Get user input for the move
        print("Enter your move (row, column, number).")
        try:
            row = int(input("Row (1-9): ")) - 1
            col = int(input("Column (1-9): ")) - 1
            number = int(input("Number (1-9): "))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue
        
        # Check for valid input ranges
        if row not in range(9) or col not in range(9) or number not in range(1, 10):
            print("Invalid row, column, or number. Please try again.")
            continue
        
        # Check if the move is valid
        if board[row][col] != 0:
            print("That square is already filled. Please choose another one.")
        elif validate_move(board, row, col, number):
            board[row][col] = number
            print(f"Move ({number}) placed at row {row+1}, column {col+1}.")
        else:
            print(f"Invalid move! You cannot place {number} at row {row+1}, column {col+1}.")
        
        # Ask the user if they want to save and exit
        save_exit = input("Do you want to save the game and exit? (y/n): ").lower()
        if save_exit == 'y':
            save_filename = input("Enter the filename to save the game: ")
            save_board(board, save_filename)
            print(f"Game saved to {save_filename}. Exiting...")
            break

# Run the Sudoku game
if __name__ == "__main__":
    sudoku_game()
