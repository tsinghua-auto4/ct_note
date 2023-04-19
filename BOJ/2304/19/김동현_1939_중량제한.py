from collections import deque

def bfs(weight: int):
    global p1, p2, bridges

    queue = deque([p1])
    visit = [False]*(N+1)
    visit[p1] = True

    while queue:
        x = queue.popleft()
        for i, w in bridges[x]:
            if not visit[i] and w >= weight:
                visit[i] = True
                queue.append(i)
    
    if visit[p2]:
        return True
    else:
        return False


N, M   = map(int, input().split())
bridges = [[] for _ in range(N+1)]
for _ in range(M):
    r, c, v = map(int, input().split())
    bridges[r].append((c, v))
    bridges[c].append((r, v))

p1, p2 = map(int, input().split())

start, end = 1, 1000000000
ans = 0
while start <= end:
    mid = (start + end)//2
    if bfs(mid):
        ans   = mid
        start = mid + 1
    else:
        end = mid - 1

print(ans)
