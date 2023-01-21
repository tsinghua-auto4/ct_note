import sys
import copy

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

#입력
n, m = map(int, input().split())
graph = []
cctv = []
mode = [[], 
        [[0], [1], [2], [3]], 
        [[0, 2], [1, 3]],
        [[0, 1], [1, 2], [2, 3], [3, 0]],
        [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]], 
        [[0, 1, 2, 3]]]
# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
  data = list(map(int, input().split()))
  graph.append(data)
  for j in range(m):
    if data[j] in [1, 2, 3, 4, 5]:
      cctv.append([data[j], i, j])


def fill(graph, mode, x, y):
  for i in mode:
    nx = x
    ny = y
    while True:
      nx += dx[i]
      ny += dy[i]
      if nx < 0 or nx > n - 1 or ny < 0 or ny > m - 1:
        break
      if graph[nx][ny] == 6:
        break
      elif graph[nx][ny] == 0:
        graph[nx][ny] = -1


def dfs(depth, graph):
  global min_val
  print(f'{depth} dfs 선언부')
  if depth == len(cctv):
    cnt = 0
    for i in range(n):
      cnt += graph[i].count(0)
    min_val = min(min_val, cnt)
    return

  temp = copy.deepcopy(graph)
  cctv_num, x, y = cctv[depth]
  for i in mode[cctv_num]:
    fill(temp, i, x, y)
    dfs(depth + 1, temp)
    print(f'{depth} {i}후반부')
    temp = copy.deepcopy(graph)


min_val = int(1e9)
dfs(0, graph)
print(min_val)