import tkinter as tk
from tkinter import messagebox
import boardLogic
import sudokuHelper

class SudokuGUI:
    def __init__(self, root):
        self.root = root
        # Set the window title to "Sudoku Master"
        self.root.title("Sudoku Master")
        # Set the size of the window to 540x600 pixels
        self.root.geometry("540x600")
        # Create a 9x9 grid to store the cell Entry widgets
        self.cells = [[None for _ in range(9)] for _ in range(9)]
        self.create_widgets()

    def create_widgets(self):
        # Create a canvas widget for drawing the grid
        self.canvas = tk.Canvas(self.root, width=500, height=450)
        self.canvas.grid(row=0, column=0, padx=20, pady=20)
        self.frame = tk.Frame(self.canvas)
        self.frame.pack()
        self.canvas.create_window((0, 0), window=self.frame, anchor="nw")
        self.create_grid()
        self.create_buttons()
        self.draw_grid_lines()

    def validate_input(self, value):
        # Check if the value is a single digit
        if value.isdigit() and len(value) <= 1:
            # Accept the input
            return True
        # Check if the value is empty (allowing clearing the cell)
        elif value == "":
            return True
        else:
            # Reject the input
            return False

    def create_grid(self):
        # Register the input validation function
        vcmd = (self.root.register(self.validate_input), '%P')
        for i in range(9):
            for j in range(9):
                # Create an Entry widget
                cell = tk.Entry(self.frame, width=2, justify='center', font=('Arial', 18), borderwidth=2,
                                relief='ridge', validate='key', validatecommand=vcmd)
                # Place the Entry widget in the grid
                cell.grid(row=i, column=j, padx=2, pady=2, ipadx=10, ipady=10)
                # Store a reference to the Entry widget
                self.cells[i][j] = cell

    def create_buttons(self):
        button_frame = tk.Frame(self.root)
        # Place the frame below the grid with padding
        button_frame.grid(row=1, column=0, pady=10)

        solve_button = tk.Button(button_frame, text="Solve", command=self.solve, font=('Arial', 14), width=10)
        solve_button.grid(row=0, column=0, padx=5)

        clear_button = tk.Button(button_frame, text="Clear", command=self.clear, font=('Arial', 14), width=10)
        clear_button.grid(row=0, column=1, padx=5)

    def draw_grid_lines(self):
        # Loop from 0 to 9 to draw 10 lines (including the edges)
        for i in range(10):
            # Use black for thicker lines (every 3rd line), gray otherwise
            color = "black" if i % 3 == 0 else "gray"

            x0 = i * 50
            y0 = 0
            x1 = i * 50
            y1 = 450
            # Draw vertical lines
            self.canvas.create_line(x0, y0, x1, y1, fill=color, width=2)

            x0 = 0
            y0 = i * 50
            x1 = 450
            y1 = i * 50
            # Draw horizontal lines
            self.canvas.create_line(x0, y0, x1, y1, fill=color, width=2)

    def get_board(self):
        # Create an empty board
        board_values = boardLogic.create_empty_board()
        # Loop through each row
        for i in range(9):
            # Loop through each column
            for j in range(9):
                # Get the value from the Entry widget
                value = self.cells[i][j].get()
                # Check if the value is a digit
                if value.isdigit():
                    # Convert the value to an integer and store it in the board
                    board_values[i][j] = int(value)
                else:
                    # If the value is not a digit, store 0
                    board_values[i][j] = 0
        # Return the grid of integers
        return board_values

    # If a cell in the grid contains a zero, it clears the corresponding Entry widget, otherwise,
    # it sets the Entry widget to the corresponding number.
    def set_board(self, board_values):
        for i in range(9):
            for j in range(9):
                # Get the value from the board at position [i][j]
                value = board_values[i][j]
                # Clear any existing value in the Entry widget
                self.cells[i][j].delete(0, tk.END)
                # Check if the value is not zero
                if value != 0:
                    # Insert the value into the Entry widget as a string
                    self.cells[i][j].insert(0, str(value))

    # Attempt to solve the puzzle. Also display message to indicate if the puzzle was solved or is broken.
    def solve(self):
        # Get the current board values from the Entry widgets
        board_values = self.get_board()
        if not self.is_valid(board_values):
            messagebox.showinfo("Error", "Sudoku is broken")
            return
        # Try to solve the Sudoku puzzle
        if sudokuHelper.solve_sudoku(board_values):
            # Update the Entry widgets with the solved board
            self.set_board(board_values)
            # Show a success message if the puzzle was solved
            messagebox.showinfo("Solved", "Sudoku was solved")
        else:
            # Show an error message if the puzzle cannot be solved
            messagebox.showinfo("Error", "Sudoku cannot be solved")

    # Checks for the suduko rules if are valid by ensuring that there are no duplicate numbers in any row,
    # column, or 3x3 subgrid.
    def is_valid(self, board_values):
        # Check each row and column for duplicate numbers
        for i in range(9):
            row = set()  # Create a set to keep track of numbers in the current row
            col = set()  # Create a set to keep track of numbers in the current column
            for j in range(9):
                # Ignore empty cells (value 0)
                if board_values[i][j] != 0:
                    # If the number is already in the row, it's invalid
                    if board_values[i][j] in row:
                        return False
                    row.add(board_values[i][j])  # Add the number to the row set
                # Check the current column
                if board_values[j][i] != 0:
                    #If the number is already in the column, it's invalid
                    if board_values[j][i] in col:
                        return False
                    col.add(board_values[j][i])  # Add the number to the column set

        # Check each 3x3 subgrid for duplicate numbers
        for box_row in range(3):  # Loop over each row of subgrids
            for box_col in range(3):  # Loop over each column of subgrids
                box = set()
                for i in range(3):
                    for j in range(3):
                        # Get the number in the subgrid
                        num = board_values[box_row * 3 + i][box_col * 3 + j]
                        # Ignore empty cells (value 0)
                        if num != 0:
                            # If the number is already in the subgrid, it's invalid
                            if num in box:
                                return False
                            box.add(num)
        # If no duplicates are found, return True indicating the board is valid
        return True

    # Clears all the values in the Sudoku grid by deleting the content of each Entry widget.
    def clear(self):
        for i in range(9):
            for j in range(9):
                # Delete the content of the Entry widget at position [i][j]
                self.cells[i][j].delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuGUI(root)
    root.mainloop()
