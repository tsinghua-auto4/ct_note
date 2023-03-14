import sys
from collections import deque

input = sys.stdin.readline
T = int(input())
for _ in range(T):
  N, M = map(int, input().split())
  q = deque()
  temp = list(map(int, input().split()))
  for i in range(len(temp)):
    q.append((temp[i], i))

  cnt = 0
  while (q):
    max_val = q[0][0]
    max_idx = 0
    for idx, val in enumerate(q):
      if int(val[0]) > max_val:
        max_val = int(val[0])
        max_idx = idx
    for i in range(max_idx):
      q.append(q.popleft())
    x, y = q.popleft()
    cnt += 1
    if y == M:
      print(cnt)
      break
