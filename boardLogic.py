
#Creates and returns an empty 9x9 board full of 0
def create_empty_board():
    sudoku_board = []
    # Loop 9 times for creating 9 rows
    for _ in range(9):
        # Create a row with 9 zeros
        row = [0] * 9
        # Add the row to the board
        sudoku_board.append(row)
    print("Debug: Created empty board")
    return sudoku_board

#Converts the 9x9 board to a string, with rows and columns.
def board_to_string(board):
    sudoku_board_string = []
    # Loop through each row in the board
    for row in board:
        # Convert each row to a string
        row_string = ' '.join(map(str, row))
        # Add the row string to the list
        sudoku_board_string.append(row_string)
        # Join all row strings with newlines
    return '\n'.join(sudoku_board_string)

# Converts a string representation of a Sudoku board back to a 9x9 grid of integers.
def string_to_board(board_string):
    # Split the string into lines based on newlines
    lines = board_string.strip().split('\n')
    # Initialize an empty list to hold the rows
    board = []
    for line in lines:
        # Convert each line to a list of integers
        row = list(map(int, line.split()))
        # Add the row to the sudoku board
        board.append(row)
    return board

# Example usage
if __name__ == "__main__":
    empty_board = create_empty_board()
    print("Empty board:")
    print(board_to_string(empty_board))

    board_str = board_to_string(empty_board)
    print("\nBoard as String:")
    print(board_str)

    converted_board = string_to_board(board_str)
    print("\nConverted Board:")
    print(board_to_string(converted_board))
