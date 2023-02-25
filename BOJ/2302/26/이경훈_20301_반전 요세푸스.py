import sys
from collections import deque

input = sys.stdin.readline

N, K, M = map(int, input().split())

q = deque()
for i in range(1, N + 1):
  q.append(i)
ans = []
cnt = 0
while (q):
  # print('현재 cnt : ', cnt)
  # print('기존 : ', q)
  for i in range(K - 1):
    if ((cnt // M) % 2 == 0):
      q.append(q.popleft())
    else:
      q.appendleft(q.pop())
    # print('자리 전환 후 : ', q)
  if ((cnt // M) % 2 == 0):
    print(q.popleft())
  else:
    print((q.pop()))
  cnt += 1
  # print('삭제 후 : ', q)