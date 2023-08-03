import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
dq = deque()
for _ in range(N):
    cur = list(map(int, sys.stdin.readline().split()))

    if cur[0] == 1:
        dq.appendleft(cur[1])
    elif cur[0] == 2:
        dq.append(cur[1])
    elif cur[0] == 3:
        if len(dq):
            print(dq.popleft())
        else:
            print(-1)
    elif cur[0] == 4:
        if len(dq):
            print(dq.pop())
        else:
            print(-1)
    elif cur[0] == 5:
        print(len(dq))
    elif cur[0] == 6:
        if len(dq):
            print(0)
        else:
            print(1)
    elif cur[0] == 7:
        if len(dq):
            print(dq[0])
        else:
            print(-1)
    elif cur[0] == 8:
        if len(dq):
            print(dq[-1])
        else:
            print(-1)