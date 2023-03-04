import sys
from collections import deque

input = sys.stdin.readline


def bfs():
  q = deque()
  q.append((0, 0, 0))
  visited[0][0][0] = 1
  while (q):
    k, x, y = q.popleft()

    if x == N - 1 and y == M - 1:
      return visited[k][x][y]

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if -1 < nx < N and -1 < ny < M:
        if map[nx][ny] == 0 and visited[k][nx][ny] == 0:
          q.append((k, nx, ny))
          visited[k][nx][ny] = visited[k][x][y] + 1
        elif map[nx][ny] == 1 and k + 1 < K + 1 and visited[k+1][nx][ny] == 0:
            q.append((k + 1, nx, ny))
            visited[k + 1][nx][ny] = visited[k][x][y] + 1
  return -1


N, M, K = map(int, input().split())
map = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(K + 1)] # 가짓수가 많을수록 뒤로 가는게 시간상 유리함
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
print(bfs())