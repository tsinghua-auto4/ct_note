import sys
sys.setrecursionlimit(10**7)

def dfs(cr: int, cc: int):
    global color_max, visit, graph, N, move
    color_max = max(1, color_max)

    for dr, dc in move:
        nr, nc = cr+dr, cc+dc

        if not(0 <= nr < N and 0 <= nc < N) or graph[nr][nc] != 'X':
            continue
        
        if visit[nr][nc] == 0:
            visit[nr][nc] = -visit[cr][cc]
            dfs(nr,nc)
            color_max = max(color_max, 2)
        elif visit[nr][nc] == visit[cr][cc]:
                color_max = max(color_max, 3)
                return


N     = int(input())
visit = [[0]*N for _ in range(N)]
graph = [list(input()) for _ in range(N)]

move  = ((-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0))

color_max = 0

for r in range(N):
    for c in range(N):
        if not (graph[r][c] == 'X' and visit[r][c] == 0):
            continue
        visit[r][c] = 1
        dfs(r, c)

print(color_max)