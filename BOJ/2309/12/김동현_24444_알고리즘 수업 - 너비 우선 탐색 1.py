from collections import deque

def bfs(R):
    cnt      = 1
    q        = deque([R])
    visit[R] = 1
    while q:
        v = q.popleft()
        for g in graph[v]:
            if visit[g] == 0:
                cnt += 1
                visit[g] = cnt
                q.append(g)


N, M, R = map(int, input().split())

visit = [0 for _ in range(N+1)]
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for iter in range(N+1):
    graph[iter].sort()

bfs(R)
for iter in visit[1:]:
    print(iter)