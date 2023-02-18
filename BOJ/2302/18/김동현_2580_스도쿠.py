import sys

def checkR(x, value): #row
    for i in range(9):
        if sudoku[x][i] == value:
            return False
    return True

def checkC(y, value): #col
    for i in range(9):
        if sudoku[i][y] == value:
            return False
    return True

def checkS(x, y, value): #square
    nx, ny = x//3*3, y//3*3
    for i in range(3):
        for j in range(3):
            if sudoku[nx+i][ny+j] == value:
                return False
    return True

def solution(depth): #dfs
    if depth == len(blank):
        for i in range(9):
            print(*sudoku[i])
        exit(0)
    else:
        cx, cy = blank[depth]
        for i in range(1, 10):
            if checkR(cx, i) and checkC(cy, i) and checkS(cx, cy, i):
                sudoku[cx][cy] = i
                solution(depth+1)
                sudoku[cx][cy] = 0


sudoku  = []
blank   = []
for i in range(9):
    sudoku.append(list(map(int, sys.stdin.readline().split())))
    for j in range(9):
        if sudoku[i][j] == 0:
            blank.append((i,j))

solution(0)