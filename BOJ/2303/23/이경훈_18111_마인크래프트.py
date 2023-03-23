import sys

input = sys.stdin.readline

N, M, B = map(int, input().split())
graph = []
ans = 1e9
for _ in range(N):
  graph.append(list(map(int, input().split())))

for target in range(257):
  max_target, min_target = 0, 0
  for i in range(N):
    for j in range(M):
      if graph[i][j] >= target:
        max_target += graph[i][j] - target
      else:
        min_target += target - graph[i][j]

  if max_target + B >= min_target:
    if min_target + (max_target * 2) <= ans:
      ans = min_target + (max_target * 2)
      idx = target

print(ans, idx)