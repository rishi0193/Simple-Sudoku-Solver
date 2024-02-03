def print_sudoku(board):
    horizontal_line = "╔══════════╦══════════╦══════════╗"
    separator = "║ "
    
    print(horizontal_line)
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("╠══════════╬══════════╬══════════╣")
        for j in range(9):
            if j % 3 == 0 :
                print(separator, end="")
            num = board[i][j]
            if num == 0:
                print("   ", end="")
            else:
                print(f" {num} ", end="")
        print("║")
    print("╚══════════╩══════════╩══════════╝")

def is_valid_move(board, row, col, num):
    # Check if the number is not already present in the row and column
    if num in board[row] or num in [board[i][col] for i in range(9)]:
        return False
    
    # Check if the number is not already present in the 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    
    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid_move(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0  # Backtrack if the current move is invalid
                return False  # No valid number found for this cell
    return True  # All cells filled, Sudoku solved

# Example Sudoku puzzle (0 represents empty cells)
sudoku_board = [
    [0, 0, 0, 0, 0, 8, 0, 9, 0],
    [0, 0, 3, 0, 0, 1, 0, 0, 0],
    [2, 0, 0, 0, 0, 7, 6, 0, 0],
    [0, 0, 0, 0, 2, 0, 0, 0, 0],
    [0, 9, 4, 0, 8, 0, 2, 0, 0],
    [7, 1, 0, 0, 4, 0, 9, 0, 5],
    [1, 0, 0, 9, 0, 0, 5, 3, 0],
    [5, 7, 0, 0, 0, 0, 8, 4, 0],
    [0, 0, 0, 0, 0, 6, 0, 2, 1]
]

import time

start=time.time()
print("Initial Sudoku puzzle:")
print_sudoku(sudoku_board)
if solve_sudoku(sudoku_board):
    print("Sudoku solution:")
    print_sudoku(sudoku_board)
else:
    print("No solution exists for the given Sudoku puzzle.")
print("Time :",time.time()-start)