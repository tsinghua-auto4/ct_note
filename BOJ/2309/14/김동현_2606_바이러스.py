from collections import deque

N = int(input())
M = int(input())
visit = [0 for _ in range(N+1)]
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque([1])
visit[1] = 1
while queue:
    cur = queue.popleft()
    for node in graph[cur]:
        if visit[node] == 0:
            queue.append(node)
            visit[node] = 1
print(sum(visit)-1)