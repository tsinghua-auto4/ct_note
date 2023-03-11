import sys
from collections import deque

def solution(start, end):
    visit = [0]*10000
    visit[start] = 1
    queue = deque([start])

    while queue:
        cur = queue.popleft()
        if cur == end:
            print(visit[end]-1)
            return
        cur = str(cur)
        for i in range(4):
            for delta in range(10):
                nxt = cur[:i] + str(delta) + cur[i+1:]
                nxt = int(nxt)
                if 1000 <= nxt and prime[nxt] and not visit[nxt]:
                    visit[nxt] = visit[int(cur)] + 1
                    queue.append(nxt)


prime = [True]*10000
for i in range(2, 100+1):
    if prime[i]:
        for j in range(i+i, 10000, i):
            prime[j] = False

for _ in range(int(sys.stdin.readline().rstrip())):
    start, end = map(int, sys.stdin.readline().split())
    solution(start, end)