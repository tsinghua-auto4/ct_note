from collections import deque

def bfs(q: deque):
    global N, M, graph, move

    queue = q
    while queue:
        cr, cc = queue.popleft()
        for dr, dc in move:
            nr, nc = cr+dr, cc+dc
            if not (0 <= nr < N and 0 <= nc < M):
                continue
            if graph[nr][nc] == 0:
                graph[nr][nc] = graph[cr][cc]+1
                queue.append([nr, nc])


N, M  = map(int, input().split())
graph = []
shark = deque()
for _ in range(N):
    row = list(map(int, input().split()))
    graph.append(row)
    for col in range(M):
        if row[col] == 1:
            shark.append([_, col])

move = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
bfs(shark)

ans = -1
for r in graph:
    ans = max(ans, max(r))
print(ans-1)
# print(max(map(max, graph))-1)