import sys
from collections import deque
input = sys.stdin.readline

#입력
n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)] # 동서남북

# bfs 함수
def bfs(x, y):
  ans = 1
  q = deque()
  q.append((x, y))
  visited[x][y] = True
  while q:
    x, y = q.popleft()
    for dx, dy in dirs:
      nx = x + dx
      ny = y + dy
      if -1 < nx < n and -1 < ny < m:
        if data[nx][ny] == 1 and not visited[nx][ny]:
          q.append((nx, ny))
          visited[nx][ny] = True
          ans += 1
  return ans

num = 0
ans = 0

for i in range(n):
  for j in range(m):
    if data[i][j] == 1 and not visited[i][j]:
      temp = bfs(i, j)
      num += 1
      if temp > ans:
        ans = temp

print(num)
print(ans)