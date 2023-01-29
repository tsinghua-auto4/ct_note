import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def if_inrange(x, y):
    global n, m
    if 0 <= x < n and 0 <= y < m:
        return True
    return False

def solution(cnt, x, y, c, tx, ty):
    global graph, mark, move

    if cnt >= 4 and (x,y) == (tx,ty):
        print("Yes")
        exit()

    for nxt in move:
        nx, ny = x + nxt[0], y + nxt[1]
        if not if_inrange(nx, ny) or graph[nx][ny] != c:
            continue
        if not mark[nx][ny]:
            mark[nx][ny] = True
            solution(cnt + 1, nx, ny, c, tx, ty)
            mark[nx][ny] = False


if __name__ == "__main__":
    n, m  = map(int, input().split())
    graph = [list(map(str, input().rstrip())) for _ in range(n)]
    mark  = [[False]*m for _ in range(n)]
    move  = [[0, -1], [0, 1], [-1, 0], [1, 0]]

    for i in range(n):
        for j in range(m):
            solution(1, i, j, graph[i][j], i, j)
    print("No")