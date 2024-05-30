
def is_valid(board, row, col, num):
    # Check if 'num' is not in the current row and column
    for i in range(9):
        # Check if 'num' is already in the current row / column
        if board[row][i] == num or board[i][col] == num:
            return False

    # Calculate the starting indices of the 3x3 subgrid containing the cell (row, col)
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    # Check if 'num' is not in the current 3x3 subgrid
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                # If found, return False because the placement is invalid
                return False
    # If 'num' is not found in the row, column, or subgrid, return True
    return True

def solve_sudoku(board):
    # Find the next empty cell on the board
    empty = find_empty(board)
    if not empty:
        # Return True because the board is completely filled
        return True
    # Get the row and column index of the empty cell
    row, col = empty

    # Try placing numbers 1 to 9 in the empty cell
    for num in range(1, 10):
        # Check if placing 'num' in the cell is valid
        if is_valid(board, row, col, num):
            # Place the number in the cell
            board[row][col] = num
            # Recursively try to solve the rest of the board
            if solve_sudoku(board):
                # If the board is solved, return True
                return True
            # Reset the cell (backtrack) and try the next number
            board[row][col] = 0  # Reset and backtrack
    return False

def find_empty(board):
    # Loop through each row (i goes from 0 to 8)
    for i in range(9):
        # Loop through each column (j goes from 0 to 8)
        for j in range(9):
            # Check if the cell at position (i, j) is empty (contains 0)
            if board[i][j] == 0:
                return (i, j)
    # If no empty cells are found, return None
    return None


# Example usage
if __name__ == "__main__":
    board = [
        [1, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 4]
    ]

    if solve_sudoku(board):
        print("Sudoku solved successfully!")
        for row in board:
            print(row)
    else:
        print("No solution exists")
