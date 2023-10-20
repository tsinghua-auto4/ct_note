from collections import deque

def bfs(x):
    queue = deque()
    queue.append(x)
    check = [0 for _ in range(N)]

    while queue:
        q = queue.popleft()

        for i in range(N):
            if check[i] == 0 and grid[q][i] == 1:
                queue.append(i)
                check[i] = 1
                visit[x][i] = 1

N     = int(input())
grid  = [list(map(int, input().split())) for _ in range(N)]
visit = [[0]*N for _ in range(N)]

for iter in range(0, N):
    bfs(iter)

for iter in visit:
    print(*iter)