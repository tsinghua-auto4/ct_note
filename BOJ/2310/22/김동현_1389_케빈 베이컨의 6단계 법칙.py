from collections import deque

def bfs(grid, cur):
    global N, M

    num   = [0]*(N+1)
    visit = [cur]

    q = deque([cur])
    while q:
        node = q.popleft()
        for iter in grid[node]:
            if iter in visit:
                continue
            num[iter] = num[node]+1
            visit.append(iter)
            q.append(iter)
    return sum(num)


N, M = map(int, input().split())

grid = [[] for _ in range(N+1)]
for _ in range(M):
    a, b= map(int, input().split())
    grid[a].append(b)
    grid[b].append(a)

ans = []
for iter in range(1, N+1):
    ans.append(bfs(grid, iter))

print(ans.index(min(ans))+1)