import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())

q = deque()
for i in range(1, N+1):
    q.append(i)
# print(q)
ans = []

while(len(q)>1):
    for i in range(K-1):
        q.append(q.popleft())
    ans.append(q.popleft())
ans.append(q.popleft())

print(f'<{", ".join(map(str, ans))}>')
