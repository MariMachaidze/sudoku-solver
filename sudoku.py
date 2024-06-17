board = [
    [6, 0, 0, 0, 0, 0, 0, 0, 8],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 6, 9, 7, 4, 0],
    [0, 0, 0, 0, 4, 0, 0, 8, 0],
    [0, 4, 5, 1, 7, 0, 0, 9, 0],
    [0, 8, 0, 0, 9, 3, 4, 5, 0],
    [0, 9, 0, 0, 5, 0, 0, 0, 0],
    [0, 1, 7, 8, 2, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 3]
]

def print_board(sudoku):

    print()
    for i in range(len(sudoku)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")

        for j in range(len(sudoku)):
            if j % 3 == 0 and j != 0:
                print("| " , end="")

            if j == 8:
                print(sudoku[i][j])
            else:
                print(str(sudoku[i][j]) + " ", end="")
    print()

def find_empty(sudoku):

    for i in range(len(sudoku)):
        for j in range (len(sudoku)):
            if sudoku[i][j] == 0:
                return (i, j) #row, col
    return None

def valid(sudoku, row, col, n):
    
    # Row
    for i in range(len(board)):
        if n == sudoku[i][col]:
            return False
        
    # Column
    for j in range(len(board)):
        if n == sudoku[row][j]:
            return False
    return True

    # Box
    for i in range(row//3*3, row//3*3+3):
        for j in range(col//3*3, col//3*3+3):
            #print(i, j)
            if n == sudoku[i][j]:
                return False
            
    return True

def solver(sudoku):
    
    if not find_empty(sudoku):
        return True

    n, m = find_empty(sudoku) 

    for i in range(1,10):
        if valid(sudoku, n, m, i):
            sudoku[n][m] = i
        #    print(n, m, i)
        #    print_board(sudoku)
            if solver(sudoku):
                return True
    sudoku[n][m] = 0
    return False


print_board(board)
solver(board)
print_board(board)
