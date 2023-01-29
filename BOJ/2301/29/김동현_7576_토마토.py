import sys
from collections import deque

input = sys.stdin.readline
def if_inrange(x, y):
    global n, m
    if 0 <= x < n and 0 <= y < m:
        return True
    return False

def solution():
    global graph, ans

    move  = [[0, -1], [0, 1], [-1, 0], [1, 0]]
    queue = deque([])
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                queue.append([i, j]) 

    while queue:
        cx, cy = queue.popleft()

        for nxt in move:
            nx, ny = cx + nxt[0], cy + nxt[1]
            if if_inrange(nx, ny) and graph[nx][ny] == 0:
                graph[nx][ny] = graph[cx][cy] + 1
                ans = max(graph[nx][ny], ans)
                queue.append([nx, ny])


if __name__ == "__main__":
    m, n  = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    ans   = 0

    solution()
    for i in graph:
        for j in i:
            if j == 0:
                print(-1)
                exit()
    if ans == 0:
        print(ans)
    else:
        print(ans-1)
