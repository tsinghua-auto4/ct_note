import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for __ in range(n)]
dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))

def bfs(x, y):
  q = deque()
  q.append((x, y))
  visited[x][y] = True
  while q:
    x, y = q.popleft()
    for dx, dy in dirs:
      nx, ny = x + dx, y + dy
      nx = (nx + n) % n
      ny = (ny + m) % m
      if data[nx][ny] == 1:
        continue
      if visited[nx][ny]: 
        continue
      visited[nx][ny] = True
      q.append((nx, ny))
      
ans = 0
for i in range(n):
  for j in range(m):
    if data[i][j] == 0 and not visited[i][j]:
      bfs(i, j)
      ans += 1
print(ans)