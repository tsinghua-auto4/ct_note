import sys

input = sys.stdin.readline

visited = [[False] * 100 for _ in range(100)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0

n = int(input())
for i in range(n):
  x, y = map(int, input().split())
  for i in range(x, x + 10):
    for j in range(y, y + 10):
      visited[i][j] = True

for x in range(100):
  for y in range(100):
    if visited[x][y] == True:
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx == -1 or nx == 100 or ny == -1 or ny == 100:
          cnt += 1
        elif -1 < nx < 100 and -1 < ny < 100 and visited[nx][ny] == False:
          cnt += 1

print(cnt)
