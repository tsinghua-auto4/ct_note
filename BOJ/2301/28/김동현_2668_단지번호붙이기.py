import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def if_inrange(x, y):
    global n
    if 0 <= x and x < n:
        if 0 <= y and y < n:
            return True
    return False

def solution(x, y):
    global ans, mark
    if map[x][y] == 0:
        return
    ans += 1
    map[x][y] = 0

    move = [[0, -1], [0, 1], [-1, 0], [1, 0]]
    for next in move:
        nx, ny = next[0] + x, next[1] + y
        if if_inrange(nx, ny) and not mark[nx][ny]:
            mark[nx][ny] = True
            solution(nx, ny)



if __name__ == "__main__":
    n    = int(input())
    map  = [list(map(int, input().rstrip())) for _ in range(n)]
    mark = [[False]*n for _ in range(n)]
    
    ans  = 0
    quantity = []

    for i in range(n):
        for j in range(n):
            solution(i, j)
            if ans != 0:
                quantity.append(ans)
                ans = 0
    quantity.sort()
    print(len(quantity))
    for i in quantity:
        print(i)