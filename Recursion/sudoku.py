def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


def is_valid_move(board, row, col, num):
    # Check row and column for the same number
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    # Check the 3x3 box for the same number
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True


def solve_sudoku(board):
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return True

    row, col = empty_cell

    for num in range(1, 10):
        if is_valid_move(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0

    return False


def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None


if __name__ == "__main__":
    # Example Sudoku board. Fill 0 for empty cells.
    sudoku_board = [
        [0, 4, 0, 2, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 9, 8, 3],
        [9, 5, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 1, 0, 7, 0, 0, 4],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [6, 8, 3, 0, 0, 0, 4, 0, 5],
        [0, 0, 0, 5, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 8, 0, 0],
    ]

    print("Sudoku Puzzle:")
    print_board(sudoku_board)

    if solve_sudoku(sudoku_board):
        print("\nSolution:")
        print_board(sudoku_board)
    else:
        print("\nNo solution exists for this Sudoku.")
