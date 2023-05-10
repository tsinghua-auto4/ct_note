

N, M  = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

ans = 0

# top&bot은 언제나 같은 면적임
tmp = N*M
ans += tmp*2

# front&back은 언제나 같은 면적임
tmp = 0
for c in range(M):
    for r in range(N):
        if r == 0:
            tmp += graph[r][c]
        else:
            if graph[r-1][c] < graph[r][c]:
                tmp += graph[r][c] - graph[r-1][c]
ans += tmp*2

# left&right는 언제나 같은 면적임
tmp = 0
for r in range(N):
    for c in range(M):
        if c == 0:
            tmp += graph[r][c]
        else:
            if graph[r][c-1] < graph[r][c]:
                tmp += graph[r][c] - graph[r][c-1]
ans += tmp*2

print(ans)