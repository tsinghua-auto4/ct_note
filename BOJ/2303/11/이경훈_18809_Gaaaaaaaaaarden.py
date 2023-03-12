import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 백트래킹으로 배양액의 위치 고름
def chooseGround(cnt, idx, green, red, grounds):
  if green > G:
    return
  if red > R:
    return
  if (G - green) + (R - red) > len(grounds) - idx:  # 남은 배양액보다 남은 땅이 더 적다면 종료
    return
  if cnt == R + G:  # 배양액을 뿌릴 땅 선정 완료
    bfs(chosen_ground)  # bfs 돌림
    return

  # 초록색 선택
  chosen_ground.append((grounds[idx], 1))
  chooseGround(cnt + 1, idx + 1, green + 1, red, grounds)
  chosen_ground.pop(-1)
  # 빨간색 선택
  chosen_ground.append((grounds[idx], 2))
  chooseGround(cnt + 1, idx + 1, green, red + 1, grounds)
  chosen_ground.pop(-1)
  # 미선택
  chooseGround(cnt, idx + 1, green, red, grounds)


def bfs(chosen_ground):
  global ans
  _ans = 0
  # visited[x][y][z] : x, y는 좌표 z는 [a, b]의 형태로서
  # a는 상태를 의미함. 즉 0,1,2,3 각각 아무것도 없음, 초록색, 빨간색, 꽃을 의미함
  # b는 시간을 의미함
  visited = [[[0 for _ in range(2)] for _ in range(M)] for _ in range(N)]
  q = deque()

  for (x, y), c in chosen_ground:
    visited[x][y][0] = c
    q.append((x, y))

  while (q):
    x, y = q.popleft()
    # 꽃이면 continue
    if visited[x][y][0] == 3: continue
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      if not inside(nx, ny): continue
      if garden[nx][ny] == 0: continue

      # 만약 갈 칸에 아무 것도 없다면
      if visited[nx][ny][0] == 0:
        # 현재 칸의 상태를 물려주고
        visited[nx][ny][0] = visited[x][y][0]
        # 1의 시간을 더한다
        visited[nx][ny][1] = visited[x][y][1] + 1
        # 큐에 넣어준다
        q.append((nx, ny))

      # 만약 갈 칸에 초록색 배양액이 있다면
      elif visited[nx][ny][0] == 1:
        # 만약 현재 칸에 빨간색 배양액이 있고 시간이 1초 차이라면
        if visited[x][y][0] == 2 and visited[nx][ny][1] == visited[x][y][1] + 1:
          # 갈 칸을 꽃으로 만들어주고
          visited[nx][ny][0] = 3
          # 결과값에 1 추가
          _ans += 1

      # 위와 같다
      elif visited[nx][ny][0] == 2:
        if visited[x][y][0] == 1 and visited[nx][ny][1] == visited[x][y][1] + 1:
          visited[nx][ny][0] = 3
          _ans += 1
  # 최대값으로 갱신
  ans = max(ans, _ans)


def inside(nx, ny):
  if -1 < nx < N and -1 < ny < M:
    return True
  else:
    return False


# 입력받기
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

# 메인함수 실행
chooseGround(0, 0, 0, 0, grounds)
print(ans)
