import sys
sys.setrecursionlimit(10**9)

def dfs(graph, M, N, r, c):
    move  = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    graph[r][c] = 0
    for dr, dc in move:
        nr, nc = r+dr, c+dc
        if not (0 <= nr < M) or not (0 <= nc < N):
            continue
        if graph[nr][nc] == 1:
            dfs(graph, M, N, nr, nc)

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    graph   = [[0 for _ in range(N)] for _ in range(M)]
    for _ in range(K):
        r, c= map(int, sys.stdin.readline().split())
        graph[r][c] = 1
    worm = 0
    for r in range(M):
        for c in range(N):
            if graph[r][c] == 1:
                worm += 1
                dfs(graph, M, N, r, c)

    sys.stdout.write(str(worm)+'\n')