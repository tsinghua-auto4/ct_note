import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
data = []
chick = []
people = []
min_val = 1e9

for i in range(N):
  temp = list(map(int, input().split()))
  for j in range(len(temp)):
    if temp[j] == 2:
      chick.append((i, j))
      temp[j] = 0
    elif temp[j] == 1:
      people.append((i, j))
  data.append(temp)

combi = list(combinations(chick, M))
for chicken in combi:
  chicken_dist = [100] * len(people)
  for ch in chicken:
    r, c = ch
    for idx, val in enumerate(people):
      p_r, p_c = val
      chicken_dist[idx] = min(chicken_dist[idx], abs(r - p_r) + abs(c - p_c))
  min_val = min(min_val, sum(chicken_dist))
print(min_val)
