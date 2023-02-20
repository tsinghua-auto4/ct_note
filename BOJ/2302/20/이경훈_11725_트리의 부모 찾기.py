import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
# 인접리스트 만듦
graph = [[] for _ in range(N + 1)]
# 방문처리
visited = [False] * (N + 1)
for _ in range(N - 1):
  n1, n2 = map(int, input().split())
  graph[n1].append(n2)
  graph[n2].append(n1)

q = deque()
q.append(1)
visited[0], visited[1] = True, True

ans = [0] * (N + 1)

# 인접리스트를 활용한 bfs
def bfs():
  while q:
    n = q.popleft()
    for next_n in graph[n]:
      if not visited[next_n]:
        ans[next_n] = n
        visited[next_n] = True
        q.append(next_n)
        
bfs()

for idx, val in enumerate(ans):
  if idx > 1:
    print(val)
