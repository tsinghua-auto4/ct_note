import sys
sys.setrecursionlimit(10**5)

def dfs(cur):
    global cnt
    visit[cur] = cnt
    for iter in graph[cur]:
        if visit[iter] == 0:
            cnt += 1
            dfs(iter)

N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
visit = [0 for _ in range(N+1)]

cnt = 1

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for iter in range(N+1):
    graph[iter].sort()

dfs(R)

for iter in range(1, N+1):
    print(visit[iter])