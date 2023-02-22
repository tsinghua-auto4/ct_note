import sys
from collections import deque

input = sys.stdin.readline


def bfs():
  q = deque()
  q.append((0, 0, 0))
  while q:
    x, y, punc = q.popleft()

    if x == n - 1 and y == m - 1:
      return visited[x][y][punc]

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if -1 < nx < n and -1 < ny < m and visited[nx][ny][punc] == 0:
        if data[nx][ny] == 0:
          q.append((nx, ny, punc))
          visited[nx][ny][punc] = visited[x][y][punc] + 1
        elif data[nx][ny] == 1 and punc == 0:
          q.append((nx, ny, punc + 1))
          visited[nx][ny][punc + 1] = visited[x][y][punc] + 1
  return -1


n, m = map(int, input().split())
data = [list(map(int, input().rstrip())) for _ in range(n)]
print(data)
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
dx = [0, -1, 1, 0]
dy = [1, 0, 0, -1]
visited[0][0][0] = 1

print(bfs())
