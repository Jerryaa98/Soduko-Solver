board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def printBoard(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(board)):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

def findEmpty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if (board[i][j] == 0):
                return(i , j)
    return None

def  Valid(board, num, position):
    # row check
    for i in range(len(board[0])):
        if board[position[0]][i] == num and position[1] != i:
            return False
    # column check
    for i in range(len(board)):
        if board[i][position[1]] == num and position[0] != i:
            return False
    # 3x3 square check
    xBox = position[1] // 3
    yBox = position[0] // 3

    for i in range(yBox * 3, yBox * 3 + 3):
            for j in range(xBox * 3, xBox * 3 + 3):
                if (board[i][j] == num and position != (i,j)):
                    return False
    return True

def  Solve (board):
    find = findEmpty(board)
    if not find:
        return True
    else:
        row , col = find

    for i in range(1,10):
        if Valid(board, i, (row, col)):
            board[row][col] = i

            if Solve(board):
                return True

            board[row][col] = 0

    return False

printBoard(board)
Solve(board)
print("---------------------------------------")
printBoard(board)
