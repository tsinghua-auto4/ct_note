import sys
from collections import deque

input = sys.stdin.readline
def if_inrange(x, y, z):
    global n, m
    if 0 <= x < n and 0 <= y < m and 0 <= z < h:
        return True
    return False

def solution():
    global graph, ans

    move  = [[0, -1, 0], [0, 1, 0], [-1, 0, 0], [1, 0, 0], [0, 0, -1], [0, 0, 1]]
    queue = deque([])
    for k in range(h):
        for i in range(n):
            for j in range(m):
                if graph[k][i][j] == 1:
                    queue.append([i, j, k]) 

    while queue:
        cx, cy, cz = queue.popleft()

        for nxt in move:
            nx, ny, nz = cx + nxt[0], cy + nxt[1], cz + nxt[2]
            if if_inrange(nx, ny, nz) and graph[nz][nx][ny] == 0:
                graph[nz][nx][ny] = graph[cz][cx][cy] + 1
                ans = max(graph[nz][nx][ny], ans)
                queue.append([nx, ny, nz])


if __name__ == "__main__":
    m, n, h  = map(int, input().split())
    graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
    ans   = 0

    solution()
    for k in graph:
        for i in k:
            for j in i:
                if j == 0:
                    print(-1)
                    exit()
    if ans == 0:
        print(ans)
    else:
        print(ans-1)