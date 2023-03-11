import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def chooseGround(cnt, idx, green, red, grounds):
  if green > G:
    return
  if red > R:
    return
  if (G - green) + (R - red) > len(grounds) - idx:
    return
  if cnt == R + G:
    bfs(chosen_ground)
    return

  if idx > len(grounds) - 1:
    return

  chosen_ground.append((grounds[idx], 1))
  chooseGround(cnt + 1, idx + 1, green + 1, red, grounds)
  chosen_ground.pop(-1)
  chosen_ground.append((grounds[idx], 2))
  chooseGround(cnt + 1, idx + 1, green, red + 1, grounds)
  chosen_ground.pop(-1)
  chooseGround(cnt, idx + 1, green, red, grounds)


def bfs(chosen_ground):
  global ans
  _ans = 0
  visited = [[[0 for _ in range(2)] for _ in range(M)] for _ in range(N)]
  q = deque()

  for (x, y), c in chosen_ground:
    visited[x][y][0] = c
    q.append((x, y))

  while (q):
    x, y = q.popleft()
    if visited[x][y][0] == 3: continue
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      if not inside(nx, ny): continue
      if garden[nx][ny] == 0: continue

      if visited[nx][ny][0] == 0:
        visited[nx][ny][0] = visited[x][y][0]
        visited[nx][ny][1] = visited[x][y][1] + 1
        q.append((nx, ny))

      elif visited[nx][ny][0] == 1:
        if visited[x][y][0] == 2 and visited[nx][ny][1] == visited[x][y][1] + 1:
          visited[nx][ny][0] = 3
          _ans += 1

      elif visited[nx][ny][0] == 2:
        if visited[x][y][0] == 1 and visited[nx][ny][1] == visited[x][y][1] + 1:
          visited[nx][ny][0] = 3
          _ans += 1
  ans = max(ans, _ans)


def inside(nx, ny):
  if -1 < nx < N and -1 < ny < M:
    return True
  else:
    return False


N, M, G, R = map(int, input().split())
garden = []
grounds = []
chosen_ground = []
ans = 0

for i in range(N):
  temp = list(map(int, input().split()))
  for j in range(M):
    if temp[j] == 2:
      grounds.append((i, j))
  garden.append(temp)

chooseGround(0, 0, 0, 0, grounds)
print(ans)
