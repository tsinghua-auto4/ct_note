from collections import deque

def bfs(r, c):
    global N, M, grid, visit

    q = deque([[r, c]])
    visit[r][c] = 0

    while q:
        cr, cc = q.popleft()

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = cr+dr, cc+dc
            if not (0 <= nr < N and 0 <= nc < M) or visit[nr][nc] != -1:
                continue
            if grid[nr][nc] == 0:
                visit[nr][nc] = 0
            elif grid[nr][nc] == 1:
                visit[nr][nc] = visit[cr][cc] + 1
                q.append([nr, nc])



N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

visit = [[-1]*M for _ in range(N)]

for r in range(N):
    for c in range(M):
        if grid[r][c] == 2 and visit[r][c] == -1:
            bfs(r, c)

for r in range(N):
    for c in range(M):
        if grid[r][c] == 0:
            print(0, end=' ')
        else:
            print(visit[r][c], end=' ')
    print()