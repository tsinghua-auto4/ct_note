

def dfs(x: int, y: int, depth: int, sum: int):
    global ans
    if depth == K:
        ans = max(ans, sum)
        return
    else:
        for i in range(x, N):
            for j in range(y if i == x else 0, M):
                if [i, j] not in memory:
                    if ([i + 1, j] not in memory) and ([i - 1, j] not in memory) and ([i, j + 1] not in memory) and ([i, j - 1] not in memory):
                        memory.append([i, j])
                        dfs(i, j, depth + 1, sum +graph[i][j])
                        memory.pop()


N, M, K = map(int, input().split())
graph  = [list(map(int, input().split())) for _ in range(N)]
memory = []
ans = -1e10
dfs(0, 0, 0, 0)
print(ans)