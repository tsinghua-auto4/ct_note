import sys

def solution(x, y, z):
    global ans
    cur = paper[x][y]

    for i in range(x, x+z):
        for j in range(y, y+z):
            if paper[i][j] != cur:
                for m in range(3):
                    for n in range(3):
                        solution(x+m*z//3, y+n*z//3, z//3)
                return
    
    ans[cur+1] += 1


n     = int(sys.stdin.readline().rstrip())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
ans   = [0, 0, 0]

solution(0, 0, n)
[print(cur) for cur in ans]