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
    return 10, 10

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
    for i in range(int(row/3)*3, int(row/3)*3+3):
        for j in range(int(col/3)*3, int(col/3)*3+3):
            #print(i, j)
            if n == sudoku[i][j]:
                return False
            
    return True

def solver(sudoku):
    n, m = find_empty(sudoku)
#    print(n, m)
    if n == 10 and m == 10:
        print_board(sudoku)
        exit()
    for i in range(1,10):
        if valid(sudoku, n, m, i) == True:
            sudoku[n][m] = i
        #    print(n, m, i)
        #    print_board(sudoku)
            solver(sudoku)
    sudoku[n][m] = 0
    return


print_board(board)
#print(find_empty(board))
#print(find_row(board, 4, 4, 2))
#print(find_col(board, 6, 3, 1))
#print(find_full(board, 1, 1, 3))
solver(board)

